@echo off
setlocal

set PROJECT_DIR=%~dp0

echo ===============================
echo Iniciando todos los servicios...
echo ===============================

REM Storage Service
start "Storage Service (5002)" cmd /k "cd /d %PROJECT_DIR%services\storage_service && python app.py"
timeout /t 2 /nobreak >nul

REM Logging Service
start "Logging Service (5003)" cmd /k "cd /d %PROJECT_DIR%services\logging_service && python app.py"
timeout /t 2 /nobreak >nul

REM Notification Service
start "Notification Service (5004)" cmd /k "cd /d %PROJECT_DIR%services\notification_service && python app.py"
timeout /t 2 /nobreak >nul

REM Task Service
start "Task Service (5001)" cmd /k "cd /d%PROJECT_DIR%services\task_service && python app.py"
timeout /t 2 /nobreak >nul

REM Client
start "Client (5000)" cmd /k "cd /d %PROJECT_DIR%client && python app.py"

echo.
echo              ^^
echo             /_\
echo            /___\
echo           /_____\
echo          /_______\
echo           ^|=   =^|      
echo           ^|     ^|    
echo           ^|     ^|     
echo           ^|     ^|     
echo           ^|     ^|   
echo           ^|     ^|
echo          /^|##!##^|\                Todos los servicios han sido lanzados
echo         / ^|##!##^| \
echo        /  ^|##!##^|  \
echo       ^|  /  ^| ^| \  ^|      Accede al sistema en:
echo       ^| /   ^( ^)  \ ^|
echo       ^|/    ^( ^)   \^|
echo           ^(^(   ^)^)               http://localhost:5000
echo          ^(^(  :  ^)^)
echo          ^(^(  :  ^)^)
echo           ^(^(   ^)^)
echo            ^(^( ^)^)
echo             ^( ^)
