import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='WEBCRAWLER'
)

#List of keywords to find relevance scores
relevant_keywords = ["mass", "force of attraction", "weight"]

# Title of seed page
seed_page_title = "gravity"

# Retrieve the seed page 
seed_page = wiki_wiki.page(seed_page_title)

#Accessing the seed URL 
seed_page_url = seed_page.fullurl
print("Seed Page URL:", seed_page_url)

# Access the links on the seed page
links = seed_page.links

# To Create a list to store URLs and their relevance scores
url_priority_list = []

# Calculate revelance score based on number of keywords present
def calculate_relevance_score(page_title, page_content):
    title_score = sum(keyword in page_title.lower() for keyword in relevant_keywords)
    content_score = sum(keyword in page_content.lower() for keyword in relevant_keywords)
    return title_score + content_score

for link_title in links:
    link_url = "https://en.wikipedia.org/wiki/" + link_title
    
    linked_page = wiki_wiki.page(link_title)
    linked_page_content = linked_page.text.lower()
    
    relevance_score = calculate_relevance_score(link_title, linked_page_content)
    
    # Setting a threshold score
    if relevance_score > 2:
        url_priority_list.append((link_url, relevance_score))
url_priority_list.sort(key=lambda x: x[1], reverse=True)

# Print the prioritized URLs
print("\nPrioritized Page URLs:")
for url, relevance_score in url_priority_list:
    print(f"URL: {url}, Relevance Score: {relevance_score}")


