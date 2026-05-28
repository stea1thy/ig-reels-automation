# FOR EDUCATIONAL PURPOSES ONLY 


# 📱 Instagram Reels Automation

A Python automation script that batch-uploads `.mp4` videos as Instagram Reels. It handles session management, randomizes hashtags, introduces human-like delays between uploads, and automatically cleans up local files after posting.

## ✨ Features

* **Secure Credential Management:** Uses `.env` files to keep your Instagram username and password out of the source code.
* **Session Caching:** Saves your login session locally (`instagram_session2.pkl`) to prevent repetitive logins and reduce the risk of your account getting flagged.
* **Batch Processing:** Automatically reads, sorts, and queues all `.mp4` files placed in the `reels/` directory.
* **Dynamic Hashtags:** Selects 5 random hashtags from a massive predefined list of trending "core" and "brainrot" tags to maximize reach.
* **Auto-Cleanup:** Deletes the local video file immediately after a successful upload to save disk space.
* **Human-like Delays:** Implements a random delay (30 to 80 seconds) between uploads to mimic organic user behavior.

## 🛠️ Prerequisites

Before you begin, ensure you have Python installed on your machine. You will also need to install the following Python libraries:

```bash
pip install instagrapi python-dotenv
