# Code Protection (Nuitka) Guide — Optional

[보호가이드.md](../ko/보호가이드.md) · [protection-guide.md](protection-guide.md) · [protection-guide.md](../ja/protection-guide.md) · [protection-guide.md](../zh-CN/protection-guide.md)

An exe built with `build.bat` (PyInstaller) contains the Python code as "bytecode." You can't read it in Notepad, but a dedicated tool like `uncompyle6` **can decompile it back to something close to the original source.**

This guide shows how to use **Nuitka** to turn the Python code into **C and compile it to real machine code**, instead of bytecode. Because the result is an actual compiled program rather than bytecode, ordinary Python decompilers simply don't work on it. Among the **free** protection options available today, this is about as strong as it gets.

> A correction first: in an earlier answer, PyArmor was recommended as the "strongest" option, but while the PyArmor CLI itself can be installed with pip, its **real protection features (like string encryption) and commercial use require a paid license** (its own documentation labels it "Free To Use But Restricted," and states the trial can't be used in a commercial product — [source](https://pyarmor.readthedocs.io/en/v8.2/licenses.html)). The research itself was done correctly, but the cost should have been flagged clearly up front. So the default is changed to **Nuitka, which is completely free and open source.** (Nuitka is licensed under AGPLv3 rather than something like Apache, but it carries an exception stating it does **not** apply to the compiled executable it produces — so you can distribute your MyPass.exe as-is, without its source code — [source](https://nuitka.net/pages/overview.html))

## 1. Running the protected build

Follow Step 2 of `빌드가이드.en.md` exactly the same way to gather the files from `mypass_package.zip` (`mypass.py`, `mypass_i18n.py`, `build.bat`, `build_protected.bat`, `requirements.txt`, `requirements-protected.txt`, the `fonts` folder, `icon.ico`, etc.) into one folder (e.g. `C:\mypass_build`). This time, double-click **`build_protected.bat`** instead of `build.bat`.

- It installs packages, compiles the code, and builds the exe automatically.
- **The first time, it also downloads a C compiler automatically, so it takes noticeably longer (can be 10+ minutes).** Don't close it even if you see "WARNING" messages — just wait.
- When done, `dist\MyPass.exe` is created (same file name and location as the regular build).

## 2. Things to know (please read)

- **The autofill/browser-linking part (uiautomation/comtypes) hasn't been tested by me directly.** comtypes generates some of its code on the fly while running, so whether that still works correctly inside a Nuitka-compiled exe needs to be verified once on an actual Windows machine. If it doesn't work, `build.bat` (PyInstaller) is the already-verified path — use that instead.
- **The exe's size and first-launch time** may be a bit larger or slower than the PyInstaller build (since it bundles a compiled runtime). This isn't a functional problem.
- Since the exe is unsigned, Windows may show a security warning (the blue "Windows protected your PC" screen, "unknown publisher"). This happens with the PyInstaller build too, so it isn't specific to Nuitka. Consider a code-signing certificate if you plan to distribute more widely.
- For updates (Step 6 in `빌드가이드.en.md`), after changing `mypass.py`, just run `build_protected.bat` again.

## 3. (Reference) PyArmor — a paid alternative

If you'd like to add string-level encryption on top (the kind PyArmor does), it remains an option, but keep in mind:

- **The free trial can't be used for commercial distribution.** To actually use it, you need a Pro or Group license (a one-time payment; pricing may change on PyArmor's end) — check their [official licensing page](https://pyarmor.readthedocs.io/en/latest/licenses.html) for current terms before buying.
- Unlike Nuitka's approach of compiling to machine code, PyArmor works by "encrypting bytecode + adding decryption code," so there's no benefit to using both together — pick one or the other.
- Depending on the license type, the end user's PC may need an internet connection the first time it runs, which fits less well with a USB-portable use case.

If you'd like, I can also put together a separate build script for PyArmor, but if cost isn't a constraint for you, **Nuitka (free) is the recommended default.**
