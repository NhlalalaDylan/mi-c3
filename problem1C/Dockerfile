# Use an official Python runtime as a parent image
FROM python:3.11.2

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for node ID
ENV NODE_ID="default_node_id"

# Run app.py when the container launches
CMD ["python", "main.py"]
