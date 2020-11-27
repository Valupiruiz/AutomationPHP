@echo off
set PROJECT_ROOT=%cd%
set PROJECT_VENV=%PROJECT_ROOT%\venv
set VENV_ACTIVATE=%PROJECT_VENV%\Scripts\Activate

echo ::Instalando venv::
pip install virtualenv
echo ::Instalación exitosa::
echo ::Generar venv::
virtualenv "%PROJECT_VENV%"
echo ::Venv generado::

echo ::Activo VENV::
call "%VENV_ACTIVATE%"
echo ::Instalando requisitos::
pip install -r requirements.txt
call deactivate.bat
echo ::Se instalaron todos los paquetes::
