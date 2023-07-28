import requests
import json
import xmltodict

def get_json_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the response
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from {url}: {e}")
        return None

def convert_to_xml(json_data):
    try:
        xml_data = xmltodict.unparse(json_data, pretty=True)
        return xml_data
    except Exception as e:
        print(f"Error converting JSON to XML: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    url = "https://example.com/api/data"  # Replace this with the URL you want to extract JSON from
    data = get_json_from_url(url)
    if data:
        print("JSON Data:")
        print(json.dumps(data, indent=4))  # Print the JSON data with indentation
        
        xml_data = convert_to_xml(data)
        if xml_data:
            print("\nXML Data:")
            print(xml_data)  # Print the XML data
