@echo off
rem  
rem file: lgbk.bat
rem Utilitat de backup pel LG
rem 
rem   Autor: David Sabalete
rem   Email: dsabalete@gmail.com
rem
rem
rem Declaració de variables
rem
set "ORIGEN=E:"
set "DESTI=%USERPROFILE%\Mis documentos\LG Backup"
rem set "DESTI=%USERPROFILE%\tmp"
rem
rem Descripció 
echo "ORIGEN --> %ORIGEN%"
echo "DESTI  --> %DESTI%"
rem
rem Carpetes que volem copiar
xcopy "%ORIGEN%" "%DESTI%" /c /d /e /h /i /k /f /r /s /x /y
rem