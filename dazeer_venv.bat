@echo off
@REM check if venv is a folder
if not exist venv python -m venv venv
@call "%~dp0venv\Scripts\activate.bat"
Cmd /k