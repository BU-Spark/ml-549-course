# Creating Reproducible Container Images

Follow these steps to containerize a repository to create a reproducible environment using Docker. In this example we will use the ML-549 course repository as an example 

## Pre-requisites
1. Install Docker https://docs.docker.com/engine/install/ based on your Operating System
2. Create a DockerHub account: https://hub.docker.com/


1. Clone the course repository or a repository of your choice:
```bash
$ git clone git@github.com:oindrillac/ml-549-course.git
$ cd ml-549-course
```

   - Ensure the repository contains a `requirements.txt` file with the necessary dependencies for running the desired notebooks.

2. Add a Dockerfile to the root of the repository with the following content:

The name of the file should be `Dockerfile`

```Dockerfile
# Use an official Python runtime as a base image
FROM registry.access.redhat.com/ubi9/python-311:latest

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the local directory to the working directory
COPY . .

# Install dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Command to run the Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
```

3. Now we will build a Docker using the above Dockerfile:
```bash
$ docker build -t ml-549 .
```

   - After the build completes, check that the image was created:
```bash
$ docker images
```

   - You should see a list of images, including `ml-549`.

4. Run the Docker image to test if it is working as expected:
```bash
$ docker run -p 8888:8888 ml-549
```

   - Open the link prompted in the log to access the Jupyter window. Navigate to the EDA folder and try executing the `eda.ipynb` file.

5. Push the Docker image to Docker Hub (or an alternative container registry):

   - Create an account on [Docker Hub](https://hub.docker.com) or [Quay.io](https://quay.io).

   - Generate an access token on Docker Hub from [Security Settings](https://hub.docker.com/settings/security) and create a repository named `ml549-project` (set it as public).

   - Tag the image:
```bash
$ docker tag ml-549 ochatterjee/ml549-project
```

   - Log in to Docker Hub and use your personal access token to log in:
```bash
$ docker login
Username: ochatterjee
Password: personal-access-token
```

   - Push the latest tagged image:
```bash
$ docker push ochatterjee/ml549-project:latest
```

   - Check the recently pushed image on your Docker Hub repository.

6. Test if someone else can pull the image and run the notebooks:

   - Delete your local images:
```bash
$ docker rmi ml-549
$ docker rmi ochatterjee/ml549-project
```

   - Pull the image:
```bash
$ docker pull ochatterjee/ml549-project
```

   - Run the image:
```bash
$ docker run -p 8888:8888 ochatterjee/ml549-project
```

   - Access the Jupyter notebook in the browser.

---

**Note:** Ensure Docker is properly installed and running on your system for these commands to work. This setup allows you to create a reproducible environment for ML-549 course materials, and you can follow the same instructions for your course project.













