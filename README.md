# Django base

basic [Django](https://www.djangoproject.com/) project image to easy and quickly run up, using [Docker](https://www.docker.com/), [PostgreSQL](https://www.postgresql.org/) and [Bootstrap 4](https://v4-alpha.getbootstrap.com/).

## Run the project

To run the project in a local enviroment, follow next steps:

1. **Install Docker**.

Download Docker from the [offical website](https://docs.docker.com/engine/installation/) and install it.

2. **Clone the project**.

Clone the project code locally using [Git](https://git-scm.com/):

    git clone git@github.com:roadhousestudio/django_base.git

3. **Build the Docker image**

Make sure that Docker is running. Move to the root project folder and run the following command:

    docker-compose build

4. **Run the project**

Run the following command to run the project:

    docker-compose up

Now you can navigate to *localhost:8000* in your browser and you will see a Django project runing.

## Architecture

Python 3.6.0
Django 1.11.7
PostgreSQL 10.1
Bootstrap 4
Jquery 3.2.1

## keep in mind

1. If you will to create your own git repository, move to project root and remove the *.git/* folder configuration running the following comand:

    rm -rf .git/

2. It's amazing if you want to contribute. Please create your pull requests from your own branch to *development* branch.

3. Change the name of the root folder from *django_base* to your project name, and go to *docker-compose.yml* and edit image names from *djangobase* to your project name.

4. If you have any suggestion or you want to contribute, I want to recommend you register it on [utopian.io](https://utopian.io/).
