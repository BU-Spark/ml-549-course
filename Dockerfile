# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the local directory to the working directory
COPY . .

# Install dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Command to run the Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

