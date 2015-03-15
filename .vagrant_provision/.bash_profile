source /usr/local/bin/virtualenvwrapper.sh
source ~/.git-prompt.bash
source ~/.git-completion.bash
source ~/.mdid-funcs

alias mdidenv="source ~/mdid/venv.vagrant/bin/activate"

GIT_PS1_SHOWDIRTYSTATE=true

PS1='\[`[ $? = 0 ] && X=2 || X=1; tput setaf $X`\]\h\[`tput sgr0`\]:$PWD\[\033[31m\]$(__git_ps1)\[`tput sgr0`\]\n\$'

