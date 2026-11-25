# Building the exe Guide (start to finish, step by step)

[빌드가이드.md](../ko/빌드가이드.md) · [build-guide.md](build-guide.md) · [build-guide.md](../ja/build-guide.md) · [build-guide.md](../zh-CN/build-guide.md)

> This guide is for **the person building MyPass.exe**. (You only need to do this once, on one PC)
> The person who uses the finished exe does not need Python. → See `설치가이드.en.md`
> Follow the steps below **in order, exactly as written**. Text written `like this` is a command you should type exactly as shown.

Time required: about 10–15 minutes the first time (mostly installation and download time)
What you need: a Windows 10/11 PC, an internet connection

---

## Step 1. Install Python

1. Open **https://www.python.org/downloads/** in your web browser.
2. Click the yellow **`Download Python 3.x.x`** button to download the installer. (Any version 3.10 or higher is fine)
3. Double-click the downloaded file (`python-3.x.x-amd64.exe`) to run it.
4. On the first screen, at the **very bottom**, **make sure to check** the box for **`Add python.exe to PATH`**. ← This is the most important step
5. Click **`Install Now`**. (If a permission prompt appears, click `Yes`)
6. When you see `Setup was successful`, click **`Close`**.

### Confirming the installation
1. Press **`Windows key + R`** on your keyboard, type `cmd` in the box, and press Enter → a black window (Command Prompt) will open.
2. Type the following and press Enter:

   `python --version`

3. If a version number like `Python 3.12.x` appears, it was successful. You can close the black window. (Type `exit` and press Enter)

> If you see `Python was not found`, or the Microsoft Store opens instead → see **[Troubleshooting item 1]** at the bottom.

---

## Step 2. Create a working folder and put the files in it

1. In File Explorer, create a new folder named `mypass_build` on your **C drive**. → `C:\mypass_build`
   (Using a short path with no Korean characters or spaces results in fewer errors. **You may extract the files to a different folder instead** — in that case, read `C:\mypass_build` below as "the folder I put the files in." The result will be `dist\MyPass.exe` inside that folder.)
2. Unzip the `mypass_package.zip` you received. (Right-click the zip → `Extract All...` or `Extract Here`)
3. After unzipping, you'll see a `mypass` folder. Move the **files inside it** into `C:\mypass_build`.
4. When you open `C:\mypass_build`, you should **immediately see these items** (directly inside this folder, not inside a subfolder):

   - `mypass.py`
   - `mypass_i18n.py` (translation file)
   - `build.bat`
   - `requirements.txt` (list of packages to install — build.bat reads this automatically and installs them all at once)
   - `fonts` folder (fonts used by the app — automatically copied next to the exe when you build it)
   - `icon.ico`

---

## Step 3. Build the exe

### Method A. The easiest way (recommended)

1. In the `C:\mypass_build` folder, **double-click `build.bat`**.
2. A black window will open and text will scroll by. **Don't close it — just wait.** (3–10 minutes the first time, depending on your internet speed)
   - `[0/4]` checking Python → `[1/4]` virtual environment → `[2/4]` installing packages → `[3/4]` building the exe → `[4/4] Done`
   - It's normal to see `WARNING` messages along the way. If it stops with an `ERROR`, see **[Troubleshooting]**.
3. If the last lines show the exe's path (something like `...\dist\MyPass.exe`) followed by a "press any key to continue" line (shown in your own Windows display language, since that's the `pause` command's built-in text), it succeeded. Press any key to close the window.
4. Confirm that `C:\mypass_build\dist\MyPass.exe` was created. → Go to **Step 5**.

> If Windows shows a "Windows protected your PC" window, click `More info` → `Run anyway`.

### Method B. Typing commands directly (if Method A doesn't work)

**B-1. Opening Command Prompt in the working folder**
1. Open the `C:\mypass_build` folder in File Explorer.
2. Click once in the **address bar** at the top of the window (the area showing `C:\mypass_build`).
3. Delete the text there, type `cmd`, and press Enter. → A black window will open, and you should see `C:\mypass_build>` at the front.

**Whichever black window you use (cmd / PowerShell / Git Bash)** — only change the `.venv\Scripts\python.exe` part at the front of the commands below to match your window type. (Everything else stays the same)

| Window type | Change the beginning to this |
|---|---|
| Command Prompt (cmd) | `.venv\Scripts\python.exe` (as written below) |
| PowerShell | `.\.venv\Scripts\python.exe` (add `.\` at the front) |
| Git Bash (bash) | `./.venv/Scripts/python.exe` (use forward slashes `/`) |

The first command, `python -m venv .venv`, is typed the same way in all three windows.
(If you're not sure which window to use, double-clicking `build.bat` from Method A is simplest.)

**B-2. Type the commands below one line at a time — enter one, press Enter, wait for it to finish, then the next line** (you can also copy and paste; in the black window, right-click pastes)

① Create a virtual environment (1–2 minutes; when done, `C:\mypass_build>` will appear again)

`python -m venv .venv`

② Update pip (the installer tool) to the latest version

`.venv\Scripts\python.exe -m pip install --upgrade pip`

③ Install the required packages all at once (installs everything listed in `requirements.txt`; 1–3 minutes, you should see `Successfully installed ...` at the end)

`.venv\Scripts\python.exe -m pip install -r requirements.txt`

④ Build the exe (1–3 minutes; you should see `Building EXE ... completed successfully.` at the end)

`.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name MyPass --icon icon.ico --collect-all uiautomation --collect-all comtypes mypass.py`

⑤ When finished, type `exit` and press Enter to close the window. Confirm that `C:\mypass_build\dist\MyPass.exe` was created.

---

## Step 4. (Reference) What each command does
| Command | What it does |
|---|---|
| `python -m venv .venv` | Creates an independent Python space (a virtual environment) used only within this folder. It doesn't mix with any other Python on your PC. |
| `pip install ... cryptography` | Encryption functionality |
| `pip install ... uiautomation` | Reading the browser address and the fill feature (Windows only) |
| `pip install ... pyinstaller` | The tool that bundles the Python program into an exe |
| `PyInstaller ...` | Bundles Python and the packages into a single file (MyPass.exe). |

---

## Step 5. Try running it
1. **Double-click** `C:\mypass_build\dist\MyPass.exe`. (It may take a few seconds the first time)
2. If the login screen appears, it worked. Try creating a user with `New user(N)` and using the app.
3. When you run it, a `data` folder is created in the **same folder** as the exe, and your information is stored there.
4. To distribute the app, just copy **the `MyPass.exe` file only** to wherever you want (such as a USB drive). You don't need the `build` or `.venv` folders.
5. You can remove the test user information you created by deleting the `dist\data` folder. (Don't copy this folder when distributing the app)

---

## Step 6. Building a new version later
1. Replace `mypass.py` and `mypass_i18n.py` with the new versions. (Same folder, overwrite the existing files)
2. Double-click `build.bat` again. (This will be much faster since `.venv` already exists)
3. A new `dist\MyPass.exe` will be created.

---

## Troubleshooting

**1. Typing `python` shows `Python was not found`, or the Microsoft Store opens**
- Cause: `Add python.exe to PATH` wasn't checked during Python installation, or this is due to Windows' Store link.
- Solution ①: Run the Python installer again → choose `Modify` or `Uninstall` and reinstall from the beginning, making sure to **check PATH**.
- Solution ②: Press `Windows key` → search for `Manage app execution aliases` → turn **off** the two entries for `python.exe` and `python3.exe` (App Installer).
- After installing, close all open black windows and **open a new one** for the change to take effect.
- (Note: `build.bat` will also automatically try the `py` command if `python` isn't found.)

**2. During `pip install`, you get an error like `Could not find a version` / `Connection` / `timed out`**
- Check your internet connection and run the command again. On a company or school network, security software may be blocking it.

**3. Error: `'.venv\Scripts\python.exe' is not recognized as an internal or external command...`** (the exact wording follows your Windows display language)
- This means creating the virtual environment (step ①) failed. Delete the `.venv` folder and start again from `python -m venv .venv`.
- Make sure Command Prompt was opened from `C:\mypass_build>`.

**4. `can't open file ... mypass.py` / `No such file`**
- `mypass.py` isn't directly inside `C:\mypass_build`. Double-check Step 2, item 4.

**5. The text looks garbled when you open `build.bat`**
- This doesn't affect how it runs. You can proceed with Method B instead.

**6. Antivirus deletes the exe or flags it as a "threat"**
- This is a common false positive for a self-made, unsigned exe. Add the `dist` folder and `MyPass.exe` to your antivirus exception list, then build it again.

**7. No window appears after running the exe**
- Wait 10–20 seconds. If it still doesn't appear, check your antivirus (item 6), and if `MyPass.exe` is still listed in Task Manager, end it and run it again.
- If it still doesn't work, you can run it directly with `python mypass.py` to see the error message:
  `.venv\Scripts\python.exe mypass.py` (this will run even without `pyinstaller`)

**8. `ModuleNotFoundError: No module named ...`**
- Step 3, item ③ (installing packages) didn't finish completely. Run step ③ again.
