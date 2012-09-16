instalando GitHub

Debian/Ubuntu
$ apt-get install git-core
Fedora
$ yum install git
Gentoo
$ emerge --ask --verbose dev-vcs/git
Arch Linux
$ pacman -S git
FreeBSD
$ cd /usr/ports/devel/git
$ make install
Solaris 11 Express
$ pkg install developer/versioning/git
OpenBSD
$ pkg_add git


configurando git
git config --global user.name "Tú nombre"

git config --global user.email "túemail@túemail.com"

git init
git add README.md
git commit -m "primer commit :')"
git remote add origin https://github.com/HecThorFer/CSLUESFMO.git
git push -u origin master   
