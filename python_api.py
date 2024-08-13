import urllib.request
import json
import sys
import base64

def fetch_the_data():
    #print("hello world\n\n")

    #response = urllib.request.urlopen("")

    #if response.getcode() == 200:
    #    output = json.loads(response.read())
    #    print(output)

    url = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    # USE BELOW CREDENTIALS IF YOU ARE USING BASIC AUTHORISATION
    #username = "API_KEY"
    #password = ""
    
    # ALSO USE THESE 2 LINES BELOW FOR BASIC AUTHORISATION
    #credentials = f"{username}:{password}"
    #encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    request = urllib.request.Request(url)
    # USE THE LINE BELOW FOR BASICA AUTHORISATION ELSE USE THE CLASSIC ONE BELOW WITH NO USERNAME AND NO PASSWORD
    #request.add_header("Authorization", f"Basic {encoded_credentials}")
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            output = json.loads(response.read().decode('utf-8'))
            print(output)
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)

if __name__ == "__main__":
    fetch_the_data()
