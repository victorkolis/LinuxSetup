#!/bin/bash

# First setup and installation
sudo apt update
sudo apt install docker
sudo apt install docker-compose

# Second upgrade check
sudo apt update && sudo apt upgrade -y

# Post install config
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker 
docker run hello-world

# Error handling
# sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
# sudo chmod g+rwx "$HOME/.docker" -R

# Run docker on system start
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
# sudo systemctl disable docker.service
# sudo systemctl disable containerd.service
