From the $MDID_ROOT/dist/mac directory

    tar xzvf MySQL-python-1.2.4b4
    sudo ln -s /usr/local/mysql/lib /usr/local/mysql/lib/mysql
    python setup.py clean
    python setup.py build
    python setup.py install
    # test with
    python -c "import MySQLdb"
    # if you get no messages, everything is ok - if you get a 'Library not loaded/Reason: image not found' error do this:
    sudo ln -s /usr/local/mysql/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib


source: [How to install MySQLdb (Python data access library to MySQL) on Mac OS X?](http://stackoverflow.com/questions/1448429/how-to-install-mysqldb-python-data-access-library-to-mysql-on-mac-os-x)