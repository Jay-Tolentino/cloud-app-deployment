# Cloud App Deployment on AWS (Flask + Nginx + Gunicorn)

Deployed a production-style Python web application on AWS EC2, configuring a full Linux-based backend stack with Nginx, Gunicorn, and systemd. This project focuses on understanding real-world deployment, networking, and debugging at the infrastructure level.

## 🚀 Live Demo
http://3.138.194.188

---

## 🧠 Architecture

Client → Nginx (Port 80) → Gunicorn (Unix Socket) → Flask Application

- **Nginx** handles incoming HTTP traffic
- **Gunicorn** serves the Python application
- **Flask** processes requests and returns responses
- **Systemd** ensures the app runs continuously in the background

---

## 🛠 Tech Stack

- Python (Flask)
- AWS EC2 (Ubuntu Linux)
- Gunicorn (WSGI Server)
- Nginx (Reverse Proxy)
- systemd (Service Management)
- Git / GitHub

---

## ⚙️ Key Features

- Deployed a cloud-hosted web application accessible via public IP
- Configured Nginx as a reverse proxy for clean routing (no port exposure)
- Implemented Gunicorn for production-level request handling
- Created a systemd service for persistent background execution
- Managed AWS security groups for controlled network access

---

## 🔧 Deployment Process

1. Launched and configured an AWS EC2 Ubuntu instance  
2. Installed Python environment and dependencies  
3. Built and tested a Flask web application locally  
4. Deployed the app using Gunicorn with a Unix socket  
5. Configured Nginx to forward HTTP traffic to the application  
6. Created a systemd service for continuous uptime  
7. Configured AWS security groups (ports 22, 80, 5000)  

---

## 🧩 Challenges & Solutions

- **Application inaccessible externally**  
  → Diagnosed and fixed AWS security group rules (opened required ports)

- **502 Bad Gateway errors**  
  → Debugged Nginx to Gunicorn communication via Unix sockets

- **Permission denied on socket**  
  → Resolved Linux file and socket permissions using `chmod` and `umask`

- **Nginx unable to reach application**  
  → Fixed directory traversal permissions (`/home/ubuntu`) to allow access

---

## 📚 What I Learned

- End-to-end cloud deployment of a backend application  
- How web servers (Nginx) and application servers (Gunicorn) interact  
- Linux system administration and permission management  
- Debugging real infrastructure and networking issues  
- How production environments differ from local development  

---

## 🔮 Future Improvements

- Add a custom domain name  
- Enable HTTPS with SSL (Let’s Encrypt)  
- Containerize application using Docker  
- Integrate a database backend  
- Implement CI/CD pipeline for automated deployment  