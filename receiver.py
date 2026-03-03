import os
import re
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Directory where your Plaud notes will be stored
INBOX_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inbox")

def sanitize_filename(filename):
    """Remove characters that are illegal in filenames."""
    return re.sub(r'[\/*?:"<>|]', "", filename).strip()

@app.route("/webhook", methods=["POST"])
def receive_plaud():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    # Extract fields from the Zapier Webhook
    title = data.get("title", "Untitled Recording")
    transcript = data.get("transcript", "No transcript provided.")
    summary = data.get("summary", "No summary provided.")
    create_time = data.get("create_time", datetime.now().isoformat())
    
    # Prepare the filename
    safe_title = sanitize_filename(title)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_title}_{timestamp}.md"
    file_path = os.path.join(INBOX_DIR, filename)

    # Format the Markdown with Obsidian frontmatter
    md_content = f"""---
title: "{title}"
date: {create_time}
source: Plaud
tags:
  - plaud
  - transcription
  - meeting
---

# {title}

## Summary
{summary}

---

## Full Transcript
{transcript}
"""

    try:
        if not os.path.exists(INBOX_DIR):
            os.makedirs(INBOX_DIR)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"✅ Created: {filename}")
        return jsonify({"status": "success", "file": filename}), 200
    except Exception as e:
        print(f"❌ Error saving file: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"🚀 Plaud Receiver listening on http://0.0.0.0:5001/webhook")
    print(f"📁 Saving files to: {INBOX_DIR}")
    app.run(port=5001, host="0.0.0.0")
