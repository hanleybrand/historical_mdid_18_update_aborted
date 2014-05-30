#!/bin/bash

export OSX_DIST_DIR=$(pwd)
export XC_SDK=$(xcrun --show-sdk-path)
export USR_INC=$XC_SDK/usr/include
export PATH=$OSX_DIST_DIR/inc:$USR_INC:$PATH

echo "Installing MDID3 software"

# installer downloads =
# MySQL - http://dev.mysql.com/downloads/mysql/
# memcached - http://dev.mysql.com/downloads/mysql/

# homebrew (mac package manager - http://brew.sh)
# since we'll be installing services, you may wish to read
# http://robots.thoughtbot.com/starting-and-stopping-background-services-with-homebrew

install-homebrew() {
    if hash brew 2>/dev/null; then
        echo "Homebrew already installed, updating"
        #brew update
    else
        ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    fi
}

install-mysql() {
    if hash mysql 2>/dev/null; then
        echo "mysql already installed use: "
        echo "    brew services [start|stop|restart] mysql    "
        echo "to start, stop, restart"
    else
        brew install mysql
    fi
}

install-memcached() {
    if hash memcached 2>/dev/null; then
        echo "memcached already installed use: "
        echo "    brew services [start|stop|restart] memcached    "
        echo "to start, stop, restart"
    else
        brew install memcached
    fi
}

install-pyldap() {
    echo "Checking python-ldap"
    echo $(python -c "import ldap")
    if "python -c \"import ldap\"" 2>/dev/null; then
        echo "python-ldap already installed (thank goodness!)"
    else
        echo "installing python-ldap"
        ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install python-ldap
        echo "Checking python-ldap (again)"
        echo $(python -c "import ldap")
    fi
}


install-homebrew
install-mysql
install-memcached
#install-pyldap

#pip install -r base.txt

if $(python -c "import ldap") 2>/dev/null; then
    echo 'Hey, no error'
else
    echo "Error!"
fi


#tar xzvf MySQL-python-1.2.4.tar.gz

# install pycrypto
#ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install pycrypto