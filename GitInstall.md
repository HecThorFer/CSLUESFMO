///////////////////////////////////////////////////////
///instalando GitHub
///////////////////////////////////////////////////////

///////////////////////////////////////////////////////
///Debian/Ubuntu
    apt-get install git-core
///Fedora
    yum install Gentoo
///git
    emerge --ask --verbose dev-vcs/git
///Arch Linux
    pacman -S git
///FreeBSD
    cd /usr/ports/devel/git
    make install
///Solaris 11 Express
    pkg install developer/versioning/git
///OpenBSD
    pkg_add git

///////////////////////////////////////////////////////
///configurando git
    git config --global user.name "Tú nombre"
    git config --global user.email "túemail@túemail.com"

///////////////////////////////////////////////////////
///Inicializamos la carpeta git en nuestra PC
    git init
//////////////////////////////////////////////////////
///Agregamos un archivo... 
    git add README.md
///Realizamos un commit para hacer validos los cambios
    git commit -m "primer commit :')"
//////////////////////////////////////////////////////
///Especificamos la direccion de nuestro GitHub
    git remote add origin https://github.com/HecThorFer/CSLUESFMO.git
//////////////////////////////////////////////////////
///Especificamos en que branch se realizaran los cambios
    git push -u origin master

///////////////////////////////////////////////////////
//Agregar nuevo Branch
///////////////////////////////////////////////////////
///creamos un nuevo branch en la PC local
    git branch <nombre_del_branch_nuevo>
///////////////////////////////////////////////////////
///enviamos en nuevo branch a github
    git push origin <nombre_del_branch_nuevo>
///////////////////////////////////////////////////////
///cambiamos al nuevo branch
    git checkout <nombre_del_branch_nuevo>
//////////////////////////////////////////////////////
///revisamos todos los branch existentes
    git branch

