The deployment
===================================

The main tools used for deployment.
--------------------

The Dockefile
---------------------------------------
The Dockerfile is a text document in yml or ymal format that contains all the commands 
and create an image based on the image. Using docker build users can create an automated build that executes several command-line instructions in succession.


ci/cd
---------------------------------------
In the workflow we need to define the steps that will be executed in the build and deployment of the project.
The workflow is defined in the file .github/workflows/ci_cd.yml and it is executed by Github Actions.
So we can have a continues integration and deployment of the project.

The deployment
---------------------------------------

The deployment is done using Github Pages.
The repository is created in Github and the code is pushed in the repository.
The branch master is used for the production version of the project.

Actions in github.
-----------------------------------------------
At this stage the actions will fail because we don't have the Docker Hub acces identification.
We can produce on our Docker Hub account a 'DOCKER_HUB_ACCESS_TOKEN' and record it in githube.

.. note::

   On Settings of our ripository.
    In the left sidebar, go to Secrets and variables → Actions.
    Click New repository secret.
    Add: Name → DOCKER_HUB_ACCESS_TOKEN Value → paste your Docker Hub access token


Platform-as-a-Service (PaaS) part.
-----------------------------------------------


First you need to create a repository in Github and push the code in the repository.
use the branch master for the production version (you will see why in the explenantion of
continues deployment).

If you have a dockerhub account you need to create a ripository. than in the personal
access tokens you shall create 2 tokens: 'RENDER_TOKEN' and 'DOCKER_HUB_ACCESS_TOKEN'.(or the name of other web server plaftorm),
'DOCKER_HUB_ACCESS_TOKEN'. This tokens will be saved in the web version control system
and in the web server plaftorm.

When you create a web service in Rener or in an other platform, you can add the 'RENDER_TOKEN'
the credentials options. Once you create


Than you need to create a Render project and associete the docker image

and add the repository in the project. Than you can launch the project in
Render.

In Render you can use the next commands to launch the project:

.. code-block:: bash

    docker-compose up -d
.. code-block:: yml


Launchement in local
-----------------------------------

In your local machine.
--------------------------------------------------
In your local machine you will need just to check the dockerc-ompse.yml
file that you can find in the repository `docker`.
In the docker-compose.yml check for the Port part.

.. code-block:: yml

    ports:
      - "8003:8000"

***The port 8003 is the port that you will use to access the application.***
change it if you want or need to use another port.***

Than you can launch the docker with the next commands:

.. code-block:: bash

    cd docker
    docker-compose up -d