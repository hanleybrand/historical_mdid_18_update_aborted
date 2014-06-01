Installation Guide
==================

.. sectionauthor:: Peter Hanley
.. publishdate:: 2014-04-25
.. summary:: An overview of the MDID3 installation process

.. index::
    single: installation
    single: windows
    single: iis
    single: linux
    single: apache

.. warning::
    **Note**: This page is a work in progress - ask on the list if a
    step doesn't make sense

The Madison Digital Image Database is a freely distributed, open source
web application developed at James Madison University. MDID is a digital
media management system with sophisticated tools for discovering,
aggregating, and presenting digital media in a wide variety of learning
spaces.

-  MDID3 Website: http://mdid.org
-  Official Repository:
   https://github.com/cit-jmu/rooibos/tree/experimental
-  MDID3 Mailing List:
   https://listserv.jmu.edu/cgi-bin/wa?SUBED1=mdidusers-l&A=1

Please join the list and introduce yourself if you end up working with
MDID3.

Technical Overview
------------------

MDID3 is a `django web application <https://docs.djangoproject.com/>`__
that requires at minimum to run:

-  a web server capable of serving WSGI applications, either using
   `mod\_wsgi <http://code.google.com/p/modwsgi/>`__ with `Apache HTTP
   Server <http://httpd.apache.org>`__ or other alternative that works
   similarly (e.g.`uWSGI <https://github.com/unbit/uwsgi-docs#readme>`__
   & `nginx <http://wiki.nginx.org/Main>`__) or `Microsoft
   IIS <http://www.iis.net>`__ with
   `pyisapie <http://sourceforge.net/apps/trac/pyisapie>`__

   -  the webserver needs to be able to run python as a daemon for
      worker processes like image processing, data import, etc.

-  a `Apache Solr <http://lucene.apache.org/solr/>`__ server for search
-  a memory object caching server like
   `memcached <http://memcached.org>`__ or `Couchbase
   Server <http://www.couchbase.com/couchbase-server/overview>`__
-  a database server - all known installations are currently based in
   `mySQL <http://www.mysql.com/downloads/mysql/>`__ or MS SQL Server,
   but Postgress should theoretically work - let us know, won't you?
-  `django 1.2.3 <https://docs.djangoproject.com/en/1.2/>`__ is the most
   used, but 1.2.7 looks stable. It is possible that it is fully
   compatible with Django 1.4, but that is based solely on `this repo's
   commit
   notes <https://github.com/jcarbaugh/rooibos/commit/f80aca5c9614439735a9c7e93115bdaaff26c396>`__

Software Installation
=====================

Install Dependencies
--------------------

Management systems
~~~~~~~~~~~~~~~~~~

To install the software dependencies required for mdid3 to run, use the
system-specific methods listed below. Experienced developers or system
admins may take issue with some details - in many cases the way
described is not "the only way" but rather "just a way" - in some cases
it's aiming to be describe simplest way. Feedback and alternative
procedures are welcome, please feel free to submit them.

**Package Management System/Command**

.. raw:: html

   <table width=100%>
   <tr>
   <th width=25% align="center" valign="middle">Ubuntu</th>
   <th width=25% align="center" valign="middle" bgcolor="#efefef">Red Hat</th>
   <th width=25% align="center" valign="middle" >Mac OS X</th>
   <th width=25% align="center" valign="middle" bgcolor="#efefef">Windows 2008 or other</th>
   </tr>
   <tr>
   <td  align="center" valign="middle"><a href="https://help.ubuntu.com/community/AptGet/Howto">apt-get</a> </td>
   <td  align="center" valign="middle" bgcolor="#efefef">Redhat - <a href="http://www.ibm.com/developerworks/linux/library/l-lpic1-v3-102-5/">yum</a> <a href="https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/5/html/Deployment_Guide/c1-yum.html">rhel 5</a> | <a href="https://access.redhat.com/knowledge/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/ch-yum.html">rhel 6</a> </td>
   <td  align="center" valign="middle"> <a href="http://mxcl.github.com/homebrew/">homebrew</a> <br/>download installers &amp; compile source</td>
   <td  align="center" valign="middle" bgcolor="#efefef">None (true? any dissent?).<br/>Download installers or executables.</td>
   </tr>
   </table>

Software package installation
-----------------------------

Below is a matrix of the software dependencies required for mdid3 to run
correctly. In general, software installed via a package manager like apt
or yum will be displayed as ``package-name`` whereas a downloadable
installer, binary or downloadable source will be a `text link <#>`__

Apt and Yum generally need to be run via sudo, but the Mac OS X package
manager homebrew is designed specifically to **not** use sudo (assumedly
because the normative mac user account has installation privileges). So
to install ``packageX``, use the commands:

.. raw:: html

   <table width=99%>
   <tr>
   <th width=33% align="center" valign="middle">apt (Ubuntu)</th>
   <th width=33% align="center" valign="middle" bgcolor="#efefef">yum (Red Hat)</th>
   <th width=33% align="center" valign="middle" >homebrew (Mac OS X)</th>
   </tr>
   <tr>
   <td  align="center" valign="middle"><pre><code>sudo apt-get install packageX</code></pre></td>
   <td  align="center" valign="middle" bgcolor="#efefef"><pre><code>sudo yum install packageX</code></pre>
   </td>
   <td  align="center" valign="middle">
   <pre><code>brew install packageX</code></pre>
   </td>
   </tr>
   </table>

Optionally, package managers can be given a list of packages, and be
told to say "yes" to every question, and the human being installing the
software can do something important, like drink coffee. A
copy/paste-able single command will be presented at the bottom of the
matrix.

.. raw:: html

   <table width=100%>
   <tr>
   <td width=16% align="center" valign="middle" bgcolor="#efefef">&nbsp;</td>
   <th width=21%>Ubuntu</th>
   <th width=21% bgcolor="#efefef">Red Hat</th>
   <th width=21%>Mac OS X</th>
   <th width=21% bgcolor="#efefef">Windows 2008 or other</th>
   </tr>
   <tr>
   <tr>
   <th bgcolor="#efefef">python</th>
   <td align="center" valign="middle">installed</td>
   <td align="center" valign="middle" bgcolor="#efefef"><pre><code>python26</code></pre></td>
   <td align="center" valign="middle"><a href="http://mac.github.com">installed</a></td>
   <td align="center" valign="middle" bgcolor="#efefef">Python 2.7.3 <br>(<a href="http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi">32-bit</a>) | (<a href="http://www.python.org/ftp/python/2.7.3/python-2.7.3.amd64.msi">64-bit</a>)</td>
   </tr>

   <th bgcolor="#efefef">git</th>
   <td align="center" valign="middle"><pre><code> git-core</code></pre></td>
   <td align="center" valign="middle" bgcolor="#efefef"><pre><code>git-core</code></pre></td>
   <td align="center" valign="middle"><a href="http://mac.github.com">Github for Mac</a></td>
   <td align="center" valign="middle" bgcolor="#efefef"><a href="http://windows.github.com">Github for Windows</a></td>
   </tr>
   </table>



Update installation
~~~~~~~~~~~~~~~~~~~

::

    sudo apt-get -y upgrade && install

Install python packages using PIP

| Many of the python libraries can be installed with ``pip install``
[after pip is installed]
(http://www.pip-installer.org/en/latest/installing.html) or via
easy\_install (do your self a favor and install pip).
| The exception in quite a few cases is Red Hat Enterprise Linux, where
it is better to use yum to install many python libraries.

::

    sudo pip install mysql-python pyodbc pil python-dateutil flickrapi werkzeug reportlab

Optional Installs
-----------------

FFMPEG\_EXECUTABLE for audio/video file support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    mdid3 uses `ffmpeg <http://ffmpeg.org>`__ to process audio & video
    media files. The current repo includes a windows installer, although
    a newer version may be available. Other platforms have to install
    the software and edit settings\_local.py in order for a/v files to
    be processed.

The setting in
`settings.py <https://github.com/cit-jmu/rooibos/blob/experimental/rooibos/settings.py>`__
is:

::

    FFMPEG_EXECUTABLE = os.path.join(install_dir, 'dist', 'windows', 'ffmpeg', 'bin', 'ffmpeg.exe')

which won't work on linux installations, naturally.

Linux admins should install ffmpeg if it isn't installed and add the
correct path (get with ``which ffmpeg``) to settings\_local.py, for
example on RHEL/Centos:

::

    FFMPEG_EXECUTABLE = '/usr/local/bin/ffmpeg'

Links to the latest version for most platforms covered in this guide can
be found at http://ffmpeg.org/download.html

Installation on RHEL 5 & 6 can follow this guide if a yum package is not
available for your specific version & architecture:
http://ffmpeg.org/trac/ffmpeg/wiki/CentosCompilationGuide

Open Office
~~~~~~~~~~~

TBD (for PPT import and export)

Configuration
=============

As might be expected for a web application as complex and flexible as
mdid3, a number of configuration steps are required to get going.

Setup user accounts
-------------------

Create MDID user account (this allows mdid3 to run programs on it’s
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

own behalf)

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

### Download and Install MDID3
------------------------------

Create the directory where MDID3 will be installed as root, and then
chown it to the account that will run the web app processes

::

    sudo mkdir /var/local/mdid
    sudo chown mdid:mdid /var/local/mdid
    sudo chmod 775 /var/local/mdid
    cd ..

Git MDID3!
~~~~~~~~~~

There are a few ways to approach getting the mdid3 repo onto your
server, the instructions below

    ``su mdid`` -- this is optional - you could also continue as root or
    yourself, and then

::

    git clone git://github.com/cit-jmu/rooibos.git mdid
    cd mdid
    git checkout -b ourSite upstream/experimental

    ``sudo chown -R mdid:staff /var/local/mdid/*`` # this is only
    necessary if you didn't su to the mdid account before downloading
    the mdid3 files.

This step may be necessary if you execute git via root in your mdid3
directories.

::

    sudo chown -R mdid:staff /var/local/mdid/*

Setup the database
------------------

::

    nano mdid.sql

and type this text in

::

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

::

    mysql -u 'root' -p < mdid.sql

type the following two commands at /var/local/mdid/rooibos :

::

    python manage.py syncdb --noinput
    python manage.py createcachetable cache

    Configure Apache & mod_wsgi
    The developers of django recommend using a seperate webserver for static files on a production system
    See How to use Django with Apache and mod_wsgi for more information
    Edit /etc/apache2/httpd.conf:
    sudo cp /var/local/mdid/dist/linux/httpd.conf /etc/apache2/httpd.conf

and add this line

::

    WSGIScriptAlias / /var/local/mdid/rooibos/dist/linux/django.wsgi

    | *note*: the lone forward slash is not a typo - the first “/”
    indicates
    | that mdid will be the root o TRUNCATED! Please download pandoc if
    you
    | want to convert large files.
