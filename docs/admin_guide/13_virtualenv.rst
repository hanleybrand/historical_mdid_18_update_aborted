Python and the Virtual Environment
==================================

.. warning:: This page needs review and likely revision

-----------------

    "Virtualenv is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable." - `Hitchhiker's Guide to Python <http://docs.python-guide.org/en/latest/dev/env/#virtualenv>`__


Install virtualenv
------------------

.. prompt:: bash

   pip install virtualenv


.. note::  if setting up an RHEL 5 server, you need to install python26 & setuptools first
(`walkthrough <http://bda.ath.cx/blog/2009/04/08/installing-python-26-in-centos-5-or-rhel5/>`__)
and use easy\_install with python26, i.e.

.. prompt:: bash

    sudo python26 /usr/lib/python2.6/site-packages/easy_install.py virtualenv

Create a virtualenv for mdid3
-----------------------------

Once installed, make a directory for storing your virtualenv - if you've
installed mdid to /var/local/mdid consider putting your virtualenv in
/var/local/virt to keep things close, but remember to chown/chgrp the
directory so the user ``mdid`` can use it

.. prompt:: bash

    sudo mkdir /var/local/virt
    sudo chown mdid:staff virt
    virtualenv-2.6 -v --no-site-packages virt/mdid3

Ok, so now all you have to do is switch to the virtualenv:

.. prompt:: bash

    source /var/local/virt/mdid3/bin/activate

and your terminal prompt should go from ``$`` to this: ``(mdid3)$`` (if
your prompt is just ``$``)

To switch back to your default system python, just type ``deactivate``
and you'll be back to normal.

bash tip
~~~~~~~~

Add this to your ``.bash_profile`` to activate by typing ``mdid3``:

.. prompt:: bash

    alias mdid3='source /var/local/virt/mdid3-py26/bin/activate'

then type

.. prompt:: bash

    source ~/.bash_profile

to activate your new command.


Now activate

.. prompt:: bash

    source /var/local/virt/mdid3-py26/bin/activate

or (if you listened to my advice about adding the alias to your bash shell)

.. prompt:: bash

    mdid3



Re-get your python libraries
----------------------------


#. ``pip install -r mdid-dep.txt``
#. Sip coffee
#. (optional, not your choice) Curse when you realize it didn't work
   **exactly**.

Reconfigure your apache.conf & wsgi script to use the virtual env
-----------------------------------------------------------------

You'll need to add something like this to your wsgi script and then
restart your webserver (safety note: a typo or wrong path will result in
downtime)

See
`http://code.google.com/p/modwsgi/wiki/VirtualEnvironments <http://code.google.com/p/modwsgi/wiki/VirtualEnvironments>`__
for more information.

httpd.conf
~~~~~~~~~~

::

    WSGIPythonHome /var/local/virt/mdid3-py26/

rooibos.wsgi
~~~~~~~~~~~~

::

    import site
    site.addsitedir('/var/local/virt/mdid3-py26/lib/python2.6/site-packages')
