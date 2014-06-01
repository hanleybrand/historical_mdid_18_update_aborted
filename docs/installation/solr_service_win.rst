| Title: Installing Solr as a Windows Service
| Tags: installation, windows, solr, service
| Author: Andreas Knab
| Date: 2014-02-18
| Summary: Installing Solr as a Windows Service

To automatically start the Solr full-text indexing service whenever the
server starts, it can be installed as a Windows service.

Test service command
--------------------

Before installing the service, it is useful to make sure the command
that will run as the service actually works.

Determine the full path to your Java executable, e.g.

::

    "C:\Program Files (x86)\Java\jre6\bin\java.exe"

You'll need the following parameters (without line breaks):

::

    -Dsolr.solr.home=C:/mdid/solr/solr -Djetty.home=C:/mdid/solr/ -Djetty.logs=C:/mdid/solr/logs/ -cp C:/mdid/solr/lib/*.jar;C:/mdid/solr/start.jar -jar C:/mdid/solr/start.jar

This assumes you installed MDID in C:\\mdid\\, if you used another
directory, change the options accordingly.

Combining the executable and the parameters and running it in a command
prompt should yield the following output, without any errors:

::

    C:\>"C:\Program Files (x86)\Java\jre6\bin\java.exe" -Dsolr.solr.home=C:/mdid/solr/solr -Djetty.home=C:/mdid/solr/ -Djetty.logs=C:/mdid/solr/logs/ -cp C:/mdid/solr/lib/*.jar;C:/mdid/solr/start.jar -jar C:/mdid/solr/start.jar
    2014-02-18 15:11:36.442::INFO:  Logging to STDERR via org.mortbay.log.StdErrLog
    2014-02-18 15:11:36.504::INFO:  jetty-6.1.3

    [...]

    INFO: using system property solr.solr.home: C:/mdid/solr/solr
    Feb 18, 2014 3:11:37 PM org.apache.solr.servlet.SolrServlet init
    INFO: SolrServlet.init() done
    Feb 18, 2014 3:11:37 PM org.apache.solr.core.SolrResourceLoader locateInstanceDir
    INFO: JNDI not configured for solr (NoInitialContextEx)
    Feb 18, 2014 3:11:37 PM org.apache.solr.core.SolrResourceLoader locateInstanceDir
    INFO: using system property solr.solr.home: C:/mdid/solr/solr
    Feb 18, 2014 3:11:37 PM org.apache.solr.servlet.SolrUpdateServlet init
    INFO: SolrUpdateServlet.init() done
    2014-02-18 15:11:37.614::INFO:  Started SocketConnector @ 0.0.0.0:8983

Installation
------------

Download and extract `NMSS <http://nssm.cc/download>`__. The download
contains both 32 and 64 bit versions.

Open a Command Prompt as Administrator and run

::

    nssm install solr

A dialog box opens, in which you can enter the details for the service.

Enter the full path to your Java executable in the Application input
box, e.g.

::

    "C:\Program Files (x86)\Java\jre6\bin\java.exe"

In the Options input box, enter the parameters:

::

    -Dsolr.solr.home=C:/mdid/solr/solr -Djetty.home=C:/mdid/solr/ -Djetty.logs=C:/mdid/solr/logs/ -cp C:/mdid/solr/lib/*.jar;C:/mdid/solr/start.jar -jar C:/mdid/solr/start.jar

Click the Install Service button.

You can now configure the service to e.g. start automatically in the
Windows Services manager.
