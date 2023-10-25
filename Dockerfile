# Use an official Python runtime as a parent image
FROM python:3.9-slim

 

# Set the working directory to /app
WORKDIR /app

 

# Copy the current directory contents into the container at /app
COPY . /app

 

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y git


VOLUME /efento_server

# Make port 80 available to the world outside this container
EXPOSE 3737

 

# Define environment variable
ENV NAME EfentoServer

 

# Run app.py when the container launches
CMD ["python3", "main.py"]