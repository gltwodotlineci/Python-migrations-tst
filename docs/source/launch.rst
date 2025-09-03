Launching
===================================
We will procide with a step-by-step guide to launch the application.

Envirenement Variables
-----------------------------------
First let start with Sentry. As you see in settings.py there is a variable called SENTRY_DSN.
You need to add your own DSN from Sentry. You can find it in your project settings in Sentry.
Add it to your .env file.

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
