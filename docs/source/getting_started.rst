Welcome to the Lettings Application
===================================

This application can be used to create and list rental places all around
the world and view the details of each place.

Technical Background
--------------------

To adapt this app from its original version, it was necessary to create
two new Django apps: ``lettings`` and ``profiles``.  
The data was then migrated into the models of these new apps, and the
views and URLs were updated accordingly to use ``lettings`` and ``profiles``.

Download Repository
-------------------

.. code-block:: bash

   git clone https://github.com/gltwodotlineci/Python-migrations-tst.git
   # Or if you have the SSH key configured in your GitHub account:
   git clone git@github.com:gltwodotlineci/Python-migrations-tst.git
   # Enter the repository directory:
   cd Python-migrations-tst

Preparing Virtual Environment
-----------------------------

If you want to use Poetry:

.. code-block:: bash

   # Install Poetry:
   pip install poetry
   # Or install directly with curl:
   curl -sSL https://install.python-poetry.org | python3 -
   # After installation, set up the virtual environment:
   poetry update
   poetry shell
   # !!! Verify that the root directory contains both 'poetry.lock' and 'pyproject.toml'
