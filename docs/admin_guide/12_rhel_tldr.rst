RHEL TLDR;
==========

EPEL rpm repo
-------------

.. prompt:: bash

    sudo rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-4.noarch.rpm
    rpm -Uvh http://yum.chrislea.com/centos/5/i386/chl-release-5-3.noarch.rpm
    rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CHL

git
----


.. prompt:: bash

    sudo yum install git-core

yum yum
-------

.. prompt:: bash

    sudo yum install python26 python26-devel mysql-server python26-setuptools java-1.6.0-openjdk  libjpeg-devel unixODBC unixODBC-devel freetds-devel  MySQL-python26 python-ldap python-memcached mod_wsgi gcc-c++ pyodbc


add alias for running easy\_intall & pip via python26
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash

    alias easy26='sudo python26 /usr/lib/python2.6/site-packages/easy_install.py'
    easy26 pip

optional, but do yourself a favor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. prompt:: bash

    pip install virtualenv
    sudo mkdir /var/local/virt
    sudo chown mdid:staff virt
    virtualenv-2.6 -v --no-site-packages virt/mdid3
    source virt/mdid3/bin/activate

... and then when you're done

.. prompt:: bash

    deactivate
