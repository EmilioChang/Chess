#!/bin/bash

# Update system packages
sudo apt update
sudo apt upgrade -y

# Install python3-pip
sudo apt install -y python3-pip

# If running from WSL2
if grep -qi microsoft /proc/version; then
    echo "WSL2 detected. Installing pygame..."
    sudo apt install -y python3-pygame
else
    echo "Debian based system detected. Installing pygame from pip..."
    pip install pygame
fi

echo "Setup completed."
