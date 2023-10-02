@echo off

if "%1" == "pack" goto pack
if "%1" == "cu" goto cu

chcp 65001

:default
pyinstaller --noconfirm --onefile  "C:\MyPrograms\Py\.Ice\ice.py"
pyinstaller --noconfirm --onefile  "C:\MyPrograms\Py\.Ice\runice.py"

:cu
del .\build\ice\*.*
del .\build\ice\localpycs\*.*
del .\build\runice\*.*
del .\build\runice\localpycs\*.*
rd .\build\ice\localpycs
rd .\build\ice
rd .\build\runice\localpycs
rd .\build\runice
rd .\build
move .\dist\*.exe .
rd build
rd dist
del *.spec
if "%1" == "dopack" goto pack
goto EOF

:pack
zip ice-build.zip ice.exe runice.exe ice-0.0.1.vsix
del ice.exe
del runice.exe

:eof