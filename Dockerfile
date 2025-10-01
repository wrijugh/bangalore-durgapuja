# Use the official Python image
FROM python:3.11-slim

# Set environment variables to prevent Python from buffering its output 
# and ensure Streamlit knows which port to use.
ENV PYTHONUNBUFFERED 1
ENV STREAMLIT_SERVER_PORT 8501

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first. This leverages Docker's caching:
# if requirements.txt doesn't change, these layers won't be rebuilt.
# COPY requirements.txt .
RUN pip install streamlit pandas

# Copy the rest of the application files (including streamlit_app.py)
COPY . .

# Expose the port where Streamlit will run
EXPOSE 8501

# Command to run the Streamlit application
# We use 'CMD' to run the app when the container starts.
# --server.address 0.0.0.0 is crucial so the app is accessible outside the container.
CMD ["streamlit", "run", "durgapuja.py", "--server.port", "8501", "--server.address", "0.0.0.0"]