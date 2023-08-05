import urllib.request
import json

def get_comment_counts(url):
    try:
        # Retrieve JSON data from the URL
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        print(f"Retrieving {url}")
        print(f"Retrieved {len(data)} characters")

        # Parse the JSON data
        json_data = json.loads(data)

        # Extract the 'comments' list from the JSON data
        comments_list = json_data.get('comments', [])

        # Compute the sum of comment counts
        total_count = sum(comment.get('count', 0) for comment in comments_list)

        return total_count
    except Exception as e:
        print("Error:", e)
        return None

def main():
    # Prompt the user for the URL
    url = input("Enter location: ")

    # Get the total comment count
    total_count = get_comment_counts(url)

    if total_count is not None:
        print("Sum:", total_count)

if __name__ == "__main__":
    main()
