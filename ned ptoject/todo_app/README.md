# Create a new project
poetry new todo_app
cd todo_app

# Add dependencies
poetry add streamlit fastapi uvicorn sqlmodel sqlalchemy

# Define the Database Model
Create a SQLModel model:
Create a file models.py and define your to-do item model

# Create the database:
Create a file database.py for initializing the database

# Create the FastAPI Backend
Create a FastAPI app:
Create a file main.py for your FastAPI application

# Run FastAPI server
poetry run uvicorn main:app --reload

# Create the Streamlit Frontend
Create a Streamlit app:
Create a file streamlit_app.py

# Run Streamlit app
poetry run streamlit run streamlit_app.py

# Create a Dockerfile: 
This file contains instructions for building the Docker image

# Create a .dockerignore File: 
This file specifies which files and directories to ignore when building the Docker image

# Build the Docker Image
Navigate to the directory containing your Dockerfile and run the following command to build the Docker image
docker build -t my-fastapi-app .

# Run the Docker Container: 
After building the image, you can run a container based on that image
docker run -d --name fastapi-container -p 8000:8000 my-fastapi-app

# Create a docker-compose.yml File

# Run Docker Compose
docker-compose up -d

# Build and Run the Services
docker-compose up --build
