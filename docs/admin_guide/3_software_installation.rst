=====================
Software Installation
=====================


********************
Install dependencies
********************


Package Management systems
=====================================

.. rst-class:: lead
To install the software dependencies required for mdid3 to run, use the
system-specific methods listed below. Feedback and alternative
procedures are welcome, please feel free to submit them.

------------


**Package Management System/Command**

.. raw:: html

    <table width="100%" class="table table-bordered">
    <tbody class="table-striped table-hover">
    <th width="25%" >Ubuntu</th>
    <th width="25%" >Red Hat</th>
    <th width="25%" >Mac OS X</th>
    <th width="25%" >Windows 2008 or other</th>

    <tr>
    <td >
    <a href="https://help.ubuntu.com/community/AptGet/Howto">apt-get</a> </td>
    <td >Redhat - <a href="http://www.ibm.com/developerworks/linux/library/l-lpic1-v3-102-5/">yum</a> <a href="https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/c1-yum.html">rhel 5</a> | <a href="https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/ch-yum.html">rhel 6</a> </td>
    <td > <a href="http://mxcl.github.com/homebrew/">homebrew</a>, .pkg installers, source</td>
    <td >None (true? any dissent?).<br>Download installers or executables.</td>
    </tr>
    </tbody></table>



.. raw:: html

    <table width="100%" class="table table-bordered">
    <tbody class="table-striped table-hover">
    <tr>
    <td width="16%" >&nbsp;</td>
    <th width="21%">Ubuntu</th>
    <th width="21%">Red Hat</th>
    <th width="21%">Mac OS X</th>
    <th width="21%">Windows 2008 or other</th>
    </tr>
    <tr></tr>
    <tr>
    <th>python</th>
    <td >installed</td>
    <td ><pre><code>python26</code></pre></td>
    <td ><a href="http://mac.github.com">installed</a></td>
    <td >Python 2.7.3 <br>(<a href="http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi">32-bit</a>) | (<a href="http://www.python.org/ftp/python/2.7.3/python-2.7.3.amd64.msi">64-bit</a>)</td>
    </tr>
    <tr><th>git</th>
    <td ><pre><code>git-core</code></pre></td>
    <td ><pre><code>git-core</code></pre></td>
    <td ><a href="http://mac.github.com">Github for Mac</a></td>
    <td ><a href="http://windows.github.com">Github for Windows</a></td>
    
    </tr>
    </tbody>
    </table>


Below is a matrix of the software dependencies required for mdid3 to run
correctly. In general, software installed via a package manager like apt
or yum will be displayed as ``package-name`` whereas a downloadable
installer, binary or downloadable source will be a `text link <#>`__

Apt and Yum generally need to be run via sudo, but the Mac OS X package
manager homebrew is designed specifically to **not** use sudo (assumedly
because the normative mac user account has installation privileges). So
to install the software package :file:`packageX`, use the commands:

.. glossary::

    apt-get (Ubuntu)
        .. prompt:: bash

            sudo apt-get install packageX

    yum (Red Hat)
        .. prompt:: bash

            sudo yum install packageX


    homebrew (Mac OS X)
        .. prompt:: bash

            brew install packageX


Optionally, package managers can be given a list of packages, and be
told to say "yes" to every question, and the human being installing the
software can do something important, like drink coffee. A
copy/paste-able single command will be presented at the bottom of the
matrix.

--------------


Ubuntu
~~~~~~

.. prompt:: bash

    sudo apt-get -y upgrade && install

.. prompt:: bash

    sudo apt-get  -y install openjdk-6-jre-headless python-setuptools libjpeg62-dev unixodbc unixodbc-dev freetds-dev tdsodbc python-dev libmysqlclient16-dev  python-ldap python-memcache memcached libapache2-mod-wsgi g++ mysql-server

Redhat Packages
~~~~~~~~~~~~~~~

TBD

Mac OS X homebrews
~~~~~~~~~~~~~~~~~~

TBD

Windows Installers
~~~~~~~~~~~~~~~~~~

TBD
