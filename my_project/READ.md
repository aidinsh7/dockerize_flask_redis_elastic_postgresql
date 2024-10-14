This project is a simple web application written in Python using the Flask framework, interacting with a PostgreSQL database, Redis cache, and Elasticsearch search engine.

Project Structure
 
my_project/
│
├── app/
│   ├── app.py
│   └── requirements.txt
├── docker-compose.yml
└── Dockerfile
Prerequisites
To run this project, you need Docker and Docker Compose installed.

Installation:


1.Clone the project:
git clone https://github.com/aidinsh7/dockerize_flask_redis_elastic_postgresql/tree/main/my_project

cd my_project

2.Build and start services:
Use the following command to build the Docker image and start all services:
docker-compose up --build
Accessing the Application

3.After starting, your application will be accessible at the following address:
http://localhost:5000



File Descriptions:
app.py: This file contains the main application code that establishes connections to Redis, PostgreSQL, and Elasticsearch.
requirements.txt: This file lists the required libraries for the project.
Dockerfile: This file is used to create the Docker image for the application.
docker-compose.yml: This file is used to define and start all services (application, database, cache, and search engine).
Library Usage Guide
Flask: A web framework for developing web applications.
redis: A library for working with Redis as a cache.
elasticsearch: A library for interacting with Elasticsearch.
