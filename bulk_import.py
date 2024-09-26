import os
import requests
import json

# function to read the manifest json file
def read_manifest(manifest_file):
    if os.path.isfile(manifest_file):
        with open(manifest_file, 'r') as file:
            content = json.load(file)

        return content

    else:
        print(f"File not found: {manifest_file}")
        exit(1)

# function to replace fileserver urls in the manifest
def replace_urls(file_content, old_url, new_url):
    # Recursive function to traverse and replace URLs in the dictionary
    def recursive_replace(obj):
        if isinstance(obj, dict):
            return {key: recursive_replace(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [recursive_replace(item) for item in obj]
        elif isinstance(obj, str):
            return obj.replace(old_url, new_url)
        else:
            return obj

    return recursive_replace(file_content)

# Function to post the manifest to the fhir server
def post(fhir_base_url, content):
    request_url = f"{fhir_base_url}/$import"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/fhir+json",
        "Prefer": "respond-async"
    }

    response = requests.post(request_url, headers=headers, json=content)

    if response.status_code == 202:
        print("Import request accepted.")
        content_location = response.headers.get("Content-Location")
        if content_location:
            print(f"Check status at: {content_location}")
        else:
            print("No Content-Location header found in the response.")
    else:
        print(f"Failed to post manifest. Status code: {response.status_code}")
        try:
            error_message = response.json()
            print("Error details:", json.dumps(error_message, indent=2))
        except json.JSONDecodeError:
            print("Failed to decode error response.")

default_fileserver_url = "http://localhost:8000" # The default fileserver url that synthea provides
new_fileserver_url = "http://fileserver:8080" # the fileserver address from within the compose network

fhir_base_url = "http://localhost:8080/fhir"
manifest_file = "fhir-data/parameters.json"

content = read_manifest(manifest_file)
content = replace_urls(content, default_fileserver_url, new_fileserver_url)
post(fhir_base_url, content)
