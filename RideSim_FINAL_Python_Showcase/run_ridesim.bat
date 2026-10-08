@echo off
cd /d "%~dp0"
python -m unittest discover -s tests -v
python -m ridesim.server
