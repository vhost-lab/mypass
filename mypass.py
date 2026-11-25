# -*- coding: utf-8 -*-
"""마이패스 - 알패스 스타일 아이디/비밀번호 관리 프로그램
 - 사용자별 보관함(AES-256-GCM, scrypt 키 유도), 인터넷 전송 없음
 - 주소 키워드 매칭, 그룹(폴더) 관리, 브라우저 자동 채움(Windows)
프로그램 이름을 바꾸려면 아래 APP_NAME 한 줄만 고치세요."""
import os, sys, re, json, csv, time, uuid, shutil, secrets, string, webbrowser
import threading, queue, subprocess, contextlib, io, traceback
import urllib.request, urllib.error
try:
    import certifi
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())      # exe로 묶었을 때 인증서를 못 찾아 "인터넷 연결 안 됨"으로 오인되는 문제 방지
except Exception:
    pass
import zlib, struct, base64, math, locale, tempfile
try:
    from mypass_i18n import LANGS, TR, CSV_HEAD
except ImportError:                       # 번역 파일이 없으면 한국어만
    LANGS, TR = [("ko", "한국어")], {}
    CSV_HEAD = {"ko": ["그룹", "사이트 설명", "주소", "주소 키워드", "아이디", "비밀번호"]}
from urllib.parse import urlparse
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, colorchooser
from tkinter import font as tkfont
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

APP_NAME = "마이패스"
APP_VER = "2.0"
UA_NAME = "MyPass"   # HTTP User-Agent 헤더용 영문 이름. 헤더는 한글 등 유니코드를 담지 못해 APP_NAME을 그대로 쓰면 안 됨
UPDATE_REPO = "vhost-lab/mypass"   # ★ 업데이트 확인용 GitHub 저장소 "계정/저장소". 저장소 이름이 다르면 여기만 고치세요
COPYRIGHT_HOLDER = "Y3 Company"   # ★ 정보 창에 표시할 저작권자. 바꾸려면 여기만 고치세요
MAGIC = b"PWV2"
IDLE_LOCK_SEC = 600      # 기본값(10분). 환경설정 메뉴에서 사용자가 바꿀 수 있음(설정에 저장됨)
IDLE_OPTIONS = [("5분", 300), ("10분", 600), ("15분", 900), ("30분", 1800), ("사용 안 함", 0)]
CLIP_CLEAR_SEC = 20      # 복사한 비밀번호는 20초 뒤 클립보드에서 삭제
STALE_DAYS = 180         # 이 기간(일) 이상 쓰지 않은 사이트를 '오래 안 씀'으로 표시
BG = "#F3F1EA"          # 창 바탕 (따뜻한 아이보리 — 흰 화면보다 눈이 편함)
BG2 = "#FFFFFF"         # 카드(흰 상자) 바탕
FIELD = "#FFFFFF"
BORDER = "#DEDAD0"
TEXT = "#23261F"
MUTED = "#767A6D"
ACCENT = "#1F6D5A"      # 딥 틸 — 보안·신뢰감이 느껴지면서 차분한 색
ACCENT_D = "#15503F"
ACCENT_L = "#E3EFE9"
HOVER = "#ECE8DD"
BAD_C = "#C14B3F"
GOOD_C = "#1F9D5B"
DISABLED_C = "#ADA998"
ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAALzElEQVR4nO1Ze5BU1Zn/fefc27dvd8+DYZ68BFGD+EqA4IZgDYZsiZhEwPQAvpCsSdzaGJPAkl0VL42osVyy65JUSaK1WYuHmc4GXDeCII+JYSAB0cViNDyCojwGpmemp7tvv+453/7R3TCDKEl0FKr2q+qq27dP9f39vsfv+865wP9bvxoVPxekXbDA4TgQpWsuXF84kXAaYQDAs/Pqgg822esemGn/Z+/757WVQP54bsXFP5zu3/nwHSFedGuQ/7kpsAAAnDB8OF8jUQL/yF2h6+ZPs44s/WY5H/nNpbn1/zLIm3+znx+5KzQD6JtewHnAhgFqCkNEo1CLbw/cGU/on31mZMCacWONCviFBMBrXupA66txt67KvGfhJalViwBEImAA/KkScByISAQaABbOshdns1g49uoy3DR5oNYawvM0DIOQ95i3bu/GW/uSlMqoJx+NZr7nNMKItMD71Ag0hyGbolDN3x9iv/Zu7BkpMHvSF6rUxPEVIpPVxAwQAVoziAjlZZK37Yx76zbHTNPEdxY/l/7pt8bC/FQIlLz35L1VQ44eSf8yFBATbvpytXfFZUEj5WqQOJ3bfksgk9VQihEKSl6/tVO37OgWZWViSmSlu+ETJ1AC/+jcsms7u3LNddXWsFturPEG1VuGm1YQogCJCPA8xu69SYy/pgzMADPD5xP6vzd20O43Eh0h25guzvG8j9MoHIaMtMBbdGtwZmdnbtPIiwLD5oTrVX2tZbhpDSEIzIXFWgO2X+BERw7rtnQiGJAACFIQhQKG9ptUo8E3fyIEStIXjUI5swP3p1z13JiryoO3Ta/Ttl/KTFZDCIAZ8PlOJ0Uuz/j61Bp09XjYur0Lti04+psT9MrvuySkmBdZlVrQ7ykUDkNGo1C7lsP89cv2cgLmXndtpWr8mwEil9Oki8XKDPgtwW+/l9b1NZYUohAFKQBPA6vWtnMqpTjWmTsWDBr3OiuTaxxA9GsEnEYY0SjUz78brPvVS/YGyxRzb55S410/YUBBaXqt9fsF//b33fTM6mNy2644234B5gJ4n0mYPqVaK81CGnTQWZlc4zTCWNSffaBUrI99I/C5zk7dXF1lXjL9xhrvosF+I+UWilVrwDQJDNYvboqJHa8lELJpfSaHKTOmVuuxV5aJlKuhNWNglYnWV+O5DVs6fCBaGlntzncaYfRHBKi5WKxL7gjdHIvprRcN8V9yZ7heDW3wG8le4P2WQDqr1Ko17WLX64n0wHJ565Lm9I2miac3bImJQ4fTnm0LhIISO1/v8Vq2dfk8TS2QxlMM0KIWqL+EAOEcY22pWJuiUM7s4A+6e7y1V48Old9+S70uCxgyndGQRfABW6D9ZNZ7tvm4PPi2+25VtTl54crU6nAY8tFw+h43w5vWru8wurrz+d/tjOu1608aPSn1bG2de0NkRc+BIpAPTyHHgcBWCEyCLrV8AHAAgUaIK2rBTVFoAFwqVm6GXPirwDKl+e8nfL5CT54wgPIeqNBRC4UZDAi07U95/7Oxw0i6akdDtT3zez/rOuw0wig+i3/+/fIBfzqcby0Lyc8kXQ0BPLQk6j5cwtUbz1mB8xmeZm40WpcOsZnD8sz1y78FEwCW/UPZwH+6xb/emR3g7cuH5rOto3XXplFc+nRvHsWZbaP1pn8b7D3YZPP94cDq5U5DACiMFqX/CxevF98RutyZFdj34Kzg7b3u98H1vgiUPAkAj80JjO3uUV/N5mkCwMOIYGsNF8QnfVLsCdli3UPXX76Bvv1q/sd3B684FlPRqgrz8mlTqr2Lh9lGyi3ou2bAkAQhoF/cHKNd/9tDlkWPPPxc+sEP8mhJXefdjuDSFUh9kNf7ECgtevwb9rjObl6sNKYMrvVRfZ2FqkoDpimQy2mkXIX2kzkcPZFDMqX2VJTJX8YT6gcjh9kDZ0yt8aoqTSOdKRUrw7IEMhmtfr3upHzrgJurKBfffmiF+4twGLI5Ck0AnwmsEHUQEfjDUuYUgZLnF84KLEhn9JIRQ/3muGvKcelw2wsEJFFfspzLa37veE7s3pMQb7yVxGUjA5h+Q432mSSyOYYQgNKMoC3R3pHz/uvFE8aR49njVVXmrAf+I9lSktmzgToLxrMSPEWg9GcPNNk/EqAfjh9TwZMmVGpTksxmNdSZwQVBCMBnCoBYv304oxvqLGlIorxiiF7F+sc/ud4LGzqMeNLbXTfAN3PeMz0H/gLw52ZXmssXzg5+R3t62d82VuW/OK7SSKYUMfft1aVBi6jvd8tHyOW5z++2X/CO13rUy7/tNDyt14wcHpxz9xOxxMcJHijq+tK/Kx95tCP3xsTPV5g3TR4oEilNsgicAbAGpASkIGYGeYrfR6Q0zxiSICT4pZZO+sPuOExTLF3S7M5n/jPk768wAwAfj+UXDmuw/NdPqPTSGU2iFzApACsgVHdCCdfNk2kKVFUaSmvIfL6g7SUiQgDprMILG2K8d3/KrQjRfGeV+5QDiEUMJvp4wQOA8e93WyMOtesZn72yjG1LylT69GhrSEI2p/Xm1phs2+/CzWjXNCgwfLAlJ46v5Ppai3I5fdr7BiGRUt6h99JGwBaPO6vcp5wwfJEo8hH64EL8KCaOdomvVlWaoUtG2JzNM/X2Zt5jbn6hXWx8pWtzws19qWGQb1QwJMfs3pv4yS+ix+i9YxntM+lUCuXzjMF1Fl06wkYiqa5xHIg2QOFDVOSjmpHO6i+OGOrnynKDc7k+7V5v3d4l3jzo7vzJui/cQNTiAVkAeBfAvfdNpZ4t27ruv+2WegUqdM4iEWqotQBKjp80/CJfJPJOBueQwo9igoD6UFCSFEQlFRECyOQ07z+URnmZuZSoxXtyCixmkOPACIchx48y//Xw0Uy8/UROmgYxF9QVWoMqKwwIQVW7d5wYCABOP54/CWZUWpYA9ZJLQUAmo0XSVSiz5CFm0O/K4BGBIxGoaBTq1nvqE5rRkXIVpOyzN4GUBAJMrXw+FBn0GwEAWc/jPgHWDPj9QgdtiY54figRuD4BoxgBGQ5Drosmy6WgmoAtoVRxqi3WQi6rwZpdn62SALAo0o81IATeiSfUOKWYSwWsNRC0BS672MYfD7r/yNz4PFFLdlnhdw8ABqe75o0aGSivr/OpfJ5lSYmIwImkIgbFJl83LI5lbf16fmlYPvHKyY7c17sTHoUCRuEkTACZjJZjry7ng2+nr/3u1O0bI3OCSy4bbhzcfzBfEetUc8uC8r7JEwdogdNjMAjQzPpoe5aYuO3KprZc7+m2P0wMqbOej3XnkwcOpclnEmtdqDitAcsnaObX6vSXJw6Y5BPi5Tf3eXuVptfHXBW6785wAw+u94tsUbmYAZ9BON6Rp3eOZCjok2sBYPSJ/j1AJgBYMM1aMbjBf9tdMxs81jCKgnK6E1tCdfd4IuUqsiyBARV9OzEAKAWUhYR+fkMHtu2KH5s0KnT5tCdiyeJz+q0GBACqrfYtPnw0m2lp7aZgQGrWxZmTAMVAytXSbwmqrfZxWdDgbJbfBz4UFHjzgKv2tCVFeVBGpj0RSzSHIfoTPACI5jDE/KcT+/yWXPCH1+OydVdchYKSS2lEwKnRIp9nUqrQrUtpo3UB/NH2bO7FlzvMrKdfiKx2nw4XptyPffY50wg4vZm5f6b9ODEWjP9cBX9pQqU2DSGzueJ+oI8fGUIQTJMgJem2fSn90paYEU+o1jFXhW5oipxMFdOwX71/igAKB68iGoV6aFZwnptWj40Y6jfHfbacLx1uq/ftyKi4IzuWE7v39Ii2fSkwo7muwf7mfcs6exxARND/3u9NAMDpSDw2p2JsV0/W0UxfGVRrUkOtDxXlJvyWgNaMnqTC8RNZHGnPIZPVe0Mh+aPIytQKoH9m/j+bQG8SALDkDntcPKG/lvd4PIMGEaOCQUqAjxsG7fbbYt3MGcM3XtnUlnMciEUR8CeRNuc0x4E4822gEEDr0iE2N4/2nbk+3OtM57wyx4FwGmGcSQYAOY0wms9y0HS+24Xzyv9Csf8DgdHBYNrV/3gAAAAASUVORK5CYII="
ID_RE = re.compile(r"^[A-Za-z0-9_.\-가-힣]{1,32}$")
RESERVED = {"con", "prn", "aux", "nul", "settings"} | {f"com{i}" for i in range(1, 10)} | {f"lpt{i}" for i in range(1, 10)}


# ====================
# 언어(다국어)
# ====================
LANG = "ko"
INTERACTIVE_LANG = False        # 실제 실행(__main__)일 때만 True → 처음 실행 시 언어 선택 창을 띄움
_WS = re.compile(r"^(\s*)(.*?)(\s*)$", re.S)


def set_lang(code):
    global LANG
    LANG = code if code in dict(LANGS) else "ko"


TOP_NAMES = {"최상위"} | {d.get("최상위", "최상위") for d in TR.values()}


def tr(s):
    """화면에 보이는 한국어 문구를 현재 언어로 바꿔 준다. (번역이 없으면 그대로)"""
    if LANG == "ko" or not s:
        return s
    d = TR.get(LANG)
    if not d:
        return s
    pre, core, post = _WS.match(s).groups()
    return pre + d.get(core, core) + post


def trf(template, *args):
    """{0} {1} 자리표시자가 있는 문구를 번역한 뒤 값을 채운다."""
    try:
        return tr(template).format(*args)
    except (IndexError, KeyError, ValueError):
        return template.format(*args)


def menu_label(text):
    """'파일(F)' 처럼 끝에 단축키가 붙은 메뉴 이름 → (표시 글자, 밑줄 위치)"""
    t = tr(text)
    i = t.rfind("(")
    return t, (i + 1 if 0 <= i < len(t) - 2 and t.endswith(")") else -1)


def detect_system_lang():
    code = ""
    try:
        if sys.platform == "win32":
            import ctypes
            lid = ctypes.windll.kernel32.GetUserDefaultUILanguage() & 0x3FF
            code = {0x12: "ko", 0x09: "en", 0x11: "ja", 0x04: "zh"}.get(lid, "")
        else:
            code = (locale.getlocale()[0] or "")[:2].lower()
    except Exception:
        pass
    return code if code in dict(LANGS) else "en"



# ====================
# 경로 / 설정
# ====================
def app_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def data_dir():
    d = os.path.join(app_dir(), "data")
    try:
        os.makedirs(d, exist_ok=True)
        t = os.path.join(d, ".w")
        open(t, "w").close()
        os.remove(t)
        return d
    except OSError:
        d = os.path.join(os.environ.get("APPDATA") or os.path.expanduser("~"), APP_NAME, "data")
        os.makedirs(d, exist_ok=True)
        return d


DATA_DIR = data_dir()


def settings_path():
    return os.path.join(DATA_DIR, "settings.json")


def load_settings():
    try:
        with open(settings_path(), encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_settings(s):
    try:
        with open(settings_path(), "w", encoding="utf-8") as f:
            json.dump(s, f, ensure_ascii=False)
    except OSError:
        pass


# ====================
# 공용 계정 (회사 공유드라이브에 두는 계정 하나만 그쪽에, 나머지는 전부 이 컴퓨터에 로컬로)
# ====================
def shared_conf():
    s = load_settings()
    sh = s.get("shared") or {}
    return (sh.get("user") or "").strip(), resolve_path(sh.get("path") or "")


def set_shared_conf(user, path):
    s = load_settings()
    s["shared"] = {"user": user.strip(), "path": (path or "").strip()}
    save_settings(s)


def is_shared_user(user):
    su, sp = shared_conf()
    return bool(su and sp) and user == su


def shared_reachable(path):
    """공유 폴더에 실제로 쓸 수 있는지 확인한다 (드라이브 연결 안 됐으면 False)."""
    if not path:
        return False
    try:
        os.makedirs(path, exist_ok=True)
        t = os.path.join(path, ".w")
        open(t, "w").close()
        os.remove(t)
        return True
    except OSError:
        return False


def resolve_dir(user):
    """이 사용자의 보관함 파일이 실제로 있어야 할 폴더. 공용 계정이면 공유 폴더, 아니면 이 컴퓨터의 data 폴더."""
    su, sp = shared_conf()
    if su and sp and user == su:
        return sp
    return DATA_DIR


def list_users():
    try:
        local = [f[:-4] for f in os.listdir(DATA_DIR)
                 if f.endswith(".dat") and os.path.isfile(os.path.join(DATA_DIR, f))]
    except OSError:
        local = []
    su, sp = shared_conf()
    if su and sp and su not in local:
        try:
            if os.path.isfile(os.path.join(sp, su + ".dat")):
                local.append(su)
        except OSError:
            pass
    return sorted(local)


# ====================
# 백업 / 사용자 삭제
# ====================
BACKUP_DIR = os.path.join(DATA_DIR, "backup")      # 로그인할 때마다 자동으로 쌓이는 백업
DELETED_DIR = os.path.join(DATA_DIR, "_deleted")   # 삭제한 사용자는 여기로 옮겨짐(완전 삭제 아님)
BACKUP_EXT = ".mpbak"
AUTO_BACKUP_KEEP = 10                              # 사용자당 자동 백업 보관 개수


def stamp():
    return time.strftime("%Y%m%d-%H%M%S")


def user_file(user):
    return os.path.join(resolve_dir(user), user + ".dat")


def backup_dir_for(user):
    return os.path.join(resolve_dir(user), "backup")


def deleted_dir_for(user):
    return os.path.join(resolve_dir(user), "_deleted")


def auto_backup(user):
    """로그인 직후 backup 폴더에 백업을 남긴다. 마지막 백업 이후 내용이 하나도 안 바뀌었으면
    찌꺼기 파일을 만들지 않고 건너뛴다. 바뀐 게 있으면 그날 날짜로 하나 만들고, 오래된 건 최근 N개만 남긴다.
    (공용 계정이면 공유 폴더 안의 backup 에, 아니면 이 컴퓨터의 data\\backup 에 쌓인다)"""
    src = user_file(user)
    if not os.path.exists(src):
        return None
    bdir = backup_dir_for(user)
    os.makedirs(bdir, exist_ok=True)
    pat = re.compile(r"^" + re.escape(user) + r"_(\d{8})" + re.escape(BACKUP_EXT) + r"$")
    mine = sorted(f for f in os.listdir(bdir) if pat.match(f))
    if mine:
        try:
            with open(src, "rb") as f1, open(os.path.join(bdir, mine[-1]), "rb") as f2:
                if f1.read() == f2.read():
                    return None          # 마지막 백업과 내용이 완전히 같으면 새로 만들지 않음
        except OSError:
            pass
    dst = os.path.join(bdir, f"{user}_{time.strftime('%Y%m%d')}{BACKUP_EXT}")
    shutil.copy2(src, dst)
    mine = sorted(f for f in os.listdir(bdir) if pat.match(f))
    for old in mine[:-AUTO_BACKUP_KEEP]:
        try:
            os.remove(os.path.join(bdir, old))
        except OSError:
            pass
    return dst


def move_user_to_deleted(user):
    """사용자 보관함을 지우지 않고 _deleted 로 옮긴다(복구 가능).
    (공용 계정이면 공유 폴더 안의 _deleted 로, 아니면 이 컴퓨터의 data\\_deleted 로)"""
    ddir = deleted_dir_for(user)
    os.makedirs(ddir, exist_ok=True)
    base = resolve_dir(user)
    moved = []
    for suffix in (".dat", ".dat.bak"):
        src = os.path.join(base, user + suffix)
        if os.path.exists(src):
            dst = os.path.join(ddir, f"{user}_{stamp()}{suffix}")
            shutil.move(src, dst)
            moved.append(dst)
    return moved


def is_vault_file(path):
    try:
        with open(path, "rb") as f:
            return f.read(4) == MAGIC
    except OSError:
        return False


def guess_user_from_filename(path):
    base = os.path.splitext(os.path.basename(path))[0]
    m = re.match(r"^(.+?)_\d{8}(-\d{6})?$", base)
    return (m.group(1) if m else base)[:32]


def open_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        if sys.platform == "win32":
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception:
        pass


# =================================
# 백업 위치 (사용자가 정한 폴더에 자동 백업)
# =================================
DEST_SUBDIR = "MyPass_backup"
DEST_DEFAULT = {"enabled": False, "path": "", "format": "enc", "keep": 10}
_dest_lock = threading.Lock()


def dest_conf(settings):
    """프로그램 공통 설정(모든 사용자 공통). v1.3 의 사용자별 'cloud' 설정이 있으면 이어받는다."""
    c = dict(DEST_DEFAULT)
    if "backup_dest" in settings:
        c.update(settings.get("backup_dest") or {})
    elif settings.get("cloud"):
        old = settings["cloud"]
        c.update(old.get(settings.get("last_user")) or next(iter(old.values())) or {})
    try:
        c["keep"] = max(1, min(60, int(c["keep"])))
    except (TypeError, ValueError):
        c["keep"] = 10
    if c["format"] not in ("enc", "csv"):
        c["format"] = "enc"
    c["enabled"], c["path"] = bool(c["enabled"]), str(c["path"] or "").strip()
    return c


def set_dest_conf(settings, conf):
    settings["backup_dest"] = {k: conf[k] for k in DEST_DEFAULT}


def resolve_path(p):
    """%USERPROFILE%\\OneDrive, ~/Dropbox 같은 경로를 실제 경로로 바꾼다. (컴퓨터마다 달라도 한 번만 설정)"""
    p = (p or "").strip()
    return os.path.expandvars(os.path.expanduser(p)) if p else ""


def dest_target(conf):
    return os.path.join(resolve_path(conf["path"]), DEST_SUBDIR)


def same_device(a, b):
    try:
        return os.stat(a).st_dev == os.stat(b).st_dev
    except OSError:
        return False


def vault_csv_bytes(vault):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(CSV_HEAD.get(LANG, CSV_HEAD["ko"]))
    for s in vault.data["sites"]:
        w.writerow([vault.names_path(s.get("folder")), s["desc"], s["url"], s["keyword"],
                    s.get("user", ""), s.get("pw", "")])
    return buf.getvalue().encode("utf-8-sig")


def write_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


def dest_backup(conf, user, src_dat, csv_bytes=None):
    """백업 위치에 백업을 쓴다. 돌려주는 값: (성공 여부, 안내 문구)"""
    base = resolve_path(conf.get("path"))
    if not base:
        return False, tr("백업 위치가 지정되지 않았습니다.")
    if not os.path.isdir(base):
        return False, tr("백업 폴더를 찾을 수 없습니다. (드라이브·USB·클라우드 프로그램이 연결되어 있지 않거나, 이 컴퓨터에 없는 경로)")
    try:
        with _dest_lock:
            target = dest_target(conf)
            os.makedirs(target, exist_ok=True)
            if conf["format"] == "csv":
                if csv_bytes is None:
                    return False, tr("CSV 데이터가 없습니다.")
                write_atomic(os.path.join(target, f"{user}_latest.csv"), csv_bytes)
                return True, trf('CSV(암호화 안 됨) 백업 완료: {0}', target)
            with open(src_dat, "rb") as f:
                data = f.read()
            if data[:4] != MAGIC:
                return False, tr("보관함 파일이 올바르지 않아 백업하지 않았습니다.")
            write_atomic(os.path.join(target, f"{user}_latest{BACKUP_EXT}"), data)
            write_atomic(os.path.join(target, f"{user}_{time.strftime('%Y%m%d')}{BACKUP_EXT}"), data)
            pat = re.compile(r"^" + re.escape(user) + r"_(\d{8})" + re.escape(BACKUP_EXT) + r"$")
            days = sorted(f for f in os.listdir(target) if pat.match(f))
            for old in days[:-conf["keep"]]:
                try:
                    os.remove(os.path.join(target, old))
                except OSError:
                    pass
            return True, trf('백업 완료: {0}', target)
    except OSError as e:
        return False, trf('백업하지 못했습니다: {0}', e)


def detect_cloud_folders():
    """흔한 클라우드 동기화 폴더를 찾아 목록으로 돌려준다."""
    out = []

    def add(p):
        if p and os.path.isdir(p) and p not in out:
            out.append(p)
    home = os.path.expanduser("~")
    for env in ("OneDrive", "OneDriveConsumer", "OneDriveCommercial"):
        add(os.environ.get(env, ""))
    try:
        for n in sorted(os.listdir(home)):
            if re.match(r"^(OneDrive|Dropbox|Google ?Drive|iCloud ?Drive|MYBOX|Box|pCloud|Sync)", n, re.I):
                add(os.path.join(home, n))
    except OSError:
        pass
    if sys.platform == "win32":                      # 구글 드라이브 데스크톱은 가상 드라이브(G: 등)로 나타난다
        for L in "DEFGHIJKLMNOPQRSTUVWXYZ":
            for sub in (tr("내 드라이브"), "My Drive"):
                add(f"{L}:\\{sub}")
    return out


# ==================================================
# 업데이트 확인 (GitHub Releases · 알림만, 자동 설치 안 함)
# ==================================================
def parse_ver(s):
    return tuple(int(x) for x in re.findall(r"\d+", s or "")[:4])


def update_conf(settings):
    u = settings.get("update") or {}
    return {"repo": (UPDATE_REPO or "").strip().strip("/"),
            "token": (u.get("token") or "").strip(),
            "auto": bool(u.get("auto", True))}


def check_update(repo, token="", timeout=8):
    """돌려주는 값: (상태, 내용) — 상태: new / latest / error"""
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repo or ""):
        return "error", tr("저장소 이름을 '계정/저장소' 형식으로 입력하세요.")
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases/latest",
                                 headers={"Accept": "application/vnd.github+json", "User-Agent": UA_NAME})
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 404):
            if token:
                return "error", trf('저장소·릴리스를 찾을 수 없거나 토큰 권한이 부족합니다. (오류 {0})', e.code)
            return "error", (trf('저장소·릴리스를 찾을 수 없습니다. (오류 {0})\n비공개(private) 저장소라면 읽기 전용 토큰이 필요합니다.', e.code))
        return "error", trf('업데이트 서버 오류 ({0})', e.code)
    except (urllib.error.URLError, OSError, ValueError) as e:
        try:                                   # 진단용: 실제 오류 내용을 data\update_debug.log 에 남김 (화면 표시는 그대로)
            with open(os.path.join(DATA_DIR, "update_debug.log"), "a", encoding="utf-8") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  {type(e).__name__}: {e}\n")
                f.write(traceback.format_exc() + "\n")
        except Exception:
            pass
        return "error", tr("인터넷에 연결할 수 없어 확인하지 못했습니다.")
    tag = str(d.get("tag_name") or "")
    assets = d.get("assets") or []
    exe = next((a for a in assets if str(a.get("name", "")).lower().endswith(".exe")), None)
    info = {"tag": tag, "name": d.get("name") or tag, "url": d.get("html_url") or f"https://github.com/{repo}/releases",
            "notes": (d.get("body") or "").strip(),
            "asset": {"id": exe["id"], "name": exe["name"], "size": exe.get("size") or 0} if exe else None}
    if parse_ver(tag) and parse_ver(tag) > parse_ver(APP_VER):
        return "new", info
    return "latest", info


def download_asset(repo, asset_id, token, dest, progress_cb=None, timeout=20):
    """GitHub 릴리스 첨부파일(exe)을 dest 경로로 내려받는다. 비공개 저장소도 토큰으로 가능."""
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/releases/assets/{asset_id}",
                                 headers={"Accept": "application/octet-stream", "User-Agent": UA_NAME})
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            total = int(r.headers.get("Content-Length") or 0)
            got = 0
            with open(dest, "wb") as f:
                while True:
                    chunk = r.read(65536)
                    if not chunk:
                        break
                    f.write(chunk)
                    got += len(chunk)
                    if progress_cb:
                        progress_cb(got, total)
        if total and got != total:
            raise OSError("incomplete")
        return True, None
    except Exception as e:
        try:
            os.remove(dest)
        except OSError:
            pass
        return False, str(e)


def apply_update_and_restart(new_path, cur_exe=None):
    '''새 exe 를 현재 exe 자리로 옮겨 넣고 다시 시작한다. (Windows 전용)
    현재 프로그램이 완전히 끝날 때까지 기다리는 작은 배치 스크립트를 띄우고,
    적용이 끝나면 그 배치 스크립트 자신도 지워서 찌꺼기 파일을 남기지 않는다.'''
    cur = cur_exe or sys.executable
    name = os.path.basename(cur)
    bat = os.path.join(tempfile.gettempdir(), f"mypass_upd_{uuid.uuid4().hex}.bat")
    lines = [
        "@echo off",
        "chcp 65001 >nul",
        ":loop",
        f'tasklist /fi "imagename eq {name}" | find /i "{name}" >nul',
        "if not errorlevel 1 (",
        "  ping -n 2 127.0.0.1 >nul",
        "  goto loop",
        ")",
        f'move /y "{new_path}" "{cur}" >nul',
        f'start "" "{cur}"',
        'del "%~f0"',
    ]
    with open(bat, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(lines) + "\n")
    flags = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    subprocess.Popen(["cmd", "/c", bat], creationflags=flags, close_fds=True)


# ====================
# 주소 키워드
# ====================
SLD = {"co", "or", "go", "ne", "ac", "re", "pe", "hs", "ms", "es", "sc", "com", "net", "org", "gov", "edu"}


def host_of(url):
    u = url.strip()
    if not u:
        return ""
    if "://" not in u:
        u = "http://" + u
    try:
        return (urlparse(u).hostname or "").lower()
    except ValueError:
        return ""


def keyword_candidates(url):
    h = host_of(url)
    if not h:
        return []
    if h.startswith("www."):
        h = h[4:]
    if re.fullmatch(r"[\d.]+", h) or "." not in h:
        return [h.upper()]
    lab = h.split(".")
    if len(lab) >= 3 and len(lab[-1]) == 2 and lab[-2] in SLD:
        dom = ".".join(lab[-3:])
    else:
        dom = ".".join(lab[-2:])
    out = [dom.upper()]
    if h != dom:
        out.append(h.upper())
    return out


def find_matches(sites, url):
    u = url.strip().lower()
    if not u:
        return []
    res = [s for s in sites if s.get("keyword") and s["keyword"].lower() in u]
    res.sort(key=lambda s: -len(s["keyword"]))
    return res


def gen_password(n=16):
    sym = "!@#$%^&*?"
    chars = string.ascii_letters + string.digits + sym
    while True:
        p = "".join(secrets.choice(chars) for _ in range(n))
        if (any(c.islower() for c in p) and any(c.isupper() for c in p)
                and any(c.isdigit() for c in p) and any(c in sym for c in p)):
            return p


_PW_PATTERNS = ("1234", "abcd", "qwer", "0000", "asdf", "1111")


def pw_strength(p):
    """비밀번호 강도를 0~4 로 가늠한다. (zxcvbn 같은 외부 라이브러리 없이 길이·문자 종류·뻔한 패턴으로 어림)
    반환값: (점수 0~4, 표시 글자, 색상). 빈 문자열이면 표시하지 않도록 글자를 비워 둔다."""
    if not p:
        return 0, "", MUTED
    classes = sum([any(c.islower() for c in p), any(c.isupper() for c in p),
                   any(c.isdigit() for c in p), any(not c.isalnum() for c in p)])
    n = len(p)
    if n < 8:
        score = 0
    elif n < 10:
        score = 1 if classes <= 2 else 2
    elif n < 14:
        score = 2 if classes <= 2 else 3
    else:
        score = 3 if classes <= 2 else 4
    low = p.lower()
    if re.search(r"(.)\1{2,}", low) or any(seq in low for seq in _PW_PATTERNS):
        score = max(0, score - 1)
    labels = [tr("매우 약함"), tr("약함"), tr("보통"), tr("강함"), tr("매우 강함")]
    colors = [BAD_C, BAD_C, "#C98A2E", GOOD_C, ACCENT]
    return score, labels[score], colors[score]


def add_strength_meter(parent, var):
    """비밀번호 입력칸과 함께 쓰는 강도 표시줄 (1Password 스타일 막대+글자). parent 안에서 pack/grid 둘 다 가능."""
    wrap = tk.Frame(parent, bg=BG)
    bar = tk.Frame(wrap, bg=BG)
    bar.pack(fill="x")
    segs = []
    for i in range(4):
        s = tk.Frame(bar, bg=BORDER, height=4)
        s.pack(side="left", fill="x", expand=True, padx=(0 if i == 0 else 3, 0))
        segs.append(s)
    lbl = tk.Label(wrap, bg=BG, fg=MUTED, font=fnt(8), anchor="w")
    lbl.pack(fill="x", pady=(2, 0))

    def update(*_a):
        score, text, color = pw_strength(var.get())
        for i, s in enumerate(segs):
            s.config(bg=color if i < score else BORDER)
        lbl.config(text=text, fg=color)
    var.trace_add("write", update)
    update()
    return wrap


# ====================
# 보관함
# ====================
class Vault:
    def __init__(self, user):
        self.user, self.key, self.salt = user, None, None
        self.data = self.blank()

    @staticmethod
    def blank():
        return {"folders": [], "sites": []}

    @property
    def path(self):
        return os.path.join(resolve_dir(self.user), self.user + ".dat")

    @staticmethod
    def exists(user):
        try:
            return os.path.exists(os.path.join(resolve_dir(user), user + ".dat"))
        except OSError:
            return False

    @staticmethod
    def _derive(pw, salt):
        return Scrypt(salt=salt, length=32, n=2 ** 15, r=8, p=1).derive(pw.encode("utf-8"))

    def create(self, pw):
        self.salt = os.urandom(16)
        self.key = self._derive(pw, self.salt)
        self.data = self.blank()
        self.save()

    def unlock(self, pw, path=None):
        with open(path or self.path, "rb") as f:
            raw = f.read()
        if raw[:4] != MAGIC:
            raise ValueError(tr("올바른 보관함 파일이 아닙니다."))
        salt, nonce, ct = raw[4:20], raw[20:32], raw[32:]
        key = self._derive(pw, salt)
        try:
            plain = AESGCM(key).decrypt(nonce, ct, MAGIC)
        except InvalidTag:
            return False
        self.salt, self.key = salt, key
        d = json.loads(plain.decode("utf-8"))
        d.setdefault("folders", [])
        d.setdefault("sites", [])
        today = time.strftime("%Y-%m-%d")
        for s in d["sites"]:
            s.setdefault("last_use", today)   # 기존(업데이트 이전) 사이트는 지금을 기준으로 다시 셈
        self.data = d
        return True

    def save(self):
        nonce = os.urandom(12)
        raw = json.dumps(self.data, ensure_ascii=False).encode("utf-8")
        ct = AESGCM(self.key).encrypt(nonce, raw, MAGIC)
        tmp = self.path + ".tmp"
        with open(tmp, "wb") as f:
            f.write(MAGIC + self.salt + nonce + ct)
        if os.path.exists(self.path):
            shutil.copy2(self.path, self.path + ".bak")
        os.replace(tmp, self.path)

    def lock(self):
        self.key = None
        self.data = self.blank()

    def change_password(self, new_pw):
        self.salt = os.urandom(16)
        self.key = self._derive(new_pw, self.salt)
        self.save()

    # ====================
    # 폴더
    # ====================
    def folder(self, fid):
        return next((f for f in self.data["folders"] if f["id"] == fid), None)

    def names_path(self, fid):
        parts = []
        while fid:
            f = self.folder(fid)
            if not f:
                break
            parts.append(f["name"])
            fid = f.get("parent")
        return "/".join(reversed(parts))

    def folder_path(self, fid):
        p = self.names_path(fid)
        return tr("최상위") + ("/" + p if p else "")

    def folder_choices(self):
        out = [(tr("최상위"), None)]

        def walk(pid, prefix):
            kids = [f for f in self.data["folders"] if f.get("parent") == pid]
            for f in sorted(kids, key=lambda f: f["name"].lower()):
                label = prefix + "/" + f["name"]
                out.append((label, f["id"]))
                walk(f["id"], label)
        walk(None, tr("최상위"))
        return out

    def descendants(self, fid):
        ids = set()
        for f in self.data["folders"]:
            if f.get("parent") == fid:
                ids.add(f["id"])
                ids |= self.descendants(f["id"])
        return ids

    def add_folder(self, name, parent):
        name = name.strip()
        if not name or "/" in name or "\\" in name:
            return None
        if any(f.get("parent") == parent and f["name"].lower() == name.lower()
               for f in self.data["folders"]):
            return None
        fid = uuid.uuid4().hex
        self.data["folders"].append({"id": fid, "name": name, "parent": parent})
        return fid

    def ensure_folder_path(self, path):
        parts = [p.strip() for p in re.split(r"[\\/]", path or "") if p.strip()]
        if parts and parts[0] in TOP_NAMES:
            parts = parts[1:]
        pid = None
        for name in parts:
            ex = next((f for f in self.data["folders"]
                       if f.get("parent") == pid and f["name"].lower() == name.lower()), None)
            pid = ex["id"] if ex else self.add_folder(name, pid)
        return pid

    def delete_folder(self, fid):
        f = self.folder(fid)
        if not f:
            return
        ids = {fid} | self.descendants(fid)
        for s in self.data["sites"]:
            if s.get("folder") in ids:
                s["folder"] = f.get("parent")
        self.data["folders"] = [x for x in self.data["folders"] if x["id"] not in ids]

    def rename_folder(self, fid, name):
        f = self.folder(fid)
        name = (name or "").strip()
        if not f or not name or "/" in name or "\\" in name:
            return False
        if any(x["id"] != fid and x.get("parent") == f.get("parent") and x["name"].lower() == name.lower()
               for x in self.data["folders"]):
            return False
        f["name"] = name
        return True

    def move_folder(self, fid, new_parent):
        """그룹을 다른 그룹 안으로 옮긴다. 자기 자신/자기 하위로, 또는 같은 이름이 있는 곳으로는 옮길 수 없다."""
        f = self.folder(fid)
        if not f or new_parent == f.get("parent"):
            return False
        if new_parent == fid or (new_parent is not None and new_parent in self.descendants(fid)):
            return False
        if new_parent is not None and not self.folder(new_parent):
            return False
        if any(x["id"] != fid and x.get("parent") == new_parent and x["name"].lower() == f["name"].lower()
               for x in self.data["folders"]):
            return False
        f["parent"] = new_parent
        return True

    def move_sites(self, site_ids, fid):
        ids = set(site_ids)
        n = 0
        for s in self.data["sites"]:
            if s["id"] in ids and s.get("folder") != fid:
                s["folder"] = fid
                n += 1
        return n

    def count_sites(self, fid):
        """그룹(하위 그룹 포함)에 들어 있는 사이트 수. fid=None 이면 전체."""
        if fid is None:
            return len(self.data["sites"])
        ids = {fid} | self.descendants(fid)
        return sum(1 for s in self.data["sites"] if s.get("folder") in ids)

    def site(self, sid):
        return next((s for s in self.data["sites"] if s["id"] == sid), None)

    # ====================
    # 안 쓰는 사이트
    # ====================
    def touch_site(self, sid):
        """사이트를 실제로 사용(채움·비밀번호 복사)했을 때 '마지막 사용'을 지금으로 갱신한다."""
        s = self.site(sid)
        if s:
            s["last_use"] = time.strftime("%Y-%m-%d")

    def is_stale(self, s):
        lu = s.get("last_use")
        if not lu:
            return False
        try:
            days = (time.time() - time.mktime(time.strptime(lu, "%Y-%m-%d"))) / 86400
        except ValueError:
            return False
        return days >= STALE_DAYS

    def stale_sites(self):
        return [s for s in self.data["sites"] if self.is_stale(s)]


# ============================
# 브라우저 자동 채움 (Windows)
# ============================
if sys.platform == "win32":
    import ctypes
    from ctypes import wintypes

    class _MI(ctypes.Structure):
        _fields_ = [("dx", wintypes.LONG), ("dy", wintypes.LONG), ("mouseData", wintypes.DWORD),
                    ("dwFlags", wintypes.DWORD), ("time", wintypes.DWORD), ("dwExtraInfo", ctypes.c_size_t)]

    class _KI(ctypes.Structure):
        _fields_ = [("wVk", wintypes.WORD), ("wScan", wintypes.WORD), ("dwFlags", wintypes.DWORD),
                    ("time", wintypes.DWORD), ("dwExtraInfo", ctypes.c_size_t)]

    class _HI(ctypes.Structure):
        _fields_ = [("uMsg", wintypes.DWORD), ("wParamL", wintypes.WORD), ("wParamH", wintypes.WORD)]

    class _U(ctypes.Union):
        _fields_ = [("mi", _MI), ("ki", _KI), ("hi", _HI)]

    class _INPUT(ctypes.Structure):
        _anonymous_ = ("u",)
        _fields_ = [("type", wintypes.DWORD), ("u", _U)]

    def _ki(vk, scan, flags):
        i = _INPUT()
        i.type = 1
        i.ki = _KI(vk, scan, flags, 0, 0)
        return i

    def _send(items):
        arr = (_INPUT * len(items))(*items)
        ctypes.windll.user32.SendInput(len(items), arr, ctypes.sizeof(_INPUT))

    def type_text(text):
        for ch in text:
            b = ch.encode("utf-16-le")
            for k in range(0, len(b), 2):
                u = int.from_bytes(b[k:k + 2], "little")
                _send([_ki(0, u, 0x0004), _ki(0, u, 0x0004 | 0x0002)])
            time.sleep(0.008)

    def press_vk(vk):
        _send([_ki(vk, 0, 0), _ki(vk, 0, 0x0002)])


# =====================
# 브라우저 주소 자동 연동
# =====================
BROWSER_EXES = {"chrome.exe", "msedge.exe", "whale.exe", "firefox.exe", "brave.exe",
                "opera.exe", "vivaldi.exe", "iexplore.exe", "chromium.exe", "arc.exe"}
ADDR_HINTS = ("주소", "address", "url", "search", "검색", "location", "アドレス", "検索", "地址", "搜索", "网址", "網址")


def normalize_url(val):
    """주소창 값을 http(s) 주소로 정리한다. 검색어·내부 페이지(chrome:// 등)는 None."""
    v = (val or "").strip()
    if not v or " " in v:
        return None
    if "://" in v:
        return v if v.split("://", 1)[0].lower() in ("http", "https", "ftp") else None
    if re.match(r"^(localhost|[\w\-]+(\.[\w\-]+)+)(:\d+)?([/?#].*)?$", v, re.I):
        return "https://" + v
    return None


class BrowserWatcher(threading.Thread):
    """백그라운드에서 브라우저 주소를 읽어 큐에 넣는다. 실제 읽기는 reader_factory가 만든 객체가 담당:
       reader.foreground_browser() -> 앞창이 브라우저면 창 핸들, 아니면 None
       reader.read(hwnd)           -> 주소창 값(정리 전)"""

    def __init__(self, reader_factory, ctx_factory=None, interval=1.0):
        super().__init__(daemon=True)
        self.reader_factory, self.ctx_factory, self.interval = reader_factory, ctx_factory, interval
        self.q = queue.Queue()
        self.enabled = True
        self.last = None
        self.last_hwnd = None
        self._force = False
        self._wake = threading.Event()
        self._stop_ev = threading.Event()

    def refresh(self):
        """직전에 사용한 브라우저 창에서 주소를 즉시 다시 읽는다."""
        self._force = True
        self._wake.set()

    def stop(self):
        self._stop_ev.set()
        self._wake.set()

    def run(self):
        try:
            ctx = self.ctx_factory() if self.ctx_factory else contextlib.nullcontext()
            with ctx:
                reader = self.reader_factory()
                while not self._stop_ev.is_set():
                    self._wake.wait(self.interval)
                    self._wake.clear()
                    if self._stop_ev.is_set():
                        break
                    force, self._force = self._force, False
                    if not self.enabled and not force:
                        continue
                    try:
                        hwnd = reader.foreground_browser()
                        if hwnd:
                            self.last_hwnd = hwnd
                        elif force and self.last_hwnd:
                            hwnd = self.last_hwnd
                        else:
                            if force:
                                self.q.put(("fail", "no-browser"))
                            continue
                        url = normalize_url(reader.read(hwnd))
                        if url and (url != self.last or force):
                            self.last = url
                            self.q.put(("url", url))
                        elif force and not url:
                            self.q.put(("fail", "no-address"))
                    except Exception:
                        if force:
                            self.q.put(("fail", "error"))
        except Exception as e:
            self.q.put(("unavailable", str(e)))


if sys.platform == "win32":
    def _fg_info():
        u32, k32 = ctypes.windll.user32, ctypes.windll.kernel32
        u32.GetForegroundWindow.restype = wintypes.HWND
        k32.OpenProcess.restype = wintypes.HANDLE
        k32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
        k32.CloseHandle.argtypes = [wintypes.HANDLE]
        hwnd = u32.GetForegroundWindow()
        if not hwnd:
            return None, ""
        pid = wintypes.DWORD()
        u32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        h = k32.OpenProcess(0x1000, False, pid.value)      # PROCESS_QUERY_LIMITED_INFORMATION
        if not h:
            return hwnd, ""
        try:
            buf = ctypes.create_unicode_buffer(1024)
            n = wintypes.DWORD(1024)
            ok = k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n))
            return hwnd, (os.path.basename(buf.value).lower() if ok else "")
        finally:
            k32.CloseHandle(h)

    class WinBrowserReader:
        def __init__(self):
            import uiautomation as auto          # 설치되어 있지 않으면 ImportError → 연동 비활성
            self.auto = auto
            self.cache = {}

        def foreground_browser(self):
            hwnd, exe = _fg_info()
            return hwnd if (hwnd and exe in BROWSER_EXES) else None

        @staticmethod
        def _value(ctl):
            try:
                return ctl.GetValuePattern().Value
            except Exception:
                try:
                    return ctl.GetLegacyIAccessiblePattern().Value
                except Exception:
                    return None

        def _find(self, root, max_depth=9):
            """브라우저 창 안에서 주소창(Edit)을 찾는다. 웹페이지(Document) 안쪽은 들어가지 않는다."""
            best, stack = None, [(root, 0)]
            while stack:
                c, d = stack.pop()
                try:
                    t = c.ControlTypeName
                    if t == "EditControl":
                        name = (c.Name or "").lower()
                        if any(h in name for h in ADDR_HINTS):
                            return c
                        best = best or c
                        continue
                    if t == "DocumentControl" or d >= max_depth:
                        continue
                    kids = c.GetChildren()
                except Exception:
                    continue
                for k in reversed(kids):
                    stack.append((k, d + 1))
            return best

        def read(self, hwnd):
            ctl = self.cache.get(hwnd)
            val = self._value(ctl) if ctl else None
            if val is None:
                ctl = self._find(self.auto.ControlFromHandle(hwnd))
                self.cache = {hwnd: ctl} if ctl else {}
                val = self._value(ctl) if ctl else None
            return val

    def make_win_watcher():
        import uiautomation as auto
        return BrowserWatcher(WinBrowserReader, ctx_factory=auto.UIAutomationInitializerInThread)


# ====================
# 창 크기 / 위치
# ====================
def ui_scale(win):
    try:
        return max(1.0, min(3.0, win.winfo_fpixels("1i") / 96.0))
    except tk.TclError:
        return 1.0


def place_window(win, settings, key, w, h, minw, minh):
    sc = ui_scale(win)
    win.minsize(int(minw * sc), int(minh * sc))
    sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
    W, H, X, Y = int(w * sc), int(h * sc), None, None
    saved = (settings.get("windows") or {}).get(key)
    if isinstance(saved, list) and len(saved) == 4:
        try:
            W, H, X, Y = int(saved[0] * sc), int(saved[1] * sc), int(saved[2]), int(saved[3])
        except (TypeError, ValueError):
            W, H, X, Y = int(w * sc), int(h * sc), None, None
    W = min(max(W, int(minw * sc)), sw)
    H = min(max(H, int(minh * sc)), sh)
    if X is not None and not (-W + 80 < X < sw - 80 and 0 <= Y < sh - 80):
        X = Y = None                                   # 저장된 위치가 화면 밖(모니터 변경 등)
    win.geometry(f"{W}x{H}" + (f"+{X}+{Y}" if X is not None else ""))


def remember_window(win, settings, key):
    try:
        if win.state() in ("zoomed", "iconic", "withdrawn"):
            return
        mt = re.match(r"^(\d+)x(\d+)\+(-?\d+)\+(-?\d+)$", win.geometry())
        if not mt:
            return
        sc = ui_scale(win)
        w, h, x, y = (int(g) for g in mt.groups())
        if w < 100 or h < 100:
            return
        settings.setdefault("windows", {})[key] = [round(w / sc), round(h / sc), x, y]
    except tk.TclError:
        pass


def auto_remember(win, settings, key):
    """창 크기·위치가 바뀌면(0.6초 뒤) 설정에 저장한다."""
    state = {"job": None}

    def flush():
        state["job"] = None
        remember_window(win, settings, key)
        save_settings(settings)

    def on_cfg(e):
        if e.widget is not win:
            return
        if state["job"]:
            win.after_cancel(state["job"])
        state["job"] = win.after(600, flush)
    win.bind("<Configure>", on_cfg, add="+")


# ====================
# 공통 대화상자
# ====================
# ====================
# 화면 디자인(테마)
# ====================
def _png_bytes(w, h, rgba):
    raw = b"".join(b"\x00" + bytes(rgba[y * w * 4:(y + 1) * w * 4]) for y in range(h))

    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xffffffff)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b""))


def _seg(px, py, x0, y0, x1, y1):
    dx, dy = x1 - x0, y1 - y0
    ln = dx * dx + dy * dy
    t = 0 if ln == 0 else max(0, min(1, ((px - x0) * dx + (py - y0) * dy) / ln))
    return math.hypot(px - (x0 + t * dx), py - (y0 + t * dy))


def S_line(x0, y0, x1, y1, t):
    h = t / 2
    return lambda x, y: _seg(x, y, x0, y0, x1, y1) <= h


def S_circle(cx, cy, r):
    return lambda x, y: (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def S_ring(cx, cy, r1, r0, gap=None):
    def f(x, y):
        d = math.hypot(x - cx, y - cy)
        if not (r0 <= d <= r1):
            return False
        if gap:
            a = math.degrees(math.atan2(y - cy, x - cx)) % 360
            if gap[0] <= a <= gap[1]:
                return False
        return True
    return f


def S_rrect(x0, y0, x1, y1, r):
    def f(x, y):
        if x < x0 or x > x1 or y < y0 or y > y1:
            return False
        cx, cy = min(max(x, x0 + r), x1 - r), min(max(y, y0 + r), y1 - r)
        return (x - cx) ** 2 + (y - cy) ** 2 <= r * r
    return f


def S_poly(pts):
    def f(x, y):
        inside = False
        j = len(pts) - 1
        for i in range(len(pts)):
            xi, yi = pts[i]
            xj, yj = pts[j]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                inside = not inside
            j = i
        return inside
    return f


ICON_DEFS = {
    "folder": ("#E0A233", lambda c: [(c, [S_rrect(0.06, 0.16, 0.46, 0.42, 0.06), S_rrect(0.06, 0.28, 0.94, 0.84, 0.08)])]),
    "key": (ACCENT, lambda c: [(c, [S_ring(0.3, 0.5, 0.24, 0.12), S_line(0.5, 0.5, 0.92, 0.5, 0.1),
                                       S_line(0.76, 0.5, 0.76, 0.7, 0.1), S_line(0.9, 0.5, 0.9, 0.66, 0.1)])]),
    "list": ("#3A3D32", lambda c: [(c, [S_line(0.32, 0.25, 0.9, 0.25, 0.1), S_line(0.32, 0.5, 0.9, 0.5, 0.1),
                                        S_line(0.32, 0.75, 0.9, 0.75, 0.1), S_circle(0.14, 0.25, 0.07),
                                        S_circle(0.14, 0.5, 0.07), S_circle(0.14, 0.75, 0.07)])]),
    "plus": (ACCENT, lambda c: [(c, [S_line(0.18, 0.5, 0.82, 0.5, 0.13), S_line(0.5, 0.18, 0.5, 0.82, 0.13)])]),
    "pencil": ("#3A3D32", lambda c: [(c, [S_line(0.34, 0.66, 0.74, 0.26, 0.22), S_poly([(0.1, 0.9), (0.18, 0.62), (0.38, 0.82)])])]),
    "trash": (BAD_C, lambda c: [(c, [S_line(0.16, 0.26, 0.84, 0.26, 0.09), S_line(0.38, 0.17, 0.62, 0.17, 0.09),
                                         S_poly([(0.25, 0.34), (0.75, 0.34), (0.69, 0.88), (0.31, 0.88)])])]),
    "refresh": (ACCENT, lambda c: [(c, [S_ring(0.5, 0.52, 0.36, 0.24, gap=(285, 345)),
                                           S_poly([(0.86, 0.12), (0.88, 0.5), (0.52, 0.34)])])]),
    "go": (GOOD_C, lambda c: [(c, [S_line(0.12, 0.5, 0.74, 0.5, 0.11), S_poly([(0.9, 0.5), (0.6, 0.22), (0.6, 0.78)])])]),
    "ok": (GOOD_C, lambda c: [(c, [S_circle(0.5, 0.5, 0.46)]),
                                 ("#FFFFFF", [S_line(0.28, 0.52, 0.44, 0.67, 0.11), S_line(0.44, 0.67, 0.74, 0.35, 0.11)])]),
    "none": ("#A7A99C", lambda c: [(c, [S_circle(0.5, 0.5, 0.46)]), ("#FFFFFF", [S_line(0.3, 0.5, 0.7, 0.5, 0.11)])]),
    "search": (MUTED, lambda c: [(c, [S_ring(0.42, 0.42, 0.3, 0.19), S_line(0.63, 0.63, 0.88, 0.88, 0.14)])]),
    "warn": ("#C98A2E", lambda c: [(c, [S_poly([(0.5, 0.1), (0.94, 0.86), (0.06, 0.86)])]),
                                      ("#FFFFFF", [S_line(0.5, 0.36, 0.5, 0.63, 0.12), S_circle(0.5, 0.74, 0.065)])]),
    "chev_r": (MUTED, lambda c: [(c, [S_line(0.36, 0.2, 0.64, 0.5, 0.13), S_line(0.64, 0.5, 0.36, 0.8, 0.13)])]),
    "chev_d": (MUTED, lambda c: [(c, [S_line(0.2, 0.36, 0.5, 0.64, 0.13), S_line(0.5, 0.64, 0.8, 0.36, 0.13)])]),
    "blank": ("#FFFFFF", lambda c: []),
}


def render_icon(layers, size, ss=4):
    n = size * ss
    cols = [(int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)) for c, _ in layers]
    out = bytearray(size * size * 4)
    for py in range(size):
        for px in range(size):
            hit = r = g = b = 0
            for sy in range(ss):
                y = (py * ss + sy + 0.5) / n
                for sx in range(ss):
                    x = (px * ss + sx + 0.5) / n
                    for li in range(len(layers) - 1, -1, -1):
                        if any(f(x, y) for f in layers[li][1]):
                            c = cols[li]
                            r, g, b, hit = r + c[0], g + c[1], b + c[2], hit + 1
                            break
            if hit:
                i = (py * size + px) * 4
                out[i], out[i + 1], out[i + 2], out[i + 3] = r // hit, g // hit, b // hit, hit * 255 // (ss * ss)
    return _png_bytes(size, size, out)


class Icons:
    """코드로 그린 아이콘(그림 파일 없이). 화면 배율에 맞춰 선명하게 만든다."""

    def __init__(self, root):
        self.root, self.sc, self.cache = root, ui_scale(root), {}

    def get(self, name, base=18, color=None):
        size = max(10, int(round(base * self.sc)))
        key = (name, size, color)
        if key not in self.cache:
            dc, bld = ICON_DEFS[name]
            try:
                data = base64.b64encode(render_icon(bld(color or dc), size))
                self.cache[key] = tk.PhotoImage(master=self.root, data=data)
            except Exception:
                self.cache[key] = tk.PhotoImage(master=self.root, width=1, height=1)
        return self.cache[key]


ACCENT_PRESETS = [
    ("딥 틸 (기본)", "#1F6D5A"),
    ("네이비", "#2C4A72"),
    ("자두색", "#6B3F63"),
    ("포레스트 그린", "#2E6B3E"),
    ("슬레이트 블루", "#3E4F72"),
    ("테라코타", "#A85A3A"),
    ("차콜", "#3A3D40"),
    ("버건디", "#7A3B4A"),
]


def set_accent(hexcolor):
    """프로그램 전체의 강조 색을 바꾼다. 강조색을 쓰는 아이콘도 함께 새로 그린다."""
    global ACCENT, ACCENT_D
    ACCENT, ACCENT_D = hexcolor, _shade(hexcolor, 0.72)
    for name in ("key", "plus", "refresh"):
        _, bld = ICON_DEFS[name]
        ICON_DEFS[name] = (ACCENT, bld)


FONT_SCALE = 1.0
FONT_BOLD = False
FONT_SCALES = [("작은 글자", 0.9), ("보통 글자", 1.0), ("큰 글자", 1.15), ("아주 큰 글자", 1.3)]


def set_font_prefs(scale=None, bold=None):
    global FONT_SCALE, FONT_BOLD
    if scale:
        FONT_SCALE = scale
    if bold is not None:
        FONT_BOLD = bold


def fnt(size, *styles):
    """현재 글자 크기 배율/굵게 설정을 반영한 폰트 튜플을 만든다."""
    sz = max(6, round(size * FONT_SCALE))
    sl = list(styles)
    if FONT_BOLD and "bold" not in sl:
        sl.append("bold")
    return ("", sz, " ".join(sl)) if sl else ("", sz)


FONT_PREF = {
    "ko": ("Pretendard", "Segoe UI", "맑은 고딕", "Malgun Gothic", "Noto Sans CJK KR", "NanumGothic", "Apple SD Gothic Neo"),
    "ja": ("Noto Sans JP", "Yu Gothic UI", "Meiryo UI", "Segoe UI", "Noto Sans CJK JP", "Hiragino Sans"),
    "zh": ("Noto Sans SC", "Microsoft YaHei UI", "Microsoft YaHei", "Segoe UI", "Noto Sans CJK SC", "PingFang SC"),
    "en": ("Pretendard", "Segoe UI", "Helvetica Neue", "Noto Sans", "DejaVu Sans"),
}

FONT_DIR = os.path.join(app_dir(), "fonts")
_FONTS_LOADED = False
BUNDLED_FONT_FILES = (
    "Pretendard-Regular.ttf", "Pretendard-Bold.ttf",
    "NotoSansJP-Regular.ttf", "NotoSansJP-Bold.ttf",
    "NotoSansSC-Regular.ttf", "NotoSansSC-Bold.ttf",
)


def load_bundled_fonts():
    """같이 배포하는 글꼴 파일을(fonts 폴더) 프로그램 실행 중에만 등록한다.
    실제 글꼴 파일을 설치하는 게 아니라 이 프로그램이 켜져 있는 동안만 쓸 수 있게 임시로 올리는 것뿐이라
    사용자 컴퓨터에 아무 흔적도 남기지 않는다. (Windows 전용, 실패해도 조용히 넘어가고 시스템 글꼴을 그대로 씀)"""
    global _FONTS_LOADED
    if _FONTS_LOADED or sys.platform != "win32":
        return
    _FONTS_LOADED = True
    try:
        import ctypes
        gdi32 = ctypes.windll.gdi32
        for name in BUNDLED_FONT_FILES:
            path = os.path.join(FONT_DIR, name)
            if os.path.isfile(path):
                gdi32.AddFontResourceExW(path, 0x10, 0)   # FR_PRIVATE: 이 프로세스에서만 보임
    except Exception:
        pass


def pick_font_family(root):
    try:
        fams = set(tkfont.families(root))
    except tk.TclError:
        return None
    for f in FONT_PREF.get(LANG, FONT_PREF["ko"]) + FONT_PREF["ko"]:
        if f in fams:
            return f
    return None


def apply_theme(root, icons):
    """프로그램 전체의 색·글꼴·위젯 모양을 한 곳에서 정한다."""
    fam = pick_font_family(root)
    for n in ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont", "TkCaptionFont", "TkTooltipFont"):
        try:
            f = tkfont.nametofont(n)
            if fam:
                f.configure(family=fam)
            f.configure(size=max(6, round(10 * FONT_SCALE)), weight=("bold" if FONT_BOLD else "normal"))
        except tk.TclError:
            pass
    root.configure(bg=BG)
    oa = root.option_add
    for cls in ("Toplevel", "Frame", "Label", "Checkbutton", "Radiobutton"):
        oa(f"*{cls}.background", BG)
    oa("*Label.foreground", TEXT)
    for cls in ("Checkbutton", "Radiobutton"):
        oa(f"*{cls}.foreground", TEXT)
        oa(f"*{cls}.activeBackground", BG)
        oa(f"*{cls}.selectColor", "#FFFFFF")
        oa(f"*{cls}.highlightThickness", 0)
    for cls in ("Entry", "Spinbox"):
        oa(f"*{cls}.relief", "flat")
        oa(f"*{cls}.borderWidth", 4)
        oa(f"*{cls}.background", "#FFFFFF")
        oa(f"*{cls}.foreground", TEXT)
        oa(f"*{cls}.highlightThickness", 1)
        oa(f"*{cls}.highlightBackground", BORDER)
        oa(f"*{cls}.highlightColor", ACCENT)
        oa(f"*{cls}.insertBackground", TEXT)
        oa(f"*{cls}.selectBackground", ACCENT)
        oa(f"*{cls}.selectForeground", "#FFFFFF")
    for cls in ("Listbox", "Text"):
        oa(f"*{cls}.relief", "flat")
        oa(f"*{cls}.borderWidth", 0)
        oa(f"*{cls}.background", "#FFFFFF")
        oa(f"*{cls}.foreground", TEXT)
        oa(f"*{cls}.highlightThickness", 1)
        oa(f"*{cls}.highlightBackground", BORDER)
        oa(f"*{cls}.highlightColor", ACCENT)
        oa(f"*{cls}.selectBackground", ACCENT_L)
        oa(f"*{cls}.selectForeground", TEXT)
    oa("*TCombobox*Listbox.background", "#FFFFFF")
    oa("*TCombobox*Listbox.selectBackground", ACCENT)
    oa("*TCombobox*Listbox.selectForeground", "#FFFFFF")
    oa("*Button.relief", "flat")
    oa("*Button.highlightThickness", 0)

    sc = ui_scale(root)
    st = ttk.Style(root)
    try:
        st.theme_use("clam")
    except tk.TclError:
        pass
    st.configure(".", background=BG, foreground=TEXT, bordercolor=BORDER, focuscolor=BG)
    st.configure("Treeview", background="#FFFFFF", fieldbackground="#FFFFFF", foreground=TEXT, borderwidth=0,
                 relief="flat", rowheight=int(30 * sc * max(1.0, FONT_SCALE)))
    st.map("Treeview", background=[("selected", ACCENT_L)], foreground=[("selected", TEXT)])
    st.configure("Treeview.Heading", background="#EFEBE0", foreground=MUTED, relief="flat", borderwidth=0,
                 padding=(8, 6))
    st.map("Treeview.Heading", background=[("active", "#E2DCC8")])
    # 트리 펼침 표시(▸ ▾)
    try:
        ch_r, ch_d, blank = icons.get("chev_r", 12), icons.get("chev_d", 12), icons.get("blank", 12)
        st.element_create("Treeitem.chev", "image", ch_r, ("user2", blank), ("user1", ch_d))
        st.layout("Treeview.Item", [("Treeitem.padding", {"sticky": "nswe", "children": [
            ("Treeitem.chev", {"side": "left", "sticky": ""}),
            ("Treeitem.image", {"side": "left", "sticky": ""}),
            ("Treeitem.text", {"side": "left", "sticky": ""})]})])
    except tk.TclError:
        pass
    # 얇은 스크롤바
    st.configure("Vertical.TScrollbar", background="#D6D1C0", troughcolor=BG, bordercolor=BG, lightcolor="#D6D1C0",
                 darkcolor="#D6D1C0", relief="flat", gripcount=0, width=int(11 * sc))
    st.map("Vertical.TScrollbar", background=[("active", "#C2BBA4"), ("pressed", "#AFA68A")],
           lightcolor=[("active", "#C2BBA4")], darkcolor=[("active", "#C2BBA4")])
    st.layout("Vertical.TScrollbar", [("Vertical.Scrollbar.trough", {"sticky": "ns", "children": [
        ("Vertical.Scrollbar.thumb", {"expand": "1", "sticky": "nswe"})]})])
    st.configure("TCombobox", fieldbackground="#FFFFFF", background="#FFFFFF", foreground=TEXT, bordercolor=BORDER,
                 lightcolor="#FFFFFF", darkcolor="#FFFFFF", arrowcolor=MUTED, padding=5, relief="flat",
                 selectbackground="#FFFFFF", selectforeground=TEXT)
    st.map("TCombobox", fieldbackground=[("readonly", "#FFFFFF"), ("disabled", BG)],
           bordercolor=[("focus", ACCENT)], lightcolor=[("focus", ACCENT)], darkcolor=[("focus", ACCENT)],
           selectbackground=[("readonly", "#FFFFFF")], selectforeground=[("readonly", TEXT)],
           foreground=[("disabled", MUTED)], arrowcolor=[("hover", ACCENT)])
    st.configure("TPanedwindow", background=BG)
    st.configure("Sash", sashthickness=6, background=BG)


def _shade(hexcolor, factor):
    """색을 살짝 더 어둡게(factor<1) 만든다. 버튼을 누르는 순간의 깊이감(눌림 효과)을 위한 보조 함수."""
    r, g, b = int(hexcolor[1:3], 16), int(hexcolor[3:5], 16), int(hexcolor[5:7], 16)
    return "#%02X%02X%02X" % (max(0, int(r * factor)), max(0, int(g * factor)), max(0, int(b * factor)))


class RoundButton(tk.Canvas):
    """둥글고 부드러운 입체감의 버튼. tk.Button을 Canvas에 직접 그려서 각진 느낌을 없앴다.
    마우스를 올리면 색이 바뀌고, 누르는 순간 살짝 더 진해져 눌림감을 준다."""

    def __init__(self, parent, text="", command=None, primary=False, danger=False,
                 width=None, font=None, radius=10, state="normal", **kw):
        if primary:
            bg, fg, hv, bd = ACCENT, "#FFFFFF", ACCENT_D, ACCENT
            font = font or fnt(10, "bold")
        elif danger:
            bg, fg, hv, bd = "#FFFFFF", BAD_C, "#F6E6E2", BORDER
            font = font or fnt(10)
        else:
            bg, fg, hv, bd = "#FFFFFF", TEXT, HOVER, BORDER
            font = font or fnt(10)
        try:
            pbg = parent.cget("bg")
        except tk.TclError:
            pbg = BG
        padx = kw.pop("padx", 16)
        pady = kw.pop("pady", 8)
        super().__init__(parent, bg=pbg, highlightthickness=0, bd=0, cursor="hand2")
        self._cmd = command
        self._radius = radius
        self._bg, self._fg, self._hv, self._bd = bg, fg, hv, bd
        self._press = _shade(hv, 0.92)
        self._font = tkfont.Font(font=font)
        self._text = text
        self._state = state
        self._cur_fill = bg
        tw = self._font.measure(text)
        th = self._font.metrics("linespace")
        chw = self._font.measure("0")
        w = max((width * chw if width else 0) + padx * 2, tw + padx * 2)
        h = th + pady * 2
        self.configure(width=w, height=h)
        self.bind("<Configure>", self._redraw)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self._redraw()

    def _points(self, w, h, r):
        r = max(0, min(r, w / 2, h / 2))
        return [r, 0, w - r, 0, w, 0, w, r, w, h - r, w, h, w - r, h, r, h, 0, h, 0, h - r, 0, r, 0, 0]

    def _dims(self):
        w = self.winfo_width()
        h = self.winfo_height()
        if w <= 1:
            w = int(self.cget("width"))
        if h <= 1:
            h = int(self.cget("height"))
        return w, h

    def _redraw(self, event=None):
        w, h = self._dims()
        self.delete("all")
        self.create_polygon(self._points(w, h, self._radius), smooth=True,
                             fill=self._cur_fill, outline=self._bd, width=1)
        tc = self._fg if self._state != "disabled" else DISABLED_C
        self.create_text(w / 2, h / 2, text=self._text, fill=tc, font=self._font)

    def _set_fill(self, color):
        self._cur_fill = color
        self._redraw()

    def _on_enter(self, e):
        if self._state != "disabled":
            self._set_fill(self._hv)

    def _on_leave(self, e):
        self._set_fill(self._bg)

    def _on_press(self, e):
        if self._state != "disabled":
            self._set_fill(self._press)

    def _on_release(self, e):
        if self._state == "disabled":
            return
        w, h = self._dims()
        inside = 0 <= e.x <= w and 0 <= e.y <= h
        self._set_fill(self._hv if inside else self._bg)
        if inside and self._cmd:
            self._cmd()

    def config(self, **kw):
        redraw = False
        if "state" in kw:
            self._state = kw.pop("state")
            redraw = True
        if "text" in kw:
            self._text = kw.pop("text")
            redraw = True
        if kw:
            super().config(**kw)
        if redraw:
            self._redraw()

    configure = config

    def cget(self, key):
        if key == "state":
            return self._state
        if key == "text":
            return self._text
        return super().cget(key)


def Btn(parent, text="", command=None, primary=False, danger=False, **kw):
    """RoundButton 생성 편의 함수 (기존 호출부와의 호환용)."""
    return RoundButton(parent, text=text, command=command, primary=primary, danger=danger, **kw)


def card(parent, border=BORDER, bg="#FFFFFF"):
    """옅은 그림자가 드리운 카드형 패널을 만든다. (outer, inner) 를 반환 — outer 를 배치(pack/grid)하고
    내용물은 inner 안에 넣는다. 오른쪽·아래쪽에 그림자색이 살짝 비쳐 공중에 떠 있는 듯한 입체감을 준다."""
    outer = tk.Frame(parent, bg="#DAD5C6")
    inner = tk.Frame(outer, bg=bg, highlightthickness=1, highlightbackground=border, highlightcolor=ACCENT)
    inner.pack(fill="both", expand=True, padx=(0, 2), pady=(0, 2))
    return outer, inner


def autoscroll(sb, target):
    """내용이 넘칠 때만 스크롤바를 보여 주는 set 함수"""
    def _set(first, last):
        sb.set(first, last)
        full = float(first) <= 0.0 and float(last) >= 1.0
        if full and sb.winfo_manager():
            sb.pack_forget()
        elif not full and not sb.winfo_manager():
            sb.pack(side="right", fill="y", before=target)
    return _set


PRIMARY_LABELS = ("확인", "지금 백업", "저장", "다운로드 페이지 열기")


def mkbtn(parent, text, cmd, width=10):
    prim = {tr(x) for x in PRIMARY_LABELS} | set(PRIMARY_LABELS)
    return Btn(parent, text, cmd, primary=text.split("(")[0].strip() in prim, width=width)


def add_entry_placeholder(entry, text, color=None):
    """빈 입력칸 안에 연한 회색 안내문을 보여 준다. 포커스가 가거나 글자를 입력하면 사라지고,
    다시 비운 채로 포커스를 벗어나면 되돌아온다. show=... (비밀번호 칸)도 안내문이 떠 있는 동안만 해제한다."""
    color = color or MUTED
    normal_fg = entry.cget("fg") or "black"
    show_char = entry.cget("show")
    entry._placeholder_on = False

    def _show():
        entry.configure(show="", fg=color)
        entry.insert(0, text)
        entry._placeholder_on = True

    def _hide():
        if entry._placeholder_on:
            entry.delete(0, "end")
            entry.configure(show=show_char, fg=normal_fg)
            entry._placeholder_on = False

    entry.bind("<FocusIn>", lambda ev: _hide(), add="+")
    entry.bind("<FocusOut>", lambda ev: (not entry.get()) and _show(), add="+")
    if not entry.get():
        _show()
    return entry


def fade_in(win, ms=140, steps=10):
    """창이 뜰 때 살짝 투명했다가 또렷해지는 정도의 짧은 페이드인. 과하지 않게 일반적인 프로그램 수준으로만.
    Windows 의 DWM(항상 켜져 있는 합성 효과) 에서만 자연스럽게 보여서 Windows 에서만 동작시킨다."""
    if sys.platform != "win32":
        return

    def step(i=0):
        try:
            win.attributes("-alpha", min(1.0, (i + 1) / steps))
        except tk.TclError:
            return
        if i + 1 < steps:
            win.after(max(1, ms // steps), lambda: step(i + 1))

    try:
        win.attributes("-alpha", 0.0)
    except tk.TclError:
        return
    win.after(1, step)


class Dlg(tk.Toplevel):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.configure(bg=BG)
        self.title(title)
        self.resizable(False, False)
        self.result = None
        self._parent = parent
        try:
            if parent is not None and parent.winfo_viewable():
                self.transient(parent)
        except tk.TclError:
            pass
        self.bind("<Escape>", lambda e: self.destroy())

    def run(self):
        self.update_idletasks()
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        p = self._parent
        try:
            if p is not None and p.winfo_viewable():
                x = p.winfo_rootx() + (p.winfo_width() - w) // 2
                y = p.winfo_rooty() + max(20, (p.winfo_height() - h) // 3)
            else:
                x = (self.winfo_screenwidth() - w) // 2
                y = (self.winfo_screenheight() - h) // 3
        except tk.TclError:
            x = y = 100
        self.geometry(f"+{max(x, 0)}+{max(y, 0)}")
        fade_in(self)
        try:
            self.wait_visibility()
            self.grab_set()
        except tk.TclError:
            pass
        self.focus_force()
        self.wait_window(self)
        return self.result


class NewUserDialog(Dlg):
    def __init__(self, parent):
        super().__init__(parent, trf('{0} - 새 사용자 등록', APP_NAME))
        f = tk.Frame(self, bg=BG)
        f.pack(padx=16, pady=(14, 6))
        self.e = {}
        for r, (label, show) in enumerate([(tr("아이디"), ""), (tr("비밀번호"), "*"), (tr("비밀번호 확인"), "*")]):
            tk.Label(f, text=label, bg=BG, anchor="w").grid(row=r, column=0, sticky="w", pady=5)
            en = tk.Entry(f, width=24, show=show)
            en.grid(row=r, column=1, padx=(14, 0), pady=5)
            self.e[r] = en
        pw_v = tk.StringVar()
        self.e[1].config(textvariable=pw_v)
        add_strength_meter(f, pw_v).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 4))
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=4)
        mkbtn(bf, tr("확인"), self.ok, 12).pack(side="left", padx=8)
        mkbtn(bf, tr("취소"), self.destroy, 12).pack(side="left", padx=8)
        tk.Label(self, bg=BG2, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER, justify="left", anchor="w", padx=10, pady=8,
                 text=tr("INFO : 입력하신 정보는 암호화되어 사용자의\n컴퓨터에 저장되며 인터넷으로 전송되지\n않으므로 회원가입이 필요 없습니다.\n\n※ 비밀번호를 잊으면 복구할 수 없습니다.")
                 ).pack(fill="x", padx=16, pady=(6, 14))
        self.e[0].focus_set()
        self.bind("<Return>", lambda e: self.ok())

    def ok(self):
        uid, p1, p2 = self.e[0].get().strip(), self.e[1].get(), self.e[2].get()
        if not ID_RE.match(uid) or uid.lower() in RESERVED:
            messagebox.showwarning(APP_NAME, tr("아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요."), parent=self)
            return
        if Vault.exists(uid):
            messagebox.showwarning(APP_NAME, tr("이미 등록된 아이디입니다."), parent=self)
            return
        if len(p1) < 8:
            messagebox.showwarning(APP_NAME, tr("비밀번호는 8자 이상 입력하세요."), parent=self)
            return
        if p1 != p2:
            messagebox.showwarning(APP_NAME, tr("비밀번호가 일치하지 않습니다."), parent=self)
            return
        self.result = (uid, p1)
        self.destroy()


def do_delete_user(parent, user, require_password=False):
    """사용자 보관함을 data\\_deleted 폴더로 옮긴다. 완전히 지우지 않으므로 복구할 수 있다."""
    if not user or not Vault.exists(user):
        messagebox.showwarning(APP_NAME, tr("삭제할 사용자를 먼저 선택하세요."), parent=parent)
        return False
    if require_password:
        pw = simpledialog.askstring(APP_NAME, trf("'{0}' 의 마스터 비밀번호를 입력하세요:", user), show="*", parent=parent)
        if pw is None:
            return False
        try:
            ok = Vault(user).unlock(pw)
        except Exception:
            ok = False
        if not ok:
            messagebox.showwarning(APP_NAME, tr("비밀번호가 틀렸습니다."), parent=parent)
            return False
    if not messagebox.askyesno(
            APP_NAME, trf("사용자 '{0}' 와(과) 저장된 모든 사이트 정보를 삭제합니다.\n\n파일은 data\\_deleted 폴더로 옮겨지며, 필요하면 그곳에서 되살릴 수 있습니다.\n계속할까요?", user), parent=parent):
        return False
    typed = simpledialog.askstring(APP_NAME, trf("확인을 위해 아이디 '{0}' 를 그대로 입력하세요:", user), parent=parent)
    if typed is None or typed.strip() != user:
        messagebox.showinfo(APP_NAME, tr("아이디가 일치하지 않아 삭제를 취소했습니다."), parent=parent)
        return False
    try:
        move_user_to_deleted(user)
    except OSError as e:
        messagebox.showerror(APP_NAME, trf('삭제하지 못했습니다.\n{0}', e), parent=parent)
        return False
    messagebox.showinfo(APP_NAME, trf("사용자 '{0}' 를 삭제했습니다.\n(data\\_deleted 폴더에 보관됨)", user), parent=parent)
    return True


def do_restore_backup(parent):
    """백업 파일에서 사용자 보관함을 되살린다. 복원된 아이디를 돌려주고, 취소/실패하면 None."""
    init = BACKUP_DIR if os.path.isdir(BACKUP_DIR) else DATA_DIR
    p = filedialog.askopenfilename(parent=parent, title=tr("복원할 백업 파일 선택"), initialdir=init,
                                   filetypes=[(tr("마이패스 백업"), f"*{BACKUP_EXT} *.dat"), (tr("모든 파일"), "*.*")])
    if not p:
        return None
    if not is_vault_file(p):
        messagebox.showwarning(APP_NAME, tr("올바른 백업 파일이 아닙니다."), parent=parent)
        return None
    pw = simpledialog.askstring(APP_NAME, tr("이 백업을 만들 당시의 마스터 비밀번호를 입력하세요:"), show="*", parent=parent)
    if pw is None:
        return None
    try:
        ok = Vault("_verify").unlock(pw, path=p)
    except Exception:
        ok = False
    if not ok:
        messagebox.showwarning(APP_NAME, tr("비밀번호가 틀렸거나 손상된 백업 파일입니다."), parent=parent)
        return None
    uid = simpledialog.askstring(APP_NAME, tr("복원할 사용자 아이디:"), initialvalue=guess_user_from_filename(p),
                                 parent=parent)
    if uid is None:
        return None
    uid = uid.strip()
    if not ID_RE.match(uid) or uid.lower() in RESERVED:
        messagebox.showwarning(APP_NAME, tr("아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요."), parent=parent)
        return None
    try:
        if Vault.exists(uid):
            if not messagebox.askyesno(APP_NAME, trf("이미 '{0}' 사용자가 있습니다. 백업 내용으로 덮어쓸까요?\n(기존 파일은 data\\_deleted 폴더에 보관됩니다)", uid), parent=parent):
                return None
            move_user_to_deleted(uid)
        shutil.copy2(p, user_file(uid))
    except OSError as e:
        messagebox.showerror(APP_NAME, trf('복원하지 못했습니다.\n{0}', e), parent=parent)
        return None
    messagebox.showinfo(APP_NAME, trf("복원했습니다.\n아이디 '{0}' 와(과) 백업 당시의 마스터 비밀번호로 로그인하세요.", uid), parent=parent)
    return uid


HELP = [
    ("주요 기능", """■ 보관함과 사용자
· 한 대의 컴퓨터에서 여러 사람(또는 용도별)이 각자 독립된 보관함을 쓸 수 있습니다. (서로의 정보는 볼 수 없습니다)
· 저장한 사이트는 '그룹(폴더)'으로 나눠서 정리할 수 있고, 마우스로 끌어다 옮길 수 있습니다.

■ 브라우저 연동과 채움
· 지원하는 브라우저(Chrome·Edge·Whale 등)의 주소창을 읽어서, 지금 보고 있는 사이트의 저장된 정보를 자동으로 찾아줍니다. (Windows 전용)
· [채움] 버튼 하나로 아이디·비밀번호를 브라우저 입력칸에 자동으로 넣어 줍니다.

■ 검색
· 메인 창에서 Ctrl+F(또는 돋보기 버튼)를 누르면 검색창이 열립니다. 사이트 설명·주소·키워드·아이디로 모든 그룹을 한 번에 찾아 줍니다.
· 검색 중에도 그룹(폴더) 구조는 그대로 보이며, 찾은 사이트가 들어 있는 그룹만 펼쳐서 보여 줍니다.

■ 비밀번호 강도 표시
· 새 비밀번호를 만들 때(회원가입, 사이트 추가/수정) 길이와 문자 종류를 보고 '매우 약함~매우 강함'을 막대와 글자로 바로 보여 줍니다.

■ 안 쓰는 사이트 알림
· 오랫동안(기본 180일) [채움]이나 비밀번호 복사로 쓰지 않은 사이트는 목록에 주황색으로 '오래 안 씀' 표시가 붙습니다.
· 로그인하면 오래 안 쓴 사이트가 몇 개인지 요약으로 알려 줍니다. 더 안 쓰는 계정은 정리하거나 비밀번호를 새로 바꾸는 걸 권장합니다.
· [목록관리] 창 왼쪽의 '오래 안 쓴 사이트'를 누르면 그룹과 상관없이 오래 안 쓴 사이트만 한 번에 모아서 볼 수 있습니다. (오래 쓴 순서대로 정렬)

■ 백업
· 로그인할 때마다 자동으로 백업됩니다.
· 원하는 위치(USB, 클라우드 동기화 폴더 등)에 자동 또는 수동으로 백업하도록 설정할 수 있습니다.
· 기본은 암호화된 백업이며, 필요하면 암호화되지 않은 CSV로도 내보낼 수 있습니다 (내보낼 때 경고가 표시됩니다).

■ 들고 다니기 (USB)
· exe 파일 옆에 생기는 'data' 폴더만 있으면 되므로, 둘을 함께 USB에 넣어 다른 컴퓨터에서도 바로 쓸 수 있습니다.

■ 업데이트
· 새 버전이 나오면 알려 주고, [지금 업데이트]를 누르면 새 exe로 자동 교체 · 재시작됩니다.

■ 여러 언어
· 한국어 · English · 日本語 · 简体中文을 지원합니다. 환경설정에서 언제든 바꿀 수 있습니다."""),

    ("시작하기", """■ 처음 사용할 때
1. 프로그램을 실행하면 로그인 창이 나옵니다. [새 사용자(N)]를 눌러 아이디와 마스터 비밀번호를 등록합니다.
2. 등록한 아이디와 비밀번호로 로그인합니다.
3. 메인 창의 [추가] 버튼으로 자주 쓰는 사이트의 주소, 아이디, 비밀번호를 저장합니다.

■ 마스터 비밀번호란?
저장한 모든 정보를 잠그는 열쇠입니다. 8자 이상으로 정하고 꼭 기억해 두세요.
잊어버리면 누구도 복구할 수 없습니다. (프로그램 제작자도 마찬가지입니다)

■ 화면 구성
· 위쪽 버튼: 목록관리 / 추가(▾ 메뉴) / 수정 / 삭제
· 주소 칸: 주소를 입력하거나 브라우저에서 자동으로 가져옵니다.
   ➜ 사이트 열기,  ↻ 브라우저 주소 지금 가져오기
· 사이트 정보 표시줄: 저장된 정보가 있으면 초록 ✔, 없으면 회색 표시
· 아이디·비밀번호 칸과 [채움] 버튼
· 아래 목록: 그룹과 저장된 사이트 (끌어서 그룹으로 이동)
· 맨 아래 상태줄: 현재 로그인한 사용자와 안내 메시지"""),

    ("창 크기와 위치", """■ 기본 크기
처음 열 때는 화면 배율(125%, 150% 등)에 맞춰 보정한 기본 크기로 열립니다. 어느 컴퓨터에서나 같은 모양으로 나옵니다.

■ 마음대로 조절
창 가장자리를 끌어 크기를 자유롭게 줄이고 늘릴 수 있고, 옮겨 둔 위치도 기억합니다.
메인 창, 목록관리 창, 도움말 창이 각각 따로 기억됩니다. 너무 작아지지 않도록 최소 크기는 정해져 있습니다.

■ 되돌리기
환경설정 메뉴 → '창 크기 초기화' 를 누르면 기본 크기로 돌아갑니다.
(모니터를 바꾸는 등으로 저장된 위치가 화면 밖이 되면 자동으로 기본 위치에서 열립니다)"""),

    ("사이트 추가·수정·삭제", """■ 추가
[추가] 버튼 → 주소, 아이디, 비밀번호를 입력하고 [확인].
· 주소 칸에 이미 주소가 들어 있으면 그 주소로 창이 열립니다.
· [추가] 옆 ▾ 에서 '빈 사이트 추가', '그룹 추가'도 고를 수 있습니다.
· 비밀번호 옆 [생성] 버튼은 16자리 무작위 비밀번호를 만들어 줍니다. [보기]로 확인하세요.
· 가입할 때 쓴 비밀번호를 그대로 저장하세요. 생성한 비밀번호는 사이트에도 같이 바꿔 주어야 합니다.

■ 수정 / 삭제
· 목록에서 사이트를 고르고 [수정] 또는 [삭제].
· 목록의 사이트를 더블클릭하면 주소가 채워지고 사이트가 열립니다.
· 목록에서 오른쪽 클릭하면 사이트 열기 / 수정 / 삭제 메뉴가 나옵니다.

■ 같은 사이트에 계정이 여러 개일 때
같은 주소로 사이트를 여러 개 저장하면, 주소가 맞을 때 주소 칸 아래 작은 목록에 모두 나타납니다. 쓸 계정을 고르세요."""),

    ("주소 키워드란?", """저장된 정보를 찾는 기준 단어입니다. 주소창의 주소 안에 이 키워드가 들어 있으면 해당 사이트 정보가 나타납니다.

■ 예시
· NAVER.COM → mail.naver.com, cafe.naver.com 등 네이버 전체에 적용
· MAIL.NAVER.COM → 네이버 메일 주소에만 적용
· 같은 사이트에 키워드가 둘 이상 맞으면 더 긴(구체적인) 키워드가 위에 나옵니다.

■ 자동 생성
주소를 넣으면 키워드가 자동으로 만들어집니다. (www. 는 제외, co.kr 같은 주소도 처리)
키워드 칸의 목록에서 범위를 고를 수 있습니다.

■ 직접 정하고 싶을 때
'이 주소 키워드를 수동 사이트로 설정' 을 체크하면 키워드를 마음대로 적을 수 있습니다."""),

    ("그룹과 목록관리", """사이트가 많아지면 그룹으로 묶어서 정리할 수 있습니다. 그룹 안에 그룹을 만들 수도 있습니다. (예: 업무 ▸ 은행)

■ 그룹 만들기
· 메인 목록에서 오른쪽 클릭 → '그룹 추가' / '하위 그룹 추가'
· 사이트 추가 창의 '그룹명' 옆 [새 그룹] 버튼으로 바로 만들 수 있습니다.

■ 사이트를 그룹으로 옮기기 (3가지 방법)
1. 끌어서 놓기: 메인 목록에서 사이트를 마우스로 끌어 원하는 그룹 위에 놓습니다.
   (그룹을 다른 그룹 위에 놓으면 그 안으로 들어갑니다. 놓을 수 있는 곳은 파란색으로 표시됩니다)
2. 사이트에서 오른쪽 클릭 → '그룹으로 이동' 에서 그룹을 고릅니다.
3. 사이트 [수정] → '그룹명'을 바꿉니다.

■ 여러 개를 한꺼번에 묶기
[목록관리] 창에서 Ctrl 또는 Shift 를 누른 채 사이트를 여러 개 고른 다음 오른쪽 클릭
· '새 그룹으로 묶기': 새 그룹을 만들면서 한 번에 담기
· '그룹으로 이동': 이미 있는 그룹으로 한 번에 옮기기

■ 그룹 관리
· 이름 변경 / 다른 그룹 안으로 이동 / 삭제: 메인 목록의 오른쪽 클릭 메뉴, 또는 [목록관리] 창에서
   그룹 오른쪽의 [수정]을 눌러 팝업에서 바꿉니다.
· 그룹 이름 옆 숫자는 안에 든 사이트 수(하위 그룹 포함)입니다.
· 그룹을 삭제해도 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.
· 맨 위 '최상위' 또는 관리 메뉴에서 '모두 펼치기 / 모두 접기'를 할 수 있습니다.

■ 목록관리 창 (관리대장)
· 왼쪽: 그룹 목록 / 오른쪽: 선택한 그룹의 사이트 목록
· 각 줄 오른쪽의 [수정]을 누르면 팝업이 열립니다. 사이트는 설명·주소·아이디·비밀번호·그룹(경로)을,
   그룹은 이름과 위치(어느 그룹 안에 둘지)를 바꿀 수 있습니다. 사이트 줄의 [삭제]는 그 사이트를 지웁니다.
· 위쪽: [사이트 추가] [그룹 추가], 검색칸 (사이트 설명, 주소, 키워드, 아이디로 전체 검색 · 검색 중에는 모든 그룹에서 찾음)
· 사이트를 여러 개 골라 오른쪽 클릭: 비밀번호 복사 / 그룹으로 이동 / 새 그룹으로 묶기 / 삭제 (Ctrl+A 로 전체 선택)"""),

    ("채움 (자동 입력)", """저장된 아이디와 비밀번호를 브라우저의 로그인 칸에 자동으로 입력합니다. (Windows 전용)

■ 사용 순서
1. 사이트를 열어 로그인 페이지를 띄웁니다.
2. 이 프로그램에서 해당 사이트 정보를 선택합니다. (주소가 맞으면 자동으로 선택됩니다)
3. 브라우저의 아이디 입력칸을 클릭해 커서를 둡니다.
4. 마이패스의 [채움] 버튼을 누릅니다.
→ 아이디 입력 → Tab → 비밀번호 입력 순서로 자동 입력됩니다.

■ 자동 로그인
환경설정 메뉴의 '채움 후 Enter 키 입력' 을 켜면 입력 끝에 Enter 까지 눌러 줍니다.

■ 안 될 때
· 로그인 칸이 '아이디 → 비밀번호' 순서가 아니거나 중간에 다른 칸이 있으면 어긋날 수 있습니다.
   이럴 땐 값을 더블클릭해 아이디와 비밀번호를 각각 복사해서 붙여넣으세요.
· 아이디와 비밀번호를 따로 입력받는 사이트(2단계 로그인)도 복사해서 붙여넣는 방법을 쓰세요.
· 비밀번호는 복사 후 20초가 지나면 클립보드에서 자동으로 지워집니다."""),

    ("브라우저 주소 연동", """브라우저 주소창의 주소를 자동으로 읽어 주소 칸에 넣어 줍니다. (Windows 전용)
브라우저에서 사이트를 이동할 때마다 저장된 정보가 자동으로 나타납니다.

■ 지원 브라우저
크롬, 엣지, 웨일, 파이어폭스, 브레이브, 오페라, 비발디 등

■ 사용법
· 환경설정 메뉴의 '브라우저 주소 자동 연동' 이 켜져 있으면 자동으로 동작합니다.
· 마이패스 창을 브라우저 옆에 두고 '항상 위에 표시' 를 켜면 가장 편합니다.
· 바로 읽고 싶으면 ↻ 버튼 또는 F5 키를 누르세요. (직전에 사용한 브라우저에서 읽어옵니다)

■ 참고
· 마이패스 창을 클릭해도 마지막으로 읽은 주소는 그대로 유지됩니다.
· 주소창에 검색어를 입력 중이거나, chrome:// 같은 내부 페이지는 읽지 않습니다.
· 읽히지 않는 브라우저는 주소를 복사(Ctrl+L, Ctrl+C)해서 주소 칸에 붙여넣으세요.
· 주소는 이 컴퓨터 안에서만 읽히며 어디로도 전송되지 않습니다."""),

    ("사용자 추가·전환·삭제", """한 컴퓨터에서 여러 사람(또는 용도별)이 각자의 보관함을 따로 쓸 수 있습니다.

■ 새 사용자 추가
· 로그인 창의 [새 사용자(N)]에서만 만들 수 있습니다. (다른 사용자로 로그인한 상태에서 실수로/몰래 새 계정을
   만들지 못하도록, 로그인 화면으로 돌아간 뒤에만 가능하게 했습니다 → 파일 메뉴 '로그아웃')
· 아이디와 8자 이상의 비밀번호를 정합니다. 인터넷 회원가입은 필요 없습니다.

■ 로그아웃 / 다른 사용자로 로그인
파일 메뉴 '로그아웃' (또는 '다른 사용자로 로그인') — 지금 보관함을 잠그고 로그인 화면으로 돌아갑니다.
프로그램을 끄는 '종료'와는 다릅니다. 사용자마다 사이트 정보가 완전히 분리됩니다.

■ 사용자 삭제
· 로그인 상태: 파일 메뉴 '현재 사용자 삭제' (마스터 비밀번호 확인 필요)
· 보안을 위해 로그인 창에는 삭제·복원 버튼이 없습니다. 아이디나 비밀번호를 잊은 사용자는 복구할 수 없으며,
   정리하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 직접 지우세요.
· 안전장치: 삭제 전 확인을 거치며, 파일은 data\\_deleted 폴더로 옮겨질 뿐 지워지지 않습니다.
   되살리려면 그 파일을 data 폴더로 옮기고 이름에서 날짜 부분(_20xxxxxx-xxxxxx)만 지우세요.
   (예: aaa_20261009-135500.dat → aaa.dat)

■ 마스터 비밀번호 변경
파일 메뉴 '마스터 비밀번호 변경' (현재 비밀번호 확인 필요)"""),

    ("백업과 복원", """■ 자동 백업 (아무것도 안 해도 됩니다)
· 로그인할 때마다 data\\backup 폴더에 '아이디_날짜.mpbak' 사본이 만들어집니다. (최근 10개 보관)
   단, 지난 백업 이후 바뀐 내용이 하나도 없으면 찌꺼기 파일을 만들지 않고 건너뜁니다.
· 저장할 때마다 같은 폴더에 '아이디.dat.bak' (직전 상태)도 만들어집니다.

■ 직접 백업
파일 메뉴 '백업 만들기' → 원하는 위치(USB, 클라우드 폴더 등)에 저장합니다.
백업 파일은 암호화되어 있어 남이 열어볼 수 없습니다.

■ 복원
· 로그인한 뒤 파일 메뉴 '백업에서 복원' (로그인 창에는 복원 버튼이 없습니다)
· 새 컴퓨터라면: 로그인 창에서 [새 사용자]로 임시 사용자를 만들어 로그인 → '백업에서 복원' →
   복원이 끝나면 '다른 사용자로 로그인'으로 복원한 사용자에 들어갑니다. (임시 사용자는 '현재 사용자 삭제'로 정리)
· 백업 파일 선택 → 백업 당시의 마스터 비밀번호 입력 → 복원할 아이디 입력
· 같은 아이디가 있으면 덮어쓸지 묻고, 기존 파일은 data\\_deleted 에 보관됩니다.
· 복원 후에는 백업 당시의 마스터 비밀번호로 로그인합니다.

■ 백업 위치 (내가 정한 폴더에 자동 백업)
· 파일 메뉴 '백업 위치 설정'에서 백업을 저장할 폴더를 지정합니다. 로그인할 때, 정보를 바꾼 뒤, 종료할 때
   그 폴더의 MyPass_backup 안에 자동으로 백업합니다. (위의 data\\backup 자동 백업과는 별개입니다)
· 폴더는 어디든 됩니다: 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS),
   또는 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더. [클라우드 찾기]로 흔한 클라우드 폴더를 찾을 수 있습니다.
· 클라우드에 직접 로그인하지 않습니다. 이 컴퓨터에 클라우드 프로그램이 설치·로그인되어 있어야 하며, 올리는 일은 그 프로그램이 합니다.
· 프로그램 데이터와 같은 드라이브(같은 USB)를 고르면 함께 사라질 수 있다고 알려 줍니다. 다른 장치를 권장합니다.
· 경로에 %USERPROFILE%\\OneDrive 처럼 환경변수를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.
· 기본은 '암호화 백업(.mpbak)'입니다. 마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 되살립니다.
   (아이디_latest.mpbak = 최신본, 아이디_날짜.mpbak = 날짜별 사본)
· 'CSV' 형식도 고를 수 있지만 암호화되지 않아 비밀번호가 글자 그대로 저장됩니다. 꼭 필요할 때만 쓰세요.
   (아이디_latest.csv 한 파일만 덮어쓰며, 되살릴 때는 'CSV 가져오기'를 사용)
· 설정한 폴더가 그 컴퓨터에 없으면(다른 PC, USB 미연결 등) 백업을 건너뛰고 상태줄에 알려 줍니다.
· [지금 백업] 또는 파일 메뉴 '지금 백업 위치에 백업'으로 바로 실행할 수 있고, 마지막 결과는 설정 창에 표시됩니다.
· 이 설정은 모든 사용자에게 공통이며, 백업 파일 이름에 사용자 아이디가 들어갑니다.

■ 공용 계정 (여러 사람이 같은 목록을 함께 쓰기)
· 환경설정 메뉴 '공용 계정 설정'에서 아이디 하나와 폴더(회사 공유드라이브 등)를 지정하면,
   그 아이디로 로그인할 때만 이 컴퓨터가 아니라 그 폴더의 보관함을 읽고 씁니다.
· 여러 PC에 똑같은 아이디·폴더를 설정해 두면, 그 아이디로 로그인한 모든 사람이 같은 목록을 보고
   추가·수정·삭제·자동채움·복사를 함께 씁니다.
· 그 외의 아이디(개인용)는 지금처럼 각자의 컴퓨터에만 따로 저장되며 서로 영향을 주지 않습니다.
· 공유 폴더에 연결할 수 없으면(네트워크·드라이브 연결 끊김) 그 아이디로는 로그인이 되지 않고 안내만 나옵니다.

■ 권장 습관
중요한 정보라면 가끔 '백업 만들기'로 다른 저장 장치에도 사본을 두세요.
컴퓨터가 고장 나면 data 폴더도 함께 사라집니다."""),

    ("CSV 가져오기·내보내기", """■ 가져오기
· 파일 메뉴 'CSV 가져오기'. 엑셀에서 만든 표나 다른 프로그램에서 내보낸 파일을 읽습니다.
· 첫 줄(제목줄)에 다음 이름이 있으면 자동으로 인식합니다.
   그룹(폴더) / 사이트 설명(사이트명, name) / 주소(url) / 주소 키워드 / 아이디(id) / 비밀번호(password)
· 주소가 없는 줄은 건너뜁니다. 주소 키워드가 비어 있으면 자동으로 만듭니다.
· '그룹' 칸에 업무/은행 처럼 적으면 그룹이 자동으로 만들어집니다. ('폴더'라는 제목도 인식합니다)

■ 내보내기
· 파일 메뉴 'CSV 내보내기'. 엑셀로 열 수 있습니다.
· ※ 내보낸 CSV는 암호화되어 있지 않습니다. 비밀번호가 그대로 보이므로 사용 후 반드시 지우세요.
· 백업 용도라면 CSV 대신 '백업 만들기'를 사용하세요."""),

    ("보안 안내", """■ 내 정보는 어떻게 보호되나요? (쉽게 설명)
· 모든 정보는 '암호화'되어 저장됩니다. 암호화란, 마스터 비밀번호가 없으면 아무도 — 프로그램을 만든 사람도 — 내용을 읽을 수 없도록 뒤섞어 두는 것입니다.
   (전문 용어로는 AES-256-GCM 방식입니다. 지금의 기술로는 사실상 풀 수 없다고 알려진 수준의 암호화 방식이라고 이해하시면 됩니다)
· 마스터 비밀번호 자체는 어디에도 그대로 저장되지 않습니다. 비밀번호를 아주 여러 번 복잡한 계산을 거쳐 '잠금을 푸는 열쇠'로 바꾼 뒤, 그 열쇠로만 보관함을 엽니다.
   (전문 용어로는 scrypt 방식입니다. 이렇게 하면 누군가 비밀번호를 무작위로 하나씩 맞혀 보려고 해도, 한 번 시도하는 데 시간이 오래 걸려서 사실상 불가능해집니다)
· 정보는 이 컴퓨터의 data 폴더에만 저장됩니다. 인터넷 어디로도 보내지지 않습니다.
· 인터넷에 연결되는 경우는 '새 버전이 나왔는지' 확인할 때뿐이며, 이때도 저장된 아이디·비밀번호는 전혀 전송되지 않습니다.

■ 자동 보호 기능
· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.
· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.
· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.
· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.

■ 주의하실 점
· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.
· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.
· 공용 컴퓨터에서는 사용 후 반드시 종료하세요."""),

    ("자주 묻는 질문", """Q. [채움]을 눌러도 입력이 안 돼요.
A. ① 브라우저 아이디 입력칸을 먼저 클릭했는지, ② 관리자 권한으로 실행된 창이 아닌지 확인하세요.
   일부 사이트는 보안 키패드를 써서 자동 입력이 막힙니다. 이때는 값을 복사해서 입력하세요.

Q. 브라우저 주소가 자동으로 안 들어와요.
A. ① 환경설정 메뉴의 '브라우저 주소 자동 연동'이 켜져 있는지, ② 지원 브라우저인지 확인하세요.
   ↻ 버튼(F5)으로 즉시 읽기를 시도해 보고, 안 되면 주소를 직접 붙여넣으세요.

Q. 마스터 비밀번호를 잊었어요.
A. 복구할 방법이 없습니다. 이전 백업의 비밀번호가 기억난다면 백업에서 복원해 보세요.
   포기하고 새로 시작하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 지우고(또는 다른 곳으로 옮기고)
   새 사용자를 만드세요.

Q. 프로그램을 다시 설치/이동하면 정보가 사라지나요?
A. 정보는 프로그램 옆의 data 폴더에 있습니다. 프로그램(exe)을 옮길 때 data 폴더도 같이 옮기세요.

Q. 다른 드라이브나 클라우드에 자동으로 백업하고 싶어요.
A. 파일 메뉴 '백업 위치 설정'에서 폴더를 고르세요. 클라우드라면 그 서비스의 동기화 폴더를 고르면 됩니다.
   (도움말 '백업과 복원' 참고. 암호화 백업을 권장합니다)

Q. 다른 컴퓨터에서도 쓰고 싶어요.
A. 'CSV'는 위험하니 쓰지 말고, '백업 만들기'로 저장한 파일을 새 컴퓨터에서 '백업에서 복원' 하세요.
   (data 폴더를 통째로 복사해도 됩니다)

Q. 백신이 exe 파일을 의심해요.
A. 개인이 만든 프로그램은 서명이 없어 오탐이 생기기도 합니다. 특히 [채움]이 키보드 입력을 대신 하기 때문입니다.
   소스(mypass.py)를 직접 확인하거나 예외 목록에 등록하세요.

Q. 알패스에서 쓰던 정보를 옮기고 싶어요.
A. 알패스가 정보를 CSV 등으로 내보낼 수 있다면 'CSV 가져오기'를 쓰세요. 없다면 직접 입력해야 합니다."""),

    ("단축키", """■ 메인 창
F1          도움말
F5          브라우저 주소 지금 가져오기
Ctrl+N      사이트 추가
Ctrl+F      검색창 열기/닫기 (설명·주소·키워드·아이디로 전체 검색, Esc 로 닫기)
Enter       (주소 칸에서) 사이트 열기
더블클릭    (아이디/비밀번호 값) 복사 · (목록의 사이트) 열기
끌어서 놓기 (메인 목록) 사이트·그룹을 다른 그룹 위에 끌어 이동
Ctrl+A      (목록관리 창) 사이트 전체 선택
오른쪽 클릭 (값/목록) 메뉴

■ 로그인 창
Enter / Alt+O   확인
Alt+C           취소
Alt+N           새 사용자

■ 모든 창
Esc             창 닫기(취소)"""),
]


HELP_FAQ = next(i for i, (t, _) in enumerate(HELP) if t == "자주 묻는 질문")
HELP_SECURITY = next(i for i, (t, _) in enumerate(HELP) if t == "보안 안내")


class HelpWindow(tk.Toplevel):
    def __init__(self, app, topic=0):
        super().__init__(app)
        self.title(trf('{0} - 도움말', APP_NAME))
        self.configure(bg=BG)
        place_window(self, app.settings, "help", 780, 540, 620, 400)
        auto_remember(self, app.settings, "help")
        left = tk.Frame(self, bg=BG)
        left.pack(side="left", fill="y", padx=(8, 4), pady=8)
        self.lb = tk.Listbox(left, width=22, exportselection=False, activestyle="none")
        self.lb.pack(fill="y", expand=True)
        for ht, _ in HELP:
            self.lb.insert("end", "  " + tr(ht))
        right = tk.Frame(self, bg=BG)
        right.pack(side="left", fill="both", expand=True, padx=(4, 8), pady=8)
        sb = ttk.Scrollbar(right, orient="vertical")
        sb.pack(side="right", fill="y")
        self.txt = tk.Text(right, wrap="word", padx=14, pady=10, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER, bg="white",
                           yscrollcommand=autoscroll(sb, self.txt) if False else sb.set, spacing1=2, spacing2=3, spacing3=2, font=fnt(10))
        self.txt.pack(side="left", fill="both", expand=True)
        sb.config(command=self.txt.yview)
        self.txt.configure(yscrollcommand=autoscroll(sb, self.txt))
        self.txt.tag_configure("title", font=fnt(14, "bold"), foreground=ACCENT_D, spacing3=8)
        self.txt.tag_configure("head", font=fnt(10, "bold"), foreground=TEXT, spacing1=10, spacing3=2)
        self.lb.bind("<<ListboxSelect>>", lambda e: self.show(self.lb.curselection()[0]) if self.lb.curselection() else None)
        self.bind("<Escape>", lambda e: self.destroy())
        self.lb.selection_set(topic)
        self.show(topic)

    def show(self, i):
        title, body = tr(HELP[i][0]), tr(HELP[i][1])
        t = self.txt
        t.config(state="normal")
        t.delete("1.0", "end")
        t.insert("end", title + "\n", "title")
        for line in body.split("\n"):
            t.insert("end", line + "\n", "head" if line.startswith("■") else ())
        t.config(state="disabled")
        t.yview_moveto(0)


class AboutDialog(Dlg):
    """정보 창. 자세한 보안·저장 방식 설명은 중복으로 적지 않고 '도움말 → 보안 안내'로 안내만 한다."""

    def __init__(self, app):
        super().__init__(app, trf('{0} - 정보', APP_NAME))
        f = tk.Frame(self, bg=BG)
        f.pack(padx=24, pady=(20, 10))
        if app.icon_img:
            tk.Label(f, image=app.icon_img, bg=BG).pack(side="left", padx=(0, 14))
        tk.Label(f, bg=BG, justify="left", anchor="w", text=trf('{0}  v{1}\n아이디·비밀번호·사이트 정보를 암호화해서 보관하는\n개인용 비밀번호 관리 프로그램', APP_NAME, APP_VER)).pack(side="left")

        def open_security_help():
            self.destroy()
            app.show_help(HELP_SECURITY)

        self.sec_lbl = tk.Label(self, fg=ACCENT, bg=BG, cursor="hand2", font=fnt(9, "underline"),
                                text=tr("암호화·저장 방식 자세히 보기"))
        self.sec_lbl.pack(anchor="w", padx=24)
        self.sec_lbl.bind("<Button-1>", lambda e: open_security_help())

        row = tk.Frame(self, bg=BG)
        row.pack(fill="x", padx=24, pady=(14, 6))
        tk.Label(row, bg=BG, fg=MUTED, text=tr("데이터 폴더")).pack(side="left")
        mkbtn(row, tr("데이터 폴더 열기"), lambda: open_folder(resolve_dir(app.vault.user)), 16).pack(side="right")

        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=(10, 14))
        mkbtn(bf, tr("닫기"), self.destroy, 10).pack(side="left", padx=6)
        tk.Label(self, bg=BG, fg=MUTED, font=fnt(8),
                 text=trf('ⓒ {0} {1}', time.strftime("%Y"), COPYRIGHT_HOLDER)).pack(pady=(0, 10))


class UpdateSettingsDialog(Dlg):
    """업데이트 설정. 저장소가 공개인지 비공개인지 자동으로 확인해서 안내한다.
    (저장소 주소 자체는 mypass.py 맨 위 UPDATE_REPO 값을 그대로 쓴다)"""

    def __init__(self, app):
        super().__init__(app, trf('{0} - 업데이트 설정', APP_NAME))
        c = update_conf(app.settings)
        self.repo = c["repo"]
        self.tok_v = tk.StringVar(value=c["token"])
        self.auto_v = tk.BooleanVar(value=c["auto"])
        self.check_q = queue.Queue()
        self.verify_q = queue.Queue()

        tk.Label(self, bg=BG, justify="left", anchor="w", wraplength=460, text=(
            tr("GitHub 저장소의 최신 Release 를 확인해서 새 버전이 있으면 알려 드립니다. "
            "자동으로 설치하지는 않으며, 다운로드 페이지만 열어 줍니다. "
            "(새 exe 로 바꿔도 data 폴더의 정보는 그대로 유지됩니다)"))).pack(fill="x", padx=16, pady=(14, 6))
        tk.Checkbutton(self, text=tr("로그인할 때 하루 한 번 자동으로 확인"), variable=self.auto_v, bg=BG,
                       activebackground=BG, anchor="w").pack(fill="x", padx=16, pady=(0, 4))

        if not self.repo:
            tk.Label(self, bg=BG, fg=BAD_C, justify="left", anchor="w", wraplength=460,
                     text=tr("업데이트를 확인할 GitHub 저장소가 설정되어 있지 않습니다.\n"
                             "mypass.py 맨 위의 UPDATE_REPO 에 '계정/저장소'를 넣고 다시 만드세요.")
                     ).pack(fill="x", padx=16, pady=(6, 10))
        else:
            st_outer, st_in = card(self, border=BORDER)
            st_outer.pack(fill="x", padx=16, pady=(8, 6))
            self.st_mark = tk.Label(st_in, text="…", bg="#FFFFFF", fg=MUTED, font=fnt(13, "bold"), width=2)
            self.st_mark.pack(side="left", padx=(12, 6), pady=12)
            self.st_text = tk.Label(st_in, bg="#FFFFFF", fg=MUTED, justify="left", anchor="w", wraplength=380,
                                     text=tr("저장소 상태를 확인하는 중..."))
            self.st_text.pack(side="left", fill="both", expand=True, pady=12, padx=(0, 12))
            self.st_outer = st_outer

            tok_outer, tok_in = card(self, border=BAD_C)
            self.tok_outer = tok_outer
            self.tok_in = tok_in
            tk.Label(tok_in, text=tr("비공개 저장소라면 접근용 토큰이 필요합니다"), bg="#FFFFFF", fg="#23261F",
                     anchor="w", font=fnt(9, "bold")).pack(fill="x", padx=12, pady=(10, 6))
            row = tk.Frame(tok_in, bg="#FFFFFF")
            row.pack(fill="x", padx=12)
            self.tok_e = tk.Entry(row, textvariable=self.tok_v, show="•", relief="flat", bd=0,
                                   highlightthickness=1, highlightbackground=BORDER, highlightcolor=ACCENT)
            self.tok_e.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 6))
            add_entry_placeholder(self.tok_e, tr("토큰 붙여넣기"))
            self.eye_btn = tk.Button(row, text=tr("보기"), command=self.toggle_tok_show, relief="flat", bd=0,
                                      bg="#FFFFFF", fg=ACCENT_D, activebackground="#FFFFFF", cursor="hand2",
                                      takefocus=0, font=fnt(8, "underline"))
            self.eye_btn.pack(side="left")
            btnrow = tk.Frame(tok_in, bg="#FFFFFF")
            btnrow.pack(fill="x", padx=12, pady=(6, 4))
            self.verify_btn = tk.Button(btnrow, text=tr("토큰 확인"), command=self.verify_token, relief="flat",
                                         bd=0, bg=ACCENT_L, fg=ACCENT_D, activebackground=ACCENT_L,
                                         cursor="hand2", padx=10, pady=4, font=fnt(9, "bold"))
            self.verify_btn.pack(side="left")
            self.verify_lbl = tk.Label(btnrow, text="", bg="#FFFFFF", fg=MUTED, font=fnt(8), anchor="w")
            self.verify_lbl.pack(side="left", padx=(8, 0), fill="x", expand=True)
            tk.Label(tok_in, bg="#FFFFFF", fg=MUTED, justify="left", anchor="w", wraplength=380, font=fnt(8),
                     text=tr("Fine-grained 토큰(이 저장소 하나, Contents: Read-only)을 발급해 입력하세요. "
                             "토큰은 이 컴퓨터의 data 폴더에만 저장되며 외부로 전송되지 않습니다. "
                             "(data 폴더를 다른 사람과 공유하지 마세요)")
                     ).pack(fill="x", padx=12, pady=(2, 10))
            self.tok_outer.pack_forget()   # 상태 확인이 끝나기 전까지는 숨겨 둔다

        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=12)
        mkbtn(bf, tr("확인"), self.ok, 10).pack(side="left", padx=5)
        mkbtn(bf, tr("취소"), self.destroy, 10).pack(side="left", padx=5)

        if self.repo:
            self.start_check(c["token"])

    def _entry_token(self):
        return "" if getattr(self.tok_e, "_placeholder_on", False) else self.tok_v.get().strip()

    def toggle_tok_show(self):
        if getattr(self.tok_e, "_placeholder_on", False):
            return
        now = self.tok_e.cget("show")
        self.tok_e.config(show="" if now else "•")
        self.eye_btn.config(text=tr("숨기기") if not now else tr("보기"))

    def start_check(self, token):
        def work():
            self.check_q.put(check_update(self.repo, token))
        threading.Thread(target=work, daemon=True).start()
        self.after(150, self._poll_check)

    def _poll_check(self):
        try:
            st, info = self.check_q.get_nowait()
        except queue.Empty:
            self.after(150, self._poll_check)
            return
        if not self.winfo_exists():
            return
        if st in ("new", "latest"):
            self.st_outer.configure(bg=GOOD_C)
            self.st_mark.config(text="✓", fg=GOOD_C)
            self.st_text.config(fg="#23261F", text=tr("저장소에 접근할 수 있습니다 — 자동으로 업데이트를 확인합니다."))
            self.tok_outer.pack_forget()
        else:
            self.st_outer.configure(bg=BAD_C)
            self.st_mark.config(text="!", fg=BAD_C)
            self.st_text.config(fg="#23261F", text=info if isinstance(info, str) else tr("저장소에 접근할 수 없습니다."))
            if not self.tok_outer.winfo_manager():
                self.tok_outer.pack(fill="x", padx=16, pady=(0, 6), before=self.winfo_children()[-1])
            self.update_idletasks()

    def verify_token(self):
        tok = self._entry_token()
        self.verify_btn.config(state="disabled")
        self.verify_lbl.config(fg=MUTED, text=tr("확인하는 중..."))

        def work():
            self.verify_q.put(check_update(self.repo, tok))
        threading.Thread(target=work, daemon=True).start()
        self.after(150, self._poll_verify)

    def _poll_verify(self):
        try:
            st, info = self.verify_q.get_nowait()
        except queue.Empty:
            self.after(150, self._poll_verify)
            return
        if not self.winfo_exists():
            return
        self.verify_btn.config(state="normal")
        if st in ("new", "latest"):
            self.verify_lbl.config(fg=GOOD_C, text=tr("✓ 이 토큰으로 접근을 확인했습니다."))
            self.st_outer.configure(bg=GOOD_C)
            self.st_mark.config(text="✓", fg=GOOD_C)
            self.st_text.config(text=tr("저장소에 접근할 수 있습니다 — 자동으로 업데이트를 확인합니다."))
            self.tok_in.configure(highlightbackground=GOOD_C)
        else:
            self.verify_lbl.config(fg=BAD_C, text=trf('✕ {0}', info if isinstance(info, str) else tr("접근하지 못했습니다.")))

    def ok(self):
        self.result = {"token": self._entry_token(), "auto": self.auto_v.get()}
        self.destroy()


class UpdateNoticeDialog(Dlg):
    def __init__(self, app, info):
        super().__init__(app, trf('{0} - 새 버전', APP_NAME))
        self.info = info
        tk.Label(self, bg=BG, justify="left", anchor="w", font=fnt(10, "bold"),
                 text=trf('새 버전이 있습니다: {0}   (현재 v{1})', info['tag'], APP_VER)).pack(fill="x", padx=16, pady=(14, 4))
        if info["notes"]:
            t = tk.Text(self, width=58, height=9, wrap="word", bg="white", relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
            t.insert("1.0", info["notes"][:1500])
            t.config(state="disabled")
            t.pack(padx=16, pady=4)
        if info.get("asset"):
            msg = tr("[지금 업데이트]를 누르면 새 버전을 받아 자동으로 바꿔 넣고 다시 시작합니다. "
                     "data 폴더는 그대로 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)")
        else:
            msg = tr("다운로드 페이지에서 새 exe 를 받아, 지금 쓰는 exe 파일만 바꿔 넣으세요. "
                     "data 폴더는 그대로 두면 정보가 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)")
        tk.Label(self, bg=BG, fg=MUTED, justify="left", anchor="w", wraplength=440, text=msg
                 ).pack(fill="x", padx=16, pady=4)
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=12)
        if info.get("asset"):
            mkbtn(bf, tr("지금 업데이트"), self.apply_now, 14).pack(side="left", padx=5)
        mkbtn(bf, tr("다운로드 페이지 열기"), self.go, 16).pack(side="left", padx=5)
        mkbtn(bf, tr("나중에"), self.destroy, 10).pack(side="left", padx=5)

    def go(self):
        webbrowser.open(self.info["url"])
        self.destroy()

    def apply_now(self):
        app = self._parent
        self.destroy()
        app.start_self_update(self.info)


class BackupDestDialog(Dlg):
    """백업 위치 설정. result = 새 설정 dict (취소하면 None)"""

    def __init__(self, app):
        super().__init__(app, trf('{0} - 백업 위치 설정', APP_NAME))
        self.app, self.user = app, app.vault.user
        c = dest_conf(app.settings)
        self._csv_asked = c["enabled"] and c["format"] == "csv"
        self._same_asked = False
        self.en_v = tk.BooleanVar(value=c["enabled"])
        self.path_v = tk.StringVar(value=c["path"])
        self.fmt_v = tk.StringVar(value=c["format"])
        self.keep_v = tk.StringVar(value=str(c["keep"]))
        W = 500
        tk.Label(self, bg=BG, justify="left", anchor="w", wraplength=W, text=(
            tr("백업 파일을 자동으로 저장할 폴더를 정하세요. 이 컴퓨터의 다른 드라이브, 외장하드·USB, "
            "네트워크 드라이브(NAS)는 물론 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 "
            "클라우드 동기화 폴더도 됩니다.\n"
            "(클라우드는 계정에 직접 로그인하지 않으며, 이 컴퓨터의 클라우드 프로그램이 파일을 올려 줍니다)"))
                 ).pack(fill="x", padx=16, pady=(14, 6))
        tk.Checkbutton(self, text=tr("백업 위치로 자동 백업 사용"), variable=self.en_v, bg=BG, activebackground=BG,
                       anchor="w").pack(fill="x", padx=16)
        g = tk.Frame(self, bg=BG, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
        g.pack(fill="x", padx=16, pady=6)
        g.columnconfigure(0, weight=1)
        tk.Label(g, text=tr("백업 폴더"), bg=BG, anchor="w").grid(row=0, column=0, columnspan=3, sticky="w",
                                                         padx=10, pady=(8, 2))
        self.path_cb = ttk.Combobox(g, textvariable=self.path_v, width=44)
        self.path_cb.grid(row=1, column=0, sticky="ew", padx=(10, 4))
        Btn(g, text=tr("찾아보기"), command=self.browse).grid(row=1, column=1, padx=2)
        Btn(g, text=tr("클라우드 찾기"), command=self.find).grid(row=1, column=2, padx=(2, 10))
        self.real_v = tk.StringVar()
        tk.Label(g, textvariable=self.real_v, bg=BG, fg=MUTED, anchor="w", justify="left", wraplength=W - 20
                 ).grid(row=2, column=0, columnspan=3, sticky="w", padx=10, pady=(4, 0))
        tk.Label(g, bg=BG, fg=MUTED, anchor="w", justify="left", wraplength=W - 20, font=fnt(8), text=(
            tr("팁: %USERPROFILE%\\OneDrive 처럼 환경변수 경로를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다."))
                 ).grid(row=3, column=0, columnspan=3, sticky="w", padx=10, pady=(0, 8))

        f = tk.Frame(self, bg=BG, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
        f.pack(fill="x", padx=16, pady=4)
        tk.Label(f, text=tr("백업 형식"), bg=BG, anchor="w").pack(fill="x", padx=10, pady=(8, 0))
        tk.Radiobutton(f, text=tr("암호화 백업 (.mpbak) — 권장"), value="enc", variable=self.fmt_v, bg=BG,
                       activebackground=BG, anchor="w", command=self.on_fmt).pack(fill="x", padx=20)
        tk.Label(f, bg=BG, fg=MUTED, anchor="w", justify="left", wraplength=W - 50,
                 text=tr("마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 바로 되살릴 수 있습니다.")
                 ).pack(fill="x", padx=42)
        tk.Radiobutton(f, text=tr("CSV (표 파일) — 암호화되지 않음"), value="csv", variable=self.fmt_v, bg=BG,
                       activebackground=BG, anchor="w", command=self.on_fmt).pack(fill="x", padx=20)
        self.csv_warn = tk.Label(f, bg=BG, fg=BAD_C, anchor="w", justify="left", wraplength=W - 50, text=(
            tr("⚠ 모든 아이디·비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 "
            "전부 노출됩니다. 엑셀로 바로 열어 볼 수 있다는 점이 장점입니다.")))
        kr = tk.Frame(f, bg=BG)
        kr.pack(fill="x", padx=20, pady=(6, 8))
        self.keep_lbl = tk.Label(kr, text=tr("날짜별 사본 보관:"), bg=BG)
        self.keep_lbl.pack(side="left")
        self.keep_sp = tk.Spinbox(kr, from_=1, to=60, width=4, textvariable=self.keep_v)
        self.keep_sp.pack(side="left", padx=4)
        tk.Label(kr, text=tr("개 (암호화 백업만 · 최신본은 항상 따로 저장)"), bg=BG, fg=MUTED).pack(side="left")
        self.csv_after = kr

        self.status_v = tk.StringVar()
        tk.Label(self, textvariable=self.status_v, bg=BG2, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER, anchor="w", justify="left",
                 wraplength=W - 10, padx=8, pady=6).pack(fill="x", padx=16, pady=6)
        tk.Label(self, bg=BG, fg=MUTED, anchor="w", justify="left", wraplength=W,
                 text=tr("자동 백업 시점: 로그인할 때 · 정보를 바꾼 뒤 · 프로그램을 종료할 때")
                 ).pack(fill="x", padx=16)
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=12)
        mkbtn(bf, tr("지금 백업"), self.backup_now, 11).pack(side="left", padx=5)
        mkbtn(bf, tr("확인"), self.ok, 11).pack(side="left", padx=5)
        mkbtn(bf, tr("취소"), self.destroy, 11).pack(side="left", padx=5)
        self.path_v.trace_add("write", lambda *a: self.update_real())
        self.update_real()
        self.on_fmt()
        self.show_status()

    # ====================
    # 화면
    # ====================
    def update_real(self):
        p = self.path_v.get().strip()
        self.real_v.set(trf('실제 저장 위치: {0}', dest_target({'path': p})) if p else
                        trf("선택한 폴더 안에 '{0}' 폴더를 만들어 저장합니다.", DEST_SUBDIR))

    def on_fmt(self):
        csv_on = self.fmt_v.get() == "csv"
        if csv_on:
            self.csv_warn.pack(fill="x", padx=42, before=self.csv_after)
        else:
            self.csv_warn.pack_forget()
        self.keep_sp.config(state="disabled" if csv_on else "normal")
        self.keep_lbl.config(fg=DISABLED_C if csv_on else TEXT)

    def show_status(self):
        st = (self.app.settings.get("backup_dest_status") or {}).get(self.user)
        if st:
            self.status_v.set(trf('마지막 백업: {0}  {1}\n{2}', st.get('time', ''), tr('✔ 성공') if st.get('ok') else tr('✖ 실패'), st.get('msg', '')))
        else:
            self.status_v.set(tr("아직 백업 위치로 백업한 기록이 없습니다."))

    def browse(self):
        cur = resolve_path(self.path_v.get())
        d = filedialog.askdirectory(parent=self, title=tr("백업 폴더 선택"),
                                    initialdir=cur if os.path.isdir(cur) else os.path.expanduser("~"))
        if d:
            self.path_v.set(os.path.normpath(d))

    def find(self):
        self.config(cursor="watch")
        self.update_idletasks()
        try:
            found = detect_cloud_folders()
        finally:
            self.config(cursor="")
        if not found:
            messagebox.showinfo(APP_NAME, tr("클라우드 폴더를 자동으로 찾지 못했습니다.\n[찾아보기]로 직접 고르세요."), parent=self)
            return
        self.path_cb["values"] = found
        if not self.path_v.get().strip():
            self.path_v.set(found[0])
        messagebox.showinfo(APP_NAME, trf('{0}곳을 찾았습니다. 입력칸 오른쪽 ▼ 에서 고르세요.\n\n', len(found)) + "\n".join(found[:8]),
                            parent=self)

    # ====================
    # 확인 / 지금 백업
    # ====================
    def _collect(self):
        p = self.path_v.get().strip()
        try:
            keep = max(1, min(60, int(self.keep_v.get())))
        except ValueError:
            keep = 10
        if p and "%" not in p and not p.startswith("~"):
            p = os.path.normpath(p)
        return {"enabled": self.en_v.get(), "path": p, "format": self.fmt_v.get(), "keep": keep}

    def _check_path(self, conf):
        base = resolve_path(conf["path"])
        if not base:
            messagebox.showwarning(APP_NAME, tr("백업 폴더를 지정하세요."), parent=self)
            return False
        if not os.path.isdir(base):
            messagebox.showwarning(APP_NAME, tr("지정한 폴더를 찾을 수 없습니다.\n경로가 맞는지, 드라이브·USB·클라우드 프로그램이 연결되어 있는지 확인하세요."), parent=self)
            return False
        if not self._same_asked and same_device(base, resolve_dir(self.user)):
            ok = messagebox.askyesno(
                APP_NAME, tr("이 폴더는 프로그램 데이터(data 폴더)와 같은 드라이브(또는 같은 USB)에 있습니다.\n"
                          "그 장치가 고장 나거나 분실되면 원본과 백업이 함께 사라집니다.\n\n"
                          "다른 장치(다른 드라이브·클라우드 등)의 폴더를 권장합니다.\n그래도 이 폴더를 사용할까요?"), parent=self)
            if not ok:
                return False
            self._same_asked = True
        return True

    def _confirm_csv(self, conf):
        if conf["format"] != "csv" or self._csv_asked:
            return True
        ok = messagebox.askokcancel(
            APP_NAME, tr("CSV 백업은 암호화되지 않습니다.\n\n모든 사이트의 아이디와 비밀번호가 글자 그대로 저장됩니다. "
                      "그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다.\n\n"
                      "그래도 CSV로 백업할까요?\n(권장: 암호화 백업)"), icon="warning", parent=self)
        self._csv_asked = bool(ok)
        return bool(ok)

    def backup_now(self):
        conf = self._collect()
        if not self._check_path(conf) or not self._confirm_csv(conf):
            return
        csv_bytes = vault_csv_bytes(self.app.vault) if conf["format"] == "csv" else None
        ok, msg = dest_backup(conf, self.user, self.app.vault.path, csv_bytes)
        self.app.dest_status_set(ok, msg, user=self.user)
        self.show_status()
        (messagebox.showinfo if ok else messagebox.showwarning)(APP_NAME, msg, parent=self)

    def ok(self):
        conf = self._collect()
        if conf["enabled"] and (not self._check_path(conf) or not self._confirm_csv(conf)):
            return
        self.result = conf
        self.destroy()


class SharedAccountDialog(Dlg):
    """공용 계정 설정. 지정한 아이디 하나만 이 컴퓨터가 아니라 공유 폴더(회사 공유드라이브 등)에 저장하게 한다.
    그 아이디로 로그인하는 모든 PC가 같은 폴더를 보게 되므로, 모든 직원 PC에 이 설정을 똑같이 입력해야 한다.
    result = (user, path) 또는 끄기면 ("", "") (취소면 None)"""

    def __init__(self, app):
        super().__init__(app, trf('{0} - 공용 계정 설정', APP_NAME))
        su, sp = shared_conf()
        W = 480
        tk.Label(self, bg=BG, justify="left", anchor="w", wraplength=W, text=(
            tr("한 아이디만 이 컴퓨터가 아니라 지정한 공유 폴더(회사 공유드라이브 등)에 저장되게 합니다. "
            "그 아이디로 여러 PC에서 로그인하면 전부 같은 비밀번호 목록을 보게 됩니다. "
            "그 외의 아이디는 지금처럼 각자의 컴퓨터에만 저장됩니다.\n"
            "모든 PC에 이 설정(아이디·폴더)을 똑같이 입력해야 같은 곳을 보게 됩니다."))
                 ).pack(fill="x", padx=16, pady=(14, 8))

        g = tk.Frame(self, bg=BG, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
        g.pack(fill="x", padx=16, pady=4)
        g.columnconfigure(1, weight=1)
        tk.Label(g, text=tr("공용 아이디"), bg=BG, anchor="w").grid(row=0, column=0, sticky="w", padx=(10, 6), pady=(10, 4))
        self.user_v = tk.StringVar(value=su)
        tk.Entry(g, textvariable=self.user_v, width=20).grid(row=0, column=1, sticky="w", pady=(10, 4))
        tk.Label(g, text=tr("공유 폴더"), bg=BG, anchor="w").grid(row=1, column=0, sticky="w", padx=(10, 6), pady=4)
        row = tk.Frame(g, bg=BG)
        row.grid(row=1, column=1, sticky="ew", pady=4, padx=(0, 10))
        self.path_v = tk.StringVar(value=sp)
        self.path_e = tk.Entry(row, textvariable=self.path_v)
        self.path_e.pack(side="left", fill="x", expand=True, padx=(0, 6))
        Btn(row, text=tr("찾아보기"), command=self.browse).pack(side="left")
        tk.Label(g, bg=BG, fg=MUTED, justify="left", anchor="w", wraplength=W - 20, font=fnt(8), text=(
            tr("비워 두면 공용 계정 기능이 꺼집니다. (모든 아이디가 지금처럼 로컬에만 저장됩니다)")
                 )).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=(0, 10))

        self.status_v = tk.StringVar()
        tk.Label(self, textvariable=self.status_v, bg=BG2, relief="flat", bd=0, highlightthickness=1,
                 highlightbackground=BORDER, anchor="w", justify="left", wraplength=W - 10, padx=8, pady=6
                 ).pack(fill="x", padx=16, pady=(8, 4))

        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=12)
        mkbtn(bf, tr("연결 확인"), self.check_now, 10).pack(side="left", padx=5)
        mkbtn(bf, tr("확인"), self.ok, 10).pack(side="left", padx=5)
        mkbtn(bf, tr("취소"), self.destroy, 10).pack(side="left", padx=5)
        self.check_now(silent=True)

    def browse(self):
        cur = resolve_path(self.path_v.get())
        d = filedialog.askdirectory(parent=self, title=tr("공유 폴더 선택"),
                                    initialdir=cur if os.path.isdir(cur) else os.path.expanduser("~"))
        if d:
            self.path_v.set(os.path.normpath(d))

    def check_now(self, silent=False):
        path = resolve_path(self.path_v.get())
        if not path:
            self.status_v.set(tr("공유 폴더가 비어 있습니다. (공용 계정 기능이 꺼진 상태로 저장됩니다)"))
            return
        if shared_reachable(path):
            self.status_v.set(trf('✓ 이 폴더에 연결되고 쓸 수 있습니다.\n{0}', path))
        else:
            self.status_v.set(trf('✕ 이 폴더에 연결할 수 없습니다. 경로·네트워크 연결을 확인하세요.\n{0}', path))
            if not silent:
                messagebox.showwarning(APP_NAME, tr("지정한 폴더에 연결할 수 없습니다. 그래도 저장할 수는 있지만, "
                                                  "실제로 연결되기 전까지는 그 아이디로 로그인할 수 없습니다."), parent=self)

    def ok(self):
        user = self.user_v.get().strip()
        path = resolve_path(self.path_v.get())
        if not user and not path:
            self.result = ("", "")
            self.destroy()
            return
        if not user or not path:
            messagebox.showwarning(APP_NAME, tr("아이디와 폴더를 둘 다 입력하거나, 둘 다 비워서 꺼 주세요."), parent=self)
            return
        if not ID_RE.match(user) or user.lower() in RESERVED:
            messagebox.showwarning(APP_NAME, tr("아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요."), parent=self)
            return
        self.result = (user, path)
        self.destroy()


class LoginDialog(Dlg):
    def __init__(self, app, last_user, remember):
        super().__init__(app, trf('{0} - 로그인', APP_NAME))
        self.app = app
        self.remember = remember
        tk.Label(self, text=tr("아이디와 비밀번호를 입력해 주세요."), bg=BG, anchor="w"
                 ).pack(fill="x", padx=16, pady=(14, 6))
        box = tk.Frame(self, bg=BG, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
        box.pack(fill="x", padx=16, pady=4)
        if app.icon_img:
            tk.Label(box, image=app.icon_img, bg=BG).grid(row=0, column=0, rowspan=2, padx=12, pady=10)
        tk.Label(box, text=tr("아이디"), bg=BG).grid(row=0, column=1, sticky="e", padx=(6, 8), pady=(12, 4))
        self.id_cb = ttk.Combobox(box, values=list_users(), width=18)
        self.id_cb.grid(row=0, column=2, padx=(0, 12), pady=(12, 4))
        tk.Label(box, text=tr("비밀번호"), bg=BG).grid(row=1, column=1, sticky="e", padx=(6, 8), pady=(4, 12))
        self.pw = tk.Entry(box, show="*", width=21)
        self.pw.grid(row=1, column=2, padx=(0, 12), pady=(4, 12))
        self.rem = tk.BooleanVar(value=remember)
        tk.Checkbutton(self, text=tr("아이디 기억(A)"), variable=self.rem, bg=BG, activebackground=BG,
                       anchor="w").pack(fill="x", padx=16, pady=(8, 0))
        tk.Label(self, bg="white", relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER, justify="left", anchor="w", padx=10, pady=10,
                 text=tr("입력하신 정보는 암호화되어 이 컴퓨터에만\n저장되며 인터넷으로 전송되지 않습니다.\n처음이시면 [새 사용자]를 눌러 등록하세요.")
                 ).pack(fill="x", padx=16, pady=8)
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=(0, 6))
        mkbtn(bf, tr("확인(O)"), self.ok, 9).pack(side="left", padx=4)
        mkbtn(bf, tr("취소(C)"), self.destroy, 9).pack(side="left", padx=4)
        mkbtn(bf, tr("새 사용자(N)"), self.new_user, 11).pack(side="left", padx=4)
        tk.Frame(self, bg=BG, height=8).pack()
        if last_user:
            self.id_cb.set(last_user)
        self.bind("<Return>", lambda e: self.ok())
        self.bind("<Alt-o>", lambda e: self.ok())
        self.bind("<Alt-c>", lambda e: self.destroy())
        self.bind("<Alt-n>", lambda e: self.new_user())
        try:
            self.attributes("-topmost", True)
        except tk.TclError:
            pass
        (self.pw if last_user else self.id_cb).focus_set()
        if not list_users():
            self.after(250, self.new_user)

    def ok(self):
        self.remember = self.rem.get()
        self.result = (self.id_cb.get().strip(), self.pw.get())
        self.destroy()

    def new_user(self):
        r = NewUserDialog(self).run()
        if not r:
            return
        uid, pw = r
        try:
            Vault(uid).create(pw)
        except Exception as e:
            messagebox.showerror(APP_NAME, trf('사용자를 만들 수 없습니다.\n{0}', e), parent=self)
            return
        self.id_cb["values"] = list_users()
        self.id_cb.set(uid)
        self.pw.delete(0, "end")
        self.pw.focus_set()
        messagebox.showinfo(APP_NAME, tr("등록되었습니다. 비밀번호를 입력하고 로그인하세요."), parent=self)


class SiteDialog(Dlg):
    def __init__(self, parent, vault, site=None, url="", folder=None, on_group_added=None):
        super().__init__(parent, trf('{0} - 사이트 {1}', APP_NAME, tr('수정') if site else tr('추가')))
        self.vault, self.site, self.on_group_added = vault, site, on_group_added
        s = site or {}
        self.url_v = tk.StringVar(value=s.get("url", url))
        self.kw_v = tk.StringVar(value=s.get("keyword", ""))
        self.manual_v = tk.BooleanVar(value=s.get("manual", False))
        self.desc_v = tk.StringVar(value=s.get("desc", ""))
        self.user_v = tk.StringVar(value=s.get("user", ""))
        self.pw_v = tk.StringVar(value=s.get("pw", ""))
        self.choices = vault.folder_choices()
        self.folder_v = tk.StringVar(value=vault.folder_path(s.get("folder", folder)))

        tk.Label(self, bg=BG, anchor="w", text=tr('다음 주소에 대한 사이트 정보를 수정합니다.' if site else '다음 주소에 대한 사이트 정보를 추가합니다.')
                 ).pack(fill="x", padx=16, pady=(14, 4))
        tk.Entry(self, textvariable=self.url_v, width=46).pack(fill="x", padx=16, pady=(0, 6))
        g = tk.Frame(self, bg=BG, relief="flat", bd=0, highlightthickness=1, highlightbackground=BORDER)
        g.pack(fill="x", padx=16, pady=4)
        g.columnconfigure(1, weight=1)

        def lab(r, t):
            tk.Label(g, text=t, bg=BG).grid(row=r, column=0, sticky="w", padx=(10, 8), pady=5)
        lab(0, tr("주소 키워드"))
        self.kw_cb = ttk.Combobox(g, textvariable=self.kw_v, width=26)
        self.kw_cb.grid(row=0, column=1, sticky="ew", pady=5)
        Btn(g, text="?", width=2, command=self.help).grid(row=0, column=2, padx=8)
        tk.Checkbutton(g, text=tr("이 주소 키워드를 수동 사이트로 설정(M)"), variable=self.manual_v, bg=BG,
                       activebackground=BG, command=self.on_manual).grid(row=1, column=0, columnspan=3,
                                                                          sticky="w", padx=6)
        lab(2, tr("사이트 설명"))
        tk.Entry(g, textvariable=self.desc_v).grid(row=2, column=1, columnspan=2, sticky="ew", padx=(0, 8), pady=5)
        lab(3, tr("아이디"))
        tk.Entry(g, textvariable=self.user_v).grid(row=3, column=1, columnspan=2, sticky="ew", padx=(0, 8), pady=5)
        lab(4, tr("비밀번호"))
        self.pw_e = tk.Entry(g, textvariable=self.pw_v, show="*")
        self.pw_e.grid(row=4, column=1, sticky="ew", pady=5)
        pf = tk.Frame(g, bg=BG)
        pf.grid(row=4, column=2, padx=(4, 8))
        self.show_v = tk.BooleanVar(value=False)
        tk.Checkbutton(pf, text=tr("보기"), variable=self.show_v, bg=BG, activebackground=BG,
                       command=lambda: self.pw_e.config(show="" if self.show_v.get() else "*")).pack(side="left", padx=(0, 6))
        Btn(pf, text=tr("생성"), command=self.generate).pack(side="left")
        add_strength_meter(g, self.pw_v).grid(row=5, column=1, columnspan=2, sticky="ew", padx=(0, 8), pady=(0, 4))
        lab(6, tr("그룹명"))
        self.folder_cb = ttk.Combobox(g, textvariable=self.folder_v, state="readonly", width=22,
                                      values=[l for l, _ in self.choices])
        self.folder_cb.grid(row=6, column=1, sticky="ew", pady=(5, 10))
        Btn(g, text=tr("새 그룹"), command=self.new_group).grid(row=6, column=2, padx=(4, 8), pady=(5, 10))
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=10)
        mkbtn(bf, tr("확인"), self.ok, 14).pack(side="left", padx=8)
        mkbtn(bf, tr("취소"), self.destroy, 14).pack(side="left", padx=8)
        self.url_v.trace_add("write", lambda *a: self.on_url())
        self.on_manual()
        self.bind("<Return>", lambda e: self.ok())

    def on_url(self):
        if self.manual_v.get():
            return
        c = keyword_candidates(self.url_v.get())
        self.kw_cb["values"] = c
        if self.kw_v.get() not in c:
            self.kw_v.set(c[0] if c else "")

    def on_manual(self):
        self.kw_cb.config(state="normal" if self.manual_v.get() else "readonly")
        if not self.manual_v.get():
            self.on_url()

    def generate(self):
        self.pw_v.set(gen_password())
        self.show_v.set(True)
        self.pw_e.config(show="")

    def new_group(self):
        """지금 선택된 그룹 안에 새 그룹을 만들고 바로 선택한다."""
        name = simpledialog.askstring(APP_NAME, trf("'{0}' 안에 만들 새 그룹 이름:", self.folder_v.get()), parent=self)
        if name is None:
            return
        parent_id = dict(self.choices).get(self.folder_v.get())
        fid = self.vault.add_folder(name, parent_id)
        if not fid:
            messagebox.showwarning(APP_NAME, tr("그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)"), parent=self)
            return
        try:
            self.vault.save()
        except OSError:
            pass
        self.choices = self.vault.folder_choices()
        self.folder_cb["values"] = [l for l, _ in self.choices]
        self.folder_v.set(self.vault.folder_path(fid))
        if self.on_group_added:
            self.on_group_added()

    def help(self):
        messagebox.showinfo(APP_NAME,
                            tr("주소 키워드는 저장된 로그인 정보를 찾는 기준입니다.\n"
                            "주소창의 주소에 이 키워드가 들어 있으면 이 사이트 정보가 표시됩니다.\n\n"
                            "예) NAVER.COM → mail.naver.com, cafe.naver.com 모두 적용\n"
                            "    MAIL.NAVER.COM → 메일 주소에만 적용\n\n"
                            "'수동 사이트로 설정'을 체크하면 키워드를 직접 입력할 수 있습니다."), parent=self)

    def ok(self):
        url, kw = self.url_v.get().strip(), self.kw_v.get().strip()
        if not url:
            messagebox.showwarning(APP_NAME, tr("주소를 입력하세요."), parent=self)
            return
        if not kw:
            messagebox.showwarning(APP_NAME, tr("주소 키워드가 비어 있습니다.\n주소를 확인하거나 수동으로 입력하세요."), parent=self)
            return
        desc = self.desc_v.get().strip() or kw.split(".")[0].capitalize()
        fid = dict(self.choices).get(self.folder_v.get())
        if self.folder_v.get() not in dict(self.choices):
            fid = None
        self.result = {"id": (self.site or {}).get("id") or uuid.uuid4().hex, "url": url, "keyword": kw,
                       "manual": self.manual_v.get(), "desc": desc, "user": self.user_v.get().strip(),
                       "pw": self.pw_v.get(), "folder": fid,
                       "last_use": (self.site or {}).get("last_use") or time.strftime("%Y-%m-%d")}
        self.destroy()


class GroupPickDialog(Dlg):
    """그룹을 고르는 작은 창. result = {"fid": 그룹id 또는 None(최상위)}"""

    def __init__(self, parent, vault, title, message, exclude=(), current=None):
        super().__init__(parent, title)
        ex = set(exclude)
        self.choices = [(l, i) for l, i in vault.folder_choices() if i not in ex]
        tk.Label(self, text=message, bg=BG, justify="left", anchor="w").pack(fill="x", padx=16, pady=(14, 6))
        first = next((l for l, i in self.choices if i == current), self.choices[0][0] if self.choices else "")
        self.v = tk.StringVar(value=first)
        ttk.Combobox(self, textvariable=self.v, state="readonly", width=38,
                     values=[l for l, _ in self.choices]).pack(padx=16, pady=4)
        bf = tk.Frame(self, bg=BG)
        bf.pack(pady=12)
        mkbtn(bf, tr("확인"), self.ok, 10).pack(side="left", padx=6)
        mkbtn(bf, tr("취소"), self.destroy, 10).pack(side="left", padx=6)
        self.bind("<Return>", lambda e: self.ok())

    def ok(self):
        d = dict(self.choices)
        if self.v.get() in d:
            self.result = {"fid": d[self.v.get()]}
        self.destroy()


class GroupEditDialog(Dlg):
    """그룹 수정 팝업: 이름·위치 바꾸기, 삭제. result = {"name", "parent"} 또는 {"delete": True}"""

    def __init__(self, parent, vault, folder):
        super().__init__(parent, trf('{0} - 그룹 수정', APP_NAME))
        self.f = folder
        ex = {folder["id"]} | vault.descendants(folder["id"])
        self.choices = [(l, i) for l, i in vault.folder_choices() if i not in ex]
        cur = next((l for l, i in self.choices if i == folder.get("parent")), self.choices[0][0])
        self.name_v, self.pos_v = tk.StringVar(value=folder["name"]), tk.StringVar(value=cur)
        g = tk.Frame(self, bg=BG)
        g.pack(fill="x", padx=16, pady=(16, 6))
        g.columnconfigure(1, weight=1)
        tk.Label(g, text=tr("그룹 이름"), bg=BG).grid(row=0, column=0, sticky="w", pady=6)
        e = tk.Entry(g, textvariable=self.name_v, width=34)
        e.grid(row=0, column=1, sticky="ew", padx=(12, 0))
        tk.Label(g, text=tr("위치"), bg=BG).grid(row=1, column=0, sticky="w", pady=6)
        ttk.Combobox(g, textvariable=self.pos_v, state="readonly", width=32,
                     values=[l for l, _ in self.choices]).grid(row=1, column=1, sticky="ew", padx=(12, 0))
        tk.Label(self, bg=BG, fg=MUTED, justify="left", anchor="w", wraplength=380, font=fnt(9), text=(
            tr("'위치'는 이 그룹을 어느 그룹 안에 둘지입니다. 그룹을 삭제해도 안에 있던 사이트는 지워지지 않고 "
            "상위 그룹으로 옮겨집니다."))).pack(fill="x", padx=16, pady=(0, 4))
        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=16, pady=14)
        Btn(bf, tr("그룹 삭제"), self.delete, danger=True, width=9).pack(side="left")
        mkbtn(bf, tr("취소"), self.destroy, 9).pack(side="right")
        mkbtn(bf, tr("확인"), self.ok, 9).pack(side="right", padx=6)
        e.focus_set()
        e.select_range(0, "end")
        self.bind("<Return>", lambda ev: self.ok())

    def ok(self):
        name = self.name_v.get().strip()
        if not name:
            messagebox.showwarning(APP_NAME, tr("그룹 이름을 입력하세요."), parent=self)
            return
        self.result = {"name": name, "parent": dict(self.choices).get(self.pos_v.get())}
        self.destroy()

    def delete(self):
        self.result = {"delete": True}
        self.destroy()


class AccentDialog(Dlg):
    """강조 색상을 고르는 작은 팝업. result = 선택한 16진 색상 문자열(취소 시 None)"""

    def __init__(self, parent):
        super().__init__(parent, trf('{0} - 강조 색상', APP_NAME))
        tk.Label(self, text=tr("버튼·테두리 등에 쓸 강조 색을 골라 주세요."), bg=BG, fg=MUTED,
                 font=fnt(9)).pack(padx=16, pady=(16, 8), anchor="w")
        grid = tk.Frame(self, bg=BG)
        grid.pack(padx=16)
        cols = 4
        for i, (name, hexcolor) in enumerate(ACCENT_PRESETS):
            cell = tk.Frame(grid, bg=BG)
            cell.grid(row=i // cols, column=i % cols, padx=6, pady=6)
            cv = tk.Canvas(cell, width=40, height=40, bg=BG, highlightthickness=0, cursor="hand2")
            ring = TEXT if hexcolor.upper() == ACCENT.upper() else BG
            cv.create_oval(3, 3, 37, 37, fill=hexcolor, outline=ring, width=3)
            cv.bind("<Button-1>", lambda e, c=hexcolor: self.pick(c))
            cv.pack()
            tk.Label(cell, text=tr(name), bg=BG, fg=MUTED, font=fnt(8)).pack()
        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=16, pady=(8, 14))
        Btn(bf, tr("직접 선택..."), self.custom).pack(side="left")
        mkbtn(bf, tr("취소"), self.destroy, 9).pack(side="right")

    def pick(self, hexcolor):
        self.result = hexcolor
        self.destroy()

    def custom(self):
        c = colorchooser.askcolor(color=ACCENT, parent=self, title=tr("강조 색상 직접 선택"))
        if c and c[1]:
            self.result = c[1]
            self.destroy()


class ManagerWindow(tk.Toplevel):
    def __init__(self, app):
        super().__init__(app)
        self.app, self.v = app, app.vault
        self.title(trf('{0} - 목록관리', APP_NAME))
        self.configure(bg=BG)
        place_window(self, app.settings, "manager", 780, 480, 660, 380)
        auto_remember(self, app.settings, "manager")
        self.transient(app)
        fade_in(self)
        top = tk.Frame(self, bg=BG)
        top.pack(fill="x", padx=12, pady=(12, 6))
        tk.Label(top, text=tr("검색"), bg=BG, fg=MUTED).pack(side="left")
        self.q = tk.StringVar()
        self.q.trace_add("write", lambda *a: self.refresh_list())
        tk.Entry(top, textvariable=self.q, width=26).pack(side="left", padx=8)
        Btn(top, tr("그룹 추가"), self.add_folder).pack(side="right")
        Btn(top, tr("사이트 추가"), self.add_site, primary=True).pack(side="right", padx=(0, 6))

        bot = tk.Frame(self, bg=BG)
        bot.pack(side="bottom", fill="x", padx=12, pady=(6, 12))
        self.count_v = tk.StringVar()
        tk.Label(bot, textvariable=self.count_v, bg=BG, fg=MUTED, font=fnt(9)).pack(side="left")
        mkbtn(bot, tr("닫기"), self.destroy, 8).pack(side="right")
        tk.Label(bot, bg=BG, fg=MUTED, font=fnt(9), text=tr("여러 개 선택(Ctrl/Shift) 후 오른쪽 클릭: 이동 · 묶기 · 삭제   ")
                 ).pack(side="right")

        pw = ttk.PanedWindow(self, orient="horizontal")
        pw.pack(fill="both", expand=True, padx=12)
        sc = ui_scale(self)
        lf = tk.Frame(pw, bg="#FFFFFF", highlightthickness=1, highlightbackground=BORDER)
        self.ft = ttk.Treeview(lf, columns=("edit",), displaycolumns=("edit",), show="tree", selectmode="browse")
        self.ft.column("#0", width=int(140 * sc), minwidth=int(90 * sc), stretch=True)
        self.ft.column("edit", width=int(66 * sc), anchor="center", stretch=False)
        self.ft.pack(fill="both", expand=True)
        self.ft.bind("<<TreeviewSelect>>", lambda e: self.refresh_list())
        self.ft.bind("<Button-1>", self.on_ft_click, add="+")
        self.ft.bind("<Button-3>", self.ft_menu)
        self.ft.bind("<Motion>", lambda e: self.ft.config(cursor=self._hand(self.ft, e, {"#1"}, "f:")))
        pw.add(lf, weight=1)
        rf = tk.Frame(pw, bg="#FFFFFF", highlightthickness=1, highlightbackground=BORDER)
        cols = ("desc", "keyword", "user", "folder", "edit", "del")
        self.st = ttk.Treeview(rf, columns=cols, show="headings", selectmode="extended")
        for c, t, w in [("desc", tr("사이트 설명"), 120), ("keyword", tr("주소 키워드"), 100),
                        ("user", tr("아이디"), 90), ("folder", tr("그룹"), 100)]:
            self.st.heading(c, text=t, anchor="w")
            self.st.column(c, width=int(w * sc), minwidth=int(60 * sc), anchor="w")
        for c in ("edit", "del"):
            self.st.heading(c, text="")
            self.st.column(c, width=int(66 * sc), anchor="center", stretch=False)
        sb = ttk.Scrollbar(rf, orient="vertical", command=self.st.yview)
        self.st.configure(yscrollcommand=autoscroll(sb, self.st))
        sb.pack(side="right", fill="y")
        self.st.pack(fill="both", expand=True)
        self.ft.tag_configure("stale", foreground="#C98A2E")
        self.st.tag_configure("stale", foreground="#C98A2E")
        self.st.tag_configure("odd", background="#FAF8F0")   # 줄무늬(얼룩말 패턴)로 한 줄씩 번갈아 살짝 음영
        self.st.bind("<Double-1>", self.on_st_double)
        self.st.bind("<Button-1>", self.on_st_click, add="+")
        self.st.bind("<Motion>", lambda e: self.st.config(cursor=self._hand(self.st, e, {"#5", "#6"}, "")))
        self.st.bind("<Button-3>", self.list_menu)
        self.st.bind("<Control-a>", lambda e: (self.st.selection_set(self.st.get_children()), "break")[1])
        pw.add(rf, weight=4)
        self.refresh()

    # ====================
    # 화면 갱신
    # ====================
    def sel_folder(self):
        s = self.ft.selection()
        if s and s[0].startswith("f:"):
            return s[0][2:]
        return None

    def refresh(self):
        self.v = self.app.vault
        keep = self.ft.selection()
        self.ft.delete(*self.ft.get_children())
        self.ft.insert("", "end", iid="top", text=trf('최상위 ({0})', self.v.count_sites(None)), values=("",), image=self.app.ic_folder, open=True)
        self.ft.insert("", "end", iid="stale", text=trf('오래 안 쓴 사이트 ({0})', len(self.v.stale_sites())),
                       values=("",), image=self.app.ic_warn, tags=("stale",))

        def walk(parent_iid, pid):
            kids = [f for f in self.v.data["folders"] if f.get("parent") == pid]
            for f in sorted(kids, key=lambda f: f["name"].lower()):
                iid = "f:" + f["id"]
                self.ft.insert(parent_iid, "end", iid=iid,
                               text=f"{f['name']} ({self.v.count_sites(f['id'])})", values=(tr("✎ 수정"),),
                               image=self.app.ic_folder, open=True)
                walk(iid, f["id"])
        walk("top", None)
        self.ft.selection_set(keep[0] if keep and self.ft.exists(keep[0]) else "top")
        self.refresh_list()

    def refresh_list(self):
        self.st.delete(*self.st.get_children())
        q = self.q.get().strip().lower()
        sel = self.ft.selection()
        stale_view = bool(sel and sel[0] == "stale")
        fid = self.sel_folder()
        srcs = sorted(self.v.data["sites"], key=lambda s: s.get("last_use", "")) if (stale_view and not q) \
            else sorted(self.v.data["sites"], key=lambda s: s["desc"].lower())
        row = 0
        for s in srcs:
            if q:
                if q not in (s["desc"] + " " + s["url"] + " " + s["keyword"] + " " + s.get("user", "")).lower():
                    continue
            elif stale_view:
                if not self.v.is_stale(s):
                    continue
            elif s.get("folder") != fid:
                continue
            tags = []
            if row % 2:
                tags.append("odd")
            if self.v.is_stale(s):
                tags.append("stale")
            self.st.insert("", "end", iid=s["id"], values=(s["desc"], s["keyword"], s.get("user", ""),
                                                            self.v.folder_path(s.get("folder")), tr("✎ 수정"), tr("✕ 삭제")),
                           tags=tuple(tags))
            row += 1
        n = len(self.st.get_children())
        suffix = tr(" (검색 결과)") if q else (tr(" (오래 안 쓴 사이트)") if stale_view else "")
        self.count_v.set(trf('사이트 {0}개', n) + suffix)

    def _hand(self, tree, ev, cols, prefix):
        if tree.identify_region(ev.x, ev.y) == "cell" and tree.identify_column(ev.x) in cols:
            row = tree.identify_row(ev.y)
            if row and row.startswith(prefix):
                return "hand2"
        return ""

    def on_st_click(self, ev):
        if self.st.identify_region(ev.x, ev.y) != "cell":
            return
        row, col = self.st.identify_row(ev.y), self.st.identify_column(ev.x)
        if row and col in ("#5", "#6"):
            self.st.selection_set(row)
            self.after(10, self.edit_site if col == "#5" else self.del_site)
            return "break"

    def on_st_double(self, ev):
        if self.st.identify_region(ev.x, ev.y) == "cell" and self.st.identify_column(ev.x) not in ("#5", "#6"):
            self.edit_site()

    def on_ft_click(self, ev):
        if self.ft.identify_region(ev.x, ev.y) != "cell" or self.ft.identify_column(ev.x) != "#1":
            return
        row = self.ft.identify_row(ev.y)
        if row and row.startswith("f:"):
            self.ft.selection_set(row)
            self.after(10, lambda: self.edit_group(row[2:]))
            return "break"

    def ft_menu(self, ev):
        iid = self.ft.identify_row(ev.y)
        if not iid or iid == "stale":
            return
        self.ft.selection_set(iid)
        m = tk.Menu(self, tearoff=0)
        m.add_command(label=tr("사이트 추가"), command=self.add_site)
        m.add_command(label=tr("하위 그룹 추가"), command=self.add_folder)
        if iid.startswith("f:"):
            m.add_separator()
            m.add_command(label=tr("수정 (이름·위치)"), command=lambda: self.edit_group(iid[2:]))
            m.add_command(label=tr("삭제"), command=self.del_folder)
        m.tk_popup(ev.x_root, ev.y_root)

    def edit_group(self, fid):
        f = self.v.folder(fid)
        if not f:
            return
        r = GroupEditDialog(self, self.v, f).run()
        if not r:
            return
        if r.get("delete"):
            self.del_folder(fid)
            return
        if r["name"] != f["name"] and not self.v.rename_folder(fid, r["name"]):
            messagebox.showwarning(APP_NAME, tr("사용할 수 없는 그룹 이름입니다.\n(같은 위치에 같은 이름의 그룹이 있거나, / \\ 문자가 들어 있습니다)"), parent=self)
            return
        if r["parent"] != f.get("parent") and not self.v.move_folder(fid, r["parent"]):
            messagebox.showwarning(APP_NAME, tr("옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)"), parent=self)
            self.changed()
            return
        self.changed()

    def cur_sites(self):
        return [s for s in (self.v.site(i) for i in self.st.selection()) if s]

    def cur_site(self):
        sel = self.cur_sites()
        if not sel:
            messagebox.showinfo(APP_NAME, tr("사이트를 먼저 선택하세요."), parent=self)
            return None
        return sel[0]

    def changed(self):
        self.app.on_data_changed()

    def list_menu(self, ev):
        iid = self.st.identify_row(ev.y)
        if not iid:
            return
        if iid not in self.st.selection():
            self.st.selection_set(iid)
        m = tk.Menu(self, tearoff=0)
        m.add_command(label=tr("수정"), command=self.edit_site)
        m.add_command(label=tr("삭제"), command=self.del_site)
        m.add_command(label=tr("비밀번호 복사"), command=self.copy_pw)
        m.add_separator()
        m.add_command(label=tr("그룹으로 이동..."), command=self.move_sites)
        m.add_command(label=tr("새 그룹으로 묶기..."), command=self.bundle_sites)
        m.tk_popup(ev.x_root, ev.y_root)

    # ====================
    # 사이트
    # ====================
    def add_site(self):
        r = SiteDialog(self, self.v, folder=self.sel_folder(), on_group_added=self.changed).run()
        if r:
            self.v.data["sites"].append(r)
            self.changed()

    def edit_site(self):
        s = self.cur_site()
        if not s:
            return
        r = SiteDialog(self, self.v, site=s, on_group_added=self.changed).run()
        if r:
            s.update(r)
            self.changed()

    def del_site(self):
        sel = self.cur_sites()
        if not sel:
            messagebox.showinfo(APP_NAME, tr("사이트를 먼저 선택하세요."), parent=self)
            return
        what = trf("'{0}' 사이트 정보를", sel[0]['desc']) if len(sel) == 1 else trf('선택한 사이트 {0}개를', len(sel))
        if messagebox.askyesno(APP_NAME, trf('{0} 삭제할까요?', what), parent=self):
            for s in sel:
                self.v.data["sites"].remove(s)
                if self.app.current is s:
                    self.app.current = None
            self.changed()

    def copy_pw(self):
        s = self.cur_site()
        if s:
            self.app.copy_text(s.get("pw", ""), tr("비밀번호"), clear=True)

    def move_sites(self):
        sel = self.cur_sites()
        if not sel:
            messagebox.showinfo(APP_NAME, tr("옮길 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)"), parent=self)
            return
        r = GroupPickDialog(self, self.v, trf('{0} - 그룹으로 이동', APP_NAME),
                            trf('선택한 사이트 {0}개를 옮길 그룹을 고르세요.', len(sel)), current=self.sel_folder()).run()
        if r is None:
            return
        n = self.v.move_sites([s["id"] for s in sel], r["fid"])
        self.changed()
        self.app.say(trf("{0}개 사이트를 '{1}' 로 옮겼습니다.", n, self.v.folder_path(r['fid'])))

    def bundle_sites(self):
        sel = self.cur_sites()
        if not sel:
            messagebox.showinfo(APP_NAME, tr("묶을 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)"), parent=self)
            return
        parent_id = self.sel_folder()
        name = simpledialog.askstring(APP_NAME, trf("선택한 사이트 {0}개를 묶을 새 그룹 이름:\n('{1}' 안에 만들어집니다)", len(sel), self.v.folder_path(parent_id)), parent=self)
        if name is None:
            return
        fid = self.v.add_folder(name, parent_id)
        if not fid:
            messagebox.showwarning(APP_NAME, tr("그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)"), parent=self)
            return
        self.v.move_sites([s["id"] for s in sel], fid)
        self.changed()
        self.app.say(trf("'{0}' 그룹으로 {1}개 사이트를 묶었습니다.", name.strip(), len(sel)))

    # ====================
    # 그룹
    # ====================
    def add_folder(self):
        name = simpledialog.askstring(APP_NAME, tr("새 그룹 이름:"), parent=self)
        if name is None:
            return
        if not self.v.add_folder(name, self.sel_folder()):
            messagebox.showwarning(APP_NAME, tr("그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)"), parent=self)
            return
        self.changed()

    def rename_folder(self):
        fid = self.sel_folder()
        f = self.v.folder(fid) if fid else None
        if not f:
            messagebox.showinfo(APP_NAME, tr("이름을 바꿀 그룹을 선택하세요."), parent=self)
            return
        name = simpledialog.askstring(APP_NAME, tr("그룹 이름:"), initialvalue=f["name"], parent=self)
        if name is None:
            return
        if not self.v.rename_folder(fid, name):
            messagebox.showwarning(APP_NAME, tr("사용할 수 없는 그룹 이름입니다."), parent=self)
            return
        self.changed()

    def move_group(self):
        fid = self.sel_folder()
        f = self.v.folder(fid) if fid else None
        if not f:
            messagebox.showinfo(APP_NAME, tr("옮길 그룹을 선택하세요."), parent=self)
            return
        exclude = {fid, f.get("parent")} | self.v.descendants(fid)
        r = GroupPickDialog(self, self.v, trf('{0} - 그룹 이동', APP_NAME),
                            trf("그룹 '{0}' 을(를) 넣을 그룹을 고르세요.", f['name']), exclude=exclude).run()
        if r is None:
            return
        if not self.v.move_folder(fid, r["fid"]):
            messagebox.showwarning(APP_NAME, tr("옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)"), parent=self)
            return
        self.changed()

    def del_folder(self, fid=None):
        fid = fid or self.sel_folder()
        if not fid:
            messagebox.showinfo(APP_NAME, tr("삭제할 그룹을 선택하세요."), parent=self)
            return
        if messagebox.askyesno(APP_NAME, tr("그룹과 하위 그룹을 삭제합니다.\n안에 있던 사이트 정보는 상위 그룹으로 옮겨집니다.\n(사이트는 지워지지 않습니다) 계속할까요?"), parent=self):
            self.v.delete_folder(fid)
            self.changed()


# ====================
# 메인 창
# ====================
def pick_language_first(root):
    """처음 실행할 때 보이는 언어 선택 창. 고른 언어 코드를 돌려준다. (환경설정 메뉴에서 언제든 바꿀 수 있음)"""
    top = tk.Toplevel(root)
    top.title("Language / 언어 / 言語 / 语言")
    top.resizable(False, False)
    res = {"c": detect_system_lang()}
    tk.Label(top, text="Select your language\n언어를 선택하세요 · 言語を選択 · 请选择语言",
             pady=12, padx=24).pack()
    for code, name in LANGS:
        def go(c=code):
            res["c"] = c
            top.destroy()
        tk.Button(top, text=name, width=22, pady=4, command=go).pack(padx=24, pady=3)
    tk.Label(top, text="(Settings → Language 에서 나중에 바꿀 수 있습니다)", fg="#777", pady=10).pack()
    top.update_idletasks()
    w, h = top.winfo_reqwidth(), top.winfo_reqheight()
    top.geometry(f"+{(top.winfo_screenwidth() - w) // 2}+{(top.winfo_screenheight() - h) // 3}")
    top.protocol("WM_DELETE_WINDOW", top.destroy)
    top.grab_set()
    top.focus_force()
    root.wait_window(top)
    return res["c"]


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()           # 초기화가 끝나기 전까지 빈 메인 창이 보이지 않도록 먼저 숨김
        self.ready = False
        self.title(f"{APP_NAME} v{APP_VER}")
        self.settings = load_settings()
        if self.settings.get("lang") in dict(LANGS):
            set_lang(self.settings["lang"])
        elif INTERACTIVE_LANG:                       # 처음 실행: 언어 선택
            code = pick_language_first(self)
            set_lang(code)
            self.settings["lang"] = code
            save_settings(self.settings)
        if self.settings.get("accent"):
            try:
                set_accent(self.settings["accent"])
            except Exception:
                pass
        set_font_prefs(self.settings.get("font_scale"), self.settings.get("font_bold"))
        load_bundled_fonts()
        try:
            self.idle_sec = int(self.settings.get("idle_sec", IDLE_LOCK_SEC))
        except (TypeError, ValueError):
            self.idle_sec = IDLE_LOCK_SEC
        if self.idle_sec not in dict(IDLE_OPTIONS).values():
            self.idle_sec = IDLE_LOCK_SEC
        self.icons = Icons(self)
        apply_theme(self, self.icons)
        try:
            self.icon_img = tk.PhotoImage(data=ICON_B64)
            self.iconphoto(True, self.icon_img)
        except tk.TclError:
            self.icon_img = None
        self.vault = None
        self.current = None
        self.matches = []
        self.mgr = None
        self._lock = False
        self._msg_job = None
        self.pw_visible = False
        self.help_win = None
        self.watcher = None
        self._dest_job = None
        self.dest_q = queue.Queue()
        self.upd_q = queue.Queue()
        self.last_active = time.time()
        self.withdraw()
        if not self.login():
            self.destroy()
            return
        self.build_ui()
        self.after_login()
        self.start_watcher()
        self.after(1000, self.poll_dest)
        self.after(1500, self.poll_update)
        self.deiconify()
        fade_in(self)
        self.bind_all("<Any-KeyPress>", self.touch)
        self.bind_all("<Motion>", self.touch)
        self.after(10000, self.idle_check)
        self.ready = True

    # ====================
    # 로그인
    # ====================
    def login(self):
        fails = 0
        while True:
            dlg = LoginDialog(self, self.settings.get("last_user", ""), self.settings.get("remember", True))
            r = dlg.run()
            if r is None:
                return False
            user, pw = r
            self.settings["remember"] = dlg.remember
            self.settings["last_user"] = user if dlg.remember else ""
            save_settings(self.settings)
            if user and is_shared_user(user) and not shared_reachable(shared_conf()[1]):
                messagebox.showwarning(APP_NAME, tr("공용 계정의 저장소(공유 드라이브)에 연결할 수 없습니다.\n"
                                                  "네트워크·드라이브 연결을 확인한 뒤 다시 시도하세요."))
                continue
            if not user or not Vault.exists(user):
                messagebox.showwarning(APP_NAME, tr("등록되지 않은 아이디입니다.\n[새 사용자]로 먼저 등록하세요."))
                continue
            v = Vault(user)
            try:
                ok = v.unlock(pw)
            except Exception as e:
                messagebox.showerror(APP_NAME, trf('보관함을 열 수 없습니다.\n{0}', e))
                continue
            if ok:
                self.vault = v
                return True
            fails += 1
            if fails >= 5:
                messagebox.showerror(APP_NAME, tr("비밀번호를 5회 틀려 종료합니다."))
                return False
            messagebox.showwarning(APP_NAME, tr("비밀번호가 틀렸습니다."))

    def reset_ui_state(self):
        self.current = None
        self.matches = []
        self._lock = True
        self.addr.set("")
        self._lock = False
        self._clear_match_rows()
        self.set_current(None)
        self.refresh_tree()
        self.say(self.login_msg(), permanent=True)
        self.attributes("-topmost", bool(self.settings.get("topmost", False)))
        self.topmost_v.set(bool(self.settings.get("topmost", False)))
        self.enter_v.set(bool(self.settings.get("enter_after", False)))
        self.link_v.set(bool(self.settings.get("browser_link", True)))
        self.bold_v.set(FONT_BOLD)
        self.fontscale_v.set(FONT_SCALE)
        self.idlesec_v.set(self.idle_sec)

    def _rebuild_ui(self):
        """언어·강조색·글자 설정이 바뀐 뒤 화면을 통째로 다시 그린다."""
        if self._dest_job:
            self.after_cancel(self._dest_job)
            self._dest_job = None
        for w in list(self.winfo_children()):
            w.destroy()
        self.mgr = None
        self.help_win = None
        apply_theme(self, self.icons)
        self.build_ui()
        self.reset_ui_state()

    def change_language(self, code):
        """언어를 바꾸고 화면을 바로 다시 그린다."""
        if code == LANG or code not in dict(LANGS):
            self.lang_v.set(LANG)
            return
        set_lang(code)
        self.settings["lang"] = code
        save_settings(self.settings)
        self._rebuild_ui()
        self.say(trf('언어를 바꿨습니다: {0}', dict(LANGS)[code]))

    def pick_accent(self):
        c = AccentDialog(self).run()
        if c:
            self.change_accent(c)

    def change_accent(self, hexcolor):
        """강조 색을 바꾸고 화면을 바로 다시 그린다."""
        if hexcolor.upper() == ACCENT.upper():
            return
        set_accent(hexcolor)
        self.settings["accent"] = hexcolor
        save_settings(self.settings)
        self.icons.cache.clear()
        self._rebuild_ui()
        self.say(tr("강조 색상을 바꿨습니다."))

    def change_font_scale(self, v):
        """글자 크기 배율을 바꾸고 화면을 바로 다시 그린다."""
        if abs(v - FONT_SCALE) < 1e-6:
            return
        set_font_prefs(scale=v)
        self.settings["font_scale"] = v
        save_settings(self.settings)
        self._rebuild_ui()
        self.say(tr("글자 크기를 바꿨습니다."))

    def toggle_font_bold(self):
        """글자를 굵게/보통으로 바꾸고 화면을 바로 다시 그린다."""
        set_font_prefs(bold=self.bold_v.get())
        self.settings["font_bold"] = FONT_BOLD
        save_settings(self.settings)
        self._rebuild_ui()
        self.say(tr("굵게 표시 설정을 바꿨습니다."))

    def after_login(self):
        self.reset_ui_state()
        try:
            auto_backup(self.vault.user)
        except Exception:
            pass
        self.dest_sync(tr("로그인"))
        self.update_check(manual=False)

    # ====================
    # 브라우저 주소 연동
    # ====================
    FAIL_MSG = {"no-browser": "연동할 브라우저 창을 찾지 못했습니다. 브라우저를 한 번 사용한 뒤 다시 눌러 보세요.",
                "no-address": "브라우저 주소를 읽지 못했습니다. (검색어 입력 중이거나 지원하지 않는 화면)",
                "error": "브라우저 주소를 읽는 중 오류가 났습니다."}

    def start_watcher(self):
        self.watcher = None
        if sys.platform != "win32":
            return
        try:
            w = make_win_watcher()
        except Exception:
            self.say(tr("브라우저 주소 연동을 사용할 수 없습니다. (uiautomation 구성 요소 없음)"))
            return
        w.enabled = bool(self.settings.get("browser_link", True))
        w.start()
        self.watcher = w
        self.after(500, self.poll_watcher)

    def poll_watcher(self):
        w = self.watcher
        if w is None:
            return
        latest = None
        try:
            while True:
                kind, val = w.q.get_nowait()
                if kind == "url":
                    latest = val
                elif kind == "fail":
                    self.say(tr(self.FAIL_MSG.get(val, "브라우저 주소를 읽지 못했습니다.")))
                elif kind == "unavailable":
                    self.watcher = None
                    self.say(tr("브라우저 주소 연동을 사용할 수 없습니다."))
                    return
        except queue.Empty:
            pass
        if latest and latest != self.addr.get().strip():
            self.addr.set(latest)                      # → update_matches() 자동 호출
            self.say(trf('브라우저 주소: {0}', host_of(latest)))
        self.after(400, self.poll_watcher)

    def toggle_link(self):
        self.settings["browser_link"] = self.link_v.get()
        save_settings(self.settings)
        if self.watcher is not None:
            self.watcher.enabled = self.link_v.get()
        elif self.link_v.get():
            messagebox.showinfo(APP_NAME, tr("브라우저 주소 연동은 Windows에서만 사용할 수 있습니다."), parent=self)

    def fetch_browser_addr(self, event=None):
        if self.watcher is None:
            messagebox.showinfo(APP_NAME, tr("브라우저 주소 연동을 사용할 수 없습니다.\n(Windows 전용이며 uiautomation 구성 요소가 필요합니다)"), parent=self)
            return
        self.say(tr("브라우저에서 주소를 읽는 중..."))
        self.watcher.refresh()

    # ====================
    # 업데이트 확인
    # ====================
    def update_check(self, manual=True):
        c = update_conf(self.settings)
        if not manual:
            today = time.strftime("%Y-%m-%d")
            if not c["auto"] or not c["repo"] or self.settings.get("update_last") == today:
                return
        elif not c["repo"]:
            messagebox.showinfo(APP_NAME, tr("업데이트를 확인할 GitHub 저장소가 설정되어 있지 않습니다.\n"
                                          "mypass.py 맨 위의 UPDATE_REPO 에 '계정/저장소'를 넣고 다시 만드세요."), parent=self)
            return
        if manual:
            self.say(tr("업데이트를 확인하는 중..."))

        def work():
            self.upd_q.put((manual,) + check_update(c["repo"], c["token"]))
        threading.Thread(target=work, daemon=True).start()

    def poll_update(self):
        try:
            while True:
                manual, st, info = self.upd_q.get_nowait()
                if self.vault is None or not self.winfo_viewable():      # 로그인 창 등이 떠 있으면 나중에 알림
                    self.upd_q.put((manual, st, info))
                    break
                if st != "error":
                    self.settings["update_last"] = time.strftime("%Y-%m-%d")
                    save_settings(self.settings)
                if st == "new":
                    self.say(trf('새 버전 {0} 이(가) 있습니다. (업데이트 메뉴 → 업데이트 확인)', info['tag']), permanent=True)
                    UpdateNoticeDialog(self, info).run()
                elif manual:
                    if st == "latest":
                        messagebox.showinfo(APP_NAME, trf('최신 버전입니다. (v{0})', APP_VER), parent=self)
                    else:
                        messagebox.showwarning(APP_NAME, info, parent=self)
                    self.say("")
        except queue.Empty:
            pass
        self.after(1000, self.poll_update)

    def update_settings(self):
        new = UpdateSettingsDialog(self).run()
        if new is None:
            return
        self.settings["update"] = new
        self.settings.pop("update_last", None)
        save_settings(self.settings)
        if update_conf(self.settings)["repo"]:
            self.update_check(manual=True)

    def start_self_update(self, info):
        """새 exe 를 받아 자동으로 바꿔 넣고 다시 시작한다. exe 로 실행 중일 때만 가능."""
        asset = info.get("asset")
        if not asset or sys.platform != "win32" or not getattr(sys, "frozen", False):
            messagebox.showinfo(APP_NAME, tr(
                "이 방식으로는 자동 업데이트를 적용할 수 없습니다. (exe 로 실행 중일 때만 가능)\n"
                "다운로드 페이지에서 새 exe 를 받아 직접 바꿔 넣어 주세요."), parent=self)
            webbrowser.open(info["url"])
            return
        c = update_conf(self.settings)
        dlg = tk.Toplevel(self)
        dlg.title(trf('{0} - 업데이트 적용', APP_NAME))
        dlg.configure(bg=BG)
        dlg.resizable(False, False)
        dlg.transient(self)
        dlg.protocol("WM_DELETE_WINDOW", lambda: None)   # 적용 중에는 닫지 못하게
        lab = tk.Label(dlg, bg=BG, text=trf('업데이트 다운로드 중... {0}%', 0), width=40)
        lab.pack(padx=20, pady=(18, 6))
        pb = ttk.Progressbar(dlg, length=320, mode="determinate")
        pb.pack(padx=20, pady=(0, 18))
        dlg.update_idletasks()
        dlg.geometry(f"+{self.winfo_rootx() + 40}+{self.winfo_rooty() + 60}")
        dlg.grab_set()
        q = queue.Queue()
        tmp = os.path.join(tempfile.gettempdir(), f"MyPass_update_{uuid.uuid4().hex}.exe")

        def work():
            ok, err = download_asset(c["repo"], asset["id"], c["token"], tmp,
                                      lambda got, total: q.put(("p", got, total)))
            q.put(("done", ok, err))
        threading.Thread(target=work, daemon=True).start()

        def poll():
            try:
                while True:
                    item = q.get_nowait()
                    if item[0] == "p":
                        _, got, total = item
                        pct = (got * 100 // total) if total else 0
                        pb["value"] = pct
                        lab.config(text=trf('업데이트 다운로드 중... {0}%', pct))
                    else:
                        _, ok, err = item
                        if not ok:
                            dlg.destroy()
                            messagebox.showwarning(APP_NAME, trf('다운로드에 실패했습니다: {0}', err), parent=self)
                            return
                        lab.config(text=tr("업데이트를 적용합니다. 프로그램이 곧 다시 시작됩니다."))
                        dlg.update()
                        self.after(400, lambda: self._finish_update(tmp))
                        return
            except queue.Empty:
                pass
            dlg.after(100, poll)
        poll()

    def _finish_update(self, tmp):
        try:
            apply_update_and_restart(tmp)
        except Exception as e:
            messagebox.showwarning(APP_NAME, trf('업데이트 적용에 실패했습니다: {0}', e), parent=self)
            return
        self.destroy()
        os._exit(0)

    # ===============================
    # 백업 위치(사용자가 정한 폴더) 자동 백업
    # ===============================
    DEST_DELAY_MS = 8000

    def dest_status_set(self, ok, msg, user=None):
        user = user or self.vault.user
        self.settings.setdefault("backup_dest_status", {})[user] = {
            "time": time.strftime("%Y-%m-%d %H:%M:%S"), "ok": bool(ok), "msg": msg}
        save_settings(self.settings)

    def dest_sync(self, reason="", wait=False):
        """설정되어 있으면 백업 위치에 백업한다. (화면이 멈추지 않도록 별도 스레드에서 실행)"""
        v = self.vault
        if v is None or v.key is None:                      # 잠금 상태에서는 절대 백업하지 않는다(빈 데이터 방지)
            return
        conf = dest_conf(self.settings)
        if not conf["enabled"]:
            return
        user, src = v.user, v.path
        csv_bytes = vault_csv_bytes(v) if conf["format"] == "csv" else None

        def work():
            ok, msg = dest_backup(conf, user, src, csv_bytes)
            self.dest_q.put((user, ok, msg))
        th = threading.Thread(target=work, daemon=True)
        th.start()
        if wait:
            th.join(3)

    def dest_sync_soon(self):
        v = self.vault
        if v is None or v.key is None or not dest_conf(self.settings)["enabled"]:
            return
        if self._dest_job:
            self.after_cancel(self._dest_job)
        self._dest_job = self.after(self.DEST_DELAY_MS, self._dest_fire)

    def _dest_fire(self):
        self._dest_job = None
        self.dest_sync(tr("변경"))

    def poll_dest(self):
        try:
            while True:
                user, ok, msg = self.dest_q.get_nowait()
                self.dest_status_set(ok, msg, user=user)
                if self.vault is not None and user == self.vault.user:
                    self.say(trf('백업 위치에 백업 완료 ({0})', time.strftime('%H:%M')) if ok else trf('백업 위치 백업 실패: {0}', msg))
        except queue.Empty:
            pass
        self.after(1000, self.poll_dest)

    def dest_settings(self):
        user = self.vault.user
        old = dest_conf(self.settings)
        new = BackupDestDialog(self).run()
        if not new:
            return
        set_dest_conf(self.settings, new)
        save_settings(self.settings)
        if old["format"] == "csv" and old["path"] and (not new["enabled"] or new["format"] != "csv"
                                                        or new["path"] != old["path"]):
            f = os.path.join(dest_target(old), f"{user}_latest.csv")
            if os.path.exists(f) and messagebox.askyesno(
                    APP_NAME, trf('백업 폴더에 예전에 저장해 둔 CSV 파일(암호화 안 됨)이 남아 있습니다.\n지금 삭제할까요?\n\n{0}', f), parent=self):
                try:
                    os.remove(f)
                except OSError as e:
                    messagebox.showwarning(APP_NAME, trf('삭제하지 못했습니다.\n{0}', e), parent=self)
        if new["enabled"]:
            self.say(tr("백업 위치 자동 백업을 켰습니다. 지금 백업하는 중..."))
            self.dest_sync(tr("설정"))
        else:
            self.say(tr("백업 위치 자동 백업을 껐습니다."))

    def shared_settings(self):
        r = SharedAccountDialog(self).run()
        if r is None:
            return
        user, path = r
        set_shared_conf(user, path)
        if user:
            messagebox.showinfo(APP_NAME, trf("공용 계정 '{0}' 이(가) 설정되었습니다.\n"
                                            "이제부터 그 아이디로 로그인하면 공유 폴더의 보관함을 씁니다.\n"
                                            "(다른 PC에도 이 설정을 똑같이 입력해야 같은 곳을 보게 됩니다)", user), parent=self)
        else:
            messagebox.showinfo(APP_NAME, tr("공용 계정 설정을 껐습니다. (모든 아이디가 다시 로컬에만 저장됩니다)"), parent=self)

    def dest_backup_now(self):
        conf = dest_conf(self.settings)
        if not conf["path"]:
            if messagebox.askyesno(APP_NAME, tr("아직 백업 위치가 설정되지 않았습니다.\n지금 설정할까요?"), parent=self):
                self.dest_settings()
            return
        csv_bytes = vault_csv_bytes(self.vault) if conf["format"] == "csv" else None
        ok, msg = dest_backup(conf, self.vault.user, self.vault.path, csv_bytes)
        self.dest_status_set(ok, msg)
        (messagebox.showinfo if ok else messagebox.showwarning)(APP_NAME, msg, parent=self)

    def relogin(self):
        if self._dest_job:
            self.after_cancel(self._dest_job)
            self._dest_job = None
        for w in self.winfo_children():
            if isinstance(w, tk.Toplevel):
                w.destroy()
        self.mgr = None
        self.vault.lock()
        self.withdraw()
        if not self.login():
            self.destroy()
            return
        self.after_login()
        self.deiconify()
        fade_in(self)
        self.touch()

    # ====================
    # UI
    # ====================
    def build_ui(self):
        self.configure(bg=BG)
        place_window(self, self.settings, "main", 400, 700, 360, 560)
        auto_remember(self, self.settings, "main")
        self.topmost_v = tk.BooleanVar(value=False)
        self.enter_v = tk.BooleanVar(value=False)
        self.link_v = tk.BooleanVar(value=True)
        self.bold_v = tk.BooleanVar(value=FONT_BOLD)
        self.fontscale_v = tk.DoubleVar(value=FONT_SCALE)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.bind("<F1>", lambda e: self.show_help())
        self.bind("<F5>", self.fetch_browser_addr)
        self.bind("<Control-n>", lambda e: self.add_site())
        self.bind("<Control-f>", self.toggle_search)

        def cascade(mb, label, m):
            txt, ul = menu_label(label)
            mb.add_cascade(label=txt, menu=m, underline=ul)

        mb = tk.Menu(self, tearoff=0)
        m = tk.Menu(mb, tearoff=0)
        m.add_command(label=tr("CSV 가져오기"), command=self.import_csv)
        m.add_command(label=tr("CSV 내보내기 (암호화 안 됨)"), command=self.export_csv)
        m.add_separator()
        m.add_command(label=tr("백업 만들기..."), command=self.make_backup)
        m.add_command(label=tr("백업에서 복원..."), command=self.restore_menu)
        m.add_command(label=tr("자동 백업 폴더 열기"), command=lambda: open_folder(BACKUP_DIR))
        m.add_command(label=tr("지금 백업 위치에 백업"), command=self.dest_backup_now)
        m.add_separator()
        m.add_command(label=tr("로그아웃"), command=self.relogin)
        m.add_command(label=tr("다른 사용자로 로그인"), command=self.relogin)
        m.add_command(label=tr("현재 사용자 삭제..."), command=self.delete_me)
        m.add_command(label=tr("마스터 비밀번호 변경"), command=self.change_master)
        m.add_separator()
        m.add_command(label=tr("종료"), command=self.on_close)
        cascade(mb, tr("파일(F)"), m)
        m = tk.Menu(mb, tearoff=0)
        m.add_command(label=tr("목록관리"), command=self.open_manager)
        m.add_command(label=tr("사이트 추가\tCtrl+N"), command=self.add_site)
        m.add_command(label=tr("그룹 추가"), command=self.add_folder)
        m.add_separator()
        m.add_command(label=tr("브라우저 주소 지금 가져오기\tF5"), command=self.fetch_browser_addr)
        m.add_separator()
        m.add_command(label=tr("모든 그룹 펼치기"), command=lambda: self.expand_all(True))
        m.add_command(label=tr("모든 그룹 접기"), command=lambda: self.expand_all(False))
        cascade(mb, tr("관리(T)"), m)
        m = tk.Menu(mb, tearoff=0)
        lm = tk.Menu(m, tearoff=0)
        self.lang_v = tk.StringVar(value=LANG)
        for code, name in LANGS:
            lm.add_radiobutton(label=name, value=code, variable=self.lang_v,
                               command=lambda c=code: self.change_language(c))
        m.add_cascade(label=tr("언어 (Language)"), menu=lm)
        m.add_separator()
        m.add_checkbutton(label=tr("항상 위에 표시"), variable=self.topmost_v, command=self.apply_options)
        m.add_checkbutton(label=tr("채움 후 Enter 키 입력(자동 로그인)"), variable=self.enter_v, command=self.apply_options)
        m.add_checkbutton(label=tr("브라우저 주소 자동 연동"), variable=self.link_v, command=self.toggle_link)
        m.add_separator()
        m.add_command(label=tr("강조 색상..."), command=self.pick_accent)
        fm = tk.Menu(m, tearoff=0)
        for label, val in FONT_SCALES:
            fm.add_radiobutton(label=tr(label), value=val, variable=self.fontscale_v,
                               command=lambda v=val: self.change_font_scale(v))
        m.add_cascade(label=tr("글자 크기"), menu=fm)
        m.add_checkbutton(label=tr("글자 굵게 표시"), variable=self.bold_v, command=self.toggle_font_bold)
        m.add_separator()
        im = tk.Menu(m, tearoff=0)
        self.idlesec_v = tk.IntVar(value=self.idle_sec)
        for label, val in IDLE_OPTIONS:
            im.add_radiobutton(label=tr(label), value=val, variable=self.idlesec_v,
                                command=lambda v=val: self.change_idle_sec(v))
        m.add_cascade(label=tr("자동 잠금 시간"), menu=im)
        m.add_separator()
        m.add_command(label=tr("백업 위치 설정..."), command=self.dest_settings)
        m.add_command(label=tr("공용 계정 설정..."), command=self.shared_settings)
        m.add_command(label=tr("창 크기 초기화"), command=self.reset_window_size)
        cascade(mb, tr("환경설정(S)"), m)
        m = tk.Menu(mb, tearoff=0)
        m.add_command(label=tr("업데이트 확인"), command=lambda: self.update_check(True))
        m.add_command(label=tr("업데이트 설정..."), command=self.update_settings)
        cascade(mb, tr("업데이트(U)"), m)
        m = tk.Menu(mb, tearoff=0)
        m.add_command(label=tr("사용법\tF1"), command=self.show_help)
        m.add_command(label=tr("자주 묻는 질문"), command=lambda: self.show_help(HELP_FAQ))
        m.add_separator()
        m.add_command(label=tr("정보"), command=lambda: AboutDialog(self).run())
        cascade(mb, tr("도움말(H)"), m)
        self.config(menu=mb)

        ic = self.icons
        W = "#FFFFFF"

        def hover(b, base, hv=HOVER):
            press = _shade(hv, 0.92)
            b.bind("<Enter>", lambda e: b.config(bg=hv))
            b.bind("<Leave>", lambda e: b.config(bg=base))
            b.bind("<ButtonPress-1>", lambda e: b.config(bg=press), add="+")
            b.bind("<ButtonRelease-1>", lambda e: b.config(bg=hv), add="+")

        self.statusbar = tk.Label(self, text="", anchor="w", bg=BG, fg=MUTED, padx=12, pady=5, font=fnt(9))
        self.statusbar.pack(side="bottom", fill="x")
        tk.Frame(self, bg=BORDER, height=1).pack(side="bottom", fill="x")

        tb = tk.Frame(self, bg=BG)
        tb.pack(fill="x", padx=10, pady=(10, 4))

        def tbtn(text, icon, cmd, parent=tb):
            b = tk.Button(parent, text=text, image=ic.get(icon, 22), compound="top", command=cmd, relief="flat",
                          bd=0, bg=BG, activebackground=ACCENT_L, fg=TEXT, activeforeground=TEXT, padx=10, pady=6,
                          cursor="hand2", takefocus=0)
            b.pack(side="left", padx=1)
            hover(b, BG)
            return b
        tbtn(tr("목록관리"), "list", self.open_manager)
        af = tk.Frame(tb, bg=BG)
        af.pack(side="left")
        tbtn(tr("추가"), "plus", self.add_site, af)
        arrow = tk.Button(af, image=ic.get("chev_d", 12), relief="flat", bd=0, bg=BG, activebackground=ACCENT_L,
                          padx=2, cursor="hand2", takefocus=0, command=self.show_add_menu)
        arrow.pack(side="left", fill="y")
        hover(arrow, BG)
        self.add_btn_frame = af
        tbtn(tr("수정"), "pencil", self.edit_site)
        tbtn(tr("삭제"), "trash", self.delete_site)
        tbtn(tr("검색"), "search", self.toggle_search)

        self.search_v = tk.StringVar()
        sf_outer, sf = card(self, border=ACCENT)
        tk.Label(sf, image=ic.get("search", 16), bg=W).pack(side="left", padx=(12, 6), pady=8)
        self.search_e = tk.Entry(sf, textvariable=self.search_v, relief="flat", bd=0, highlightthickness=0, bg=W)
        self.search_e.pack(side="left", fill="x", expand=True, pady=8)
        close_b = tk.Button(sf, text="✕", command=self.close_search, relief="flat", bd=0, bg=W, fg=MUTED,
                             activebackground=W, cursor="hand2", takefocus=0)
        close_b.pack(side="right", padx=(0, 10))
        self.search_e.bind("<Escape>", lambda e: self.close_search())
        self.search_v.trace_add("write", lambda *a: self.refresh_tree())
        self.search_frame = sf_outer

        ar_outer, ar = card(self)
        self.addr_frame = ar_outer
        ar_outer.pack(fill="x", padx=10, pady=4)
        tk.Label(ar, text=tr("주소"), bg=W, fg=MUTED).pack(side="left", padx=(12, 6))
        self.addr = tk.StringVar()
        e = tk.Entry(ar, textvariable=self.addr, relief="flat", bd=0, highlightthickness=0, bg=W)
        e.pack(side="left", fill="x", expand=True, pady=10)

        def ibtn(icon, cmd, tip):
            b = tk.Button(ar, image=ic.get(icon, 18), command=cmd, relief="flat", bd=0, bg=W,
                          activebackground=ACCENT_L, cursor="hand2", takefocus=0, padx=6, pady=4)
            b.pack(side="right", padx=(0, 4))
            hover(b, W)
            return b
        ibtn("go", self.go, tr("사이트 열기"))
        ibtn("refresh", self.fetch_browser_addr, tr("브라우저 주소 가져오기"))
        e.bind("<Return>", lambda ev: self.go())
        e.bind("<FocusIn>", lambda ev: ar.config(highlightbackground=ACCENT))
        e.bind("<FocusOut>", lambda ev: ar.config(highlightbackground=BORDER))
        self.addr.trace_add("write", lambda *a: None if self._lock else self.update_matches())

        st_outer, st = card(self)
        st_outer.pack(fill="x", padx=10, pady=4)
        self.ic_ok, self.ic_none = ic.get("ok", 20), ic.get("none", 20)
        self.ico = tk.Label(st, image=self.ic_none, bg=W)
        self.ico.pack(side="left", padx=(12, 8), pady=10)
        self.info = tk.Label(st, text=tr("사이트 정보가 없습니다."), bg=W, fg=MUTED, anchor="w")
        self.info.pack(side="left", fill="x", expand=True)

        lb_outer, lb_inner = card(self, border=ACCENT)
        self.match_outer = lb_outer
        mh = tk.Frame(lb_inner, bg=W)
        mh.pack(fill="x", padx=12, pady=(9, 4))
        tk.Label(mh, image=ic.get("search", 13), bg=W).pack(side="left", padx=(0, 5))
        tk.Label(mh, text=tr("같은 주소에 여러 개가 있습니다 — 하나를 고르세요"), bg=W, fg=ACCENT_D,
                 anchor="w", font=fnt(8, "bold")).pack(side="left", fill="x", expand=True)
        self.match_reveal = False
        self.match_reveal_btn = tk.Button(mh, text=tr("아이디 보기"), relief="flat", bd=0, bg=W, fg=ACCENT_D,
                                           activebackground=W, activeforeground=ACCENT, cursor="hand2",
                                           takefocus=0, font=fnt(8, "underline"), command=self.toggle_match_reveal)
        self.match_reveal_btn.pack(side="right")
        self.match_list = tk.Frame(lb_inner, bg=W)
        self.match_list.pack(fill="both", expand=True, padx=8, pady=(0, 9))
        self.match_rows = []

        cred_outer, cred = card(self)
        self.cred_outer = cred_outer
        cred_outer.pack(fill="x", padx=10, pady=4)
        cred.columnconfigure(1, weight=1)
        self.val = []
        for r, label in enumerate([tr("아이디"), tr("비밀번호")]):
            tk.Label(cred, text=label, bg=W, fg=MUTED, anchor="w", width=8).grid(
                row=r * 2, column=0, sticky="nsew", padx=(12, 4), pady=11)
            v = tk.Label(cred, text="", bg=W, fg=TEXT, anchor="w", padx=4, cursor="hand2")
            v.grid(row=r * 2, column=1, sticky="nsew")
            v.bind("<Double-Button-1>", lambda ev, i=r: self.copy_field(i))
            v.bind("<Button-3>", self.field_menu)
            self.val.append(v)
        tk.Frame(cred, bg=BORDER, height=1).grid(row=1, column=0, columnspan=2, sticky="ew", padx=12)
        self.fill_btn = Btn(cred, tr("채움"), self.do_fill, primary=True, width=7, font=fnt(11, "bold"))
        self.fill_btn.grid(row=0, column=2, rowspan=3, sticky="nsew", padx=10, pady=10)
        tk.Label(self, text=tr("값을 더블클릭하면 복사됩니다 · 오른쪽 클릭: 메뉴"), bg=BG, fg=MUTED,
                 font=fnt(8), anchor="w").pack(fill="x", padx=12, pady=(0, 2))

        tf_outer, tf = card(self)
        tf_outer.pack(fill="both", expand=True, padx=10, pady=(4, 10))
        self.ic_folder, self.ic_key = ic.get("folder", 16), ic.get("key", 16)
        self.ic_warn = ic.get("warn", 16)
        self.tree = ttk.Treeview(tf, show="tree", selectmode="browse")
        sb = ttk.Scrollbar(tf, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=autoscroll(sb, self.tree))
        sb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.on_tree_double)
        self.tree.bind("<Button-3>", self.tree_menu)
        self.tree.tag_configure("drop", background="#C7E6DA")
        self.tree.tag_configure("stale", foreground="#C98A2E")
        self._dd = None
        self.tree.bind("<ButtonPress-1>", self._dd_press, add="+")
        self.tree.bind("<B1-Motion>", self._dd_motion, add="+")
        self.tree.bind("<ButtonRelease-1>", self._dd_release, add="+")

    # ====================
    # 상태 표시
    # ====================
    def say(self, msg, permanent=False):
        self.statusbar.config(text=msg)
        if self._msg_job:
            self.after_cancel(self._msg_job)
            self._msg_job = None
        if not permanent:
            self._msg_job = self.after(4000, lambda: self.say(self.login_msg(), True))

    def login_msg(self):
        msg = trf('{0}님 로그인', self.vault.user)
        n = len(self.vault.stale_sites())
        if n:
            msg += trf('  ·  오래 안 쓴 사이트 {0}개', n)
        return msg

    # ====================
    # 검색
    # ====================
    def toggle_search(self, event=None):
        if self.search_frame.winfo_ismapped():
            self.close_search()
        else:
            self.search_frame.pack(fill="x", padx=10, pady=4, before=self.addr_frame)
            self.search_e.focus_set()
        return "break"

    def close_search(self):
        self.search_v.set("")      # → refresh_tree() 자동 호출(trace)
        self.search_frame.pack_forget()
        self.focus_set()

    def apply_options(self):
        self.settings["topmost"] = self.topmost_v.get()
        self.settings["enter_after"] = self.enter_v.get()
        self.attributes("-topmost", self.topmost_v.get())
        save_settings(self.settings)

    # ====================
    # 목록 트리
    # ====================
    def _walk_items(self, parent=""):
        for c in self.tree.get_children(parent):
            yield c
            yield from self._walk_items(c)

    def refresh_tree(self, select=None):
        t, v = self.tree, self.vault
        q = self.search_v.get().strip().lower() if hasattr(self, "search_v") else ""
        was = {i: bool(t.item(i, "open")) for i in self._walk_items() if i == "top" or i.startswith("f:")}
        t.delete(*t.get_children())

        def site_match(s):
            return q in (s["desc"] + " " + s.get("url", "") + " " + s.get("keyword", "") + " "
                         + s.get("user", "")).lower()

        match_ids = {s["id"] for s in v.data["sites"] if site_match(s)} if q else None
        folder_match_count = {}   # 검색 중에는 그룹 옆 숫자도 '전체 개수'가 아니라 '검색에 걸린 개수'로 보여 줌
        if q:
            parent_of = {f["id"]: f.get("parent") for f in v.data["folders"]}
            for s in v.data["sites"]:
                if s["id"] in match_ids:
                    fid = s.get("folder")
                    while fid:
                        folder_match_count[fid] = folder_match_count.get(fid, 0) + 1
                        fid = parent_of.get(fid)

        top_text = trf('최상위 ({0})', v.count_sites(None)) if not q else trf('검색 결과 {0}개', len(match_ids))
        t.insert("", "end", iid="top", text=top_text, image=self.ic_folder, open=True)

        def walk(piid, fid):
            kids = [f for f in v.data["folders"] if f.get("parent") == fid]
            for f in sorted(kids, key=lambda f: f["name"].lower()):
                if q and f["id"] not in folder_match_count:
                    continue
                iid = "f:" + f["id"]
                count = folder_match_count[f["id"]] if q else v.count_sites(f["id"])
                t.insert(piid, "end", iid=iid, text=f"{f['name']} ({count})",
                         image=self.ic_folder, open=(True if q else was.get(iid, True)))
                walk(iid, f["id"])
            for s in sorted((s for s in v.data["sites"] if s.get("folder") == fid), key=lambda s: s["desc"].lower()):
                if q and s["id"] not in match_ids:
                    continue
                text = s["desc"] + (tr(" · 오래 안 씀") if v.is_stale(s) else "")
                t.insert(piid, "end", iid="s:" + s["id"], text=text, image=self.ic_key,
                         tags=("stale",) if v.is_stale(s) else ())
        walk("top", None)
        if select and t.exists(select):
            p = t.parent(select)
            while p:
                t.item(p, open=True)
                p = t.parent(p)
            t.selection_set(select)
            t.see(select)
        if q:
            self.say(trf('검색 결과 {0}개', len(match_ids)), permanent=True)

    def expand_all(self, flag):
        for i in self._walk_items():
            if i.startswith("f:"):
                self.tree.item(i, open=flag)
        self.tree.item("top", open=True)

    def tree_site(self):
        s = self.tree.selection()
        return self.vault.site(s[0][2:]) if s and s[0].startswith("s:") else None

    def sel_group(self):
        s = self.tree.selection()
        return s[0][2:] if s and s[0].startswith("f:") else None

    def on_tree_select(self, e=None):
        s = self.tree_site()
        if s:
            self.show_site(s)

    def on_tree_double(self, e=None):
        s = self.tree_site()
        if s:
            self.show_site(s)
            self.go()

    def tree_menu(self, ev):
        iid = self.tree.identify_row(ev.y)
        if not iid:
            return
        self.tree.selection_set(iid)
        m = tk.Menu(self, tearoff=0)
        if iid.startswith("s:"):
            m.add_command(label=tr("사이트 열기"), command=self.go)
            m.add_command(label=tr("수정"), command=self.edit_site)
            m.add_command(label=tr("삭제"), command=self.delete_site)
            m.add_separator()
            m.add_cascade(label=tr("그룹으로 이동"), menu=self._move_menu(m, site_id=iid[2:]))
        elif iid == "top":
            m.add_command(label=tr("여기에 사이트 추가"), command=self.add_site)
            m.add_command(label=tr("그룹 추가"), command=self.add_folder)
            m.add_separator()
            m.add_command(label=tr("모두 펼치기"), command=lambda: self.expand_all(True))
            m.add_command(label=tr("모두 접기"), command=lambda: self.expand_all(False))
        else:
            m.add_command(label=tr("여기에 사이트 추가"), command=self.add_site)
            m.add_command(label=tr("하위 그룹 추가"), command=self.add_folder)
            m.add_command(label=tr("그룹 이름 변경"), command=self.rename_group)
            m.add_cascade(label=tr("다른 그룹 안으로 이동"), menu=self._move_menu(m, group_id=iid[2:]))
            m.add_command(label=tr("그룹 삭제"), command=self.delete_group)
        m.tk_popup(ev.x_root, ev.y_root)

    def selected_folder(self):
        s = self.tree.selection()
        if not s:
            return None
        if s[0].startswith("f:"):
            return s[0][2:]
        if s[0].startswith("s:"):
            site = self.vault.site(s[0][2:])
            return site.get("folder") if site else None
        return None

    # ====================================
    # 그룹: 이동 / 이름 변경 / 삭제 / 끌어서 놓기
    # ====================================
    def _move_menu(self, parent, site_id=None, group_id=None):
        v, sub, exclude, cur = self.vault, tk.Menu(parent, tearoff=0), set(), None
        if site_id:
            s = v.site(site_id)
            cur = s.get("folder") if s else None
        if group_id:
            f = v.folder(group_id)
            cur = f.get("parent") if f else None
            exclude = {group_id} | v.descendants(group_id)
        for label, gid in v.folder_choices():
            if gid in exclude:
                continue
            sub.add_command(label=label, state="disabled" if gid == cur else "normal",
                            command=lambda g=gid: self.do_move(site_id, group_id, g))
        return sub

    def do_move(self, site_id, group_id, to):
        v = self.vault
        if site_id:
            v.move_sites([site_id], to)
            sel = "s:" + site_id
        else:
            if not v.move_folder(group_id, to):
                messagebox.showwarning(APP_NAME, tr("옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)"), parent=self)
                return
            sel = "f:" + group_id
        self.on_data_changed(select=sel)
        self.say(trf("'{0}' 로 옮겼습니다.", v.folder_path(to)))

    def rename_group(self):
        fid = self.sel_group()
        f = self.vault.folder(fid) if fid else None
        if not f:
            return
        name = simpledialog.askstring(APP_NAME, tr("그룹 이름:"), initialvalue=f["name"], parent=self)
        if name is None:
            return
        if not self.vault.rename_folder(fid, name):
            messagebox.showwarning(APP_NAME, tr("사용할 수 없는 그룹 이름입니다."), parent=self)
            return
        self.on_data_changed(select="f:" + fid)

    def delete_group(self):
        fid = self.sel_group()
        if not fid:
            return
        if messagebox.askyesno(APP_NAME, tr("그룹과 하위 그룹을 삭제합니다.\n안에 있던 사이트 정보는 상위 그룹으로 옮겨집니다.\n(사이트는 지워지지 않습니다) 계속할까요?"), parent=self):
            self.vault.delete_folder(fid)
            self.on_data_changed()

    def _dd_press(self, ev):
        iid = self.tree.identify_row(ev.y)
        self._dd = {"src": iid, "x": ev.x, "y": ev.y, "on": False, "hl": None} if iid and iid != "top" else None

    def _dd_dest(self, src, tgt):
        """끌어온 항목(src)을 tgt 위에 놓았을 때 (이동 가능 여부, 대상 그룹id)"""
        v = self.vault
        if not tgt or not self.tree.exists(tgt):
            return False, None
        if tgt == "top":
            dest = None
        elif tgt.startswith("f:"):
            dest = tgt[2:]
        else:
            s = v.site(tgt[2:])
            if not s:
                return False, None
            dest = s.get("folder")
        if src.startswith("s:"):
            s = v.site(src[2:])
            return (bool(s) and s.get("folder") != dest), dest
        gid = src[2:]
        f = v.folder(gid)
        if not f or dest == f.get("parent") or dest == gid or (dest is not None and dest in v.descendants(gid)):
            return False, None
        return True, dest

    def _dd_motion(self, ev):
        d = self._dd
        if not d:
            return
        if not d["on"]:
            if abs(ev.x - d["x"]) + abs(ev.y - d["y"]) < 10:
                return
            d["on"] = True
            self.tree.config(cursor="hand2")
        ok, dest = self._dd_dest(d["src"], self.tree.identify_row(ev.y))
        new = ("top" if dest is None else "f:" + dest) if ok else None
        if new != d["hl"]:
            if d["hl"] and self.tree.exists(d["hl"]):
                self.tree.item(d["hl"], tags=())
            if new:
                self.tree.item(new, tags=("drop",))
            d["hl"] = new

    def _dd_release(self, ev):
        d, self._dd = self._dd, None
        if not d:
            return
        self.tree.config(cursor="")
        if d["hl"] and self.tree.exists(d["hl"]):
            self.tree.item(d["hl"], tags=())
        if not d["on"]:
            return
        ok, dest = self._dd_dest(d["src"], self.tree.identify_row(ev.y))
        if not ok:
            return
        if d["src"].startswith("s:"):
            self.do_move(d["src"][2:], None, dest)
        else:
            self.do_move(None, d["src"][2:], dest)

    # ====================
    # 주소 / 매칭
    # ====================
    def show_site(self, site):
        self._lock = True
        self.addr.set(site["url"])
        self._lock = False
        self.update_matches(prefer=site)

    def update_matches(self, prefer=None):
        ms = find_matches(self.vault.data["sites"], self.addr.get())
        if prefer is not None and all(m is not prefer for m in ms):
            ms = [prefer] + ms
        self.matches = ms
        self.match_reveal = False
        self.match_reveal_btn.config(text=tr("아이디 보기"))
        if len(ms) > 1:
            if not self.match_outer.winfo_manager():
                self.match_outer.pack(fill="x", padx=10, pady=4, before=self.cred_outer)
        else:
            self.match_outer.pack_forget()
        if ms:
            idx = next((i for i, m in enumerate(ms) if m is prefer), 0)
            self.set_current(ms[idx])
        else:
            self._clear_match_rows()
            self.set_current(None)

    def _mask_id(self, uid):
        if not uid:
            return ""
        if self.match_reveal:
            return uid
        return (uid[:2] if len(uid) > 2 else uid[:1]) + "••••"

    def toggle_match_reveal(self):
        self.match_reveal = not self.match_reveal
        self.match_reveal_btn.config(text=tr("아이디 숨기기") if self.match_reveal else tr("아이디 보기"))
        self._render_match_rows()

    def _clear_match_rows(self):
        for w in self.match_rows:
            w.destroy()
        self.match_rows = []

    def _render_match_rows(self):
        self._clear_match_rows()
        ms = self.matches
        if len(ms) <= 1:
            return
        for i, s in enumerate(ms):
            self.match_rows.append(self._build_match_row(i, s))

    def _build_match_row(self, i, s):
        selected = s is self.current
        bg = ACCENT_L if selected else "#FFFFFF"
        row = tk.Frame(self.match_list, bg=bg, cursor="hand2")
        row.pack(fill="x", pady=1)
        bar = tk.Frame(row, bg=ACCENT if selected else bg, width=3)
        bar.pack(side="left", fill="y")
        badge = tk.Label(row, image=self.ic_key, bg=ACCENT_L if selected else HOVER, padx=5, pady=5)
        badge.pack(side="left", padx=(8, 8), pady=6)
        txt = tk.Frame(row, bg=bg)
        txt.pack(side="left", fill="both", expand=True, pady=6)
        name_l = tk.Label(txt, text=s["desc"], bg=bg, fg=TEXT, anchor="w", font=fnt(10, "bold"))
        name_l.pack(fill="x")
        id_l = tk.Label(txt, text=self._mask_id(s.get("user", "")), bg=bg, fg=MUTED, anchor="w", font=fnt(8))
        id_l.pack(fill="x")
        chk = tk.Label(row, text=("✓" if selected else ""), bg=bg, fg=ACCENT, font=fnt(11, "bold"), width=2)
        chk.pack(side="right", padx=(0, 8))
        widgets = (row, bar, badge, txt, name_l, id_l, chk)

        def pick(e=None, s=s):
            self.set_current(s)
            self._render_match_rows()
        for w in widgets:
            w.bind("<Button-1>", pick)

        if not selected:
            def on_enter(e):
                for w in (row, txt, name_l, id_l, chk):
                    w.config(bg=HOVER)
            def on_leave(e):
                for w in (row, txt, name_l, id_l, chk):
                    w.config(bg="#FFFFFF")
            row.bind("<Enter>", on_enter)
            row.bind("<Leave>", on_leave)
        return row

    def set_current(self, site):
        self.current = site
        self.pw_visible = False
        if site:
            self.ico.config(image=self.ic_ok)
            self.info.config(text=trf('사이트 정보가 있습니다.  [{0}]', site['desc']), fg=TEXT)
            self.val[0].config(text=site.get("user", ""))
        else:
            self.ico.config(image=self.ic_none)
            self.info.config(text=tr("사이트 정보가 없습니다."), fg=MUTED)
            self.val[0].config(text="")
        self.paint_pw()
        self._render_match_rows()

    def paint_pw(self):
        s = self.current
        if not s:
            self.val[1].config(text="")
        else:
            pw = s.get("pw", "")
            self.val[1].config(text=pw if self.pw_visible else "●" * len(pw))

    def field_menu(self, ev):
        m = tk.Menu(self, tearoff=0)
        m.add_command(label=tr("아이디 복사"), command=lambda: self.copy_field(0))
        m.add_command(label=tr("비밀번호 복사"), command=lambda: self.copy_field(1))
        m.add_command(label=tr("비밀번호 숨기기") if self.pw_visible else tr("비밀번호 보기"), command=self.toggle_pw)
        m.tk_popup(ev.x_root, ev.y_root)

    def toggle_pw(self):
        self.pw_visible = not self.pw_visible
        self.paint_pw()

    def go(self):
        u = self.addr.get().strip()
        if not u:
            return
        webbrowser.open(u if "://" in u else "https://" + u)

    # ====================
    # 복사
    # ====================
    def copy_text(self, text, label, clear=False):
        self.clipboard_clear()
        self.clipboard_append(text)
        msg = trf('{0} 복사됨', label)
        if clear:
            msg += trf(' ({0}초 후 클립보드 삭제)', CLIP_CLEAR_SEC)
            self.after(CLIP_CLEAR_SEC * 1000, lambda: self._clear_clip(text))
        self.say(msg)

    def _clear_clip(self, text):
        try:
            if self.clipboard_get() == text:
                self.clipboard_clear()
                self.clipboard_append("")
        except tk.TclError:
            pass

    def copy_field(self, i):
        s = self.current
        if not s:
            return
        if i == 0:
            self.copy_text(s.get("user", ""), tr("아이디"))
        else:
            self.mark_used(s)
            self.copy_text(s.get("pw", ""), tr("비밀번호"), clear=True)

    def mark_used(self, s):
        """사이트를 실제로 사용했을 때 '마지막 사용' 날짜를 갱신하고 조용히 저장한다."""
        self.vault.touch_site(s["id"])
        try:
            self.vault.save()
        except OSError:
            pass

    # ====================
    # 채움
    # ====================
    def do_fill(self):
        s = self.current
        if not s:
            self.say(tr("채울 사이트 정보가 없습니다."))
            return
        self.mark_used(s)
        if sys.platform != "win32":
            self.copy_text(s.get("pw", ""), tr("비밀번호(이 OS에서는 자동 채움 미지원)"), clear=True)
            return
        self.say(tr("채우는 중... 브라우저의 아이디 입력칸에 커서가 있어야 합니다."))
        self.iconify()
        self.after(700, lambda: self._fill_now(s))

    def _fill_now(self, s):
        try:
            type_text(s.get("user", ""))
            press_vk(0x09)
            type_text(s.get("pw", ""))
            if self.settings.get("enter_after"):
                time.sleep(0.15)
                press_vk(0x0D)
        finally:
            self.after(500, self._restore)

    def _restore(self):
        self.deiconify()
        self.lift()

    # ====================
    # 편집
    # ====================
    def on_data_changed(self, select=None):
        try:
            self.vault.save()
        except OSError as e:
            messagebox.showerror(APP_NAME, trf('저장하지 못했습니다.\n{0}', e), parent=self)
        self.dest_sync_soon()
        self.refresh_tree(select)
        if self.mgr is not None and self.mgr.winfo_exists():
            self.mgr.refresh()
        cur = self.current if self.current in self.vault.data["sites"] else None
        self.update_matches(prefer=cur)

    def add_site(self):
        r = SiteDialog(self, self.vault, url=self.addr.get().strip(), folder=self.selected_folder(),
                       on_group_added=self.on_data_changed).run()
        if r:
            self.vault.data["sites"].append(r)
            self.on_data_changed()
            self.show_site(r)

    def add_site_blank(self):
        r = SiteDialog(self, self.vault, folder=self.selected_folder(), on_group_added=self.on_data_changed).run()
        if r:
            self.vault.data["sites"].append(r)
            self.on_data_changed()
            self.show_site(r)

    def show_add_menu(self):
        m = tk.Menu(self, tearoff=0)
        m.add_command(label=tr("현재 주소로 사이트 추가"), command=self.add_site)
        m.add_command(label=tr("빈 사이트 추가"), command=self.add_site_blank)
        m.add_command(label=tr("그룹 추가"), command=self.add_folder)
        f = self.add_btn_frame
        m.tk_popup(f.winfo_rootx(), f.winfo_rooty() + f.winfo_height())

    def edit_site(self):
        s = self.current
        if not s:
            messagebox.showinfo(APP_NAME, tr("수정할 사이트를 먼저 선택하세요."), parent=self)
            return
        r = SiteDialog(self, self.vault, site=s, on_group_added=self.on_data_changed).run()
        if r:
            s.update(r)
            self.on_data_changed()
            self.show_site(s)

    def delete_site(self):
        s = self.current
        if not s:
            messagebox.showinfo(APP_NAME, tr("삭제할 사이트를 먼저 선택하세요."), parent=self)
            return
        if messagebox.askyesno(APP_NAME, trf("'{0}' 사이트 정보를 삭제할까요?", s['desc']), parent=self):
            self.vault.data["sites"].remove(s)
            self.current = None
            self.on_data_changed()

    def add_folder(self):
        name = simpledialog.askstring(APP_NAME, tr("새 그룹 이름:"), parent=self)
        if name is None:
            return
        if not self.vault.add_folder(name, self.selected_folder()):
            messagebox.showwarning(APP_NAME, tr("그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다."), parent=self)
            return
        self.on_data_changed()

    def open_manager(self):
        if self.mgr is not None and self.mgr.winfo_exists():
            self.mgr.lift()
            return
        self.mgr = ManagerWindow(self)

    # ====================
    # 기타
    # ====================
    def change_master(self):
        p0 = simpledialog.askstring(APP_NAME, tr("현재 마스터 비밀번호:"), show="*", parent=self)
        if p0 is None:
            return
        try:
            ok = Vault(self.vault.user).unlock(p0)
        except Exception:
            ok = False
        if not ok:
            messagebox.showwarning(APP_NAME, tr("현재 비밀번호가 틀렸습니다."), parent=self)
            return
        p1 = simpledialog.askstring(APP_NAME, tr("새 비밀번호 (8자 이상):"), show="*", parent=self)
        if not p1:
            return
        if len(p1) < 8:
            messagebox.showwarning(APP_NAME, tr("8자 이상 입력하세요."), parent=self)
            return
        if p1 != simpledialog.askstring(APP_NAME, tr("새 비밀번호 확인:"), show="*", parent=self):
            messagebox.showwarning(APP_NAME, tr("일치하지 않습니다."), parent=self)
            return
        self.vault.change_password(p1)
        self.dest_sync_soon()
        messagebox.showinfo(APP_NAME, tr("비밀번호가 변경되었습니다."), parent=self)

    def export_csv(self):
        if not messagebox.askokcancel(APP_NAME, tr("내보낸 CSV는 암호화되지 않습니다.\n사용 후 반드시 안전하게 삭제하세요.\n계속할까요?"), parent=self):
            return
        p = filedialog.asksaveasfilename(parent=self, defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not p:
            return
        with open(p, "wb") as f:
            f.write(vault_csv_bytes(self.vault))
        messagebox.showinfo(APP_NAME, tr("내보내기 완료"), parent=self)

    def import_csv(self):
        p = filedialog.askopenfilename(parent=self, filetypes=[("CSV", "*.csv"), (tr("모든 파일"), "*.*")])
        if not p:
            return
        raw = open(p, "rb").read()
        text = None
        for enc in ("utf-8-sig", "cp949", "shift_jis", "gbk"):
            try:
                text = raw.decode(enc)
                break
            except UnicodeDecodeError:
                pass
        if text is None:
            text = raw.decode("utf-8", errors="replace")
        km = {"그룹": "folder", "폴더": "folder", "folder": "folder", "group": "folder",
              "사이트 설명": "desc", "사이트명": "desc", "사이트": "desc", "name": "desc", "title": "desc", "desc": "desc",
              "주소": "url", "url": "url", "address": "url",
              "주소 키워드": "keyword", "키워드": "keyword", "keyword": "keyword",
              "아이디": "user", "id": "user", "user": "user", "username": "user",
              "비밀번호": "pw", "패스워드": "pw", "password": "pw", "pw": "pw"}
        for heads in CSV_HEAD.values():                          # 어느 언어로 내보낸 파일이든 읽는다
            for key, h in zip(("folder", "desc", "url", "keyword", "user", "pw"), heads):
                km.setdefault(h.strip().lower(), key)
        n = 0
        for row in csv.DictReader(text.splitlines()):
            d = {"folder": "", "desc": "", "url": "", "keyword": "", "user": "", "pw": ""}
            for k, val in row.items():
                t = km.get((k or "").strip().lower())
                if t:
                    d[t] = (val or "").strip()
            if not d["url"]:
                continue
            cands = keyword_candidates(d["url"])
            kw = d["keyword"].upper() or (cands[0] if cands else "")
            if not kw:
                continue
            self.vault.data["sites"].append({
                "id": uuid.uuid4().hex, "url": d["url"], "keyword": kw, "manual": bool(d["keyword"]) and kw not in cands,
                "desc": d["desc"] or kw.split(".")[0].capitalize(), "user": d["user"], "pw": d["pw"],
                "folder": self.vault.ensure_folder_path(d["folder"])})
            n += 1
        self.on_data_changed()
        messagebox.showinfo(APP_NAME, trf('{0}개 사이트를 가져왔습니다.', n), parent=self)

    def show_help(self, topic=0):
        if self.help_win is not None and self.help_win.winfo_exists():
            self.help_win.lift()
            self.help_win.lb.selection_clear(0, "end")
            self.help_win.lb.selection_set(topic)
            self.help_win.show(topic)
            return
        self.help_win = HelpWindow(self, topic)

    # ====================
    # 사용자 / 백업
    # ====================
    def new_user_menu(self):
        r = NewUserDialog(self).run()
        if not r:
            return
        uid, pw = r
        try:
            Vault(uid).create(pw)
        except Exception as e:
            messagebox.showerror(APP_NAME, trf('사용자를 만들 수 없습니다.\n{0}', e), parent=self)
            return
        if messagebox.askyesno(APP_NAME, trf("사용자 '{0}' 를 등록했습니다.\n지금 이 사용자로 로그인할까요?", uid), parent=self):
            self.settings["last_user"] = uid
            save_settings(self.settings)
            self.relogin()

    def delete_me(self):
        user = self.vault.user
        if do_delete_user(self, user, require_password=True):
            if self.settings.get("last_user") == user:
                self.settings["last_user"] = ""
                save_settings(self.settings)
            self.relogin()

    def make_backup(self):
        p = filedialog.asksaveasfilename(
            parent=self, title=tr("백업 파일 저장"), defaultextension=BACKUP_EXT,
            initialfile=f"{self.vault.user}_{stamp()}{BACKUP_EXT}",
            filetypes=[(tr("마이패스 백업"), f"*{BACKUP_EXT}"), (tr("모든 파일"), "*.*")])
        if not p:
            return
        try:
            self.vault.save()
            shutil.copy2(self.vault.path, p)
        except OSError as e:
            messagebox.showerror(APP_NAME, trf('백업하지 못했습니다.\n{0}', e), parent=self)
            return
        messagebox.showinfo(APP_NAME, tr("백업했습니다.\n백업 파일은 암호화되어 있으며, 복원할 때 지금의 마스터 비밀번호가 필요합니다."), parent=self)

    def restore_menu(self):
        uid = do_restore_backup(self)
        if uid and uid == self.vault.user:
            messagebox.showinfo(APP_NAME, tr("현재 로그인한 사용자를 복원했습니다. 다시 로그인합니다."), parent=self)
            self.relogin()

    def touch(self, e=None):
        self.last_active = time.time()

    def idle_check(self):
        if self.idle_sec > 0 and time.time() - self.last_active > self.idle_sec:
            self.relogin()
            if not self.winfo_exists():
                return
        self.after(10000, self.idle_check)

    def change_idle_sec(self, v):
        """자동 잠금까지 걸리는 시간을 바꾼다. (0 = 사용 안 함)"""
        self.idle_sec = v
        self.settings["idle_sec"] = v
        save_settings(self.settings)
        self.touch()
        label = next((tr(n) for n, val in IDLE_OPTIONS if val == v), str(v))
        self.say(trf('자동 잠금 시간을 바꿨습니다: {0}', label))

    def reset_window_size(self):
        for k in ("main", "manager", "help"):
            (self.settings.get("windows") or {}).pop(k, None)
        place_window(self, self.settings, "main", 400, 700, 360, 560)
        save_settings(self.settings)
        self.say(tr("창 크기를 기본값으로 되돌렸습니다. (목록관리·도움말 창은 다음에 열 때 적용)"))

    def on_close(self):
        if self._dest_job:
            self.after_cancel(self._dest_job)
            self._dest_job = None
        self.dest_sync(tr("종료"), wait=True)
        if self.watcher is not None:
            self.watcher.stop()
        remember_window(self, self.settings, "main")
        save_settings(self.settings)
        self.destroy()


if __name__ == "__main__":
    # 창 없는(windowed) exe에서는 stdout/stderr 가 없어 일부 라이브러리가 오류를 내므로 대신 비워 둔다
    for _n in ("stdout", "stderr"):
        if getattr(sys, _n) is None:
            setattr(sys, _n, open(os.devnull, "w"))
    if sys.platform == "win32":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    INTERACTIVE_LANG = True
    app = App()
    if app.ready:
        app.mainloop()
