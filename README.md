# DevOps Bus Schedule Viewer 🚌

A modern Flask web application displaying the local bus schedule for Saraswati College of Engineering, deployed using a complete CI/CD pipeline. 

## Project Architecture
This project demonstrates a fully automated DevOps workflow:
* **Version Control:** Source code is hosted and managed on GitHub.
* **Continuous Integration:** Jenkins automatically pulls new code, sets up a Python virtual environment, and runs Pytest verification.
* **Containerization:** The application is packaged into a standalone Docker container for consistent deployment.
* **Cloud Infrastructure:** Hosted on an AWS EC2 Ubuntu instance with exposed security group ports for web access.

## Application Endpoints
* `/` - Main landing page and UI.
* `/routes` - Displays active transit routes (e.g., Campus to Thane East).
* `/health` - Returns a 200 OK `{"status": "healthy"}` JSON response for infrastructure monitoring.

## Developer
Developed by Tanishq Dinesh Jadhav.