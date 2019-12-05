hi this is for anybody who wants to help. this code does not works fortunatly, but is identical to the code that does work;
This is a long version of my project which has a problem with a view function that does not return upon validate, it is 
the funtion "books" and "stock" which does not return on the main project. but it is a lot larger with several foriegn keys
There are several .csv files that need to be loaded, start with pid jn type aux gen and finish with books.csv.  there is also 
a requirements.txt
using the add_book link Follow these steps and all should work!!!!!

python3 -m venv env

. env/bin/activate

pip3 install flask

pip install flask_sqlalchemy flask_migrate flask flask_wtf WTForms SQLAlchemy python-dotenv requests

sudo apt-get install mariadb-server mariadb-client

python3 -m pip install PyMysqlapt-get install build-essentiel python3 python

apt-get install python3-dev python-dev

CREATE DATABASE bdf;

CREATE USER accounting IDENTIFIED BY 'password';

GRANT USAGE ON . TO accounting@localhost IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON bdf.* TO 'accounting'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR accounting@localhost;

flask db init

flask db migrate -m "book table"

flask db upgrade

To register a new user use 
http://localhost/register


