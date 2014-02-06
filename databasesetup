*Building a database on a Mac*
====================

*Step 1: install Mysql*
Mac: The easiest way to install all necessary packages is to use Homebrew (http://brew.sh/) . You can follow the instructions at the Homebrew site. After that, you need to install the Mysql package. Just open and terminal and type: 
`brew install mysql`

To handle python libs, the best way is to use Pip. You can use Homebrew to install pip:
`brew install pip`

After that, install the Mysqldb-python lib:
`pip install MySQL-python`

*Step 2: Create a database*
`$mysql -u root -p`
`<enter password when asked>`
`create database MYDB;`

*Step 3: Create a user account in the database*
`create user epigraphcollector@localhost' identified by '123456';`
(Here you can change, but you need also change the code too)
`grant all privileges on epigraphDB.* to epigraphcollector@localhost;`
`quit;`
