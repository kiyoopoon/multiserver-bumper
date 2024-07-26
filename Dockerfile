# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install discord.py-self
RUN git clone https://github.com/dolfies/discord.py-self && \
    python3 -m pip install -U ./discord.py-self

# Run main.py when the container launches
CMD ["python3", "main.py"]
