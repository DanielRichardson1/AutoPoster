import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.auth.transport.requests
import json
import datetime

# OAuth 2.0 scopes for the YouTube Data API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Path to token file (to store user credentials)
TOKEN_FILE = "token.json"

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.auth.transport.requests
import json

# OAuth 2.0 scopes for YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Path to token file (to store user credentials)
TOKEN_FILE = './Secrets/youtube_token.json'

# Get Youtube User 
def get_authenticated_service():  # Just asked for every permission when setting up API lol sorry
    creds = None
    
    # Check if token file with credentials already exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            creds = google.oauth2.credentials.Credentials.from_authorized_user_info(json.load(token))
    
    # If no valid credentials, request the user to authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file('./Secrets/youtube_client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)  # This opens the browser for user authorization
        
        # Save the credentials for future use
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube


def upload_video(file_path, title, description, tags, category_id, scheduled_time):
    # Get credentials and create an API client
    youtube = get_authenticated_service()

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": "public",  # Maybe should change to initially upload as private
            "publishAt": scheduled_time,  # Time in ISO 8601 format (for scheduling)
            "selfDeclaredMadeForKids": False
        }
    }

    media_body = googleapiclient.http.MediaFileUpload(file_path, chunksize=-1, resumable=True)

    # Upload the video
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_body
    )
    
    response = request.execute()
    print(f"Video uploaded with ID: {response['id']}")

# Define your video details
file_path = "path/to/your/video.mp4"
title = "Your YouTube Shorts Title"
description = "Description of your video."
tags = ["Shorts", "example", "demo"]
category_id = "22"  # Category ID for People & Blogs, adjust accordingly

# Schedule the post to 24 hours from now
scheduled_time = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)).isoformat("T") + "Z"

# Call the function to upload and schedule the video
upload_video(file_path, title, description, tags, category_id, scheduled_time)
