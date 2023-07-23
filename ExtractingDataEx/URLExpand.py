import urllib.request
from bs4 import BeautifulSoup

def follow_links(url, count, position):
    for i in range(count):
        # Retrieve the HTML content from the URL
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find all anchor tags in the page
            anchors = soup.find_all('a')
            #print(anchors)

            # Check if the specified position exists
            if len(anchors) >= position:
                # Get the URL from the anchor tag at the specified position
                url = anchors[position - 1].get('href')
                print(f"Retrieving: {url}")
            else:
                print("Invalid position!")
                break

    # Extract the last name from the URL
    last_name = url.split('/')[-1].split('.')[0]
    return last_name

start_url = input("Enter URL: ")
position = int(input("Enter position: "))
count = int(input("Enter count: "))

last_name = follow_links(start_url, count, position)
print(f"The answer to the assignment is \"{last_name}\".")
