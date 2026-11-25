@echo off
cd /d "%~dp0"

echo [0/4] Checking Python...
set PYCMD=python
python --version >nul 2>&1 || set PYCMD=py -3
%PYCMD% --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo Python not found. Please follow Step 1 - Install Python - in the build guide first.
    pause
    exit /b 1
)
%PYCMD% --version

echo [1/4] Preparing virtual environment (.venv)...
if not exist .venv\Scripts\python.exe (
    %PYCMD% -m venv .venv
    if errorlevel 1 (
        echo Failed to create the virtual environment.
        pause
        exit /b 1
    )
)

echo [2/4] Installing packages in the virtual environment... (using requirements.txt)
.venv\Scripts\python.exe -m pip install --upgrade pip
if exist requirements.txt (
    .venv\Scripts\python.exe -m pip install -r requirements.txt
) else (
    .venv\Scripts\python.exe -m pip install cryptography pyinstaller uiautomation
)
if errorlevel 1 (
    echo Package installation failed. Please check your internet connection.
    pause
    exit /b 1
)

echo [3/4] Building the exe... (takes 1-3 minutes. WARNING messages are normal)
if exist icon.ico (set ICONOPT=--icon icon.ico) else (set ICONOPT=)
.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name MyPass %ICONOPT% --collect-all uiautomation --collect-all comtypes mypass.py
if errorlevel 1 (
    echo Failed to build the exe. Please check the error message above.
    pause
    exit /b 1
)

if exist fonts (
    echo Copying the fonts folder next to the result... - improves text appearance, not required to run
    xcopy /e /i /y fonts dist\fonts >nul
)

echo [4/4] Done
echo.
echo Result: %~dp0dist\MyPass.exe
echo (A "data" folder will appear next to the exe. All info is stored only there.)
echo (Keep the "fonts" folder next to the exe too, so text displays nicely.)
pause
