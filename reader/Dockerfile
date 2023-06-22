# Use an official Python runtime as the base image
FROM python:3.8

RUN mkdir /app

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Set the command to run your app
CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000" ]
