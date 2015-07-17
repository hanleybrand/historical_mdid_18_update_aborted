HOME_DIR=`pwd`
VAGRANT_DIR=/vagrant
PROVISION_DIR=$VAGRANT_DIR/.vagrant_provision
MDID_DIR=$HOME_DIR/mdid
MDID_DATA_DIR=$HOME_DIR/mdid-data
CONFIG_DIR=$MDID_DIR/config
ROOIBOS_DIR=$MDID_DIR/rooibos


export WORKON_HOME=$HOME/.virtualenvs
# export PROJECT_HOME=$HOME/


source /usr/local/bin/virtualenvwrapper.sh
source ~/.bash-completion
source ~/.git-prompt
source ~/.mdid-funcs

alias mdidenv="source ~/mdid/venv.vagrant/bin/activate"

GIT_PS1_SHOWDIRTYSTATE=true

PS1='\[`[ $? = 0 ] && X=2 || X=1; tput setaf $X`\]\h\[`tput sgr0`\]:$PWD\[\033[31m\]$(__git_ps1)\[`tput sgr0`\]\n\$'

