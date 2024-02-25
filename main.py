import instaloader
import os
import requests

def download_profile_picture(username):
    loader = instaloader.Instaloader()

    try:
        # Retrieve profile information
        profile = instaloader.Profile.from_username(loader.context, username)

        # Get the URL of the profile picture
        pic_url = profile.profile_pic_url

        # Set the initial file name based on the username
        file_name = f"{username}.jpg"

        # Check if the file already exists, and if it does, increment the number
        count = 1
        while os.path.exists(file_name):
            count += 1
            base_name, extension = os.path.splitext(file_name)
            file_name = f"{base_name}-{count}{extension}"

        # Download and save the profile picture
        response = requests.get(pic_url)
        with open(file_name, 'wb') as f:
            f.write(response.content)

        print(f"Profile picture downloaded for {profile.username}")
    except Exception as e:
        print(f"Error downloading profile picture for {username}: {e}")

if __name__ == "__main__":
    # Specify the path to your text file containing Instagram usernames
    input_file_path = "input.txt"

    with open(input_file_path, "r") as file:
        # Read each line from the file and download the profile picture
        for line in file:
            username = line.strip().split("/")[-2]
            download_profile_picture(username)
