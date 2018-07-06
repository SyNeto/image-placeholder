# Proyecto Image Placeholder

- Requerimientos
- Instalar Python
- Project setup

## Requerimientos

* Python > 3.5

## Instalando Python

### Windows

* [Python para windows](https://www.python.org/downloads/windows/)

### MacOS

* [HomeBrew](https://brew.sh/)

Tras instalar homebrew ejecutar el siguiente comando:

	$ brew install python

### Linux

La mayoría de los sistemas operativos linux modernos tienen instalados python3.x
por lo cual no es necesario instalar nada

	$ python3 --version
	Python 3.x.x

En caso de no contar con un interprete de Python adecuado existen diferentes maneras
de instalarlo, consulta la documentación de tu distro y sigue los pasos que te
indiquen

## Project setup

### Creación de un entorno virtual

Python desde su version 3.4.x cuenta con una herramienta para generar enotrnos
virtuales

Linux & MacOS

	$ python3 -m venv path/to/venv

Windows

	C:\>python -m venv c:\>path\to\venv

Los entornos virtuales son una gran herramienta ya que nos permiten mantener un
aislando las dependencias de nuestro proyecto de las de nuestro sistema operativo
esto es especialmente importante en los sistemas operativos *nix ya que nos
permiten mantener intactas las dependencias que utiliza el sistema.

### Activar el entorno virtual

Linux & MacOS

	$ source path\to\venv\bin\activate

Windows CMD

	C:\>path\to\venv\Scripts\activate.bat

Windows PowerShell

	PS C:\>path\to\venv\Scripts\Activate.ps1

### Instalar las dependencias del projecto

Instalando dependencias con pip (Sin haber clonado o descargado este repositorio):

	(venv) > pip install flask pillow

Si descargaste este repositorio instalar las dependencias del proyecto es muy
sencillo:

	(venv) > pip install -r requirements.txt
