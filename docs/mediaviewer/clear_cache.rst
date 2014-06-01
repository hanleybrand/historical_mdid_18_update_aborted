| Title: Clearing the MediaViewer cache on MacOS X
| Tags: macos, mediaviewer, cache
| Author: Andreas Knab
| Date: 2014-02-22
| Summary: Clearing the MediaViewer cache on MacOS X

The Desktop MediaViewer (DMV) caches images here:

::

    /Users/[user]/Library/Preferences/DesktopMediaViewer/Local Store

| The ``Local Store`` folder will contain one or more folders with
numeric names.
| The numeric names correspond to individual users. Each MDID user who
logs into
| DMV with the MacOS ``[user]`` account will get a uniquely numbered
folder. It is
| safe to delete any or all of the folders within ``Local Store``.

Please close the MediaViewer before deleting folders from
``Local Store``.
