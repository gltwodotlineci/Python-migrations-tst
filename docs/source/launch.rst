Launching
===================================
We will procide with a step-by-step guide to launch the application.

Envirenement Variables
-----------------------------------
Sentry
----------------------------------------------------
First let start with Sentry. As you see in settings.py there is a variable called **SENTRY_DSN**.
You need to add your own DSN from Sentry. You can find it in your project settings in Sentry.
Add it to your **.env** file.
**Attention when you use .env. It is imperative to add .env in .gitignore file.**

In your Sentry account you can find it here:
Go to Project Settings:
On the left-hand sidebar, click Settings → Projects → [Your Project].
Find Client Keys (DSN):
Inside your project settings, click Client Keys (DSN).
Here you’ll see your DSN URL. You can copy it directly.

  

Example format:

.. code-block:: bash
    https://<PUBLIC_KEY>@o123456.ingest.sentry.io/123456


Than you create a .env file and add the variable:

.. code-block:: bash

    SENTRY_DSN=https://your-dsn-from-sentry.com

Django Secret Key
----------------------------------------------------
You need to add your own secret key to a .env file, or in **Render** if you are using it as your web server.
In settings.py, you will find **SECRET_KEY**. Use the default key in debug mode and in production your own secret key.
Add it to your .env file. Or in the Host platform (Render in my case) add it as an environment variable.
**Attention If you use .env, do not forget to add .env in .gitignore file.**

Example format:

.. code-block:: bash

    # in .env file
    SECRET_KEY=your-secret-key
    # Attention: Most Host servers have their field where you can add environment variables.
    # If for a reason you can't add it to .env file in the host plaftorm.

Example format:

.. code-block:: bash

    SECRET_KEY=your-secret-key

For the continues deployment, you will need `DOCKER_HUB_ACCESS_TOKEN` and `DOCKER_HUB_USERNAME` as well, but
it will be explained further to the deployment part.

Launchement
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


In a public server
--------------------------------------------------
In a public server the simplest way is to use a server platform and a
public version control.

.. code-block:: yml
