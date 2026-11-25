# exe 制作指南（从头到尾，按顺序）

[빌드가이드.md](../ko/빌드가이드.md) · [build-guide.md](../en/build-guide.md) · [build-guide.md](../ja/build-guide.md) · [build-guide.md](build-guide.md)

> 本指南面向 **制作 MyPass.exe 的人**。（在一台电脑上只需做一次）
> 使用制作好的exe的人不需要 Python。→ 参见 `설치가이드.zh.md`
> 请**从上到下**按顺序照做。`这种样式的文字`是需要原样输入的命令。

所需时间：首次约 10～15 分钟（大部分是安装和下载时间）
所需条件：Windows 10/11 电脑、互联网连接

---

## 第1步. 安装 Python

1. 在浏览器中打开 **https://www.python.org/downloads/**。
2. 点击黄色按钮 **`Download Python 3.x.x`** 下载安装文件。（3.10 及以上任意版本均可）
3. 双击下载的文件（`python-3.x.x-amd64.exe`）运行。
4. **务必勾选**首屏**最下方**的 **`Add python.exe to PATH`**。← 这是最重要的一步
5. 点击 **`Install Now`**。（如弹出权限确认窗口，选择"是"）
6. 出现 `Setup was successful` 后点击 **`Close`**。

### 确认安装
1. 按 **`Windows 键 + R`**，在输入框中输入 `cmd` 并回车 → 会打开黑色窗口（命令提示符）。
2. 输入以下内容并回车：

   `python --version`

3. 如出现类似 `Python 3.12.x` 的版本号即为成功。可以关闭黑色窗口。（输入 `exit` 后回车）

> 如果出现 `Python was not found`，或打开了 Microsoft Store → 请参见最下方的 **[疑难解答 1]**。

---

## 第2步. 新建工作文件夹并放入文件

1. 在资源管理器中，于 **C 盘** 下新建文件夹 `mypass_build` → `C:\mypass_build`
   （使用没有中文字符和空格的短路径可减少出错。**也可以解压到其他文件夹**，此时下文的 `C:\mypass_build` 请替换为"你放文件的文件夹"。成品位于该文件夹内的 `dist\MyPass.exe`。）
2. 解压收到的 `mypass_package.zip`。（右键点击 zip → `解压` 或 `全部解压`）
3. 解压后会出现 `mypass` 文件夹，把**其中的文件**移动到 `C:\mypass_build` 内。
4. 打开 `C:\mypass_build` 时，应**直接看到以下内容**。（不是文件夹里的文件夹，而是直接在此文件夹内）

   - `mypass.py`
   - `mypass_i18n.py`（翻译文件）
   - `build.bat`
   - `requirements.txt`（需要安装的软件包列表 — build.bat 会自动读取并一次性安装）
   - `fonts` 文件夹（程序使用的字体 — 构建时会自动复制到生成的 exe 旁边）
   - `icon.ico`

---

## 第3步. 制作 exe

### 方法A. 最简单的方法（推荐）

1. 在 `C:\mypass_build` 文件夹中**双击 `build.bat`**。
2. 会打开黑色窗口并不断滚动文字。**不要关闭，耐心等待。**（首次需 3～10 分钟，视网速而定）
   - `[0/4]` 检查 Python → `[1/4]` 虚拟环境 → `[2/4]` 安装依赖包 → `[3/4]` 正在制作 exe → `[4/4] 完成`
   - 中途出现 `WARNING` 属于正常现象。若因 `ERROR` 中止，请参见 **[疑难解答]**。
3. 最后一行若显示 exe 的路径（类似 `...\dist\MyPass.exe`），紧接着是"按任意键继续"之类的提示行（该提示是 Windows 自带 `pause` 命令的内容，会以你 Windows 系统的显示语言出现），即为成功。按任意键关闭窗口。
4. 确认 `C:\mypass_build\dist\MyPass.exe` 已生成。→ 前往**第5步**。

> 如果 Windows 弹出"Windows 已保护你的电脑"窗口，点击 `更多信息` → `仍要运行`。

### 方法B. 手动输入命令的方法（方法A不成功时使用）

**B-1. 在工作文件夹中打开命令提示符**
1. 用资源管理器打开 `C:\mypass_build` 文件夹。
2. 点击窗口上方的**地址栏**（显示 `C:\mypass_build` 的位置）一次。
3. 删除显示的内容，输入 `cmd` 后回车 → 会打开黑色窗口，最前面应显示 `C:\mypass_build>`。

**无论使用哪种黑色窗口（cmd / PowerShell / Git Bash）** —— 只需按窗口类型替换以下命令开头的 `.venv\Scripts\python.exe` 部分即可输入。（其余部分相同）

| 窗口类型 | 开头部分这样写 |
|---|---|
| 命令提示符(cmd) | `.venv\Scripts\python.exe`（原样照下文输入） |
| PowerShell | `.\.venv\Scripts\python.exe`（开头加上 `.\`） |
| Git Bash (bash) | `./.venv/Scripts/python.exe`（使用斜杠 `/`） |

最开始的 `python -m venv .venv` 在三种窗口中输入方式相同。
（如果不确定该用哪种窗口，最简单的方法是用方法A双击 `build.bat`。）

**B-2. 逐行输入以下命令，输完一行回车，完成后再输下一行**（也可以复制粘贴；在黑色窗口中右键即为粘贴）

① 创建虚拟环境（1～2分钟，完成后会再次出现 `C:\mypass_build>`）

`python -m venv .venv`

② 将 pip（安装工具）更新到最新

`.venv\Scripts\python.exe -m pip install --upgrade pip`

③ 一次性安装所需依赖包（按 `requirements.txt` 中的列表安装；1～3分钟，最后应出现 `Successfully installed ...`）

`.venv\Scripts\python.exe -m pip install -r requirements.txt`

④ 制作 exe（1～3分钟，最后应出现 `Building EXE ... completed successfully.`）

`.venv\Scripts\python.exe -m PyInstaller --noconfirm --clean --onefile --windowed --name MyPass --icon icon.ico --collect-all uiautomation --collect-all comtypes mypass.py`

⑤ 完成后输入 `exit` 并回车关闭窗口。确认 `C:\mypass_build\dist\MyPass.exe` 是否已生成。

---

## 第4步.（参考）各命令的作用
| 命令 | 作用 |
|---|---|
| `python -m venv .venv` | 创建仅在此文件夹内使用的独立 Python 环境（虚拟环境），不会与电脑上其他 Python 混在一起。 |
| `pip install ... cryptography` | 加密功能 |
| `pip install ... uiautomation` | 读取浏览器地址、填充（Fill）功能（仅限 Windows） |
| `pip install ... pyinstaller` | 将 Python 程序打包成 exe 的工具 |
| `PyInstaller ...` | 把 Python 和依赖包打包成一个文件（MyPass.exe）。 |

---

## 第5步. 试运行
1. **双击** `C:\mypass_build\dist\MyPass.exe`。（首次运行可能需要几秒钟）
2. 出现登录窗口即为成功。可以用`新用户`创建用户试用。
3. 运行后会在exe**同一文件夹**内生成 `data` 文件夹，信息保存在其中。
4. 要分发时，**只需复制 `MyPass.exe` 文件**到想要的位置（如 U 盘）即可，不需要 `build`、`.venv` 等文件夹。
5. 删除 `dist\data` 文件夹即可清除测试时创建的用户信息。（分发时请不要复制这个文件夹）

---

## 第6步. 日后制作新版本
1. 用新文件替换 `mypass.py` 和 `mypass_i18n.py`。（放在同一文件夹，直接覆盖）
2. 再次双击 `build.bat`。（因为 `.venv` 已存在，速度会快很多）
3. 会生成新的 `dist\MyPass.exe`。

---

## 疑难解答

**1. 输入 `python` 时出现 `Python was not found`，或打开了 Microsoft Store**
- 原因：安装 Python 时没有勾选 `Add python.exe to PATH`，或是 Windows 的应用商店关联所致。
- 解决①：重新运行 Python 安装文件 → 选择 `Modify` 或先 `Uninstall` 后重新从头安装，并**勾选 PATH**。
- 解决②：按 `Windows 键` → 搜索"应用执行别名"(App execution aliases) → **关闭** `python.exe`、`python3.exe`（应用安装程序）两项。
- 安装完成后，需要**关闭所有已打开的黑色窗口并重新打开**才会生效。
- （参考：若没有 `python`，`build.bat` 会自动尝试 `py` 命令。）

**2. `pip install` 过程中出现 `Could not find a version` / `Connection` / `timed out` 错误**
- 请检查网络连接后重新执行命令。公司或学校网络可能因安全软件而被阻止。

**3. 出现 `'.venv\Scripts\python.exe' is not recognized as an internal or external command...`（不是内部或外部命令）错误**（具体文字会随你 Windows 的显示语言而不同）
- 说明①创建虚拟环境失败。请删除 `.venv` 文件夹，从 `python -m venv .venv` 重新开始。
- 请确认命令提示符是否在 `C:\mypass_build>` 下打开的。

**4. `can't open file ... mypass.py` / `No such file`**
- `mypass.py` 不在 `C:\mypass_build` 的直接目录下。请重新确认第2步的第4点。

**5. 打开 `build.bat` 时文字显示为乱码**
- 窗口显示不影响实际运行，可以改用方法B继续。

**6. 杀毒软件删除了 exe，或将其标记为"威胁"**
- 这是自制的无签名 exe 常见的误报。请将 `dist` 文件夹和 `MyPass.exe` 加入杀毒软件的例外列表后重新制作。

**7. exe 运行后没有任何窗口弹出**
- 请先等待10～20秒。如仍无反应，请检查杀毒软件（见第6条），若任务管理器中仍残留 `MyPass.exe` 进程，结束后再重新运行。
- 如仍无法解决，可用 `python mypass.py` 直接运行查看错误信息：
  `.venv\Scripts\python.exe mypass.py`（此方式无需 `pyinstaller` 也能运行）

**8. `ModuleNotFoundError: No module named ...`**
- 说明第3步③（安装依赖包）没有完整完成，请重新执行③。
