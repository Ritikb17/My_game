FROM python:3.10.11-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory inside the container
WORKDIR /app

# Install any necessary dependencies
#RUN pip install --no-cache-dir <your_requirements.txt>

# Run the Python script when the container launches
CMD [ "python", "Mygame.py" ]
