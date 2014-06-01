=================
Optional Installs
=================

FFMPEG\_EXECUTABLE for audio/video file support
###############################################


mdid3 uses `ffmpeg <http://ffmpeg.org>`__ to process audio & video
media files. The current repo includes a windows installer, although
a newer version may be available. Other platforms have to install
the software and edit settings\_local.py in order for a/v files to
be processed.

The setting in
`settings.py <https://github.com/cit-jmu/rooibos/blob/experimental/rooibos/settings.py>`__
is:

.. code-block:: python

    FFMPEG_EXECUTABLE = os.path.join(install_dir, 'dist', 'windows', 'ffmpeg', 'bin', 'ffmpeg.exe')

which won't work on linux installations, naturally.

Linux admins should install ffmpeg if it isn't installed and add the
correct path (get with ``which ffmpeg``) to settings\_local.py, for
example on RHEL/Centos:

.. code-block:: python

    FFMPEG_EXECUTABLE = '/usr/local/bin/ffmpeg'

Links to the latest version for most platforms covered in this guide can
be found at
`http://ffmpeg.org/download.html <http://ffmpeg.org/download.html>`__

Installation on RHEL 5 & 6 can follow this guide if a yum package is not
available for your specific version & architecture:
`http://ffmpeg.org/trac/ffmpeg/wiki/CentosCompilationGuide <http://ffmpeg.org/trac/ffmpeg/wiki/CentosCompilationGuide>`__



PDF support
###########


RHEL 5
^^^^^^

To install gfx (for pdf thumbnails) for rhel5, (probably similar names
on ubuntu) you need to -

Add the rpmforge repo (for lame)

.. prompt:: bash

    sudo rpm -Uvh http://apt.sw.be/redhat/el5/en/i386/rpmforge/RPMS/rpmforge-release-0.3.6-1.el5.rf.i386.rpm

Get the dependencies:

.. prompt:: bash

    yum install zlib-devel libjpeg-devel.x86_64 freetype-devel giflib-devel fftw3 lame zziplib 

In a scratch/source/temp directory

.. prompt:: bash

     curl http://www.swftools.org/swftools-0.9.2.tar.gz -o swftools-0.9.2.tar.gz
    Make, build, clean
    tar -xzvf swftools-0.9.2.tar.gz
    cd swftools-0.9.2
    ./configure
    make
    make install

-  And finally, move the .so files made during the build process in
   swftools-0.9.2/lib/python to your python site-packages directory:

.. prompt:: bash

   sudo cp lib/python/\*.so /usr/lib/python2.6/site-packages/

Now this should work:

.. prompt:: bash

    python -c 'import gfx'
