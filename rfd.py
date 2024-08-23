from bs4 import BeautifulSoup
import requests

def deals_get():
     #Fetch the HTML content from the RedFlagDeals hot deals forum
    source = requests.get('https://forums.redflagdeals.com/hot-deals-f9/').text

    #Parse the HTML content using BeautifulSoup with the 'lxml' parser
    soup = BeautifulSoup(source, 'lxml')

    title_links = soup.find_all('a', class_ = 'topic_title_link')

    post_times = soup.find_all('span', class_ = 'first-post-time')

    for title, post_time in zip(title_links, post_times): #let us use zip to pair each post with the first time
        print(f"Deal title: {title.text.strip()}")
        print(f"Time Posted: {post_time.text.strip()}")
        print("-"*40)


deals_get()




































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