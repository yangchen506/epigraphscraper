*Building a database on a Mac*  
====================

*Step 1: install Mysql*

Mac: The easiest way to install all necessary packages is to use Homebrew (http://brew.sh/) . You can follow the instructions at the Homebrew site. After that, you need to install the Mysql package. Just open and terminal and type: 
`brew install mysql`

To code in python you'll need a program called Pip. Homebrew provides Pip via
`brew install python` (Preferred option since OS X's built-in version of python is usually less-than-current.) 

However you will then have two Pythons installed on your Mac, so alternatively you use 
`sudo easy_install pip`. (Not the preferred option.)  


After that, install the Mysqldb-python lib:
`pip install MySQL-python`

NOTE: If homebrew and pip are having problems installing packages, it could be that your permissions on OS X need to be fixed. You can easily check and fix your permissions using Apple's "Disk Utility" program.

*Step 2: Start & stop mySQL server* 

There are a number of ways to start your mysql database:
(1) `mysqld` (starts server regardless of OS being used; not preferred)

(2) `mysqld_safe` (tries to predict best sql settings and then starts server; still not preferred)

(3) Use the mysql.server script to start and stop server. Simply type at terminal:
`mysql.server start' (starts server, preferred)
`mysql.server stop' (stops server, preferred)    


*Step 3: Create a user account in the database*

`create user collector@localhost' identified by '123456';`

(Here you can change, but you need also change the code too)

`grant all privileges on EPIDB.* to collector@localhost;`

`quit;`
