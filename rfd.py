from bs4 import BeautifulSoup
import requests
import time

# thoughts to get only recent deals posted.
# sort the deals by time posted. If the latest deal time posted is greater than the most current deal then send a discord message of the most recent deal


def get_deals():
    try:
        #Fetch the HTML content from the RedFlagDeals hot deals forum
        source = requests.get('https://forums.redflagdeals.com/hot-deals-f9/').text

        #Parse the HTML content using BeautifulSoup with the 'lxml' parser
        soup = BeautifulSoup(source, 'lxml')
        deals = {}

        title_links = soup.find_all('a', class_ = 'topic_title_link')

        post_times = soup.find_all('span', class_ = 'first-post-time')

        for title, post_time in zip(title_links, post_times): #let us use zip to pair each post with the first time
            deal_link = f"https://forums.redflagdeals.com{title['href']}"
            deal_title = title.text.strip()
            deal_post_time = post_time.text.strip()

            print(f"Link to Deal: {deal_link}")
            print(f"Deal Title: {deal_title}")
            print(f"Posted On: {deal_post_time}")
            print("-"*40)

            deals[deal_link] = (deal_title, deal_post_time)

        return deals
    except requests.exceptions.RequestException as e:
        print(f"Error fetching deals {e}")

def check_new_deals(previous_deals):
    while True:
        try:
            current_deals = get_deals()
            new_deals = []

            for deal in current_deals:
                if deal not in current_deals:
                    new_deals.append(deal)
        
            if new_deals:
                print("No new deals Posted!")
                for title, link, post_time in new_deals:
                    print(f"Title: {title}\nLink: {link}\n Time: {post_time}")
                    print("-"*40)

                    previous_deals.update({link: (title, post_time) for link, (title, post_time) in new_deals})           
            else:
                print(f"No new deals at this time!")
        except Exception as e:
                print(f"Error getting new deals {e}")
            
        time.sleep(300)
if __name__ == "__main__":
    try:
        initial_deals = get_deals()
        previous_deals = initial_deals
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