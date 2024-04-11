@echo off

start "C:\Users\josec\AppData\Local\Programs\Opera GX\opera.exe" "http://localhost:8000/"

rem Ativa o ambiente virtual
call venv\Scripts\activate
cd odontoboard
python manage.py runserver
