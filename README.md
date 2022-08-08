# Python-Musings
Random Snippets of useful python

This is a repo of different scripts to demonstrate various python functionalities. All of the examples are tested and running in python 3.9.*


Postgre 
to install and configure a basic postgre sql database
https://kb.objectrocket.com/postgresql/how-to-create-a-role-in-postgres-1454

to configure the db to listen for external connections

location of postgre config files
/etc/postgresql/14/main

run command:

sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

then to access the local db control

sudo su - postgres  
psql

then to see existing roles 
\du

then run the following query 
CREATE ROLE <username> WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD '1234';


after that configure the installation to listen for all connections (this is for a development and testing environment ONLY)
