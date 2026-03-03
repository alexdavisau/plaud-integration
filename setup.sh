#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Plaud Integration Setup..."

# 1. Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Error: Docker is not installed. Please install it: https://docs.docker.com/get-docker/"
    exit 1
fi

# 2. Check if Docker Compose is installed
if ! docker-compose version &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Error: Docker Compose is not installed. Please install it: https://docs.docker.com/compose/install/"
    exit 1
fi

# 3. Create necessary directories
echo "📁 Preparing directories..."
mkdir -p inbox

# 4. Build and start the container
echo "📦 Building and starting the Plaud Receiver container..."
docker-compose up -d --build

# 5. Success Message
echo ""
echo "✨ Setup complete!"
echo "🚀 Plaud Receiver is now running in the background."
echo "🔗 Endpoint: http://localhost:5001/webhook"
echo "📁 Inbox: ./inbox"
echo ""
echo "📝 To check logs, run: docker-compose logs -f"
