# 代码保护（Nuitka）指南 — 可选

[보호가이드.md](../ko/보호가이드.md) · [protection-guide.md](../en/protection-guide.md) · [protection-guide.md](../ja/protection-guide.md) · [protection-guide.md](protection-guide.md)

用 `build.bat`（PyInstaller）制作的 exe 中，Python 代码以"字节码"形式存在，用记事本打不开，但用 `uncompyle6` 这类专用工具**尝试反编译，就能还原出接近原始源码的内容。**

本指南介绍如何用 **Nuitka** 这款工具，把 Python 代码直接**转换为 C 语言并编译成机器码(machine code)**。因为生成的不是字节码而是真正的可执行文件，普通的 Python 反编译工具对它不起作用。在目前的保护方案中，这是**免费方案里最强的一类**之一。

> 先做一个更正：此前的回答中把 PyArmor 作为"最强"方案推荐给您，但 PyArmor 的 CLI 工具本身虽然可以用 pip 获取，**其字符串加密等实质性保护功能以及商业用途都需要付费授权**（其官方文档自称"Free To Use But Restricted"，并明确说明试用版不能用于商业产品 — [出处](https://pyarmor.readthedocs.io/en/v8.2/licenses.html)）。调查过程本身没有问题，但应该更早、更明确地告知您需要付费这件事。因此现将默认方案改为**完全免费、开源的 Nuitka**。（Nuitka 并非 Apache 系许可，而是 AGPLv3，但其中有一条例外条款，说明"编译生成的可执行文件（exe）不受此约束"，因此您可以把制作好的 MyPass.exe 原样分发，而不必公开源代码 — [出处](https://nuitka.net/pages/overview.html)）

## 1. 运行保护版构建

先按 `빌드가이드.zh.md` 的第2步，把 `mypass_package.zip` 中的文件（`mypass.py`、`mypass_i18n.py`、`build.bat`、`build_protected.bat`、`requirements.txt`、`requirements-protected.txt`、`fonts` 文件夹、`icon.ico` 等）收集到同一个文件夹（如 `C:\mypass_build`），这次双击 **`build_protected.bat`** 而不是 `build.bat`。

- 会自动完成依赖安装、编译、生成 exe 的全过程。
- **第一次运行时会自动下载 C 编译器，因此耗时明显更长（可能超过10分钟）。** 即使看到"WARNING"也不要中途关闭，耐心等待即可。
- 完成后会生成 `dist\MyPass.exe`。（文件名和位置与常规构建相同）

## 2. 需要了解的事项（请务必阅读）

- **填充（Fill）、浏览器联动部分（uiautomation/comtypes）我本人未能直接测试。** comtypes 是在运行过程中动态生成所需代码的机制，在 Nuitka 编译出的 exe 中是否同样能正常工作，需要在真实 Windows 环境中实测一次才能确认。如果出现问题，`build.bat`（PyInstaller）那条路径已经验证可用，可以改用它。
- **可执行文件的体积和首次启动速度**可能比 PyInstaller 构建的版本更大或更慢（因为捆绑了编译运行时）。这不是功能性问题。
- 由于 exe 未经签名，Windows 可能会弹出安全警告（蓝色的"Windows 已保护你的电脑"界面、"未知发布者"）。这个问题在用 PyInstaller 构建时同样会出现，并非 Nuitka 特有。若要扩大分发范围，可以考虑申请代码签名证书。
- 发布更新（参见 `빌드가이드.zh.md` 第6步）时，修改 `mypass.py` 后这次改为重新运行 `build_protected.bat` 即可。

## 3.（参考）PyArmor — 付费替代方案

如果您想额外叠加像 PyArmor 那样连字符串都加密的方案，可以作为备选保留，但请注意：

- **免费试用版不能用于商业分发。** 要真正使用，需要 Pro 或 Group 授权（一次性付费，价格可能随 PyArmor 的政策变化）— 购买前请务必在[官方授权页面](https://pyarmor.readthedocs.io/en/latest/licenses.html)确认最新条款。
- 它不像 Nuitka 那样转换为机器码，而是"加密字节码 + 附带解密代码"的方式，因此与 Nuitka 同时使用没有意义，两者选其一即可。
- 根据授权类型的不同，有些情况下用户的电脑首次运行时需要联网，这与 U 盘便携使用的场景契合度较低。

如果您需要，我也可以另外为 PyArmor 做一份构建脚本，但如果不考虑成本问题，**仍建议以 Nuitka（免费）作为默认方案。**
