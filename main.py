import os
import time
import random
import pickle
from instagrapi import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Instagram credentials from environment variables
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')

if not username or not password:
    print("ERROR: Please set INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD in Secrets")
    print("Go to Tools > Secrets to add them")
    exit(1)

# Initialize Instagram client
cl = Client()

# Load or create session
session_file = 'instagram_session2.pkl'

# Load session if exists
if os.path.exists(session_file):
    try:
        with open(session_file, 'rb') as f:
            cl = pickle.load(f)
        print("Loaded existing session")
    except Exception as e:
        print(f"Failed to load session: {e}")
        cl.login(username, password)
        with open(session_file, 'wb') as f:
            pickle.dump(cl, f)
else:
    # Login if session does not exist
    print("Logging in to Instagram...")
    cl.login(username, password)
    with open(session_file, 'wb') as f:
        pickle.dump(cl, f)
    print("Session saved")

# Path to the reels folder (Replit-compatible)
reels_folder = "reels"

# Create reels folder if it doesn't exist
if not os.path.exists(reels_folder):
    os.makedirs(reels_folder)
    print(f"Created {reels_folder} folder. Please upload your .mp4 videos to this folder.")
    exit(0)

# Function to upload a reel with a random hashtag as caption
def upload_reel(video_path):
    try:
        # Create a list of hashtags
        hashtags = [
            "fyyyyp", "sora", "sorabrainrot", "aibrainrot", "ai", "corecore", 
            "sigma", "npc", "delusional", "aiedit", "skibidi", 
            "ohio", "grindset", "gyatt", "fanumtax", "sped", "viral", 
            "aivideo", "aicore", "weirdcore", "soracore", "real", 
            "goofy", "aesthetic", "editcore", "brainrotcore", "doomscroll", "funny", "aibrain", "delulu", 
            "core", "sigmaedit", "rot", "internetcore", "aifilter", 
            "mewing", "rizzcore", "goob", "goober", "drain", 
            "draincore", "hyperreal", "fanum", "skibiditoilet", "ohiomemes", 
            "brain", "random", "spedup", "cursed", "realism", 
            "lofi", "edittrend", "glitchcore", "soratokyo", "rotcore", 
            "mew", "soravibes", "dreamcore", "surreal", "airot", 
            "weirdedit", "nonsense", "viralreel", "reeltrend", "videomeme", 
            "memeedit", "npcmoment", "chronicallyonline", "airotwave", "delusion", 
            "scrollcore", "brainmelt", "skibidiwar", "npcvibes", "internet", 
            "rotwave", "psychcore", "delulucore", "aistuff", "aigirl", 
            "soraworld", "soraverse", "aibliss", "digitalrot", "soraisreal", 
            "unrealedit", "viralcore", "aiviral", "soraiscrazy", "mindrot", 
            "sorathemes", "realityglitch", "dreamrot", "aiedits", "airotcore"
        ]

        # Use spaghetti recipe as caption
        caption = """@buubbees"""
        
        # Add random hashtags to the caption
        selected_hashtags = random.sample(hashtags, k=min(len(hashtags), 5))
        caption += f"\n\n{' '.join(['#' + tag for tag in selected_hashtags])}"

        # Upload video as a reel (clip) with a caption
        cl.clip_upload(video_path, caption=caption)
        print(f"✓ Uploaded {os.path.basename(video_path)}")
        return True
    except Exception as e:
        print(f"✗ Failed to upload {os.path.basename(video_path)}: {e}", flush=True)
        return False

# Function to delete the reel after uploading
def delete_reel(video_path):
    try:
        os.remove(video_path)
        print(f"✓ Deleted {os.path.basename(video_path)}")
    except Exception as e:
        print(f"✗ Failed to delete {os.path.basename(video_path)}: {e}", flush=True)

# List all video files in the reels folder and sort them
reels_files = sorted([f for f in os.listdir(reels_folder) if f.endswith(".mp4")])

if not reels_files:
    print(f"No .mp4 files found in {reels_folder} folder.")
    print("Please upload your video files to the 'reels' folder and run again.")
    exit(0)

print(f"Found {len(reels_files)} video(s) to upload")

# Loop through each file and upload with a random delay
for index, reel in enumerate(reels_files, start=1):
    reel_path = os.path.join(reels_folder, reel)
    
    print(f"\n[{index}/{len(reels_files)}] Processing {reel}...")

    # Upload the reel and delete if successful
    if upload_reel(reel_path):
        delete_reel(reel_path)

    # Random delay between 30 to 80 seconds
    if index < len(reels_files):
        wait_time = random.uniform(30, 80)
        print(f"⏳ Waiting {wait_time:.1f} seconds before next upload...")
        time.sleep(wait_time)

print("\n✓ All uploads complete!")
