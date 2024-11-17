@echo off
powershell -Command "pip freeze | ForEach-Object { $_.split('==')[0] } | ForEach-Object { pip install --upgrade $_ }"
powershell -Command "pip freeze > requirements.txt"
