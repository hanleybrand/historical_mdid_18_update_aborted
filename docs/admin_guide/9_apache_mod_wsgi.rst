===================
Apache and MOD_WSGI
===================

The developers of django recommend using a seperate webserver for static
files on a production system. See How to use Django with Apache and
mod\_wsgi for more information

Edit /etc/apache2/httpd.conf:
-----------------------------

::

    sudo cp /var/local/mdid/dist/linux/httpd.conf /etc/apache2/httpd.conf

and add this line (changing **[/path/to/mdid3\_root]** to your correct
local path)

::

    WSGIScriptAlias / [/path/to/mdid3_root]/rooibos/dist/linux/django.wsgi

    | *note*: the lone forward slash is not a typo - the first “/”
    indicates
    | that mdid will be the root o TRUNCATED! Please download pandoc if
    you
    | want to convert large files.

-  **
-  **
-  **

MPM not Pre-fork[1]
-------------------

    "The worker MPM uses multiple child processes with many threads
    each. Each thread handles one connection at a time. Worker generally
    is a good choice for high-traffic servers because it has a smaller
    memory footprint than the prefork MPM." - `Switching Apache from
    Prefork to Worker MPM in RHEL / CentOS 5.x / Fedora 13 <1>`__

RHEL / CentOS 5.x / Fedora 13
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify ``/etc/sysconfig/httpd`` so that the following line is
**uncommented**:

::

    HTTPD=/usr/sbin/httpd.worker

Apache must be restarted after that, either via

::

    sudo apachectl restart

or

::

    sudo apachectl stop
    sudo apachectl start

confirm via $ /usr/sbin/apachectl -V

    Server version: Apache/2.2.3

    Architecture: 32-bit

    ::

        Server MPM:     Worker

    threaded: yes (fixed thread count)

    forked: yes (variable process count)

    Server compiled with....

    -D APACHE\_MPM\_DIR="server/mpm/worker"

..etc...

--------------

`1 <http://www.jqueryin.com/2010/08/07/switching-apache-prefork-to-worker-mpm-in-rhel-centos-5x-fedora-13>`__
