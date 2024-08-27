from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import re
import discord
from discord.ext import tasks

token = ''
channel_ID = 1

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_discord_message(channel, content):
        await channel.send(content)


def get_deals():
    try:
        source = requests.get('https://forums.redflagdeals.com/hot-deals-f9/').text

        # Parse the HTML content using BeautifulSoup with the 'lxml' parser
        soup = BeautifulSoup(source, 'lxml')
        deals = []

        title_links = soup.find_all('a', class_='topic_title_link')
        post_times = soup.find_all('span', class_='first-post-time')

        for title, post_time in zip(title_links, post_times):
            deal_link = f"https://forums.redflagdeals.com{title['href']}"
            deal_title = title.text.strip()
            deal_post_time = post_time.text.strip()

            # Clean and convert post time to a datetime object for sorting
            clean_post_time = re.sub(r'(\d+)(th|st|nd|rd)', r'\1', deal_post_time)
            sort_deal_time = datetime.strptime(clean_post_time, '%b %d, %Y %I:%M %p')

            deals.append((deal_title, deal_link, deal_post_time, sort_deal_time))

        # Sort the deals by the post time in descending order (most recent first)
        deals.sort(key=lambda x: x[3], reverse=True)

        return deals
    except requests.exceptions.RequestException as e:
        print(f"Error fetching deals: {e}")
        return []

def check_new_deals(previous_deals):
    while True:
        try:
            current_deals = get_deals()
            new_deals = []

            for deal in current_deals:
                link = deal[1]
                if link not in previous_deals:
                    new_deals.append(deal)

            if new_deals:
                print("New deals posted!")
                for title, link, post_time, _ in new_deals: 
                    print(f"Title: {title}\nLink: {link}\nPosted On: {post_time}")
                    print("-" * 40)

                # Update previous deals dictionary with the new deals
                previous_deals.update({deal[1]: (deal[0], deal[2]) for deal in new_deals})
            else:
                print("No new deals at this time.")

        except Exception as e:
            print(f"Error getting new deals: {e}")
            
        time.sleep(60)  

if __name__ == "__main__":
    try:
        initial_deals = get_deals()
        previous_deals = {deal[1]: (deal[0], deal[2]) for deal in initial_deals}
        print(f"Starting to monitor deals. Found {len(previous_deals)} deals initially.")
        check_new_deals(previous_deals)
    except Exception as e:
        print(f"Critical error during initialization: {e}")



# Find all the links with the class 'topic_title_link' which likely represent the titles of the deals
#match = soup.find_all('a', class_='topic_title_link')

# Print the prettified version of the matches to make it more readable
#for link in match:
 #   print(link.prettify())

# Additional comments for future use:
# soup.prettify() - This will print the entire HTML content in a readable format
# match = soup.p.text - This can be used to extract text from the first <p> tag
# find: retrieves the first occurrence of the specified tag
# find_all: retrieves all occurrences of the specified tag

# Example of looping through articles (this section is commented out for reference)
'''
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text  # Extract the headline text
    print(headline)
    summary = article.p.text  # Extract the summary text
    print(summary)
'''