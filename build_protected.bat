@echo off
cd /d "%~dp0"

echo =========================================================
echo  Building with Nuitka: compiles the Python code all the
echo  way down to C and then to machine code.
echo  (Not bytecode, so ordinary decompilers cannot restore it)
echo  Free and open-source tool, no payment required.
echo  The first build also downloads a C compiler (a few hundred
echo  MB), so it takes longer. (internet required)
echo =========================================================
echo.

echo [0/4] Checking Python...
set PYCMD=python
python --version >nul 2>&1 || set PYCMD=py -3
%PYCMD% --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please follow Step 1 - Install Python - in the build guide first.
    pause
    exit /b 1
)

echo [1/4] Preparing virtual environment (.venv)...
if not exist .venv\Scripts\python.exe (
    %PYCMD% -m venv .venv
    if errorlevel 1 ( echo Failed to create the virtual environment. & pause & exit /b 1 )
)

echo [2/4] Installing packages (using requirements-protected.txt: cryptography, uiautomation, nuitka, etc.)...
.venv\Scripts\python.exe -m pip install --upgrade pip
if exist requirements-protected.txt (
    .venv\Scripts\python.exe -m pip install -r requirements-protected.txt
) else (
    .venv\Scripts\python.exe -m pip install cryptography uiautomation nuitka ordered-set zstandard
)
if errorlevel 1 ( echo Package installation failed. Please check your internet connection. & pause & exit /b 1 )

echo [3/4] Compiling and building the exe... (the first run can take 10+ minutes)
if exist icon.ico (set ICONOPT=--windows-icon-from-ico=icon.ico) else (set ICONOPT=)
.venv\Scripts\python.exe -m nuitka --onefile --assume-yes-for-downloads ^
    --enable-plugin=tk-inter --windows-console-mode=disable %ICONOPT% ^
    --include-package=uiautomation --include-package=comtypes ^
    --include-package-data=certifi ^
    --output-filename=MyPass.exe --output-dir=dist ^
    mypass.py
if errorlevel 1 (
    echo Build failed. Please check the error message above.
    echo If you see a "--windows-console-mode" error, your Nuitka version may be too old.
    echo   Run: .venv\Scripts\python.exe -m pip install --upgrade nuitka   then try again.
    pause
    exit /b 1
)

if exist fonts (
    echo Copying the fonts folder next to the result... - improves text appearance, not required to run
    xcopy /e /i /y fonts dist\fonts >nul
)

echo.
echo [4/4] Done: %~dp0dist\MyPass.exe  (code compiled to machine code for protection)
echo (On first run, security software may show an "unknown publisher" warning. This is normal.)
echo (Keep the "fonts" folder next to the exe too, so text displays nicely.)
pause
