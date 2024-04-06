# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# pip packages
RUN pip install git+https://github.com/ye4241/discord.py-self.git

# Run main.py when the container launches
CMD ["python3", "main.py"]
