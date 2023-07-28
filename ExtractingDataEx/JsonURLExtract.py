import requests
import json

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

# Example usage:
if __name__ == "__main__":
    url = "https://example.com/api/data"  # Replace this with the URL you want to extract JSON from
    data = get_json_from_url(url)
    if data:
        print(json.dumps(data, indent=4))  # Print the JSON data with indentation
