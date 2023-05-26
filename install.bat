@echo off

if not exist venv python -m venv venv
@call "%~dp0venv\Scripts\activate.bat"
Cmd /k python -m pip install -r requirements.txt