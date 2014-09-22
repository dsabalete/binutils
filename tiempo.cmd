@echo off
bash wget_images.sh
set VIEWER="c:\Archivos de programa\IrfanView\i_view32.exe" 
call %VIEWER% /slideshow C:\tmp\tiempo
exit