import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# ------------------- SETUP FUNCTION -------------------
def setup_spotify_client():
    """
    Initialize and return a Spotify client using your credentials.
    """
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id="YOUR_SPOTIFY_CLIENT_ID",
            client_secret="YOUR_SPOTIFY_CLIENT_SECRET"
        )
    )
    return sp


# ------------------- SEARCH FUNCTION -------------------
def search_playlists_by_mood(sp, mood_keyword, limit=3):
    """
    Search Spotify playlists based on mood keyword.
    Returns list of {name, url} dictionaries.
    """
    print(f"🔍 Searching playlists for mood: '{mood_keyword}'")

    try:
        results = sp.search(q=mood_keyword, type="playlist", limit=limit)
        playlists = []

        # Defensive check: ensure playlists exist
        if not results or "playlists" not in results or not results["playlists"]["items"]:
            print("⚠️ No playlists found for that mood, using fallback.")
            return [{"name": "Spotify Mood Mix", "url": "https://open.spotify.com"}]

        for item in results["playlists"]["items"]:
            if item is not None:
                playlists.append({
                    "name": item.get("name", "Unknown Playlist"),
                    "url": item["external_urls"]["spotify"]
                })

        return playlists if playlists else [{"name": "Spotify Mood Mix", "url": "https://open.spotify.com"}]

    except Exception as e:
        print(f"❌ Error fetching playlists: {e}")
        return [{"name": "Spotify Mood Mix", "url": "https://open.spotify.com"}]
