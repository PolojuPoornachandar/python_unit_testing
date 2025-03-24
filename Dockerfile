# Step 1: Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to install dependencies
COPY requirements.txt /app/

# Step 4: Copy the rest of your application code to the container
COPY . /app/

# Step 5: Expose the port that your application runs on
EXPOSE 5000

# Step 6: Run the application (adjust this based on how you want to execute your tests)
CMD ["python", "-m", "unittest", "discover", "-s", "test_calculations.py"]


