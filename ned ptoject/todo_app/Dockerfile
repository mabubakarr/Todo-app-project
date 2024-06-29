# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install the dependencies specified in pyproject.toml
RUN poetry install --no-root
RUN pip install streamlit

# Copy the rest of the application code to the working directory
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000 8501

# Run uvicorn server and Streamlit app
CMD ["sh", "-c", "poetry run uvicorn todo_app.main:app --host 0.0.0.0 --port 8000 & poetry run streamlit run todo_app/streamlit_app.py --server.port 8501 --server.enableCORS false"]
