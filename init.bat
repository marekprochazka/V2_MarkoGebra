@ECHO off
    ECHO Welcome to Markogebra easy installer. Press any key to continue...
    ECHO Note: please make sure you've got installed python and set to path variable
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
    call startDB.py
    cd ..
    ECHO Making graphstyle file
    ECHO seaborn>graphstyle.txt