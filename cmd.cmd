@REM @echo off
@REM REM Navigate to the directory where your Python script is located
@REM cd "C:\Users\ashik\Documents\Code\code dump\windows"

@REM REM Run the Python script
@REM python desktop_setup.py

@REM exit


@echo off

REM Navigate to the directory where your Python script is located
cd "C:\Users\ashik\Documents\Code\code dump\windows"

REM Run the Python script
python desktop_setup.py

REM Wait 40 seconds and then close the window
timeout /t 10 /nobreak > NUL

exit