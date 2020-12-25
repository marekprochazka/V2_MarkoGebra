@ECHO off
    ECHO Welcome to Markogebra easy installer.
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
    ECHO {}>math_limits.json
    ECHO Making graphstyle file
    ECHO seaborn-whitegrid>graphstyle.txt
    cd ..
