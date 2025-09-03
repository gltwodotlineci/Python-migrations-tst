Launching credentials
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
    # If for a reason you can't add it. Add .env file in the host plaftorm.

Example format:

.. code-block:: bash

    SECRET_KEY=your-secret-key

For the continues deployment, you will need `DOCKER_HUB_ACCESS_TOKEN` and `DOCKER_HUB_USERNAME` as well, but
it will be explained further to the deployment part.


The tools for launching the aplication in public.
--------------------------------------------------
The most important tools that you need are a version control system and a virtual machine or a containerization platform (in our case we are using the second one).
and a Platform-as-a-Service (PaaS).

For the version control system I recommend 'Github', docker for the containerization platform and For the PaaS service I'm using 'Render'.

So once you have an account in this three tools, you will have to creat some token keys.
Because you have to guarantee that this platforms will be able to communicate with each other.
But at this stage, the most important thing is to connect your Github account with your Pc and also
a repository where you will store the app. Than you can push your app with your changes or as it is.
