from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

table_rows = soup.select('table tr')

# Initialize a variable to store the sum of the numbers
total_sum = 0

# Iterate through each <tr> element and extract the content from each row
for row in table_rows:
    # Find all <td> elements within the row
    table_data = row.find_all('td')
    
    # Extract the data from each <td> element
    if len(table_data) == 2:  # Assuming each row has exactly two <td> elements
        cell1_data = table_data[0].text.strip()
        
        # Find the <span> tag within the second <td> and extract its text content
        cell2_span = table_data[1].find('span', class_='comments')
        
        # Check if the <span> tag is found and extract its text content
        if cell2_span:
            cell2_data = cell2_span.text.strip()
            
            # Convert the text content to an integer and add it to the total_sum
            try:
                number = int(cell2_data)
                total_sum += number
            except ValueError:
                pass  # If the conversion to int fails, ignore the value

# Print the total sum of the numbers
print("Total Sum:", total_sum)