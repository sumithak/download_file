import requests
import os

def download_file():
    url = os.environ['URL']
    output_path = os.environ['OUTPUT_PATH']
    response = requests.get(url)
    if response.status_code ==  200:
        with open(output_path, "wb") as file:
            file.write(response.content)
        print("Download complete!")
    else:
        print(f"An error occurred while downloading the file")

download_file()