@ECHO off
    ECHO Welcome to Markogebra easy installer.
    ECHO Note: please make sure you've got installed python on version 3.7.9 and set to path variable
    PAUSE

    ECHO Starting python virutal environment...
    call python -m venv venv
    cd venv/Scripts
    call activate.bat
    cd ../..
    ECHO Installing requirements
    call pip install -r requirements.txt
    ECHO Starting database
    cd Data
    call python startDB.py
    cd ..
    ECHO F | XCOPY /y TEMPLATE_data.json Data\data.json

    ECHO Initialization finished