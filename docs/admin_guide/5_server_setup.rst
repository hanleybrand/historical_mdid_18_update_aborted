============
Server Setup
============


As might be expected for a web application as complex and flexible as
mdid3, a number of configuration steps are required to get going.

Setup user accounts
-------------------

Create MDID user account
~~~~~~~~~~~~~~~~~~~~~~~~

(this allows mdid3 to run programs on it’s own behalf)

::

    sudo adduser mdid

Add admin account (not the mdid utility account) to the staff group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    sudo nano /etc/group

Find the following line and append your username (not mdid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    staff:x:50:

    it will look like this when you’ve done it

    ::

        staff:x:50:mdid3admin:

    | (**ctrl-x** will exit, prompting you to "*save modified buffer*\ "
    (i.e.
    | the file you have open) - type “y” and the return/enter key to
    save
    | before exiting )

*Important:* **Log out of the command line and log back in**
