# Cloud App Deployment

A simple Python Flask web app deployed on AWS EC2 using Ubuntu, Gunicorn, Nginx, and systemd.

## Live Demo
http://3.138.194.188

## Tech Used
- Python
- Flask
- AWS EC2
- Ubuntu Linux
- Gunicorn
- Nginx
- systemd

## What I Did
- Built a simple Flask web app locally
- Launched and configured an AWS EC2 Ubuntu server
- Opened and managed security group rules for ports 22, 80, and 5000
- Deployed the app with Gunicorn
- Configured Nginx as a reverse proxy
- Created a systemd service so the app runs in the background
- Debugged firewall, socket, and permission issues during deployment

## What I Learned
- How cloud deployment works end to end
- How to use Linux commands on a live server
- How Nginx and Gunicorn work together
- How to debug real deployment issues
