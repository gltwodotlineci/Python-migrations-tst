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
    - In the left sidebar, go to Secrets and variables → Actions.
    - Click New repository secret.
    - Add: Name → DOCKER_HUB_ACCESS_TOKEN Value → paste your Docker Hub access token
    - You will do the same for the 'DOCKER_HUB_USERNAME'.
    - Add: Name → DOCKER_HUB_USERNAME Value → paste your Docker Hub username


Platform-as-a-Service (PaaS) part.
-----------------------------------------------
You can start create a web servervice in PaaS, in our case Render.


.. note::

   In the left side bar of Render, go to Envirenment.
    - First create a token key for Render in Docker Hub.
    - Then when you create the web service choose the option existigng image.
    - Add the name of the image in Docker Hub and also add the credentials the token you created on Docker Hub.
    - Then you can start creating the web service.
    - After that in the Envirenment variables of Render add the variable 'SECRET_KEY' with a value of your choice.

    - Once you created the web service you can access it in the url of the web service.
    - And to activate the continues deployment you need to add the 'Deploy Hook' in your Github repository.
    - So copy it and in your github environment variables add the name 'RENDER_WEBHOOK' and paste the webhook url.


The solution for the static files.
-----------------------------------------------
Your application is published, but you will notice that it looks like no css has been used.
Actually, the css and all static files are not in the public folder, so it is not being served.
One solution is to create a small web service that will serve the static files.
In our case we will use Amazon S3 to store the static files.
You can create a bucket in S3 and also a Key with it secret key.
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are the environment variables that you need to add in Render.

Now the application might have all its colors and styles.



Launchement in local
-----------------------------------

In your local machine.
--------------------------------------------------
In your local machine you will need just to check the dockerc-compse.yml
file that you can find in the repository `docker`.
In the docker-compose.yml check for the Port part.

.. code-block:: yml

    ports:
      - "8003:8000"

***The port 8003 is the port that you will use to access the application. change it if you want or need to use another port.***

Than you can launch the docker with the next commands:

.. code-block:: bash

    cd docker
    docker-compose up -d