import requests

def download_file(url, output_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as file:
            file.write(response.content)
        print("Download complete!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {str(e)}")

# Example usage
url = "https://dist.nuget.org/win-x86-commandline/latest/nuget.exe"  # Replace with your desired URL
output_path = "nuget.exe"       # Replace with your desired output path

download_file(url, output_path)