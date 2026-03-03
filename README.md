# Plaud Integration (Local Markdown Hub)

This project provides a local endpoint to capture your Plaud voice recordings, summaries, and transcripts from Zapier and save them as formatted Markdown files.

## 🚀 How It Works
1.  **Plaud Cloud:** Your device syncs a recording.
2.  **Zapier:** A "Transcript & Summary Ready" trigger is fired.
3.  **Webhook:** Zapier sends a POST request to this receiver.
4.  **Local Hub:** This receiver saves a `.md` file to your `/inbox` folder with Obsidian-compatible frontmatter.

## 📦 Production Setup (New Machine)

### 1. Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Quick Install
To build and start the service on a new machine:
```bash
cd plaud-integration
chmod +x setup.sh
./setup.sh
```

### 3. Manual Start
If you prefer manual commands:
```bash
docker-compose up -d --build
```

## 🛠 Configuration

### Port and Endpoint
- **Port:** `5001` (to avoid macOS AirPlay conflicts)
- **Endpoint:** `http://<YOUR_IP>:5001/webhook`

### Zapier Setup
1.  **Trigger:** PLAUD — "Transcript & Summary Ready"
2.  **Action:** Webhooks by Zapier — "POST"
3.  **URL:** Use your local IP or an `ngrok` tunnel pointing to port 5001.
4.  **Payload:**
    - `title`
    - `summary`
    - `transcript`
    - `create_time`

## 📁 File Structure
- `inbox/`: All generated Markdown files land here.
- `receiver.py`: The Python Flask logic.
- `docker-compose.yml`: Orchestration for the container.
