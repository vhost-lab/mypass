# MyPass Installation & Usage Guide

[설치가이드.md](../ko/설치가이드.md) · [install-guide.md](install-guide.md) · [install-guide.md](../ja/install-guide.md) · [install-guide.md](../zh-CN/install-guide.md)

## 0. Things to know first
- **If you're just using the app**: all you need is `MyPass.exe`. No Python, no installer needed.
- **If you're building the exe** (once, on one PC): you'll need Python. → See Section 4
- **If you forget your master password, there is no way to recover it.** Be sure to remember it.

## 1. Installation (if you received the exe)
1. Place `MyPass.exe` in a folder of your choice. Example: `D:\MyPass\`
   - Avoid locations without write permission, like `C:\Program Files`. (If it can't write there, your data will be saved to `%APPDATA%\마이패스\data` instead)
2. Double-click to run it. When it runs, a `data` folder is created next to the exe. **All your data is stored only in this folder.**
3. The first time you run it, a blue "Windows protected your PC" window may appear. (This warning appears because it's an unsigned, personal program)
   → Click `More info` → `Run anyway`. If your antivirus flags it, add the exe to your antivirus exceptions.

## 2. Getting started
1. On the login screen, choose `New user(N)` → set your ID and **master password**
2. `Manage(T) → Add site` (Ctrl+N): enter the site description, address, ID, and password
   - You can create groups to organize sites, and drag items in the list to move them.
3. When you open that site in your browser, the address is automatically linked and the matching info appears. (`Auto-link browser address`, or press F5 to fetch manually)
4. `Fill` button: enters your ID/password into the login screen for you. (Use the `Press Enter after Fill (auto login)` option for automatic login)
   - The browser linking and fill features use Windows' accessibility feature (UI Automation), so behavior may vary by site and browser. If it doesn't work, use the copy ID/password buttons instead.
5. The app automatically locks after 10 minutes of inactivity.
6. `Ctrl+F` (or the magnifier button): opens a search box that finds sites by description, address, keyword, or ID all at once.

## 3. Backups (please set this up)
- **Automatic backup**: An encrypted backup is added to `data\backup` every time you log in. (The most recent 10 are kept)
- **Backup location**: Set a folder under `File(F) → Set backup location...` and an encrypted backup will be automatically saved to that folder (`MyPass_backup`).
  - This can be a different drive, an external hard drive, a NAS, or a cloud sync folder like OneDrive, Google Drive, or Dropbox
  - We recommend using a **different device** than the one holding the program folder (e.g. your USB drive). If that device fails, both the original and the backup will be lost together.
  - CSV format is not encrypted, so avoid using it unless necessary.
- **Restore**: From the login screen, or via `File(F) → Restore from backup...`

## 4. Building the exe (for builders only, once)
**Open `빌드가이드.en.md` and follow it from Step 1 in order.** (It covers everything from installing Python → preparing the folder → building → confirming it runs)
- Summary: Install Python → put the files from `mypass_package.zip` (`mypass.py`, `mypass_i18n.py`, `build.bat`, `requirements.txt`, the `fonts` folder, `icon.ico`, etc.) in one folder → double-click `build.bat` → `dist\MyPass.exe`

## 5. Carrying it on a USB drive
- Keep `MyPass.exe` and the `data` folder together in one folder on the USB drive, and run it directly from the USB drive.
- Even if you use it on multiple PCs, your data only lives in the `data` folder on the USB drive.
- If the USB drive is write-protected (read-only), the data will instead be saved separately to that PC's `%APPDATA%`. Be careful about this.
- In case you lose the drive, make your master password long enough, and set a separate backup location.

## 6. Updating
- The repository address is already set at the top of `mypass.py`, as `UPDATE_REPO = "vhost-lab/mypass"`. If your repository name is different, just change this line and rebuild.
- Check immediately via `Update(U) → Check for updates`, or the app will automatically check once a day when you log in and notify you.
- If a new version is available, an **[Update now]** button appears in the window. Clicking it downloads the new exe, automatically swaps it in, and restarts the program. (This only works when running as the exe. If you're running it directly with `python mypass.py`, it will just open the download page instead)
- Under `Update(U) → Update settings...`, you can turn automatic checking on/off and enter a read-only token for a private repository.
- To publish a new version, create a new release in your GitHub repository's Releases with a tag like `v2.0`, and **be sure to upload the exe file as an attachment (Asset) on that Release.** (The [Update now] button only appears if there's an attached exe)
- Windows antivirus software may block or warn about the automatic update because it "downloads and runs an unsigned exe." If you want to distribute more widely, we recommend getting a code signing certificate.

## Copyright notice
The name you put in `COPYRIGHT_HOLDER` at the top of `mypass.py` is shown in the About window in the format `ⓒ year name`. To change it, just edit that one line.

## Language
- The first time you run the app, a language selection window appears (Korean/English/Japanese/Simplified Chinese), and you can change it anytime afterward via `Settings(S) → Language`.
- To add more languages, follow the instructions inside `mypass_i18n.py` and add entries to `LANGS`, `TR`, and `CSV_HEAD`.
- From the notification, click `Open download page` → download the new `MyPass.exe` and **replace only the existing exe file**. Leave the `data` folder as is.
- It's safer to run `File(F) → Create backup...` once before replacing it.
- A private repository requires a read-only token. (See the guidance in the settings window)

## 7. Troubleshooting
| Symptom | Solution |
|---|---|
| Won't run / closes immediately | Add it to your antivirus exceptions, run it from a different folder (e.g. D:\ instead of the Desktop) |
| It looks like my data disappeared | If you previously ran it from a different folder, check that folder's `data` folder or `%APPDATA%\마이패스\data` (`Help(H) → About → Open data folder`) |
| Browser address isn't being read | Press `F5`, click once in the browser and try again. If it still doesn't work, enter the address manually |
| Update check fails | Check your internet connection, the repository name, and (if private) your token |
| Lost password | Cannot be recovered. If you have a backup from when you remembered the password, use `Restore from backup` |

## 8. Things to know
- The program does not send your data over the internet. The internet is only used to check for updates (looking up the latest version number).
- Encryption: AES-256-GCM, key generation: scrypt
- Don't upload the `data` folder, `.mpbak` files, or `.csv` files, which contain personal information, to GitHub or similar services. (The `.gitignore` provided with the app blocks this)
</content>
