==============
Database Setup
==============

Microsoft SQL Server
--------------------

   - Create a new database and user account
   - Make the user account owner of the new database
   - If you want to run unit tests using SQL Server, give the account the *dbcreator* server role.




MySQL
-----


Create a text file called :file:`mdid.sql`

.. prompt::

    nano mdid.sql

and type this text in

.. code-block:: sql

    CREATE DATABASE rooibos CHARACTER SET utf8;
     GRANT ALL PRIVILEGES ON rooibos.* TO rooibos@localhost
       IDENTIFIED BY 'rooibos';
     UPDATE mysql.user SET Select_priv='Y',Insert_priv='Y',
       Update_priv='Y',Delete_priv='Y',Create_priv='Y',
       Drop_priv='Y',Index_priv='Y',Alter_priv='Y'
       WHERE Host='localhost' AND User='rooibos';
     FLUSH PRIVILEGES;
     \q

and then run the script with mysql

.. code-block:: shell

    mysql -u 'root' -p < mdid.sql

type the following two commands at /var/local/mdid/rooibos :

.. code-block:: sql

    python manage.py syncdb --noinput
    python manage.py createcachetable cache
