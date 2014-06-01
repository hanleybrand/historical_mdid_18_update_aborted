.. sectionauthor:: Andreas Knab
.. publishdate:: 2014-01-23
.. summary:: IIS configuration on Windows

.. index::
   single: installation
   single: windows
   single: iis

IIS configuration
=================

Mime Types
----------

To support Adobe Air applications, the following mime type needs to be
added to the IIS configuration:

::

    File extension: .air 
    Mime type: application/vnd.adobe.air-application-installer-package+zip

