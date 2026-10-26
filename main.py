from dotenv import load_dotenv
import os, requests

def main():
    envfile = load_dotenv()
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    token = get_token(client_id, client_secret)
    print(search_tracks("Sadfriendd - Transylvania", token))

def get_token(client_id, client_secret):
    response = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "client_credentials"}, auth=(client_id, client_secret))
    data = response.json()
    token = data["access_token"]
    return token

def search_tracks(search_text, token):
    params = {"q": search_text, "type": "track", "limit": 10}
    headers = {"Authorization": f"Bearer {token}"}
    inquiry = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
    print(inquiry.status_code)
    data = inquiry.json()

    return data




if __name__ == "__main__":
    main()    