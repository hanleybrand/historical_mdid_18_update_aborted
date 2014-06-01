.. sectionauthor:: Peter Hanley
.. publishdate:: 2014-01-23
.. summary:: Technical overview of MDID software and dependency installation

.. index::
   single: installation


Technical Overview
==================

.. rst-class:: lead

MDID3 is a modern `django web application <https://docs.djangoproject.com/>`__
that requires a number of interdependent but seperate technologies to run correctly.

Webserver
---------

    MDID is a `WSGI application <http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface>`__,
    and as such requires a web server capable of serving WSGI applications, such as
    `Apache HTTP Server <http://httpd.apache.org>`__  with `mod\_wsgi <http://code.google.com/p/modwsgi/>`__
    or another alternative that works similarly
    (e.g.\  `uWSGI <https://github.com/unbit/uwsgi-docs#readme>`__ in combination with
    `nginx <http://wiki.nginx.org/Main>`__ or `Microsoft
    IIS <http://www.iis.net>`__ with
    `pyisapie <http://sourceforge.net/apps/trac/pyisapie>`__)

    .. rst-class:: text-info
    The webserver needs to be able to run python as a daemon for
    worker processes like image processing, data import, etc.

Database
--------

    See :doc:`8_database_setup` for more information.

    All known installations are currently based in
    `mySQL <http://www.mysql.com/downloads/mysql/>`__ or MS SQL Server,
    but Postgress should theoretically work - let us know, won't you?


Solr Search
-----------

    `Apache Solr <http://lucene.apache.org/solr/>`__ provides search capabilities.  Solr is written in Java
    and runs as a standalone full-text search server within a servlet container such as Jetty. A sample working
    server is included in the main MDID repo. See the solr wiki for more information about
    `running Solr with Jetty <http://wiki.apache.org/solr/SolrJetty>`_

Memory Object Cache
-------------------

    A memory object caching server like
    `memcached <http://memcached.org>`__ or `Couchbase
    Server <http://www.couchbase.com/couchbase-server/overview>`__ is required.


RabbitMQ
--------

    Background processes such as data import and search index updates
    are handled by `RabbitMQ <https://www.rabbitmq.com>`__
