# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./src/requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# Copy the rest of the application code into the container at /app
COPY ./src/main.py /app
COPY ./src/text_vectorization.py /app

# Start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
