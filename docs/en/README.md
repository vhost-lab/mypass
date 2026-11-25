# MyPass

[한국어](../ko/README.md) · [English](README.md) · [日本語](../ja/README.md) · [简体中文](../zh-CN/README.md)

An encrypted ID/password manager for Windows. Nothing is ever sent over the internet — everything is encrypted and kept locally in a `data` folder next to the program (or on a USB drive).

## Features

- **Encryption**: AES-256-GCM + scrypt. Nothing can be opened without the master password.
- **Multiple users**: Several people (or purposes) on one computer, each with a fully separate vault.
- **Groups**: Organize sites into groups (folders), drag-and-drop to move them.
- **Search**: Press `Ctrl+F` to find a site by description, address, keyword, or ID all at once.
- **Browser address linking & autofill**: Reads the address bar in Chrome, Edge, Whale, etc., and can auto-fill the ID and password. (Windows only, via UI Automation)
- **Backups**: Automatic backup on every login, plus automatic/manual backup to any folder you choose (USB, cloud-sync folder, etc.). Backups are encrypted by default; an unencrypted CSV export is also available, with a warning.
- **USB-portable**: The `data` folder sits right next to the exe, so you can carry the whole thing on a USB drive and use it on another PC.
- **Update notification & one-click update**: Checks for new releases and, when running as the .exe, can download and apply a new version with a single [Update now] click, then restart. Only version info is sent over the network — your saved data never is.
- **Multiple languages**: Korean · English · Japanese · Simplified Chinese. Choose on first run, or change anytime under `Settings → Language`.

## Download & use

Grab the latest `MyPass.exe` from this repository's **Releases**. No Python installation needed. A `data` folder is created next to the exe automatically, and all your information is encrypted inside it. (You can keep both the exe and the `data` folder on a USB drive.)

## Building from source

Step-by-step build instructions are in [install-guide.md](install-guide.md) and [build-guide.md](build-guide.md). For an extra-hardened build, see [protection-guide.md](protection-guide.md).

## Publishing a new release (for maintainers)

Create a tag in GitHub Releases (e.g. `v2.1`, higher than the current version) and **make sure to attach the exe as a release asset.** The app checks the latest release of the repository preset in `UPDATE_REPO` (default `vhost-lab/mypass`) inside `mypass.py`, notifies users of a new version, and — if an exe asset is attached — lets them apply it and restart with [Update now]. (Menu: Update)

## Security

- All data is encrypted with AES-256-GCM and stored only on this computer. It is never transmitted over the internet.
- The internet is used only to check for updates (and to download a new exe when applying one) — your saved data is never sent.

---

© 2026 Y3 Company. All rights reserved.
