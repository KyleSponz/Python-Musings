
#To install a development server on ubuntu 


location of postgre config files
/etc/postgresql/*/main

run command:

sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

then to access the local db control

sudo su - postgres  
psql

then to see existing roles 
\du

then run the following query change username and password to your needs 
CREATE ROLE <username> WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD '1234'; 


after that configure the installation to listen for all connections (this is for a development and testing environment ONLY)
set the following in postgresql.conf
listen_addresses = '*'

add the following to pg_hba.conf


citations
https://kb.objectrocket.com/postgresql/how-to-create-a-role-in-postgres-1454
host    all             all             0.0.0.0/0               scram-sha-256