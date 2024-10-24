# Dockerized Flask CRUD Application with SQLite and Container Management

This project is a multi-container Flask web application with SQLite as the database. The application is fully containerized using Docker, and Docker Compose is used to manage the containers and their networks. A Python script monitors the health of the Flask container and automatically restarts it if it becomes unhealthy.

## Project Structure
```
├── app.py                   # Flask web application
├── Dockerfile                # Dockerfile for Flask app container
├── manage_containers.py      # Docker container management script
├── docker-compose.yml        # Docker Compose configuration
├── requirements.txt          # Python dependencies
├── templates/                # HTML templates for Flask app
│   └── index.html            # Main page
├── static/                   # Static files (CSS, JS)
├── data.db                   # SQLite database file
```

## Features
- **CRUD Functionality**: Users can create, read, update, and delete records in the database.
- **SQLite Database**: Persistent data storage using SQLite.
- **Containerized Application**: Flask app and SQLite are containerized and networked using Docker.
- **Health Monitoring**: A Python script monitors the health of the Flask container and restarts it if it becomes unhealthy.

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Steps to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a Docker Network**:
   ```bash
   docker network create flask-network
   ```

3. **Build the Containers**:
   ```bash
   docker-compose build
   ```

4. **Start the Application**:
   ```bash
   docker-compose up -d
   ```

5. **Access the Application**:  
   Open a web browser and go to `http://localhost:5000`.

6. **Monitor Container Health**:  
   The `manage_containers.py` script will automatically restart the Flask container if it becomes unhealthy:
   ```bash
   python manage_containers.py
   ```

### Stopping the Containers
To stop and remove all containers:
```bash
docker-compose down
```

## Advantages of Docker Compose
- **Simplifies container management** by running multi-container Docker applications using a single YAML file.
- **Easy to scale services**, manage networks, and persist data across container restarts.
- **Efficient container orchestration** for development and testing environments.

---
