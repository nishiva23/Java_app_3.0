#! /usr/bin/env python3

import requests

# Artifactory URL and repository path
artifactory_url = "http://34.232.52.195:8082/artifactory/"
repository_path = "example-repo-local/"

# Credentials for authentication (if required)
username = "admin"
password = "2aeXiiTJBiBJE492x8RT"

# Path to the JAR file you want to upload
jar_file_path = "/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"

# Construct the URL for uploading the JAR file
upload_url = f"{artifactory_url}{repository_path}{jar_file_path}"

# Open and read the JAR file
with open(jar_file_path, 'rb') as jar_file:
    # Set up authentication if required
    auth = (username, password) if username and password else None
    
    # Use a PUT request to upload the JAR file
    response = requests.put(upload_url, data=jar_file, auth=auth)

# Check the response status
if response.status_code == 201:
    print("JAR file uploaded successfully.")
else:
    print(f"Failed to upload JAR file. Status code: {response.status_code}")
    print(response.text)
