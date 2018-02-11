*** Using MySQL with Django ***

Look at myfitapp as an example.
Within a virtual environment with python3.6, before being able to use MySQL I had to install mysqlclient.
But mysqlclient has dependencies, hence these are the parts I installed:

sudo apt-get install python3.6-dev libmysqlclient-dev
pip install mysqlclient

Once this is done, and having setup the connection to the db in setting.py, create the schema in MySQL and then the initial migrations can be run.
