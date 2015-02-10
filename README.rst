Overview
----------
This is code based on a tutorial located at: http://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

Usage
-------
To setup start a virtualenv and install the requirements with pip::

   virtualenv venv
   source venv/bin/activate
   pip install -r requirements

Now create the database and tables by running the following command::

   python sqlite_ex.py

Then query the resulting database as follows::

   python sqlite_q.py

Playing with SQLAlchemy
--------------------------
Initialize using the following command::

  python sqlalchemy_create.py

To play around with the resulting database use the following command::

  python sqlalchemy_interactive.py
