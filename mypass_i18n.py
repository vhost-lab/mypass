# -*- coding: utf-8 -*-
"""마이패스 번역 파일 (mypass.py 와 같은 폴더에 두세요)

· 기본 언어는 한국어이고, 화면 문구(한국어 원문)를 키로 해서 아래 언어별 사전으로 바꿔 줍니다.
· 새 언어를 넣으려면: ① LANGS 에 ("코드", "표시 이름") 추가
                      ② TR["코드"] = {한국어 원문: 번역, ...} 추가 (en 을 복사해서 번역하면 됩니다)
                      ③ CSV_HEAD["코드"] 에 CSV 첫 줄 제목 6개 추가
  번역이 빠진 문구는 한국어 그대로 표시되므로 일부만 번역해도 동작합니다.
· 문구 안의 {0} {1} 은 프로그램이 값을 채우는 자리이니 그대로 두세요.
"""

LANGS = [("ko", "한국어"), ("en", "English"), ("ja", "日本語"), ("zh", "简体中文")]

CSV_HEAD = {
    "ko": ["그룹", "사이트 설명", "주소", "주소 키워드", "아이디", "비밀번호"],
    "en": ["Group", "Site name", "URL", "URL keyword", "ID", "Password"],
    "ja": ["グループ", "サイト名", "URL", "URLキーワード", "ID", "パスワード"],
    "zh": ["分组", "网站名称", "网址", "网址关键词", "账号", "密码"],
}

TR = {
    "en": {
        "글자 크기":
            "Text size",
        "글자 굵게 표시":
            "Show text in bold",
        "글자 크기를 바꿨습니다.":
            "Changed the text size.",
        "굵게 표시 설정을 바꿨습니다.":
            "Changed the bold text setting.",
        "작은 글자":
            "Small",
        "보통 글자":
            "Normal",
        "큰 글자":
            "Large",
        "아주 큰 글자":
            "Extra large",
        "강조 색상...":
            "Accent color...",
        "버튼·테두리 등에 쓸 강조 색을 골라 주세요.":
            "Choose the accent color used for buttons, borders, and more.",
        "직접 선택...":
            "Choose custom...",
        "강조 색상 직접 선택":
            "Choose a custom accent color",
        "강조 색상을 바꿨습니다.":
            "Changed the accent color.",
        "딥 틸 (기본)":
            "Deep Teal (default)",
        "네이비":
            "Navy",
        "자두색":
            "Plum",
        "포레스트 그린":
            "Forest Green",
        "슬레이트 블루":
            "Slate Blue",
        "테라코타":
            "Terracotta",
        "차콜":
            "Charcoal",
        "버건디":
            "Burgundy",
        "매우 약함":
            "Very weak",
        "약함":
            "Weak",
        "보통":
            "Fair",
        "강함":
            "Strong",
        "매우 강함":
            "Very strong",
        "오래 안 쓴 사이트 ({0})":
            "Unused sites ({0})",
        " (오래 안 쓴 사이트)":
            " (unused sites)",
        "주요 기능":
            "Key Features",
        " · 오래 안 씀":
            " · Unused for a while",
        "검색 결과 {0}개":
            "{0} search results",
        "  ·  오래 안 쓴 사이트 {0}개":
            "  ·  {0} unused sites",
        "■ 보관함과 사용자\n· 한 대의 컴퓨터에서 여러 사람(또는 용도별)이 각자 독립된 보관함을 쓸 수 있습니다. (서로의 정보는 볼 수 없습니다)\n· 저장한 사이트는 '그룹(폴더)'으로 나눠서 정리할 수 있고, 마우스로 끌어다 옮길 수 있습니다.\n\n■ 브라우저 연동과 채움\n· 지원하는 브라우저(Chrome·Edge·Whale 등)의 주소창을 읽어서, 지금 보고 있는 사이트의 저장된 정보를 자동으로 찾아줍니다. (Windows 전용)\n· [채움] 버튼 하나로 아이디·비밀번호를 브라우저 입력칸에 자동으로 넣어 줍니다.\n\n■ 검색\n· 메인 창에서 Ctrl+F(또는 돋보기 버튼)를 누르면 검색창이 열립니다. 사이트 설명·주소·키워드·아이디로 모든 그룹을 한 번에 찾아 줍니다.\n· 검색 중에도 그룹(폴더) 구조는 그대로 보이며, 찾은 사이트가 들어 있는 그룹만 펼쳐서 보여 줍니다.\n\n■ 비밀번호 강도 표시\n· 새 비밀번호를 만들 때(회원가입, 사이트 추가/수정) 길이와 문자 종류를 보고 '매우 약함~매우 강함'을 막대와 글자로 바로 보여 줍니다.\n\n■ 안 쓰는 사이트 알림\n· 오랫동안(기본 180일) [채움]이나 비밀번호 복사로 쓰지 않은 사이트는 목록에 주황색으로 '오래 안 씀' 표시가 붙습니다.\n· 로그인하면 오래 안 쓴 사이트가 몇 개인지 요약으로 알려 줍니다. 더 안 쓰는 계정은 정리하거나 비밀번호를 새로 바꾸는 걸 권장합니다.\n· [목록관리] 창 왼쪽의 '오래 안 쓴 사이트'를 누르면 그룹과 상관없이 오래 안 쓴 사이트만 한 번에 모아서 볼 수 있습니다. (오래 쓴 순서대로 정렬)\n\n■ 백업\n· 로그인할 때마다 자동으로 백업됩니다.\n· 원하는 위치(USB, 클라우드 동기화 폴더 등)에 자동 또는 수동으로 백업하도록 설정할 수 있습니다.\n· 기본은 암호화된 백업이며, 필요하면 암호화되지 않은 CSV로도 내보낼 수 있습니다 (내보낼 때 경고가 표시됩니다).\n\n■ 들고 다니기 (USB)\n· exe 파일 옆에 생기는 'data' 폴더만 있으면 되므로, 둘을 함께 USB에 넣어 다른 컴퓨터에서도 바로 쓸 수 있습니다.\n\n■ 업데이트\n· 새 버전이 나오면 알려 주고, [지금 업데이트]를 누르면 새 exe로 자동 교체 · 재시작됩니다.\n\n■ 여러 언어\n· 한국어 · English · 日本語 · 简体中文을 지원합니다. 환경설정에서 언제든 바꿀 수 있습니다.":
            "■ Vault and users\n· One computer can have separate vaults for multiple people (or purposes) — each vault is independent and others can't see your information.\n· Saved sites can be organized into 'groups (folders)' and moved around by dragging.\n\n■ Browser integration and autofill\n· Reads the address bar of supported browsers (Chrome, Edge, Whale, etc.) and automatically finds the saved information for the site you're currently viewing. (Windows only)\n· The [Fill] button automatically enters your ID and password into the browser's input fields.\n\n■ Search\n· Press Ctrl+F (or the magnifying-glass button) in the main window to open the search box. It searches all groups at once by site name, address, keyword, and ID.\n· The group (folder) structure stays visible while searching — only the groups containing matches are expanded.\n\n■ Password strength indicator\n· When creating a new password (sign-up, add/edit site), a bar and label instantly show how strong it is, from 'Very weak' to 'Very strong', based on length and character variety.\n\n■ Unused site notice\n· A site you haven't used (via [Fill] or copying the password) for a long time (180 days by default) gets an orange 'Unused for a while' mark in the list.\n· When you log in, you're told how many sites are unused. It's a good idea to clean up or change the password on accounts you no longer use.\n· Click 'Unused sites' on the left of the [Manage list] window to see every unused site gathered in one place, regardless of group. (sorted by how long unused)\n\n■ Backup\n· An automatic backup is made every time you log in.\n· You can set it to back up automatically or manually to a location of your choice (USB, a cloud sync folder, etc.).\n· Backups are encrypted by default; you can also export an unencrypted CSV if needed (a warning is shown when you do).\n\n■ Carrying it with you (USB)\n· All you need is the 'data' folder created next to the exe file — put both on a USB drive to use it right away on another computer.\n\n■ Updates\n· You're notified when a new version is available, and pressing [Update now] automatically replaces the exe and restarts.\n\n■ Multiple languages\n· Supports Korean, English, Japanese, and Simplified Chinese. You can change it anytime in Settings.",
        "■ 내 정보는 어떻게 보호되나요? (쉽게 설명)\n· 모든 정보는 '암호화'되어 저장됩니다. 암호화란, 마스터 비밀번호가 없으면 아무도 — 프로그램을 만든 사람도 — 내용을 읽을 수 없도록 뒤섞어 두는 것입니다.\n   (전문 용어로는 AES-256-GCM 방식입니다. 지금의 기술로는 사실상 풀 수 없다고 알려진 수준의 암호화 방식이라고 이해하시면 됩니다)\n· 마스터 비밀번호 자체는 어디에도 그대로 저장되지 않습니다. 비밀번호를 아주 여러 번 복잡한 계산을 거쳐 '잠금을 푸는 열쇠'로 바꾼 뒤, 그 열쇠로만 보관함을 엽니다.\n   (전문 용어로는 scrypt 방식입니다. 이렇게 하면 누군가 비밀번호를 무작위로 하나씩 맞혀 보려고 해도, 한 번 시도하는 데 시간이 오래 걸려서 사실상 불가능해집니다)\n· 정보는 이 컴퓨터의 data 폴더에만 저장됩니다. 인터넷 어디로도 보내지지 않습니다.\n· 인터넷에 연결되는 경우는 '새 버전이 나왔는지' 확인할 때뿐이며, 이때도 저장된 아이디·비밀번호는 전혀 전송되지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ How is my information protected? (in plain terms)\n· All information is stored 'encrypted'. Encryption means it's scrambled so that no one — not even the program's creator — can read it without the master password.\n   (The technical term is AES-256-GCM. You can think of it as an encryption method that, with today's technology, is effectively unbreakable.)\n· The master password itself is never stored anywhere as-is. It's run through many rounds of complex calculation to become an 'unlocking key', and only that key opens the vault.\n   (The technical term is scrypt. This makes each guess take a long time, so trying to guess the password one attempt at a time is effectively impossible.)\n· Information is stored only in this computer's data folder. It's never sent anywhere over the internet.\n· The only time it connects to the internet is to check 'whether a new version is out', and even then, no stored ID or password is ever sent.\n\n■ Automatic protections\n· After 10 minutes of inactivity, it returns to the login window.\n· A copied password is cleared from the clipboard after 20 seconds.\n· Passwords are masked as ●●● on screen by default.\n· If you enter the wrong password 5 times at login, the program closes.\n\n■ Things to keep in mind\n· The master password cannot be recovered. Write it down somewhere safe.\n· If this computer gets infected with a virus, no password manager is safe. Keep your antivirus up to date.\n· On a shared computer, always exit after use.",
        "'{0}' 그룹으로 {1}개 사이트를 묶었습니다.":
            "Grouped {1} sites into '{0}'.",
        "'{0}' 로 옮겼습니다.":
            "Moved to '{0}'.",
        "'{0}' 사이트 정보를":
            "Site information for '{0}'",
        "'{0}' 사이트 정보를 삭제할까요?":
            "Delete the site information for '{0}'?",
        "'{0}' 안에 만들 새 그룹 이름:":
            "New group name to create inside '{0}':",
        "'{0}' 의 마스터 비밀번호를 입력하세요:":
            "Enter the master password for '{0}':",
        "'위치'는 이 그룹을 어느 그룹 안에 둘지입니다. 그룹을 삭제해도 안에 있던 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.":
            "'Location' is the group this group is placed in. If you delete a group, the sites inside it are not deleted but moved to the parent group.",
        "({0}초 후 클립보드 삭제)":
            "(Clipboard clears in {0}s)",
        "(검색 결과)":
            "(Search results)",
        "(설정되지 않음)":
            "(Not set)",
        "8자 이상 입력하세요.":
            "Enter at least 8 characters.",
        "CSV (표 파일) — 암호화되지 않음":
            "CSV (spreadsheet file) — not encrypted",
        "CSV 가져오기":
            "Import CSV",
        "CSV 가져오기·내보내기":
            "Import/Export CSV",
        "CSV 내보내기 (암호화 안 됨)":
            "Export CSV (not encrypted)",
        "CSV 데이터가 없습니다.":
            "There is no CSV data.",
        "CSV 백업은 암호화되지 않습니다.\n\n모든 사이트의 아이디와 비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다.\n\n그래도 CSV로 백업할까요?\n(권장: 암호화 백업)":
            "CSV backups are not encrypted.\n\nThe ID and password of every site are saved as plain text. If that folder is in the cloud or visible to others, everything is exposed.\n\nBack up as CSV anyway?\n(Recommended: encrypted backup)",
        "CSV(암호화 안 됨) 백업 완료: {0}":
            "CSV (not encrypted) backup complete: {0}",
        "GitHub 저장소의 최신 Release 를 확인해서 새 버전이 있으면 알려 드립니다. 자동으로 설치하지는 않으며, 다운로드 페이지만 열어 줍니다. (새 exe 로 바꿔도 data 폴더의 정보는 그대로 유지됩니다)":
            "Checks the latest Release in the GitHub repository and notifies you if a new version is available. It does not install anything automatically; it only opens the download page. (Replacing the exe keeps the information in the data folder.)",
        "INFO : 입력하신 정보는 암호화되어 사용자의\n컴퓨터에 저장되며 인터넷으로 전송되지\n않으므로 회원가입이 필요 없습니다.\n\n※ 비밀번호를 잊으면 복구할 수 없습니다.":
            "INFO: The information you enter is encrypted and\nstored on your computer only. It is never sent\nover the internet, so no sign-up is required.\n\n※ If you forget your password, it cannot be recovered.",
        "Q. [채움]을 눌러도 입력이 안 돼요.\nA. ① 브라우저 아이디 입력칸을 먼저 클릭했는지, ② 관리자 권한으로 실행된 창이 아닌지 확인하세요.\n   일부 사이트는 보안 키패드를 써서 자동 입력이 막힙니다. 이때는 값을 복사해서 입력하세요.\n\nQ. 브라우저 주소가 자동으로 안 들어와요.\nA. ① 환경설정 메뉴의 '브라우저 주소 자동 연동'이 켜져 있는지, ② 지원 브라우저인지 확인하세요.\n   ↻ 버튼(F5)으로 즉시 읽기를 시도해 보고, 안 되면 주소를 직접 붙여넣으세요.\n\nQ. 마스터 비밀번호를 잊었어요.\nA. 복구할 방법이 없습니다. 이전 백업의 비밀번호가 기억난다면 백업에서 복원해 보세요.\n   포기하고 새로 시작하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 지우고(또는 다른 곳으로 옮기고)\n   새 사용자를 만드세요.\n\nQ. 프로그램을 다시 설치/이동하면 정보가 사라지나요?\nA. 정보는 프로그램 옆의 data 폴더에 있습니다. 프로그램(exe)을 옮길 때 data 폴더도 같이 옮기세요.\n\nQ. 다른 드라이브나 클라우드에 자동으로 백업하고 싶어요.\nA. 파일 메뉴 '백업 위치 설정'에서 폴더를 고르세요. 클라우드라면 그 서비스의 동기화 폴더를 고르면 됩니다.\n   (도움말 '백업과 복원' 참고. 암호화 백업을 권장합니다)\n\nQ. 다른 컴퓨터에서도 쓰고 싶어요.\nA. 'CSV'는 위험하니 쓰지 말고, '백업 만들기'로 저장한 파일을 새 컴퓨터에서 '백업에서 복원' 하세요.\n   (data 폴더를 통째로 복사해도 됩니다)\n\nQ. 백신이 exe 파일을 의심해요.\nA. 개인이 만든 프로그램은 서명이 없어 오탐이 생기기도 합니다. 특히 [채움]이 키보드 입력을 대신 하기 때문입니다.\n   소스(mypass.py)를 직접 확인하거나 예외 목록에 등록하세요.\n\nQ. 알패스에서 쓰던 정보를 옮기고 싶어요.\nA. 알패스가 정보를 CSV 등으로 내보낼 수 있다면 'CSV 가져오기'를 쓰세요. 없다면 직접 입력해야 합니다.":
            "Q. Nothing is entered when I press [Fill].\nA. Check that (1) you clicked the browser's ID field first, and (2) the window is not running as administrator.\n   Some sites use a secure keypad that blocks automatic input. In that case, copy the values and enter them manually.\n\nQ. The browser address is not filled in automatically.\nA. Check that (1) 'Auto-link browser address' in the Settings menu is turned on, and (2) your browser is supported.\n   Try reading it right away with the ↻ button (F5); if that fails, paste the address manually.\n\nQ. I forgot my master password.\nA. There is no way to recover it. If you remember the password of an earlier backup, try restoring from that backup.\n   To give up and start over, close the program, delete (or move elsewhere) the matching 'ID.dat' file in the data folder,\n   and create a new user.\n\nQ. Will my information disappear if I reinstall or move the program?\nA. Your information is in the data folder next to the program. When you move the program (exe), move the data folder too.\n\nQ. I want to back up automatically to another drive or the cloud.\nA. In the File menu, choose 'Set backup location' and pick a folder. For the cloud, pick that service's sync folder.\n   (See Help 'Backup and restore'. Encrypted backups are recommended.)\n\nQ. I want to use it on another computer.\nA. 'CSV' is risky, so don't use it. Save a file with 'Create backup' and use 'Restore from backup' on the new computer.\n   (You can also copy the whole data folder.)\n\nQ. My antivirus flags the exe file.\nA. Programs made by individuals have no signature, so false positives can occur. This is especially because [Fill] types keyboard input for you.\n   Check the source (mypass.py) yourself or add the program to the exclusion list.\n\nQ. I want to move the information I used in ALPass.\nA. If ALPass can export your information to CSV or similar, use 'Import CSV'. Otherwise, you will need to enter it manually.",
        "{0}  v{1}\n\n아이디·비밀번호·사이트 정보를 암호화해서\n보관하는 개인용 비밀번호 관리 프로그램":
            "{0}  v{1}\n\nA personal password manager that stores\nIDs, passwords, and site information encrypted",
        "{0} - 그룹 수정":
            "{0} - Edit group",
        "{0} - 그룹 이동":
            "{0} - Move group",
        "{0} - 그룹으로 이동":
            "{0} - Move to group",
        "{0} - 도움말":
            "{0} - Help",
        "{0} - 로그인":
            "{0} - Log in",
        "{0} - 목록관리":
            "{0} - Manage list",
        "{0} - 백업 위치 설정":
            "{0} - Set backup location",
        "{0} - 사이트 {1}":
            "{0} - Site {1}",
        "{0} - 새 버전":
            "{0} - New version",
        "{0} - 새 사용자 등록":
            "{0} - Register new user",
        "{0} - 업데이트 설정":
            "{0} - Update settings",
        "{0} - 정보":
            "{0} - About",
        "{0} 복사됨":
            "{0} copied",
        "{0} 삭제할까요?":
            "Delete {0}?",
        "{0}개 사이트를 '{1}' 로 옮겼습니다.":
            "Moved {0} sites to '{1}'.",
        "{0}개 사이트를 가져왔습니다.":
            "Imported {0} sites.",
        "{0}곳을 찾았습니다. 입력칸 오른쪽 ▼ 에서 고르세요.":
            "Found {0}. Choose one from the ▼ on the right of the field.",
        "{0}님 로그인":
            "Log in, {0}",
        "· 암호화: AES-256-GCM / scrypt\n· 정보는 이 컴퓨터에만 저장되며 인터넷으로 전송되지 않습니다.\n· (인터넷은 업데이트 확인에만 사용하며, 정보는 보내지 않습니다)\n· 데이터 폴더:\n   {0}":
            "· Encryption: AES-256-GCM / scrypt\n· Your information is stored only on this computer and is never sent over the internet.\n· (The internet is used only to check for updates, and no information is sent.)\n· Data folder:\n   {0}",
        "■ 가져오기\n· 파일 메뉴 'CSV 가져오기'. 엑셀에서 만든 표나 다른 프로그램에서 내보낸 파일을 읽습니다.\n· 첫 줄(제목줄)에 다음 이름이 있으면 자동으로 인식합니다.\n   그룹(폴더) / 사이트 설명(사이트명, name) / 주소(url) / 주소 키워드 / 아이디(id) / 비밀번호(password)\n· 주소가 없는 줄은 건너뜁니다. 주소 키워드가 비어 있으면 자동으로 만듭니다.\n· '그룹' 칸에 업무/은행 처럼 적으면 그룹이 자동으로 만들어집니다. ('폴더'라는 제목도 인식합니다)\n\n■ 내보내기\n· 파일 메뉴 'CSV 내보내기'. 엑셀로 열 수 있습니다.\n· ※ 내보낸 CSV는 암호화되어 있지 않습니다. 비밀번호가 그대로 보이므로 사용 후 반드시 지우세요.\n· 백업 용도라면 CSV 대신 '백업 만들기'를 사용하세요.":
            "■ Import\n· File menu 'Import CSV'. Reads a table made in Excel or a file exported from another program.\n· If the first row (header row) has the following names, they are recognized automatically.\n   Group (folder) / Site description (site name, name) / Address (url) / Address keyword / ID (id) / Password (password)\n· Rows without an address are skipped. If the address keyword is empty, it is created automatically.\n· If you write something like Work/Bank in the 'Group' column, the groups are created automatically. (The header 'folder' is also recognized.)\n\n■ Export\n· File menu 'Export CSV'. It can be opened in Excel.\n· ※ The exported CSV is not encrypted. Passwords are visible as they are, so be sure to delete it after use.\n· For backup purposes, use 'Create backup' instead of CSV.",
        "■ 기본 크기\n처음 열 때는 화면 배율(125%, 150% 등)에 맞춰 보정한 기본 크기로 열립니다. 어느 컴퓨터에서나 같은 모양으로 나옵니다.\n\n■ 마음대로 조절\n창 가장자리를 끌어 크기를 자유롭게 줄이고 늘릴 수 있고, 옮겨 둔 위치도 기억합니다.\n메인 창, 목록관리 창, 도움말 창이 각각 따로 기억됩니다. 너무 작아지지 않도록 최소 크기는 정해져 있습니다.\n\n■ 되돌리기\n환경설정 메뉴 → '창 크기 초기화' 를 누르면 기본 크기로 돌아갑니다.\n(모니터를 바꾸는 등으로 저장된 위치가 화면 밖이 되면 자동으로 기본 위치에서 열립니다)":
            "■ Default size\nWhen first opened, it opens at a default size adjusted for your display scaling (125%, 150%, etc.), so it looks the same on any computer.\n\n■ Resize freely\nYou can drag the window edges to make it smaller or larger, and the position you move it to is remembered.\nThe main window, Manage list window, and Help window are remembered separately. A minimum size is set so they cannot become too small.\n\n■ Reset\nChoose Settings menu → 'Reset window size' to return to the default size.\n(If a saved position ends up off-screen, for example after changing monitors, the window opens at the default position automatically.)",
        "■ 메인 창\nF1          도움말\nF5          브라우저 주소 지금 가져오기\nCtrl+N      사이트 추가\nCtrl+F      검색창 열기/닫기 (설명·주소·키워드·아이디로 전체 검색, Esc 로 닫기)\nEnter       (주소 칸에서) 사이트 열기\n더블클릭    (아이디/비밀번호 값) 복사 · (목록의 사이트) 열기\n끌어서 놓기 (메인 목록) 사이트·그룹을 다른 그룹 위에 끌어 이동\nCtrl+A      (목록관리 창) 사이트 전체 선택\n오른쪽 클릭 (값/목록) 메뉴\n\n■ 로그인 창\nEnter / Alt+O   확인\nAlt+C           취소\nAlt+N           새 사용자\n\n■ 모든 창\nEsc             창 닫기(취소)":
            "■ Main window\nF1          Help\nF5          Get browser address now\nCtrl+N      Add site\nCtrl+F      Open/close search (search all sites by name·URL·keyword·ID, Esc to close)\nEnter       (in the address field) Open site\nDouble-click    (ID/password value) Copy · (site in list) Open\nDrag and drop (main list) Drag a site or group onto another group to move it\nCtrl+A      (Manage list window) Select all sites\nRight-click (value/list) Menu\n\n■ Login window\nEnter / Alt+O   OK\nAlt+C           Cancel\nAlt+N           New user\n\n■ All windows\nEsc             Close window (cancel)",
        "■ 어떻게 보호되나요?\n· 모든 정보는 AES-256-GCM 으로 암호화되어 저장됩니다.\n· 마스터 비밀번호에서 암호화 키를 만들 때 scrypt 방식을 써서 비밀번호 대입 공격을 어렵게 합니다.\n· 정보는 이 컴퓨터(data 폴더)에만 저장되고, 인터넷으로 전송되지 않습니다.\n· 인터넷은 업데이트 확인(GitHub 에서 최신 버전 번호 조회)에만 쓰이며, 저장된 정보는 전혀 보내지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ How is it protected?\n· All information is encrypted with AES-256-GCM and then stored.\n· scrypt is used to derive the encryption key from the master password, which makes password guessing attacks difficult.\n· Information is stored only on this computer (data folder) and is never sent over the internet.\n· The internet is used only to check for updates (looking up the latest version number on GitHub); no stored information is ever sent.\n\n■ Automatic protection\n· After 10 minutes of inactivity, it returns to the login window.\n· A copied password is cleared from the clipboard after 20 seconds.\n· Passwords are masked as ●●● on screen by default.\n· If you enter the wrong password 5 times at login, the program closes.\n\n■ Things to note\n· The master password cannot be recovered. Write it down and keep it somewhere safe.\n· If this computer is infected with a virus, no password manager is safe. Keep your antivirus up to date.\n· On a shared computer, be sure to exit after use.",
        "■ 자동 백업 (아무것도 안 해도 됩니다)\n· 로그인할 때마다 data\\backup 폴더에 '아이디_날짜.mpbak' 사본이 만들어집니다. (하루 1개, 최근 10개 보관)\n· 저장할 때마다 같은 폴더에 '아이디.dat.bak' (직전 상태)도 만들어집니다.\n\n■ 직접 백업\n파일 메뉴 '백업 만들기' → 원하는 위치(USB, 클라우드 폴더 등)에 저장합니다.\n백업 파일은 암호화되어 있어 남이 열어볼 수 없습니다.\n\n■ 복원\n· 로그인한 뒤 파일 메뉴 '백업에서 복원' (로그인 창에는 복원 버튼이 없습니다)\n· 새 컴퓨터라면: 로그인 창에서 [새 사용자]로 임시 사용자를 만들어 로그인 → '백업에서 복원' →\n   복원이 끝나면 '다른 사용자로 로그인'으로 복원한 사용자에 들어갑니다. (임시 사용자는 '현재 사용자 삭제'로 정리)\n· 백업 파일 선택 → 백업 당시의 마스터 비밀번호 입력 → 복원할 아이디 입력\n· 같은 아이디가 있으면 덮어쓸지 묻고, 기존 파일은 data\\_deleted 에 보관됩니다.\n· 복원 후에는 백업 당시의 마스터 비밀번호로 로그인합니다.\n\n■ 백업 위치 (내가 정한 폴더에 자동 백업)\n· 파일 메뉴 '백업 위치 설정'에서 백업을 저장할 폴더를 지정합니다. 로그인할 때, 정보를 바꾼 뒤, 종료할 때\n   그 폴더의 MyPass_backup 안에 자동으로 백업합니다. (위의 data\\backup 자동 백업과는 별개입니다)\n· 폴더는 어디든 됩니다: 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS),\n   또는 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더. [클라우드 찾기]로 흔한 클라우드 폴더를 찾을 수 있습니다.\n· 클라우드에 직접 로그인하지 않습니다. 이 컴퓨터에 클라우드 프로그램이 설치·로그인되어 있어야 하며, 올리는 일은 그 프로그램이 합니다.\n· 프로그램 데이터와 같은 드라이브(같은 USB)를 고르면 함께 사라질 수 있다고 알려 줍니다. 다른 장치를 권장합니다.\n· 경로에 %USERPROFILE%\\OneDrive 처럼 환경변수를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.\n· 기본은 '암호화 백업(.mpbak)'입니다. 마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 되살립니다.\n   (아이디_latest.mpbak = 최신본, 아이디_날짜.mpbak = 날짜별 사본)\n· 'CSV' 형식도 고를 수 있지만 암호화되지 않아 비밀번호가 글자 그대로 저장됩니다. 꼭 필요할 때만 쓰세요.\n   (아이디_latest.csv 한 파일만 덮어쓰며, 되살릴 때는 'CSV 가져오기'를 사용)\n· 설정한 폴더가 그 컴퓨터에 없으면(다른 PC, USB 미연결 등) 백업을 건너뛰고 상태줄에 알려 줍니다.\n· [지금 백업] 또는 파일 메뉴 '지금 백업 위치에 백업'으로 바로 실행할 수 있고, 마지막 결과는 설정 창에 표시됩니다.\n· 이 설정은 모든 사용자에게 공통이며, 백업 파일 이름에 사용자 아이디가 들어갑니다.\n\n■ 권장 습관\n중요한 정보라면 가끔 '백업 만들기'로 다른 저장 장치에도 사본을 두세요.\n컴퓨터가 고장 나면 data 폴더도 함께 사라집니다.":
            "■ Automatic backup (you don't need to do anything)\n· Each time you log in, a copy named 'ID_date.mpbak' is created in the data\\backup folder. (One per day, the latest 10 are kept)\n· Each time you save, 'ID.dat.bak' (the previous state) is also created in the same folder.\n\n■ Manual backup\nFile menu 'Create backup' → save to a location you choose (USB, cloud folder, etc.).\nBackup files are encrypted, so no one else can open them.\n\n■ Restore\n· After logging in, File menu 'Restore from backup' (the login window has no restore button)\n· On a new computer: create a temporary user with [New user] in the login window and log in → 'Restore from backup' →\n   when the restore finishes, use 'Log in as another user' to enter the restored user. (Clean up the temporary user with 'Delete current user'.)\n· Select the backup file → enter the master password from when the backup was made → enter the user ID to restore\n· If the same ID exists, you are asked whether to overwrite it, and the existing file is kept in data\\_deleted.\n· After restoring, log in with the master password from when the backup was made.\n\n■ Backup location (automatic backup to a folder you choose)\n· In File menu 'Set backup location', specify the folder where backups are saved. On login, after changing information, and on exit,\n   backups are made automatically inside MyPass_backup in that folder. (This is separate from the data\\backup automatic backup above.)\n· Any folder works: another drive, an external hard drive or USB, a network drive (NAS),\n   or a cloud sync folder such as OneDrive, Google Drive, Dropbox, or Naver MYBOX. [Find cloud] can locate common cloud folders.\n· It does not log in to the cloud directly. The cloud program must be installed and logged in on this computer, and that program does the uploading.\n· If you choose the same drive (or the same USB) as the program data, you are warned that both could be lost together. A different device is recommended.\n· If you use an environment variable in the path, such as %USERPROFILE%\\OneDrive, you only need to set it once even if the user name differs on each computer.\n· The default is 'Encrypted backup (.mpbak)'. It cannot be opened without the master password, and you restore it with 'Restore from backup'.\n   (ID_latest.mpbak = latest copy, ID_date.mpbak = copy by date)\n· You can also choose the 'CSV' format, but it is not encrypted and passwords are saved as plain text. Use it only when truly necessary.\n   (Only one file, ID_latest.csv, is overwritten; to restore, use 'Import CSV'.)\n· If the configured folder does not exist on that computer (another PC, USB not connected, etc.), the backup is skipped and the status bar tells you.\n· You can run it immediately with [Back up now] or File menu 'Back up to backup location now', and the last result is shown in the settings window.\n· This setting is common to all users, and the user ID is included in the backup file name.\n\n■ Recommended habit\nFor important information, occasionally keep a copy on another storage device with 'Create backup'.\nIf the computer breaks, the data folder disappears with it.",
        "■ 처음 사용할 때\n1. 프로그램을 실행하면 로그인 창이 나옵니다. [새 사용자(N)]를 눌러 아이디와 마스터 비밀번호를 등록합니다.\n2. 등록한 아이디와 비밀번호로 로그인합니다.\n3. 메인 창의 [추가] 버튼으로 자주 쓰는 사이트의 주소, 아이디, 비밀번호를 저장합니다.\n\n■ 마스터 비밀번호란?\n저장한 모든 정보를 잠그는 열쇠입니다. 8자 이상으로 정하고 꼭 기억해 두세요.\n잊어버리면 누구도 복구할 수 없습니다. (프로그램 제작자도 마찬가지입니다)\n\n■ 화면 구성\n· 위쪽 버튼: 목록관리 / 추가(▾ 메뉴) / 수정 / 삭제\n· 주소 칸: 주소를 입력하거나 브라우저에서 자동으로 가져옵니다.\n   ➜ 사이트 열기,  ↻ 브라우저 주소 지금 가져오기\n· 사이트 정보 표시줄: 저장된 정보가 있으면 초록 ✔, 없으면 회색 표시\n· 아이디·비밀번호 칸과 [채움] 버튼\n· 아래 목록: 그룹과 저장된 사이트 (끌어서 그룹으로 이동)\n· 맨 아래 상태줄: 현재 로그인한 사용자와 안내 메시지":
            "■ First-time use\n1. When you run the program, the login window appears. Click [New user(N)] to register an ID and master password.\n2. Log in with the ID and password you registered.\n3. Use the [Add] button in the main window to save the address, ID, and password of sites you use often.\n\n■ What is the master password?\nIt is the key that locks all the information you save. Choose at least 8 characters and be sure to remember it.\nIf you forget it, no one can recover it. (This includes the program's creator.)\n\n■ Screen layout\n· Top buttons: Manage list / Add (▾ menu) / Edit / Delete\n· Address field: type an address or get it automatically from the browser.\n   ➜ Open site,  ↻ Get browser address now\n· Site information bar: green ✔ if saved information exists, gray if not\n· ID and password fields and the [Fill] button\n· List below: groups and saved sites (drag to move into a group)\n· Status bar at the bottom: the current logged-in user and messages",
        "■ 추가\n[추가] 버튼 → 주소, 아이디, 비밀번호를 입력하고 [확인].\n· 주소 칸에 이미 주소가 들어 있으면 그 주소로 창이 열립니다.\n· [추가] 옆 ▾ 에서 '빈 사이트 추가', '그룹 추가'도 고를 수 있습니다.\n· 비밀번호 옆 [생성] 버튼은 16자리 무작위 비밀번호를 만들어 줍니다. [보기]로 확인하세요.\n· 가입할 때 쓴 비밀번호를 그대로 저장하세요. 생성한 비밀번호는 사이트에도 같이 바꿔 주어야 합니다.\n\n■ 수정 / 삭제\n· 목록에서 사이트를 고르고 [수정] 또는 [삭제].\n· 목록의 사이트를 더블클릭하면 주소가 채워지고 사이트가 열립니다.\n· 목록에서 오른쪽 클릭하면 사이트 열기 / 수정 / 삭제 메뉴가 나옵니다.\n\n■ 같은 사이트에 계정이 여러 개일 때\n같은 주소로 사이트를 여러 개 저장하면, 주소가 맞을 때 주소 칸 아래 작은 목록에 모두 나타납니다. 쓸 계정을 고르세요.":
            "■ Add\n[Add] button → enter the address, ID, and password, then click [OK].\n· If the address field already contains an address, the window opens with that address.\n· From the ▾ next to [Add], you can also choose 'Add empty site' and 'Add group'.\n· The [Generate] button next to the password creates a random 16-character password. Check it with [Show].\n· Save the same password you used when signing up. If you use a generated password, you must change it on the site as well.\n\n■ Edit / Delete\n· Select a site in the list, then click [Edit] or [Delete].\n· Double-click a site in the list to fill in its address and open the site.\n· Right-click in the list for the Open site / Edit / Delete menu.\n\n■ When one site has several accounts\nIf you save several sites with the same address, all of them appear in the small list under the address field when the address matches. Choose the account to use.",
        "⚠ 모든 아이디·비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다. 엑셀로 바로 열어 볼 수 있다는 점이 장점입니다.":
            "⚠ All IDs and passwords are saved as plain text. If that folder is in the cloud or visible to others, everything is exposed. The advantage is that it can be opened directly in Excel.",
        "✎ 수정":
            "✎ Edit",
        "✔ 성공":
            "✔ Success",
        "✕ 삭제":
            "✕ Delete",
        "✖ 실패":
            "✖ Failed",
        "값을 더블클릭하면 복사됩니다 · 오른쪽 클릭: 메뉴":
            "Double-click a value to copy it · Right-click: menu",
        "개 (암호화 백업만 · 최신본은 항상 따로 저장)":
            " (encrypted backups only · the latest copy is always saved separately)",
        "검색":
            "Search",
        "관리(T)":
            "Manage(T)",
        "그룹":
            "Group",
        "그룹 '{0}' 을(를) 넣을 그룹을 고르세요.":
            "Choose the group to put group '{0}' into.",
        "그룹 삭제":
            "Delete group",
        "그룹 이름":
            "Group name",
        "그룹 이름 변경":
            "Rename group",
        "그룹 이름:":
            "Group name:",
        "그룹 이름을 입력하세요.":
            "Enter a group name.",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.":
            "The group name is empty, or a group with the same name already exists.",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)":
            "The group name is empty, or a group with the same name already exists.\n(The characters / \\ cannot be used.)",
        "그룹 추가":
            "Add group",
        "그룹과 목록관리":
            "Groups and Manage list",
        "그룹과 하위 그룹을 삭제합니다.\n안에 있던 사이트 정보는 상위 그룹으로 옮겨집니다.\n(사이트는 지워지지 않습니다) 계속할까요?":
            "This deletes the group and its subgroups.\nThe site information inside is moved to the parent group.\n(Sites are not deleted.) Continue?",
        "그룹명":
            "Group name",
        "그룹으로 이동":
            "Move to group",
        "그룹으로 이동...":
            "Move to group...",
        "나중에":
            "Later",
        "날짜별 사본 보관:":
            "Keep copies by date:",
        "내 드라이브":
            "My Drive",
        "내보내기 완료":
            "Export complete",
        "내보낸 CSV는 암호화되지 않습니다.\n사용 후 반드시 안전하게 삭제하세요.\n계속할까요?":
            "The exported CSV is not encrypted.\nBe sure to delete it securely after use.\nContinue?",
        "다른 그룹 안으로 이동":
            "Move into another group",
        "다른 사용자로 로그인":
            "Log in as another user",
        "로그아웃":
            "Log out",
        "자동 잠금 시간":
            "Auto-lock time",
        "자동 잠금 시간을 바꿨습니다: {0}":
            "Changed auto-lock time: {0}",
        "5분":
            "5 minutes",
        "10분":
            "10 minutes",
        "15분":
            "15 minutes",
        "30분":
            "30 minutes",
        "사용 안 함":
            "Off",
        "다운로드 페이지 열기":
            "Open download page",
        "다운로드 페이지에서 새 exe 를 받아, 지금 쓰는 exe 파일만 바꿔 넣으세요. data 폴더는 그대로 두면 정보가 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "Download the new exe from the download page and just replace the exe file you are using. If you leave the data folder as it is, your information is kept. (Using 'Create backup' before replacing is recommended.)",
        "다음 주소에 대한 사이트 정보를 수정합니다.":
            "Edit the site information for the following address.",
        "다음 주소에 대한 사이트 정보를 추가합니다.":
            "Add site information for the following address.",
        "단축키":
            "Shortcuts",
        "닫기":
            "Close",
        "데이터 폴더 열기":
            "Open data folder",
        "도움말(H)":
            "Help(H)",
        "등록되었습니다. 비밀번호를 입력하고 로그인하세요.":
            "Registered. Enter your password and log in.",
        "등록되지 않은 아이디입니다.\n[새 사용자]로 먼저 등록하세요.":
            "This ID is not registered.\nRegister it first with [New user].",
        "로그인":
            "Log in",
        "로그인할 때 하루 한 번 자동으로 확인":
            "Check once a day automatically at login",
        "마스터 비밀번호 변경":
            "Change master password",
        "마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 바로 되살릴 수 있습니다.":
            "It cannot be opened without the master password, and you can restore it right away with 'Restore from backup'.",
        "마이패스 백업":
            "MyPass backup",
        "마지막 백업: {0}  {1}\n{2}":
            "Last backup: {0}  {1}\n{2}",
        "모두 접기":
            "Collapse all",
        "모두 펼치기":
            "Expand all",
        "모든 그룹 접기":
            "Collapse all groups",
        "모든 그룹 펼치기":
            "Expand all groups",
        "모든 파일":
            "All files",
        "목록관리":
            "Manage list",
        "묶을 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "Select the sites to group first. (Select several with Ctrl/Shift.)",
        "백업 만들기...":
            "Create backup...",
        "백업 완료: {0}":
            "Backup complete: {0}",
        "백업 위치 백업 실패: {0}":
            "Backup to backup location failed: {0}",
        "백업 위치 설정...":
            "Set backup location...",
        "백업 위치 자동 백업을 껐습니다.":
            "Automatic backup to the backup location is turned off.",
        "백업 위치 자동 백업을 켰습니다. 지금 백업하는 중...":
            "Automatic backup to the backup location is turned on. Backing up now...",
        "백업 위치가 지정되지 않았습니다.":
            "No backup location has been specified.",
        "백업 위치로 자동 백업 사용":
            "Use automatic backup to the backup location",
        "백업 위치에 백업 완료 ({0})":
            "Backup to backup location complete ({0})",
        "백업 파일 저장":
            "Save backup file",
        "백업 파일을 자동으로 저장할 폴더를 정하세요. 이 컴퓨터의 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS)는 물론 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더도 됩니다.\n(클라우드는 계정에 직접 로그인하지 않으며, 이 컴퓨터의 클라우드 프로그램이 파일을 올려 줍니다)":
            "Choose the folder where backup files are saved automatically. It can be another drive on this computer, an external hard drive or USB, a network drive (NAS), or a cloud sync folder such as OneDrive, Google Drive, Dropbox, or Naver MYBOX.\n(For the cloud, you do not log in to the account directly; the cloud program on this computer uploads the files.)",
        "백업 폴더":
            "Backup folder",
        "백업 폴더 선택":
            "Select backup folder",
        "백업 폴더를 지정하세요.":
            "Specify a backup folder.",
        "백업 폴더를 찾을 수 없습니다. (드라이브·USB·클라우드 프로그램이 연결되어 있지 않거나, 이 컴퓨터에 없는 경로)":
            "The backup folder could not be found. (The drive, USB, or cloud program is not connected, or the path does not exist on this computer.)",
        "백업 폴더에 예전에 저장해 둔 CSV 파일(암호화 안 됨)이 남아 있습니다.\n지금 삭제할까요?\n\n{0}":
            "The backup folder contains CSV files (not encrypted) saved earlier.\nDelete them now?\n\n{0}",
        "백업 형식":
            "Backup format",
        "백업과 복원":
            "Backup and restore",
        "백업에서 복원...":
            "Restore from backup...",
        "백업하지 못했습니다.\n{0}":
            "Could not back up.\n{0}",
        "백업하지 못했습니다: {0}":
            "Could not back up: {0}",
        "백업했습니다.\n백업 파일은 암호화되어 있으며, 복원할 때 지금의 마스터 비밀번호가 필요합니다.":
            "Backup complete.\nThe backup file is encrypted, and your current master password is required to restore it.",
        "변경":
            "Change",
        "보관함 파일이 올바르지 않아 백업하지 않았습니다.":
            "The vault file is invalid, so no backup was made.",
        "보관함을 열 수 없습니다.\n{0}":
            "Cannot open the vault.\n{0}",
        "보기":
            "Show",
        "보안 안내":
            "Security notice",
        "복원하지 못했습니다.\n{0}":
            "Could not restore.\n{0}",
        "복원할 백업 파일 선택":
            "Select the backup file to restore",
        "복원할 사용자 아이디:":
            "User ID to restore:",
        "복원했습니다.\n아이디 '{0}' 와(과) 백업 당시의 마스터 비밀번호로 로그인하세요.":
            "Restored.\nLog in with ID '{0}' and the master password from when the backup was made.",
        "브라우저 주소 가져오기":
            "Get browser address",
        "브라우저 주소 연동":
            "Browser address link",
        "브라우저 주소 연동은 Windows에서만 사용할 수 있습니다.":
            "Browser address link is available only on Windows.",
        "브라우저 주소 연동을 사용할 수 없습니다.":
            "Browser address link is not available.",
        "브라우저 주소 연동을 사용할 수 없습니다.\n(Windows 전용이며 uiautomation 구성 요소가 필요합니다)":
            "Browser address link is not available.\n(It is Windows-only and requires the uiautomation component.)",
        "브라우저 주소 연동을 사용할 수 없습니다. (uiautomation 구성 요소 없음)":
            "Browser address link is not available. (uiautomation component missing)",
        "브라우저 주소 자동 연동":
            "Auto-link browser address",
        "브라우저 주소 지금 가져오기\tF5":
            "Get browser address now\tF5",
        "브라우저 주소: {0}":
            "Browser address: {0}",
        "브라우저 주소를 읽는 중 오류가 났습니다.":
            "An error occurred while reading the browser address.",
        "브라우저 주소를 읽지 못했습니다.":
            "Could not read the browser address.",
        "브라우저 주소를 읽지 못했습니다. (검색어 입력 중이거나 지원하지 않는 화면)":
            "Could not read the browser address. (You may be typing a search term, or the screen is not supported.)",
        "브라우저 주소창의 주소를 자동으로 읽어 주소 칸에 넣어 줍니다. (Windows 전용)\n브라우저에서 사이트를 이동할 때마다 저장된 정보가 자동으로 나타납니다.\n\n■ 지원 브라우저\n크롬, 엣지, 웨일, 파이어폭스, 브레이브, 오페라, 비발디 등\n\n■ 사용법\n· 환경설정 메뉴의 '브라우저 주소 자동 연동' 이 켜져 있으면 자동으로 동작합니다.\n· 마이패스 창을 브라우저 옆에 두고 '항상 위에 표시' 를 켜면 가장 편합니다.\n· 바로 읽고 싶으면 ↻ 버튼 또는 F5 키를 누르세요. (직전에 사용한 브라우저에서 읽어옵니다)\n\n■ 참고\n· 마이패스 창을 클릭해도 마지막으로 읽은 주소는 그대로 유지됩니다.\n· 주소창에 검색어를 입력 중이거나, chrome:// 같은 내부 페이지는 읽지 않습니다.\n· 읽히지 않는 브라우저는 주소를 복사(Ctrl+L, Ctrl+C)해서 주소 칸에 붙여넣으세요.\n· 주소는 이 컴퓨터 안에서만 읽히며 어디로도 전송되지 않습니다.":
            "Automatically reads the address from the browser's address bar and puts it in the address field. (Windows only)\nWhenever you navigate to a site in the browser, the saved information appears automatically.\n\n■ Supported browsers\nChrome, Edge, Whale, Firefox, Brave, Opera, Vivaldi, etc.\n\n■ How to use\n· It works automatically when 'Auto-link browser address' in the Settings menu is turned on.\n· It is most convenient to place the MyPass window next to the browser and turn on 'Always on top'.\n· To read it right away, click the ↻ button or press F5. (It reads from the browser you used most recently.)\n\n■ Notes\n· Even if you click the MyPass window, the last address read is kept.\n· It does not read while you are typing a search term in the address bar, or from internal pages such as chrome://.\n· For browsers that cannot be read, copy the address (Ctrl+L, Ctrl+C) and paste it into the address field.\n· The address is read only inside this computer and is never sent anywhere.",
        "브라우저에서 주소를 읽는 중...":
            "Reading the address from the browser...",
        "비밀번호":
            "Password",
        "비밀번호 보기":
            "Show password",
        "비밀번호 복사":
            "Copy password",
        "비밀번호 숨기기":
            "Hide password",
        "비밀번호 확인":
            "Confirm password",
        "비밀번호(이 OS에서는 자동 채움 미지원)":
            "Password (auto Fill is not supported on this OS)",
        "비밀번호가 변경되었습니다.":
            "Password changed.",
        "비밀번호가 일치하지 않습니다.":
            "Passwords do not match.",
        "비밀번호가 틀렸거나 손상된 백업 파일입니다.":
            "Wrong password or the backup file is corrupted.",
        "비밀번호가 틀렸습니다.":
            "Wrong password.",
        "비밀번호는 8자 이상 입력하세요.":
            "Enter a password of at least 8 characters.",
        "비밀번호를 5회 틀려 종료합니다.":
            "Exiting because the password was wrong 5 times.",
        "빈 사이트 추가":
            "Add empty site",
        "사용법\tF1":
            "How to use\tF1",
        "사용자 '{0}' 를 등록했습니다.\n지금 이 사용자로 로그인할까요?":
            "User '{0}' was registered.\nLog in as this user now?",
        "사용자 '{0}' 를 삭제했습니다.\n(data\\_deleted 폴더에 보관됨)":
            "User '{0}' was deleted.\n(Kept in the data\\_deleted folder)",
        "사용자 '{0}' 와(과) 저장된 모든 사이트 정보를 삭제합니다.\n\n파일은 data\\_deleted 폴더로 옮겨지며, 필요하면 그곳에서 되살릴 수 있습니다.\n계속할까요?":
            "This will delete user '{0}' and all saved site information.\n\nThe file is moved to the data\\_deleted folder, where you can restore it if needed.\nContinue?",
        "사용자 추가·전환·삭제":
            "Add, switch, and delete users",
        "사용자를 만들 수 없습니다.\n{0}":
            "Cannot create the user.\n{0}",
        "사용할 수 없는 그룹 이름입니다.":
            "This group name cannot be used.",
        "사용할 수 없는 그룹 이름입니다.\n(같은 위치에 같은 이름의 그룹이 있거나, / \\ 문자가 들어 있습니다)":
            "This group name cannot be used.\n(A group with the same name exists in the same location, or it contains the characters / \\.)",
        "사이트 {0}개":
            "{0} sites",
        "사이트 설명":
            "Site description",
        "사이트 열기":
            "Open site",
        "사이트 정보가 없습니다.":
            "There is no site information.",
        "사이트 정보가 있습니다.  [{0}]":
            "Site information found.  [{0}]",
        "사이트 추가":
            "Add site",
        "사이트 추가\tCtrl+N":
            "Add site\tCtrl+N",
        "사이트 추가·수정·삭제":
            "Add, edit, and delete sites",
        "사이트가 많아지면 그룹으로 묶어서 정리할 수 있습니다. 그룹 안에 그룹을 만들 수도 있습니다. (예: 업무 ▸ 은행)\n\n■ 그룹 만들기\n· 메인 목록에서 오른쪽 클릭 → '그룹 추가' / '하위 그룹 추가'\n· 사이트 추가 창의 '그룹명' 옆 [새 그룹] 버튼으로 바로 만들 수 있습니다.\n\n■ 사이트를 그룹으로 옮기기 (3가지 방법)\n1. 끌어서 놓기: 메인 목록에서 사이트를 마우스로 끌어 원하는 그룹 위에 놓습니다.\n   (그룹을 다른 그룹 위에 놓으면 그 안으로 들어갑니다. 놓을 수 있는 곳은 파란색으로 표시됩니다)\n2. 사이트에서 오른쪽 클릭 → '그룹으로 이동' 에서 그룹을 고릅니다.\n3. 사이트 [수정] → '그룹명'을 바꿉니다.\n\n■ 여러 개를 한꺼번에 묶기\n[목록관리] 창에서 Ctrl 또는 Shift 를 누른 채 사이트를 여러 개 고른 다음 오른쪽 클릭\n· '새 그룹으로 묶기': 새 그룹을 만들면서 한 번에 담기\n· '그룹으로 이동': 이미 있는 그룹으로 한 번에 옮기기\n\n■ 그룹 관리\n· 이름 변경 / 다른 그룹 안으로 이동 / 삭제: 메인 목록의 오른쪽 클릭 메뉴, 또는 [목록관리] 창에서\n   그룹 오른쪽의 [수정]을 눌러 팝업에서 바꿉니다.\n· 그룹 이름 옆 숫자는 안에 든 사이트 수(하위 그룹 포함)입니다.\n· 그룹을 삭제해도 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.\n· 맨 위 '최상위' 또는 관리 메뉴에서 '모두 펼치기 / 모두 접기'를 할 수 있습니다.\n\n■ 목록관리 창 (관리대장)\n· 왼쪽: 그룹 목록 / 오른쪽: 선택한 그룹의 사이트 목록\n· 각 줄 오른쪽의 [수정]을 누르면 팝업이 열립니다. 사이트는 설명·주소·아이디·비밀번호·그룹(경로)을,\n   그룹은 이름과 위치(어느 그룹 안에 둘지)를 바꿀 수 있습니다. 사이트 줄의 [삭제]는 그 사이트를 지웁니다.\n· 위쪽: [사이트 추가] [그룹 추가], 검색칸 (사이트 설명, 주소, 키워드, 아이디로 전체 검색 · 검색 중에는 모든 그룹에서 찾음)\n· 사이트를 여러 개 골라 오른쪽 클릭: 비밀번호 복사 / 그룹으로 이동 / 새 그룹으로 묶기 / 삭제 (Ctrl+A 로 전체 선택)":
            "When you have many sites, you can organize them into groups. You can also create groups inside groups. (Example: Work ▸ Bank)\n\n■ Creating groups\n· In the main list, right-click → 'Add group' / 'Add subgroup'\n· You can also create one right away with the [New group] button next to 'Group name' in the Add site window.\n\n■ Moving sites into a group (3 ways)\n1. Drag and drop: drag a site with the mouse in the main list and drop it onto the group you want.\n   (If you drop a group onto another group, it goes inside it. Places where you can drop are highlighted in blue.)\n2. Right-click a site → choose a group from 'Move to group'.\n3. Site [Edit] → change the 'Group name'.\n\n■ Grouping several at once\nIn the [Manage list] window, hold Ctrl or Shift and select several sites, then right-click\n· 'Group into new group': create a new group and put them all in at once\n· 'Move to group': move them all at once to an existing group\n\n■ Managing groups\n· Rename / move into another group / delete: from the right-click menu in the main list, or in the [Manage list] window,\n   click [Edit] to the right of the group and change it in the popup.\n· The number next to a group name is the number of sites inside it (including subgroups).\n· Deleting a group does not delete its sites; they are moved to the parent group.\n· You can use 'Expand all / Collapse all' from the 'Top level' at the top or from the Manage menu.\n\n■ Manage list window (register)\n· Left: group list / Right: site list of the selected group\n· Each row's [Edit] on the right opens a popup. For a site, you can change the description, address, ID, password, and group (path);\n   for a group, the name and location (which group to put it in). [Delete] on a site row deletes that site.\n· Top: [Add site] [Add group], and a search box (searches all by site description, address, keyword, and ID · while searching, all groups are searched)\n· Select several sites and right-click: Copy password / Move to group / Group into new group / Delete (select all with Ctrl+A)",
        "사이트를 먼저 선택하세요.":
            "Select a site first.",
        "삭제":
            "Delete",
        "삭제하지 못했습니다.\n{0}":
            "Could not delete.\n{0}",
        "삭제할 그룹을 선택하세요.":
            "Select the group to delete.",
        "삭제할 사용자를 먼저 선택하세요.":
            "Select the user to delete first.",
        "삭제할 사이트를 먼저 선택하세요.":
            "Select the site to delete first.",
        "새 그룹":
            "New group",
        "새 그룹 이름:":
            "New group name:",
        "새 그룹으로 묶기...":
            "Group into new group...",
        "새 버전 {0} 이(가) 있습니다. (업데이트 메뉴 → 업데이트 확인)":
            "New version {0} is available. (Update menu → Check for updates)",
        "새 버전이 있습니다: {0}   (현재 v{1})":
            "A new version is available: {0}   (current v{1})",
        "새 비밀번호 (8자 이상):":
            "New password (at least 8 characters):",
        "새 비밀번호 확인:":
            "Confirm new password:",
        "새 사용자 추가...":
            "Add new user...",
        "새 사용자(N)":
            "New user(N)",
        "생성":
            "Generate",
        "선택한 사이트 {0}개를":
            "{0} selected sites",
        "선택한 사이트 {0}개를 묶을 새 그룹 이름:\n('{1}' 안에 만들어집니다)":
            "New group name for the {0} selected sites:\n(It will be created inside '{1}')",
        "선택한 사이트 {0}개를 옮길 그룹을 고르세요.":
            "Choose the group to move the {0} selected sites to.",
        "선택한 폴더 안에 '{0}' 폴더를 만들어 저장합니다.":
            "A '{0}' folder will be created inside the selected folder to save backups.",
        "설정":
            "Settings",
        "수정":
            "Edit",
        "수정 (이름·위치)":
            "Edit (name·location)",
        "수정할 사이트를 먼저 선택하세요.":
            "Select the site to edit first.",
        "시작하기":
            "Get started",
        "실제 저장 위치: {0}":
            "Actual save location: {0}",
        "아이디":
            "ID",
        "아이디 기억(A)":
            "Remember ID(A)",
        "아이디 복사":
            "Copy ID",
        "아이디가 일치하지 않아 삭제를 취소했습니다.":
            "The ID did not match, so the deletion was canceled.",
        "아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요.":
            "Use only Korean, English letters, numbers, and _ . - for the ID, within 32 characters.",
        "아이디와 비밀번호를 입력해 주세요.":
            "Enter your ID and password.",
        "아직 백업 위치가 설정되지 않았습니다.\n지금 설정할까요?":
            "No backup location has been set yet.\nSet it now?",
        "아직 백업 위치로 백업한 기록이 없습니다.":
            "There is no record of a backup to the backup location yet.",
        "암호화 백업 (.mpbak) — 권장":
            "Encrypted backup (.mpbak) — recommended",
        "언어 (Language)":
            "Language",
        "언어를 바꿨습니다: {0}":
            "Language changed: {0}",
        "업데이트 서버 오류 ({0})":
            "Update server error ({0})",
        "업데이트 설정...":
            "Update settings...",
        "업데이트 확인":
            "Check for updates",
        "업데이트(U)":
            "Update(U)",
        "업데이트를 확인하는 중...":
            "Checking for updates...",
        "업데이트를 확인할 GitHub 저장소가 설정되어 있지 않습니다.\nmypass.py 맨 위의 UPDATE_REPO 에 '계정/저장소'를 넣고 다시 만드세요.":
            "No GitHub repository is set for checking updates.\nEnter 'account/repository' in UPDATE_REPO at the top of mypass.py and rebuild.",
        "여기에 사이트 추가":
            "Add site here",
        "여러 개 선택(Ctrl/Shift) 후 오른쪽 클릭: 이동 · 묶기 · 삭제":
            "Select several (Ctrl/Shift) and right-click: move · group · delete",
        "연동할 브라우저 창을 찾지 못했습니다. 브라우저를 한 번 사용한 뒤 다시 눌러 보세요.":
            "Could not find a browser window to link. Use the browser once, then try again.",
        "올바른 백업 파일이 아닙니다.":
            "This is not a valid backup file.",
        "올바른 보관함 파일이 아닙니다.":
            "This is not a valid vault file.",
        "옮길 그룹을 선택하세요.":
            "Select the group to move to.",
        "옮길 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "Select the sites to move first. (Select several with Ctrl/Shift.)",
        "옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)":
            "Cannot move. (A group with the same name exists at the destination.)",
        "위치":
            "Location",
        "이 백업을 만들 당시의 마스터 비밀번호를 입력하세요:":
            "Enter the master password from when this backup was made:",
        "이 주소 키워드를 수동 사이트로 설정(M)":
            "Set this address keyword manually(M)",
        "이 폴더는 프로그램 데이터(data 폴더)와 같은 드라이브(또는 같은 USB)에 있습니다.\n그 장치가 고장 나거나 분실되면 원본과 백업이 함께 사라집니다.\n\n다른 장치(다른 드라이브·클라우드 등)의 폴더를 권장합니다.\n그래도 이 폴더를 사용할까요?":
            "This folder is on the same drive (or the same USB) as the program data (data folder).\nIf that device fails or is lost, the original and the backup disappear together.\n\nA folder on a different device (another drive, cloud, etc.) is recommended.\nUse this folder anyway?",
        "이름을 바꿀 그룹을 선택하세요.":
            "Select the group to rename.",
        "이미 '{0}' 사용자가 있습니다. 백업 내용으로 덮어쓸까요?\n(기존 파일은 data\\_deleted 폴더에 보관됩니다)":
            "User '{0}' already exists. Overwrite it with the backup contents?\n(The existing file will be kept in the data\\_deleted folder.)",
        "이미 등록된 아이디입니다.":
            "This ID is already registered.",
        "인터넷에 연결할 수 없어 확인하지 못했습니다.":
            "Could not check because there is no internet connection.",
        "일치하지 않습니다.":
            "Does not match.",
        "입력하신 정보는 암호화되어 이 컴퓨터에만\n저장되며 인터넷으로 전송되지 않습니다.\n처음이시면 [새 사용자]를 눌러 등록하세요.":
            "The information you enter is encrypted and stored\nonly on this computer; it is never sent over the internet.\nIf you are new, click [New user] to register.",
        "자동 백업 시점: 로그인할 때 · 정보를 바꾼 뒤 · 프로그램을 종료할 때":
            "Automatic backup times: at login · after changing information · when exiting the program",
        "자동 백업 폴더 열기":
            "Open automatic backup folder",
        "자주 묻는 질문":
            "Frequently asked questions",
        "저장":
            "Save",
        "저장된 아이디와 비밀번호를 브라우저의 로그인 칸에 자동으로 입력합니다. (Windows 전용)\n\n■ 사용 순서\n1. 사이트를 열어 로그인 페이지를 띄웁니다.\n2. 이 프로그램에서 해당 사이트 정보를 선택합니다. (주소가 맞으면 자동으로 선택됩니다)\n3. 브라우저의 아이디 입력칸을 클릭해 커서를 둡니다.\n4. 마이패스의 [채움] 버튼을 누릅니다.\n→ 아이디 입력 → Tab → 비밀번호 입력 순서로 자동 입력됩니다.\n\n■ 자동 로그인\n환경설정 메뉴의 '채움 후 Enter 키 입력' 을 켜면 입력 끝에 Enter 까지 눌러 줍니다.\n\n■ 안 될 때\n· 로그인 칸이 '아이디 → 비밀번호' 순서가 아니거나 중간에 다른 칸이 있으면 어긋날 수 있습니다.\n   이럴 땐 값을 더블클릭해 아이디와 비밀번호를 각각 복사해서 붙여넣으세요.\n· 아이디와 비밀번호를 따로 입력받는 사이트(2단계 로그인)도 복사해서 붙여넣는 방법을 쓰세요.\n· 비밀번호는 복사 후 20초가 지나면 클립보드에서 자동으로 지워집니다.":
            "Automatically types your saved ID and password into the browser's login fields. (Windows only)\n\n■ Steps\n1. Open the site and bring up its login page.\n2. In this program, select that site's information. (If the address matches, it is selected automatically.)\n3. Click the browser's ID field to place the cursor there.\n4. Click MyPass's [Fill] button.\n→ It types the ID → Tab → the password automatically.\n\n■ Auto login\nIf you turn on 'Press Enter after Fill' in the Settings menu, it also presses Enter at the end.\n\n■ When it doesn't work\n· If the login fields are not in 'ID → password' order or there is another field in between, the entries may be misaligned.\n   In that case, double-click the values to copy the ID and password separately and paste them.\n· For sites that ask for the ID and password separately (two-step login), also copy and paste.\n· A password is cleared automatically from the clipboard 20 seconds after copying.",
        "저장된 정보를 찾는 기준 단어입니다. 주소창의 주소 안에 이 키워드가 들어 있으면 해당 사이트 정보가 나타납니다.\n\n■ 예시\n· NAVER.COM → mail.naver.com, cafe.naver.com 등 네이버 전체에 적용\n· MAIL.NAVER.COM → 네이버 메일 주소에만 적용\n· 같은 사이트에 키워드가 둘 이상 맞으면 더 긴(구체적인) 키워드가 위에 나옵니다.\n\n■ 자동 생성\n주소를 넣으면 키워드가 자동으로 만들어집니다. (www. 는 제외, co.kr 같은 주소도 처리)\n키워드 칸의 목록에서 범위를 고를 수 있습니다.\n\n■ 직접 정하고 싶을 때\n'이 주소 키워드를 수동 사이트로 설정' 을 체크하면 키워드를 마음대로 적을 수 있습니다.":
            "This is the keyword used to find saved information. If this keyword appears in the address in the address bar, the matching site information is shown.\n\n■ Examples\n· NAVER.COM → applies to all of Naver, such as mail.naver.com and cafe.naver.com\n· MAIL.NAVER.COM → applies only to Naver Mail addresses\n· If more than one keyword matches the same site, the longer (more specific) keyword appears first.\n\n■ Automatic creation\nWhen you enter an address, the keyword is created automatically. (www. is excluded, and addresses like co.kr are handled.)\nYou can choose the scope from the list in the keyword field.\n\n■ When you want to set it yourself\nCheck 'Set this address keyword manually' to type the keyword freely.",
        "저장소 이름을 '계정/저장소' 형식으로 입력하세요.":
            "Enter the repository name in 'account/repository' format.",
        "저장소 주소는 프로그램(mypass.py 맨 위 UPDATE_REPO)에 미리 넣어 두는 값을 씁니다. 비공개 저장소일 때만 'Fine-grained 토큰(이 저장소 하나, Contents: Read-only)'을 입력하세요. 토큰은 이 컴퓨터의 data 폴더에만 저장되며 외부로 전송되지 않습니다. (data 폴더를 다른 사람과 공유하지 마세요) 공개 저장소면 비워 두세요.":
            "The repository address uses the value preset in the program (UPDATE_REPO at the top of mypass.py). Only for a private repository, enter a 'Fine-grained token (this repository only, Contents: Read-only)'. The token is kept only on this computer's data folder and is never sent anywhere else. (Don't share your data folder with anyone else.) Leave it blank for a public repository.",
        "토큰 붙여넣기":
            "Paste token here",
        "고급 설정 (비공개 저장소용 토큰)":
            "Advanced settings (token for private repos)",
        "저장소·릴리스를 찾을 수 없거나 토큰 권한이 부족합니다. (오류 {0})":
            "The repository or release was not found, or the token lacks permission. (Error {0})",
        "저장소·릴리스를 찾을 수 없습니다. (오류 {0})\n비공개(private) 저장소라면 읽기 전용 토큰이 필요합니다.":
            "The repository or release was not found. (Error {0})\nA read-only token is required for a private repository.",
        "저장하지 못했습니다.\n{0}":
            "Could not save.\n{0}",
        "정보":
            "About",
        "종료":
            "Exit",
        "주소":
            "Address",
        "주소 키워드":
            "Address keyword",
        "주소 키워드가 비어 있습니다.\n주소를 확인하거나 수동으로 입력하세요.":
            "The address keyword is empty.\nCheck the address or enter it manually.",
        "주소 키워드는 저장된 로그인 정보를 찾는 기준입니다.\n주소창의 주소에 이 키워드가 들어 있으면 이 사이트 정보가 표시됩니다.\n\n예) NAVER.COM → mail.naver.com, cafe.naver.com 모두 적용\n    MAIL.NAVER.COM → 메일 주소에만 적용\n\n'수동 사이트로 설정'을 체크하면 키워드를 직접 입력할 수 있습니다.":
            "The address keyword is the basis for finding saved login information.\nIf the address in the address bar contains this keyword, this site's information is shown.\n\nE.g. NAVER.COM → applies to both mail.naver.com and cafe.naver.com\n    MAIL.NAVER.COM → applies only to the mail address\n\nCheck 'Set manually' to enter the keyword yourself.",
        "주소 키워드란?":
            "What is an address keyword?",
        "주소를 입력하세요.":
            "Enter an address.",
        "지금 백업":
            "Back up now",
        "지금 백업 위치에 백업":
            "Back up to backup location now",
        "지정한 폴더를 찾을 수 없습니다.\n경로가 맞는지, 드라이브·USB·클라우드 프로그램이 연결되어 있는지 확인하세요.":
            "The specified folder could not be found.\nCheck that the path is correct and that the drive, USB, or cloud program is connected.",
        "창 크기 초기화":
            "Reset window size",
        "창 크기를 기본값으로 되돌렸습니다. (목록관리·도움말 창은 다음에 열 때 적용)":
            "Window size was reset to the default. (The Manage list and Help windows apply it the next time they open.)",
        "창 크기와 위치":
            "Window size and position",
        "찾아보기":
            "Browse",
        "채우는 중... 브라우저의 아이디 입력칸에 커서가 있어야 합니다.":
            "Filling... The cursor must be in the browser's ID field.",
        "채울 사이트 정보가 없습니다.":
            "There is no site information to fill in.",
        "채움":
            "Fill",
        "채움 (자동 입력)":
            "Fill (auto input)",
        "채움 후 Enter 키 입력(자동 로그인)":
            "Press Enter after Fill (auto login)",
        "최상위":
            "Top level",
        "최상위 ({0})":
            "Top level ({0})",
        "최신 버전입니다. (v{0})":
            "You are up to date. (v{0})",
        "추가":
            "Add",
        "취소":
            "Cancel",
        "취소(C)":
            "Cancel(C)",
        "클라우드 찾기":
            "Find cloud",
        "클라우드 폴더를 자동으로 찾지 못했습니다.\n[찾아보기]로 직접 고르세요.":
            "Could not find cloud folders automatically.\nChoose one yourself with [Browse].",
        "토큰 (비공개일 때만)":
            "Token (private only)",
        "토큰":
            "Token",
        "팁: %USERPROFILE%\\OneDrive 처럼 환경변수 경로를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.":
            "Tip: If you use an environment variable path such as %USERPROFILE%\\OneDrive, you only need to set it once even if the user name differs on each computer.",
        "파일(F)":
            "File(F)",
        "하위 그룹 추가":
            "Add subgroup",
        "한 컴퓨터에서 여러 사람(또는 용도별)이 각자의 보관함을 따로 쓸 수 있습니다.\n\n■ 새 사용자 추가\n· 로그인 창의 [새 사용자(N)] 또는 파일 메뉴 '새 사용자 추가'\n· 아이디와 8자 이상의 비밀번호를 정합니다. 인터넷 회원가입은 필요 없습니다.\n\n■ 다른 사용자로 로그인\n파일 메뉴 '다른 사용자로 로그인'. 사용자마다 사이트 정보가 완전히 분리됩니다.\n\n■ 사용자 삭제\n· 로그인 상태: 파일 메뉴 '현재 사용자 삭제' (마스터 비밀번호 확인 필요)\n· 보안을 위해 로그인 창에는 삭제·복원 버튼이 없습니다. 아이디나 비밀번호를 잊은 사용자는 복구할 수 없으며,\n   정리하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 직접 지우세요.\n· 안전장치: 삭제 전 확인을 거치며, 파일은 data\\_deleted 폴더로 옮겨질 뿐 지워지지 않습니다.\n   되살리려면 그 파일을 data 폴더로 옮기고 이름에서 날짜 부분(_20xxxxxx-xxxxxx)만 지우세요.\n   (예: aaa_20261009-135500.dat → aaa.dat)\n\n■ 마스터 비밀번호 변경\n파일 메뉴 '마스터 비밀번호 변경' (현재 비밀번호 확인 필요)":
            "Several people (or purposes) can each use their own separate vault on one computer.\n\n■ Add a new user\n· [New user(N)] in the login window, or File menu 'Add new user'\n· Choose an ID and a password of at least 8 characters. No internet sign-up is required.\n\n■ Log in as another user\nFile menu 'Log in as another user'. Each user's site information is completely separate.\n\n■ Delete a user\n· While logged in: File menu 'Delete current user' (master password confirmation required)\n· For security, the login window has no delete or restore buttons. A user who forgot the ID or password cannot be recovered;\n   to clean up, close the program and delete the matching 'ID.dat' file in the data folder yourself.\n· Safeguards: a confirmation is required before deletion, and the file is only moved to the data\\_deleted folder, not erased.\n   To restore it, move the file back to the data folder and remove only the date part (_20xxxxxx-xxxxxx) from the name.\n   (Example: aaa_20261009-135500.dat → aaa.dat)\n\n■ Change master password\nFile menu 'Change master password' (current password confirmation required)",
        "항상 위에 표시":
            "Always on top",
        "현재 로그인한 사용자를 복원했습니다. 다시 로그인합니다.":
            "The current logged-in user was restored. Logging in again.",
        "현재 마스터 비밀번호:":
            "Current master password:",
        "현재 비밀번호가 틀렸습니다.":
            "The current password is wrong.",
        "현재 사용자 삭제...":
            "Delete current user...",
        "현재 주소로 사이트 추가":
            "Add site with current address",
        "확인":
            "OK",
        "확인 대상 저장소":
            "Repository to check",
        "확인(O)":
            "OK(O)",
        "확인을 위해 아이디 '{0}' 를 그대로 입력하세요:":
            "To confirm, type the ID '{0}' exactly as it is:",
        "환경설정(S)":
            "Settings(S)",
        "[지금 업데이트]를 누르면 새 버전을 받아 자동으로 바꿔 넣고 다시 시작합니다. data 폴더는 그대로 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "Click [Update now] to download the new version, replace this program automatically, and restart. The data folder is kept as is. (We recommend making a backup first)",
        "{0} - 업데이트 적용":
            "{0} - Apply update",
        "다운로드에 실패했습니다: {0}":
            "Download failed: {0}",
        "업데이트 다운로드 중... {0}%":
            "Downloading update... {0}%",
        "업데이트 적용에 실패했습니다: {0}":
            "Failed to apply the update: {0}",
        "업데이트를 적용합니다. 프로그램이 곧 다시 시작됩니다.":
            "Applying update. The program will restart shortly.",
        "이 방식으로는 자동 업데이트를 적용할 수 없습니다. (exe 로 실행 중일 때만 가능)\n다운로드 페이지에서 새 exe 를 받아 직접 바꿔 넣어 주세요.":
            "Automatic update isn't available this way. (Only works when running as the .exe)\nPlease download the new .exe from the download page and replace it yourself.",
        "지금 업데이트":
            "Update now",
    },
    "ja": {
        "글자 크기":
            "文字サイズ",
        "글자 굵게 표시":
            "太字で表示",
        "글자 크기를 바꿨습니다.":
            "文字サイズを変更しました。",
        "굵게 표시 설정을 바꿨습니다.":
            "太字表示の設定を変更しました。",
        "작은 글자":
            "小さい文字",
        "보통 글자":
            "普通の文字",
        "큰 글자":
            "大きい文字",
        "아주 큰 글자":
            "特大文字",
        "강조 색상...":
            "強調色...",
        "버튼·테두리 등에 쓸 강조 색을 골라 주세요.":
            "ボタンや枠線などに使う強調色を選んでください。",
        "직접 선택...":
            "カスタム選択...",
        "강조 색상 직접 선택":
            "強調色をカスタム選択",
        "강조 색상을 바꿨습니다.":
            "強調色を変更しました。",
        "딥 틸 (기본)":
            "ディープティール（既定）",
        "네이비":
            "ネイビー",
        "자두색":
            "プラム",
        "포레스트 그린":
            "フォレストグリーン",
        "슬레이트 블루":
            "スレートブルー",
        "테라코타":
            "テラコッタ",
        "차콜":
            "チャコール",
        "버건디":
            "バーガンディ",
        "매우 약함":
            "非常に弱い",
        "약함":
            "弱い",
        "보통":
            "普通",
        "강함":
            "強い",
        "매우 강함":
            "非常に強い",
        "오래 안 쓴 사이트 ({0})":
            "しばらく未使用のサイト ({0})",
        " (오래 안 쓴 사이트)":
            " (しばらく未使用のサイト)",
        "주요 기능":
            "主な機能",
        " · 오래 안 씀":
            " · しばらく未使用",
        "검색 결과 {0}개":
            "検索結果 {0}件",
        "  ·  오래 안 쓴 사이트 {0}개":
            "  ·  しばらく未使用のサイト {0}件",
        "■ 보관함과 사용자\n· 한 대의 컴퓨터에서 여러 사람(또는 용도별)이 각자 독립된 보관함을 쓸 수 있습니다. (서로의 정보는 볼 수 없습니다)\n· 저장한 사이트는 '그룹(폴더)'으로 나눠서 정리할 수 있고, 마우스로 끌어다 옮길 수 있습니다.\n\n■ 브라우저 연동과 채움\n· 지원하는 브라우저(Chrome·Edge·Whale 등)의 주소창을 읽어서, 지금 보고 있는 사이트의 저장된 정보를 자동으로 찾아줍니다. (Windows 전용)\n· [채움] 버튼 하나로 아이디·비밀번호를 브라우저 입력칸에 자동으로 넣어 줍니다.\n\n■ 검색\n· 메인 창에서 Ctrl+F(또는 돋보기 버튼)를 누르면 검색창이 열립니다. 사이트 설명·주소·키워드·아이디로 모든 그룹을 한 번에 찾아 줍니다.\n· 검색 중에도 그룹(폴더) 구조는 그대로 보이며, 찾은 사이트가 들어 있는 그룹만 펼쳐서 보여 줍니다.\n\n■ 비밀번호 강도 표시\n· 새 비밀번호를 만들 때(회원가입, 사이트 추가/수정) 길이와 문자 종류를 보고 '매우 약함~매우 강함'을 막대와 글자로 바로 보여 줍니다.\n\n■ 안 쓰는 사이트 알림\n· 오랫동안(기본 180일) [채움]이나 비밀번호 복사로 쓰지 않은 사이트는 목록에 주황색으로 '오래 안 씀' 표시가 붙습니다.\n· 로그인하면 오래 안 쓴 사이트가 몇 개인지 요약으로 알려 줍니다. 더 안 쓰는 계정은 정리하거나 비밀번호를 새로 바꾸는 걸 권장합니다.\n· [목록관리] 창 왼쪽의 '오래 안 쓴 사이트'를 누르면 그룹과 상관없이 오래 안 쓴 사이트만 한 번에 모아서 볼 수 있습니다. (오래 쓴 순서대로 정렬)\n\n■ 백업\n· 로그인할 때마다 자동으로 백업됩니다.\n· 원하는 위치(USB, 클라우드 동기화 폴더 등)에 자동 또는 수동으로 백업하도록 설정할 수 있습니다.\n· 기본은 암호화된 백업이며, 필요하면 암호화되지 않은 CSV로도 내보낼 수 있습니다 (내보낼 때 경고가 표시됩니다).\n\n■ 들고 다니기 (USB)\n· exe 파일 옆에 생기는 'data' 폴더만 있으면 되므로, 둘을 함께 USB에 넣어 다른 컴퓨터에서도 바로 쓸 수 있습니다.\n\n■ 업데이트\n· 새 버전이 나오면 알려 주고, [지금 업데이트]를 누르면 새 exe로 자동 교체 · 재시작됩니다.\n\n■ 여러 언어\n· 한국어 · English · 日本語 · 简体中文을 지원합니다. 환경설정에서 언제든 바꿀 수 있습니다.":
            "■ 保管庫とユーザー\n· 1台のパソコンで複数の人(または用途別)がそれぞれ独立した保管庫を使えます。(お互いの情報は見えません)\n· 保存したサイトは「グループ(フォルダ)」で分けて整理でき、マウスでドラッグして移動できます。\n\n■ ブラウザー連携と自動入力\n· 対応ブラウザー(Chrome・Edge・Whale など)のアドレスバーを読み取り、今見ているサイトの保存情報を自動的に見つけます。(Windows専用)\n· [入力]ボタン1つでID・パスワードをブラウザーの入力欄に自動で入れます。\n\n■ 検索\n· メインウィンドウで Ctrl+F(または虫めがねボタン)を押すと検索欄が開きます。サイト名・アドレス・キーワード・IDですべてのグループを一度に検索します。\n· 検索中もグループ(フォルダ)構造はそのまま表示され、見つかったサイトが入っているグループだけ展開されます。\n\n■ パスワード強度表示\n· 新しいパスワードを作るとき(新規登録、サイトの追加/編集)、長さと文字種から「非常に弱い〜非常に強い」をバーと文字ですぐ表示します。\n\n■ 未使用サイトのお知らせ\n· 長い間([入力]やパスワードのコピーで)使っていないサイト(デフォルト180日)は、一覧にオレンジ色で「しばらく未使用」と表示されます。\n· ログインすると、しばらく使っていないサイトがいくつあるか要約で知らせます。使わなくなったアカウントは整理するか、パスワードを変更することをおすすめします。\n· [一覧管理]ウィンドウ左側の「しばらく未使用のサイト」を押すと、グループに関係なく未使用のサイトだけを一箇所にまとめて見られます。(未使用期間が長い順)\n\n■ バックアップ\n· ログインのたびに自動的にバックアップされます。\n· 好きな場所(USB、クラウド同期フォルダなど)に自動または手動でバックアップするよう設定できます。\n· 基本は暗号化バックアップで、必要なら暗号化されていないCSVでも書き出せます(書き出す際に警告が表示されます)。\n\n■ 持ち運び (USB)\n· exeファイルの横にできる「data」フォルダさえあれば良いので、両方をUSBに入れれば他のパソコンでもすぐ使えます。\n\n■ アップデート\n· 新しいバージョンが出るとお知らせし、[今すぐ更新]を押すと新しいexeに自動で置き換わって再起動します。\n\n■ 多言語対応\n· 韓国語・English・日本語・简体中文に対応しています。環境設定でいつでも切り替えられます。",
        "■ 내 정보는 어떻게 보호되나요? (쉽게 설명)\n· 모든 정보는 '암호화'되어 저장됩니다. 암호화란, 마스터 비밀번호가 없으면 아무도 — 프로그램을 만든 사람도 — 내용을 읽을 수 없도록 뒤섞어 두는 것입니다.\n   (전문 용어로는 AES-256-GCM 방식입니다. 지금의 기술로는 사실상 풀 수 없다고 알려진 수준의 암호화 방식이라고 이해하시면 됩니다)\n· 마스터 비밀번호 자체는 어디에도 그대로 저장되지 않습니다. 비밀번호를 아주 여러 번 복잡한 계산을 거쳐 '잠금을 푸는 열쇠'로 바꾼 뒤, 그 열쇠로만 보관함을 엽니다.\n   (전문 용어로는 scrypt 방식입니다. 이렇게 하면 누군가 비밀번호를 무작위로 하나씩 맞혀 보려고 해도, 한 번 시도하는 데 시간이 오래 걸려서 사실상 불가능해집니다)\n· 정보는 이 컴퓨터의 data 폴더에만 저장됩니다. 인터넷 어디로도 보내지지 않습니다.\n· 인터넷에 연결되는 경우는 '새 버전이 나왔는지' 확인할 때뿐이며, 이때도 저장된 아이디·비밀번호는 전혀 전송되지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ 自分の情報はどう守られていますか? (わかりやすく説明)\n· すべての情報は「暗号化」されて保存されます。暗号化とは、マスターパスワードがないと誰も――プログラムの作者でさえ――中身を読めないように、内容を並べ替えてしまうことです。\n   (専門用語では AES-256-GCM 方式です。今の技術では事実上解読できないとされているレベルの暗号化方式だと理解しておけば十分です)\n· マスターパスワードそのものはどこにもそのまま保存されません。パスワードを何度も複雑な計算にかけて「鍵を開けるための鍵」に変え、その鍵だけで保管庫を開きます。\n   (専門用語では scrypt 方式です。こうすることで、誰かがパスワードを一つずつ総当たりで試そうとしても、1回の試行に時間がかかり事実上不可能になります)\n· 情報はこのパソコンの data フォルダにのみ保存されます。インターネットのどこにも送信されません。\n· インターネットに接続するのは「新しいバージョンが出ているか」を確認するときだけで、この際も保存されたID・パスワードは一切送信されません。\n\n■ 自動保護機能\n· 10分間操作がないとログインウィンドウに戻ります。\n· コピーしたパスワードは20秒後にクリップボードから消去されます。\n· パスワードは画面上で基本的に ●●● で隠されます。\n· ログイン時にパスワードを5回間違えるとプログラムが終了します。\n\n■ ご注意いただきたい点\n· マスターパスワードは復元できません。別の場所に安全に控えておいてください。\n· このパソコンがウイルスに感染すると、どんなパスワード管理ソフトも安全ではありません。ウイルス対策ソフトを最新に保ってください。\n· 共用パソコンでは、使用後に必ず終了してください。",
        "'{0}' 그룹으로 {1}개 사이트를 묶었습니다.":
            "{1}件のサイトをグループ「{0}」にまとめました。",
        "'{0}' 로 옮겼습니다.":
            "「{0}」に移動しました。",
        "'{0}' 사이트 정보를":
            "サイト情報「{0}」を",
        "'{0}' 사이트 정보를 삭제할까요?":
            "サイト情報「{0}」を削除しますか?",
        "'{0}' 안에 만들 새 그룹 이름:":
            "「{0}」の中に作成する新しいグループ名:",
        "'{0}' 의 마스터 비밀번호를 입력하세요:":
            "「{0}」のマスターパスワードを入力してください:",
        "'위치'는 이 그룹을 어느 그룹 안에 둘지입니다. 그룹을 삭제해도 안에 있던 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.":
            "「場所」は、このグループをどのグループの中に置くかを指定します。グループを削除しても、中にあったサイトは削除されず、上位のグループに移動されます。",
        "({0}초 후 클립보드 삭제)":
            "({0}秒後にクリップボードを消去)",
        "(검색 결과)":
            "(検索結果)",
        "(설정되지 않음)":
            "(未設定)",
        "8자 이상 입력하세요.":
            "8文字以上で入力してください。",
        "CSV (표 파일) — 암호화되지 않음":
            "CSV (表ファイル) — 暗号化なし",
        "CSV 가져오기":
            "CSVインポート",
        "CSV 가져오기·내보내기":
            "CSVインポート・エクスポート",
        "CSV 내보내기 (암호화 안 됨)":
            "CSVエクスポート (暗号化なし)",
        "CSV 데이터가 없습니다.":
            "CSVデータがありません。",
        "CSV 백업은 암호화되지 않습니다.\n\n모든 사이트의 아이디와 비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다.\n\n그래도 CSV로 백업할까요?\n(권장: 암호화 백업)":
            "CSVバックアップは暗号化されません。\n\nすべてのサイトのIDとパスワードが平文のまま保存されます。そのフォルダーがクラウド上や他の人が見られる場所にある場合、すべて漏えいします。\n\nそれでもCSVでバックアップしますか?\n(推奨: 暗号化バックアップ)",
        "CSV(암호화 안 됨) 백업 완료: {0}":
            "CSV (暗号化なし) バックアップが完了しました: {0}",
        "GitHub 저장소의 최신 Release 를 확인해서 새 버전이 있으면 알려 드립니다. 자동으로 설치하지는 않으며, 다운로드 페이지만 열어 줍니다. (새 exe 로 바꿔도 data 폴더의 정보는 그대로 유지됩니다)":
            "GitHub リポジトリの最新 Release を確認し、新しいバージョンがあればお知らせします。自動ではインストールされず、ダウンロードページを開くだけです。(新しい exe に入れ替えても data フォルダーの情報はそのまま保持されます)",
        "INFO : 입력하신 정보는 암호화되어 사용자의\n컴퓨터에 저장되며 인터넷으로 전송되지\n않으므로 회원가입이 필요 없습니다.\n\n※ 비밀번호를 잊으면 복구할 수 없습니다.":
            "INFO : 入力された情報は暗号化されて\nお使いのコンピューターに保存され、\nインターネットで送信されないため、会員登録は不要です。\n\n※ パスワードを忘れると復旧できません。",
        "Q. [채움]을 눌러도 입력이 안 돼요.\nA. ① 브라우저 아이디 입력칸을 먼저 클릭했는지, ② 관리자 권한으로 실행된 창이 아닌지 확인하세요.\n   일부 사이트는 보안 키패드를 써서 자동 입력이 막힙니다. 이때는 값을 복사해서 입력하세요.\n\nQ. 브라우저 주소가 자동으로 안 들어와요.\nA. ① 환경설정 메뉴의 '브라우저 주소 자동 연동'이 켜져 있는지, ② 지원 브라우저인지 확인하세요.\n   ↻ 버튼(F5)으로 즉시 읽기를 시도해 보고, 안 되면 주소를 직접 붙여넣으세요.\n\nQ. 마스터 비밀번호를 잊었어요.\nA. 복구할 방법이 없습니다. 이전 백업의 비밀번호가 기억난다면 백업에서 복원해 보세요.\n   포기하고 새로 시작하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 지우고(또는 다른 곳으로 옮기고)\n   새 사용자를 만드세요.\n\nQ. 프로그램을 다시 설치/이동하면 정보가 사라지나요?\nA. 정보는 프로그램 옆의 data 폴더에 있습니다. 프로그램(exe)을 옮길 때 data 폴더도 같이 옮기세요.\n\nQ. 다른 드라이브나 클라우드에 자동으로 백업하고 싶어요.\nA. 파일 메뉴 '백업 위치 설정'에서 폴더를 고르세요. 클라우드라면 그 서비스의 동기화 폴더를 고르면 됩니다.\n   (도움말 '백업과 복원' 참고. 암호화 백업을 권장합니다)\n\nQ. 다른 컴퓨터에서도 쓰고 싶어요.\nA. 'CSV'는 위험하니 쓰지 말고, '백업 만들기'로 저장한 파일을 새 컴퓨터에서 '백업에서 복원' 하세요.\n   (data 폴더를 통째로 복사해도 됩니다)\n\nQ. 백신이 exe 파일을 의심해요.\nA. 개인이 만든 프로그램은 서명이 없어 오탐이 생기기도 합니다. 특히 [채움]이 키보드 입력을 대신 하기 때문입니다.\n   소스(mypass.py)를 직접 확인하거나 예외 목록에 등록하세요.\n\nQ. 알패스에서 쓰던 정보를 옮기고 싶어요.\nA. 알패스가 정보를 CSV 등으로 내보낼 수 있다면 'CSV 가져오기'를 쓰세요. 없다면 직접 입력해야 합니다.":
            "Q. [入力]を押しても入力されません。\nA. ① ブラウザーのID入力欄を先にクリックしたか、② 管理者権限で実行されたウィンドウではないか、を確認してください。\n   一部のサイトではセキュリティキーパッドが使われており、自動入力がブロックされます。その場合は値をコピーして入力してください。\n\nQ. ブラウザーのアドレスが自動で入りません。\nA. ① 環境設定メニューの「ブラウザーのアドレス自動連携」がオンになっているか、② 対応ブラウザーか、を確認してください。\n   ↻ ボタン(F5)ですぐに読み取りを試し、それでもだめならアドレスを直接貼り付けてください。\n\nQ. マスターパスワードを忘れました。\nA. 復旧する方法はありません。以前のバックアップのパスワードを覚えていれば、バックアップから復元してみてください。\n   あきらめて最初からやり直す場合は、プログラムを終了してから data フォルダー内の該当する「ID.dat」ファイルを削除し(または別の場所に移し)、\n   新規ユーザーを作成してください。\n\nQ. プログラムを再インストール/移動すると情報は消えますか?\nA. 情報はプログラムの隣にある data フォルダーに保存されています。プログラム(exe)を移動するときは、data フォルダーも一緒に移動してください。\n\nQ. 別のドライブやクラウドに自動でバックアップしたいです。\nA. ファイルメニューの「バックアップ先の設定」でフォルダーを選んでください。クラウドの場合は、そのサービスの同期フォルダーを選べば大丈夫です。\n   (ヘルプの「バックアップと復元」を参照してください。暗号化バックアップをおすすめします)\n\nQ. 別のコンピューターでも使いたいです。\nA. 「CSV」は危険なので使わず、「バックアップを作成」で保存したファイルを、新しいコンピューターで「バックアップから復元」してください。\n   (data フォルダーをそのままコピーしても構いません)\n\nQ. ウイルス対策ソフトが exe ファイルを疑います。\nA. 個人が作成したプログラムは署名がないため、誤検知されることがあります。特に[入力]がキーボード入力を代行するためです。\n   ソース(mypass.py)を直接確認するか、除外リストに登録してください。\n\nQ. アルパスで使っていた情報を移したいです。\nA. アルパスが情報をCSVなどでエクスポートできる場合は、「CSVインポート」を使ってください。できない場合は手動で入力する必要があります。",
        "{0}  v{1}\n\n아이디·비밀번호·사이트 정보를 암호화해서\n보관하는 개인용 비밀번호 관리 프로그램":
            "{0}  v{1}\n\nID・パスワード・サイト情報を暗号化して\n保管する個人向けパスワード管理プログラム",
        "{0} - 그룹 수정":
            "{0} - グループの編集",
        "{0} - 그룹 이동":
            "{0} - グループの移動",
        "{0} - 그룹으로 이동":
            "{0} - グループへ移動",
        "{0} - 도움말":
            "{0} - ヘルプ",
        "{0} - 로그인":
            "{0} - ログイン",
        "{0} - 목록관리":
            "{0} - 一覧管理",
        "{0} - 백업 위치 설정":
            "{0} - バックアップ先の設定",
        "{0} - 사이트 {1}":
            "{0} - サイト{1}",
        "{0} - 새 버전":
            "{0} - 新バージョン",
        "{0} - 새 사용자 등록":
            "{0} - 新規ユーザー登録",
        "{0} - 업데이트 설정":
            "{0} - アップデート設定",
        "{0} - 정보":
            "{0} - バージョン情報",
        "{0} 복사됨":
            "{0}をコピーしました",
        "{0} 삭제할까요?":
            "{0}を削除しますか?",
        "{0}개 사이트를 '{1}' 로 옮겼습니다.":
            "{0}件のサイトを「{1}」に移動しました。",
        "{0}개 사이트를 가져왔습니다.":
            "{0}件のサイトをインポートしました。",
        "{0}곳을 찾았습니다. 입력칸 오른쪽 ▼ 에서 고르세요.":
            "{0}件見つかりました。入力欄の右の ▼ から選んでください。",
        "{0}님 로그인":
            "{0}さんのログイン",
        "· 암호화: AES-256-GCM / scrypt\n· 정보는 이 컴퓨터에만 저장되며 인터넷으로 전송되지 않습니다.\n· (인터넷은 업데이트 확인에만 사용하며, 정보는 보내지 않습니다)\n· 데이터 폴더:\n   {0}":
            "· 暗号化: AES-256-GCM / scrypt\n· 情報はこのコンピューターにのみ保存され、インターネットで送信されることはありません。\n· (インターネットはアップデートの確認にのみ使用し、情報は送信しません)\n· データフォルダー:\n   {0}",
        "■ 가져오기\n· 파일 메뉴 'CSV 가져오기'. 엑셀에서 만든 표나 다른 프로그램에서 내보낸 파일을 읽습니다.\n· 첫 줄(제목줄)에 다음 이름이 있으면 자동으로 인식합니다.\n   그룹(폴더) / 사이트 설명(사이트명, name) / 주소(url) / 주소 키워드 / 아이디(id) / 비밀번호(password)\n· 주소가 없는 줄은 건너뜁니다. 주소 키워드가 비어 있으면 자동으로 만듭니다.\n· '그룹' 칸에 업무/은행 처럼 적으면 그룹이 자동으로 만들어집니다. ('폴더'라는 제목도 인식합니다)\n\n■ 내보내기\n· 파일 메뉴 'CSV 내보내기'. 엑셀로 열 수 있습니다.\n· ※ 내보낸 CSV는 암호화되어 있지 않습니다. 비밀번호가 그대로 보이므로 사용 후 반드시 지우세요.\n· 백업 용도라면 CSV 대신 '백업 만들기'를 사용하세요.":
            "■ インポート\n· ファイルメニューの「CSVインポート」。Excelで作成した表や、他のプログラムからエクスポートしたファイルを読み込みます。\n· 1行目(見出し行)に次の名前があれば自動的に認識します。\n   グループ(フォルダー) / サイトの説明(サイト名、name) / アドレス(url) / アドレスキーワード / ID(id) / パスワード(password)\n· アドレスのない行はスキップされます。アドレスキーワードが空の場合は自動で作成されます。\n· 「グループ」欄に 業務/銀行 のように書くと、グループが自動的に作成されます。(「フォルダー」という見出しも認識します)\n\n■ エクスポート\n· ファイルメニューの「CSVエクスポート」。Excelで開くことができます。\n· ※ エクスポートしたCSVは暗号化されていません。パスワードがそのまま見えるため、使用後は必ず削除してください。\n· バックアップ目的の場合は、CSVではなく「バックアップを作成」を使用してください。",
        "■ 기본 크기\n처음 열 때는 화면 배율(125%, 150% 등)에 맞춰 보정한 기본 크기로 열립니다. 어느 컴퓨터에서나 같은 모양으로 나옵니다.\n\n■ 마음대로 조절\n창 가장자리를 끌어 크기를 자유롭게 줄이고 늘릴 수 있고, 옮겨 둔 위치도 기억합니다.\n메인 창, 목록관리 창, 도움말 창이 각각 따로 기억됩니다. 너무 작아지지 않도록 최소 크기는 정해져 있습니다.\n\n■ 되돌리기\n환경설정 메뉴 → '창 크기 초기화' 를 누르면 기본 크기로 돌아갑니다.\n(모니터를 바꾸는 등으로 저장된 위치가 화면 밖이 되면 자동으로 기본 위치에서 열립니다)":
            "■ 基本サイズ\n初めて開くときは、画面の拡大率(125%、150%など)に合わせて補正した基本サイズで開きます。どのコンピューターでも同じ見た目になります。\n\n■ 自由に調整\nウィンドウの端をドラッグして自由に拡大・縮小でき、移動した位置も記憶されます。\nメインウィンドウ、一覧管理ウィンドウ、ヘルプウィンドウがそれぞれ別々に記憶されます。小さくなりすぎないよう、最小サイズが決められています。\n\n■ 元に戻す\n環境設定メニュー → 「ウィンドウサイズを初期化」を押すと、基本サイズに戻ります。\n(モニターを変更するなどして保存された位置が画面外になった場合は、自動的に基本の位置で開きます)",
        "■ 메인 창\nF1          도움말\nF5          브라우저 주소 지금 가져오기\nCtrl+N      사이트 추가\nCtrl+F      검색창 열기/닫기 (설명·주소·키워드·아이디로 전체 검색, Esc 로 닫기)\nEnter       (주소 칸에서) 사이트 열기\n더블클릭    (아이디/비밀번호 값) 복사 · (목록의 사이트) 열기\n끌어서 놓기 (메인 목록) 사이트·그룹을 다른 그룹 위에 끌어 이동\nCtrl+A      (목록관리 창) 사이트 전체 선택\n오른쪽 클릭 (값/목록) 메뉴\n\n■ 로그인 창\nEnter / Alt+O   확인\nAlt+C           취소\nAlt+N           새 사용자\n\n■ 모든 창\nEsc             창 닫기(취소)":
            "■ メインウィンドウ\nF1          ヘルプ\nF5          ブラウザーのアドレスを今すぐ取得\nCtrl+N      サイトを追加\nCtrl+F      検索欄を開く/閉じる (名前・URL・キーワード・IDで全体検索、Esc で閉じる)\nEnter       (アドレス欄で) サイトを開く\nダブルクリック  (ID/パスワードの値) コピー · (一覧のサイト) 開く\nドラッグ＆ドロップ (メイン一覧) サイト・グループを別のグループ上にドラッグして移動\nCtrl+A      (一覧管理ウィンドウ) サイトをすべて選択\n右クリック  (値/一覧) メニュー\n\n■ ログインウィンドウ\nEnter / Alt+O   OK\nAlt+C           キャンセル\nAlt+N           新規ユーザー\n\n■ すべてのウィンドウ\nEsc             ウィンドウを閉じる(キャンセル)",
        "■ 어떻게 보호되나요?\n· 모든 정보는 AES-256-GCM 으로 암호화되어 저장됩니다.\n· 마스터 비밀번호에서 암호화 키를 만들 때 scrypt 방식을 써서 비밀번호 대입 공격을 어렵게 합니다.\n· 정보는 이 컴퓨터(data 폴더)에만 저장되고, 인터넷으로 전송되지 않습니다.\n· 인터넷은 업데이트 확인(GitHub 에서 최신 버전 번호 조회)에만 쓰이며, 저장된 정보는 전혀 보내지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ どのように保護されますか?\n· すべての情報は AES-256-GCM で暗号化して保存されます。\n· マスターパスワードから暗号化キーを作成する際に scrypt 方式を使い、パスワードの総当たり攻撃を困難にしています。\n· 情報はこのコンピューター(data フォルダー)にのみ保存され、インターネットで送信されることはありません。\n· インターネットはアップデートの確認(GitHub で最新バージョン番号を照会)にのみ使われ、保存された情報は一切送信しません。\n\n■ 自動保護機能\n· 10分間操作がないと、ログインウィンドウに戻ります。\n· コピーしたパスワードは20秒後にクリップボードから消去されます。\n· パスワードは画面上では通常 ●●● で隠されます。\n· ログインでパスワードを5回間違えると、プログラムが終了します。\n\n■ ご注意いただきたい点\n· マスターパスワードは復旧できません。別の場所に安全に書き留めておいてください。\n· このコンピューターがウイルスに感染した場合、どのパスワード管理ソフトも安全ではありません。ウイルス対策ソフトを最新の状態に保ってください。\n· 共用のコンピューターでは、使用後に必ず終了してください。",
        "■ 자동 백업 (아무것도 안 해도 됩니다)\n· 로그인할 때마다 data\\backup 폴더에 '아이디_날짜.mpbak' 사본이 만들어집니다. (하루 1개, 최근 10개 보관)\n· 저장할 때마다 같은 폴더에 '아이디.dat.bak' (직전 상태)도 만들어집니다.\n\n■ 직접 백업\n파일 메뉴 '백업 만들기' → 원하는 위치(USB, 클라우드 폴더 등)에 저장합니다.\n백업 파일은 암호화되어 있어 남이 열어볼 수 없습니다.\n\n■ 복원\n· 로그인한 뒤 파일 메뉴 '백업에서 복원' (로그인 창에는 복원 버튼이 없습니다)\n· 새 컴퓨터라면: 로그인 창에서 [새 사용자]로 임시 사용자를 만들어 로그인 → '백업에서 복원' →\n   복원이 끝나면 '다른 사용자로 로그인'으로 복원한 사용자에 들어갑니다. (임시 사용자는 '현재 사용자 삭제'로 정리)\n· 백업 파일 선택 → 백업 당시의 마스터 비밀번호 입력 → 복원할 아이디 입력\n· 같은 아이디가 있으면 덮어쓸지 묻고, 기존 파일은 data\\_deleted 에 보관됩니다.\n· 복원 후에는 백업 당시의 마스터 비밀번호로 로그인합니다.\n\n■ 백업 위치 (내가 정한 폴더에 자동 백업)\n· 파일 메뉴 '백업 위치 설정'에서 백업을 저장할 폴더를 지정합니다. 로그인할 때, 정보를 바꾼 뒤, 종료할 때\n   그 폴더의 MyPass_backup 안에 자동으로 백업합니다. (위의 data\\backup 자동 백업과는 별개입니다)\n· 폴더는 어디든 됩니다: 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS),\n   또는 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더. [클라우드 찾기]로 흔한 클라우드 폴더를 찾을 수 있습니다.\n· 클라우드에 직접 로그인하지 않습니다. 이 컴퓨터에 클라우드 프로그램이 설치·로그인되어 있어야 하며, 올리는 일은 그 프로그램이 합니다.\n· 프로그램 데이터와 같은 드라이브(같은 USB)를 고르면 함께 사라질 수 있다고 알려 줍니다. 다른 장치를 권장합니다.\n· 경로에 %USERPROFILE%\\OneDrive 처럼 환경변수를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.\n· 기본은 '암호화 백업(.mpbak)'입니다. 마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 되살립니다.\n   (아이디_latest.mpbak = 최신본, 아이디_날짜.mpbak = 날짜별 사본)\n· 'CSV' 형식도 고를 수 있지만 암호화되지 않아 비밀번호가 글자 그대로 저장됩니다. 꼭 필요할 때만 쓰세요.\n   (아이디_latest.csv 한 파일만 덮어쓰며, 되살릴 때는 'CSV 가져오기'를 사용)\n· 설정한 폴더가 그 컴퓨터에 없으면(다른 PC, USB 미연결 등) 백업을 건너뛰고 상태줄에 알려 줍니다.\n· [지금 백업] 또는 파일 메뉴 '지금 백업 위치에 백업'으로 바로 실행할 수 있고, 마지막 결과는 설정 창에 표시됩니다.\n· 이 설정은 모든 사용자에게 공통이며, 백업 파일 이름에 사용자 아이디가 들어갑니다.\n\n■ 권장 습관\n중요한 정보라면 가끔 '백업 만들기'로 다른 저장 장치에도 사본을 두세요.\n컴퓨터가 고장 나면 data 폴더도 함께 사라집니다.":
            "■ 自動バックアップ (何もしなくて大丈夫です)\n· ログインのたびに data\\backup フォルダーに「ID_日付.mpbak」のコピーが作成されます。(1日1個、直近10個を保管)\n· 保存のたびに同じフォルダーに「ID.dat.bak」(直前の状態)も作成されます。\n\n■ 手動バックアップ\nファイルメニューの「バックアップを作成」→ 好きな場所(USB、クラウドフォルダーなど)に保存します。\nバックアップファイルは暗号化されているため、他の人が開くことはできません。\n\n■ 復元\n· ログイン後、ファイルメニューの「バックアップから復元」(ログインウィンドウには復元ボタンがありません)\n· 新しいコンピューターの場合: ログインウィンドウで[新規ユーザー]から一時ユーザーを作成してログイン → 「バックアップから復元」 →\n   復元が終わったら「別のユーザーでログイン」で復元したユーザーに入ります。(一時ユーザーは「現在のユーザーを削除」で整理)\n· バックアップファイルを選択 → バックアップ作成時のマスターパスワードを入力 → 復元するIDを入力\n· 同じIDがある場合は上書きするか確認し、既存のファイルは data\\_deleted に保管されます。\n· 復元後は、バックアップ作成時のマスターパスワードでログインします。\n\n■ バックアップ先 (指定したフォルダーに自動バックアップ)\n· ファイルメニューの「バックアップ先の設定」で、バックアップを保存するフォルダーを指定します。ログイン時、情報を変更した後、終了時に\n   そのフォルダーの MyPass_backup 内に自動でバックアップします。(上記の data\\backup の自動バックアップとは別です)\n· フォルダーはどこでも構いません: 別のドライブ、外付けHDD・USB、ネットワークドライブ(NAS)、\n   または OneDrive・Google ドライブ・Dropbox・NAVER MYBOX などのクラウド同期フォルダー。[クラウドを探す]で一般的なクラウドフォルダーを探せます。\n· クラウドに直接ログインすることはありません。このコンピューターにクラウドのプログラムがインストール・ログインされている必要があり、アップロードはそのプログラムが行います。\n· プログラムのデータと同じドライブ(同じUSB)を選ぶと、一緒に失われる可能性があると通知します。別のデバイスをおすすめします。\n· パスに %USERPROFILE%\\OneDrive のように環境変数を使うと、コンピューターごとにユーザー名が違っても一度の設定で済みます。\n· 標準は「暗号化バックアップ(.mpbak)」です。マスターパスワードなしでは開けず、「バックアップから復元」で元に戻せます。\n   (ID_latest.mpbak = 最新版、ID_日付.mpbak = 日付別コピー)\n· 「CSV」形式も選べますが、暗号化されずパスワードが平文のまま保存されます。どうしても必要なときだけ使ってください。\n   (ID_latest.csv の1ファイルのみ上書きされ、元に戻すときは「CSVインポート」を使用)\n· 設定したフォルダーがそのコンピューターにない場合(別のPC、USB未接続など)は、バックアップをスキップしてステータスバーでお知らせします。\n· [今すぐバックアップ]またはファイルメニューの「今すぐバックアップ先にバックアップ」ですぐに実行でき、最後の結果は設定ウィンドウに表示されます。\n· この設定はすべてのユーザーに共通で、バックアップファイル名にユーザーIDが含まれます。\n\n■ おすすめの習慣\n重要な情報の場合は、ときどき「バックアップを作成」で別の記憶装置にもコピーを置いておいてください。\nコンピューターが故障すると、data フォルダーも一緒に失われます。",
        "■ 처음 사용할 때\n1. 프로그램을 실행하면 로그인 창이 나옵니다. [새 사용자(N)]를 눌러 아이디와 마스터 비밀번호를 등록합니다.\n2. 등록한 아이디와 비밀번호로 로그인합니다.\n3. 메인 창의 [추가] 버튼으로 자주 쓰는 사이트의 주소, 아이디, 비밀번호를 저장합니다.\n\n■ 마스터 비밀번호란?\n저장한 모든 정보를 잠그는 열쇠입니다. 8자 이상으로 정하고 꼭 기억해 두세요.\n잊어버리면 누구도 복구할 수 없습니다. (프로그램 제작자도 마찬가지입니다)\n\n■ 화면 구성\n· 위쪽 버튼: 목록관리 / 추가(▾ 메뉴) / 수정 / 삭제\n· 주소 칸: 주소를 입력하거나 브라우저에서 자동으로 가져옵니다.\n   ➜ 사이트 열기,  ↻ 브라우저 주소 지금 가져오기\n· 사이트 정보 표시줄: 저장된 정보가 있으면 초록 ✔, 없으면 회색 표시\n· 아이디·비밀번호 칸과 [채움] 버튼\n· 아래 목록: 그룹과 저장된 사이트 (끌어서 그룹으로 이동)\n· 맨 아래 상태줄: 현재 로그인한 사용자와 안내 메시지":
            "■ はじめて使うとき\n1. プログラムを起動すると、ログインウィンドウが表示されます。[新規ユーザー(N)]を押して、IDとマスターパスワードを登録します。\n2. 登録したIDとパスワードでログインします。\n3. メインウィンドウの[追加]ボタンで、よく使うサイトのアドレス、ID、パスワードを保存します。\n\n■ マスターパスワードとは?\n保存したすべての情報をロックする鍵です。8文字以上で決めて、必ず覚えておいてください。\n忘れてしまうと、誰にも復旧できません。(プログラムの作成者も同様です)\n\n■ 画面構成\n· 上部のボタン: 一覧管理 / 追加(▾ メニュー) / 編集 / 削除\n· アドレス欄: アドレスを入力するか、ブラウザーから自動で取得します。\n   ➜ サイトを開く、 ↻ ブラウザーのアドレスを今すぐ取得\n· サイト情報表示バー: 保存された情報があれば緑の ✔、なければ灰色で表示\n· ID・パスワード欄と[入力]ボタン\n· 下の一覧: グループと保存されたサイト (ドラッグしてグループへ移動)\n· 最下部のステータスバー: 現在ログインしているユーザーと案内メッセージ",
        "■ 추가\n[추가] 버튼 → 주소, 아이디, 비밀번호를 입력하고 [확인].\n· 주소 칸에 이미 주소가 들어 있으면 그 주소로 창이 열립니다.\n· [추가] 옆 ▾ 에서 '빈 사이트 추가', '그룹 추가'도 고를 수 있습니다.\n· 비밀번호 옆 [생성] 버튼은 16자리 무작위 비밀번호를 만들어 줍니다. [보기]로 확인하세요.\n· 가입할 때 쓴 비밀번호를 그대로 저장하세요. 생성한 비밀번호는 사이트에도 같이 바꿔 주어야 합니다.\n\n■ 수정 / 삭제\n· 목록에서 사이트를 고르고 [수정] 또는 [삭제].\n· 목록의 사이트를 더블클릭하면 주소가 채워지고 사이트가 열립니다.\n· 목록에서 오른쪽 클릭하면 사이트 열기 / 수정 / 삭제 메뉴가 나옵니다.\n\n■ 같은 사이트에 계정이 여러 개일 때\n같은 주소로 사이트를 여러 개 저장하면, 주소가 맞을 때 주소 칸 아래 작은 목록에 모두 나타납니다. 쓸 계정을 고르세요.":
            "■ 追加\n[追加]ボタン → アドレス、ID、パスワードを入力して[OK]。\n· アドレス欄にすでにアドレスが入っている場合は、そのアドレスでウィンドウが開きます。\n· [追加]の横の ▾ から「空のサイトを追加」「グループを追加」も選べます。\n· パスワードの横の[生成]ボタンは、16桁のランダムなパスワードを作成します。[表示]で確認してください。\n· 登録時に使ったパスワードをそのまま保存してください。生成したパスワードは、サイト側でも一緒に変更する必要があります。\n\n■ 編集 / 削除\n· 一覧でサイトを選び、[編集]または[削除]。\n· 一覧のサイトをダブルクリックすると、アドレスが入力されてサイトが開きます。\n· 一覧で右クリックすると、サイトを開く / 編集 / 削除のメニューが表示されます。\n\n■ 同じサイトに複数のアカウントがある場合\n同じアドレスで複数のサイトを保存すると、アドレスが一致したときにアドレス欄の下の小さな一覧にすべて表示されます。使うアカウントを選んでください。",
        "⚠ 모든 아이디·비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다. 엑셀로 바로 열어 볼 수 있다는 점이 장점입니다.":
            "⚠ すべてのIDとパスワードが平文のまま保存されます。そのフォルダーがクラウド上や他の人が見られる場所にある場合、すべて漏えいします。Excelですぐに開いて確認できる点がメリットです。",
        "✎ 수정":
            "✎ 編集",
        "✔ 성공":
            "✔ 成功",
        "✕ 삭제":
            "✕ 削除",
        "✖ 실패":
            "✖ 失敗",
        "값을 더블클릭하면 복사됩니다 · 오른쪽 클릭: 메뉴":
            "値をダブルクリックするとコピーされます · 右クリック: メニュー",
        "개 (암호화 백업만 · 최신본은 항상 따로 저장)":
            "件 (暗号化バックアップのみ · 最新版は常に別に保存)",
        "검색":
            "検索",
        "관리(T)":
            "管理(T)",
        "그룹":
            "グループ",
        "그룹 '{0}' 을(를) 넣을 그룹을 고르세요.":
            "グループ「{0}」を入れるグループを選んでください。",
        "그룹 삭제":
            "グループの削除",
        "그룹 이름":
            "グループ名",
        "그룹 이름 변경":
            "グループ名の変更",
        "그룹 이름:":
            "グループ名:",
        "그룹 이름을 입력하세요.":
            "グループ名を入力してください。",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.":
            "グループ名が空か、同じ名前のグループがすでにあります。",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)":
            "グループ名が空か、同じ名前のグループがすでにあります。\n(/ \\ は使用できません)",
        "그룹 추가":
            "グループを追加",
        "그룹과 목록관리":
            "グループと一覧管理",
        "그룹과 하위 그룹을 삭제합니다.\n안에 있던 사이트 정보는 상위 그룹으로 옮겨집니다.\n(사이트는 지워지지 않습니다) 계속할까요?":
            "グループとサブグループを削除します。\n中にあったサイト情報は上位のグループに移動されます。\n(サイトは削除されません) 続行しますか?",
        "그룹명":
            "グループ名",
        "그룹으로 이동":
            "グループへ移動",
        "그룹으로 이동...":
            "グループへ移動...",
        "나중에":
            "後で",
        "날짜별 사본 보관:":
            "日付別コピーの保管:",
        "내 드라이브":
            "マイドライブ",
        "내보내기 완료":
            "エクスポート完了",
        "내보낸 CSV는 암호화되지 않습니다.\n사용 후 반드시 안전하게 삭제하세요.\n계속할까요?":
            "エクスポートしたCSVは暗号化されません。\n使用後は必ず安全に削除してください。\n続行しますか?",
        "다른 그룹 안으로 이동":
            "別のグループの中へ移動",
        "다른 사용자로 로그인":
            "別のユーザーでログイン",
        "로그아웃":
            "ログアウト",
        "자동 잠금 시간":
            "自動ロック時間",
        "자동 잠금 시간을 바꿨습니다: {0}":
            "自動ロック時間を変更しました: {0}",
        "5분":
            "5分",
        "10분":
            "10分",
        "15분":
            "15分",
        "30분":
            "30分",
        "사용 안 함":
            "使用しない",
        "다운로드 페이지 열기":
            "ダウンロードページを開く",
        "다운로드 페이지에서 새 exe 를 받아, 지금 쓰는 exe 파일만 바꿔 넣으세요. data 폴더는 그대로 두면 정보가 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "ダウンロードページで新しい exe を入手し、現在使っている exe ファイルだけを入れ替えてください。data フォルダーをそのままにしておけば、情報は保持されます。(入れ替える前に「バックアップを作成」をおすすめします)",
        "다음 주소에 대한 사이트 정보를 수정합니다.":
            "次のアドレスのサイト情報を編集します。",
        "다음 주소에 대한 사이트 정보를 추가합니다.":
            "次のアドレスのサイト情報を追加します。",
        "단축키":
            "ショートカットキー",
        "닫기":
            "閉じる",
        "데이터 폴더 열기":
            "データフォルダーを開く",
        "도움말(H)":
            "ヘルプ(H)",
        "등록되었습니다. 비밀번호를 입력하고 로그인하세요.":
            "登録しました。パスワードを入力してログインしてください。",
        "등록되지 않은 아이디입니다.\n[새 사용자]로 먼저 등록하세요.":
            "登録されていないIDです。\n先に[新規ユーザー]で登録してください。",
        "로그인":
            "ログイン",
        "로그인할 때 하루 한 번 자동으로 확인":
            "ログイン時に1日1回自動で確認",
        "마스터 비밀번호 변경":
            "マスターパスワードの変更",
        "마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 바로 되살릴 수 있습니다.":
            "マスターパスワードなしでは開けず、「バックアップから復元」ですぐに元に戻せます。",
        "마이패스 백업":
            "MyPass バックアップ",
        "마지막 백업: {0}  {1}\n{2}":
            "最後のバックアップ: {0}  {1}\n{2}",
        "모두 접기":
            "すべて折りたたむ",
        "모두 펼치기":
            "すべて展開",
        "모든 그룹 접기":
            "すべてのグループを折りたたむ",
        "모든 그룹 펼치기":
            "すべてのグループを展開",
        "모든 파일":
            "すべてのファイル",
        "목록관리":
            "一覧管理",
        "묶을 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "まとめるサイトを先に選択してください。(Ctrl/Shift で複数選択)",
        "백업 만들기...":
            "バックアップを作成...",
        "백업 완료: {0}":
            "バックアップが完了しました: {0}",
        "백업 위치 백업 실패: {0}":
            "バックアップ先へのバックアップに失敗しました: {0}",
        "백업 위치 설정...":
            "バックアップ先の設定...",
        "백업 위치 자동 백업을 껐습니다.":
            "バックアップ先への自動バックアップをオフにしました。",
        "백업 위치 자동 백업을 켰습니다. 지금 백업하는 중...":
            "バックアップ先への自動バックアップをオンにしました。今バックアップしています...",
        "백업 위치가 지정되지 않았습니다.":
            "バックアップ先が指定されていません。",
        "백업 위치로 자동 백업 사용":
            "バックアップ先への自動バックアップを使用",
        "백업 위치에 백업 완료 ({0})":
            "バックアップ先へのバックアップが完了しました ({0})",
        "백업 파일 저장":
            "バックアップファイルの保存",
        "백업 파일을 자동으로 저장할 폴더를 정하세요. 이 컴퓨터의 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS)는 물론 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더도 됩니다.\n(클라우드는 계정에 직접 로그인하지 않으며, 이 컴퓨터의 클라우드 프로그램이 파일을 올려 줍니다)":
            "バックアップファイルを自動保存するフォルダーを指定してください。このコンピューターの別のドライブ、外付けHDD・USB、ネットワークドライブ(NAS)はもちろん、OneDrive・Google ドライブ・Dropbox・NAVER MYBOX などのクラウド同期フォルダーも指定できます。\n(クラウドのアカウントに直接ログインすることはなく、このコンピューターのクラウドプログラムがファイルをアップロードします)",
        "백업 폴더":
            "バックアップフォルダー",
        "백업 폴더 선택":
            "バックアップフォルダーの選択",
        "백업 폴더를 지정하세요.":
            "バックアップフォルダーを指定してください。",
        "백업 폴더를 찾을 수 없습니다. (드라이브·USB·클라우드 프로그램이 연결되어 있지 않거나, 이 컴퓨터에 없는 경로)":
            "バックアップフォルダーが見つかりません。(ドライブ・USB・クラウドプログラムが接続されていないか、このコンピューターに存在しないパスです)",
        "백업 폴더에 예전에 저장해 둔 CSV 파일(암호화 안 됨)이 남아 있습니다.\n지금 삭제할까요?\n\n{0}":
            "バックアップフォルダーに、以前保存したCSVファイル(暗号化なし)が残っています。\n今すぐ削除しますか?\n\n{0}",
        "백업 형식":
            "バックアップ形式",
        "백업과 복원":
            "バックアップと復元",
        "백업에서 복원...":
            "バックアップから復元...",
        "백업하지 못했습니다.\n{0}":
            "バックアップできませんでした。\n{0}",
        "백업하지 못했습니다: {0}":
            "バックアップできませんでした: {0}",
        "백업했습니다.\n백업 파일은 암호화되어 있으며, 복원할 때 지금의 마스터 비밀번호가 필요합니다.":
            "バックアップしました。\nバックアップファイルは暗号化されており、復元時には現在のマスターパスワードが必要です。",
        "변경":
            "変更",
        "보관함 파일이 올바르지 않아 백업하지 않았습니다.":
            "保管庫ファイルが正しくないため、バックアップしませんでした。",
        "보관함을 열 수 없습니다.\n{0}":
            "保管庫を開けません。\n{0}",
        "보기":
            "表示",
        "보안 안내":
            "セキュリティについて",
        "복원하지 못했습니다.\n{0}":
            "復元できませんでした。\n{0}",
        "복원할 백업 파일 선택":
            "復元するバックアップファイルの選択",
        "복원할 사용자 아이디:":
            "復元するユーザーID:",
        "복원했습니다.\n아이디 '{0}' 와(과) 백업 당시의 마스터 비밀번호로 로그인하세요.":
            "復元しました。\nID「{0}」と、バックアップ作成時のマスターパスワードでログインしてください。",
        "브라우저 주소 가져오기":
            "ブラウザーのアドレスを取得",
        "브라우저 주소 연동":
            "ブラウザーのアドレス連携",
        "브라우저 주소 연동은 Windows에서만 사용할 수 있습니다.":
            "ブラウザーのアドレス連携は Windows でのみ使用できます。",
        "브라우저 주소 연동을 사용할 수 없습니다.":
            "ブラウザーのアドレス連携を使用できません。",
        "브라우저 주소 연동을 사용할 수 없습니다.\n(Windows 전용이며 uiautomation 구성 요소가 필요합니다)":
            "ブラウザーのアドレス連携を使用できません。\n(Windows 専用で、uiautomation コンポーネントが必要です)",
        "브라우저 주소 연동을 사용할 수 없습니다. (uiautomation 구성 요소 없음)":
            "ブラウザーのアドレス連携を使用できません。(uiautomation コンポーネントがありません)",
        "브라우저 주소 자동 연동":
            "ブラウザーのアドレス自動連携",
        "브라우저 주소 지금 가져오기\tF5":
            "ブラウザーのアドレスを今すぐ取得\tF5",
        "브라우저 주소: {0}":
            "ブラウザーのアドレス: {0}",
        "브라우저 주소를 읽는 중 오류가 났습니다.":
            "ブラウザーのアドレスの読み取り中にエラーが発生しました。",
        "브라우저 주소를 읽지 못했습니다.":
            "ブラウザーのアドレスを読み取れませんでした。",
        "브라우저 주소를 읽지 못했습니다. (검색어 입력 중이거나 지원하지 않는 화면)":
            "ブラウザーのアドレスを読み取れませんでした。(検索語の入力中か、非対応の画面です)",
        "브라우저 주소창의 주소를 자동으로 읽어 주소 칸에 넣어 줍니다. (Windows 전용)\n브라우저에서 사이트를 이동할 때마다 저장된 정보가 자동으로 나타납니다.\n\n■ 지원 브라우저\n크롬, 엣지, 웨일, 파이어폭스, 브레이브, 오페라, 비발디 등\n\n■ 사용법\n· 환경설정 메뉴의 '브라우저 주소 자동 연동' 이 켜져 있으면 자동으로 동작합니다.\n· 마이패스 창을 브라우저 옆에 두고 '항상 위에 표시' 를 켜면 가장 편합니다.\n· 바로 읽고 싶으면 ↻ 버튼 또는 F5 키를 누르세요. (직전에 사용한 브라우저에서 읽어옵니다)\n\n■ 참고\n· 마이패스 창을 클릭해도 마지막으로 읽은 주소는 그대로 유지됩니다.\n· 주소창에 검색어를 입력 중이거나, chrome:// 같은 내부 페이지는 읽지 않습니다.\n· 읽히지 않는 브라우저는 주소를 복사(Ctrl+L, Ctrl+C)해서 주소 칸에 붙여넣으세요.\n· 주소는 이 컴퓨터 안에서만 읽히며 어디로도 전송되지 않습니다.":
            "ブラウザーのアドレスバーのアドレスを自動で読み取り、アドレス欄に入れます。(Windows 専用)\nブラウザーでサイトを移動するたびに、保存された情報が自動的に表示されます。\n\n■ 対応ブラウザー\nChrome、Edge、Whale、Firefox、Brave、Opera、Vivaldi など\n\n■ 使い方\n· 環境設定メニューの「ブラウザーのアドレス自動連携」がオンになっていれば、自動で動作します。\n· MyPass のウィンドウをブラウザーの横に置き、「常に手前に表示」をオンにすると最も便利です。\n· すぐに読み取りたいときは、↻ ボタンまたは F5 キーを押してください。(直前に使用したブラウザーから読み取ります)\n\n■ 参考\n· MyPass のウィンドウをクリックしても、最後に読み取ったアドレスはそのまま保持されます。\n· アドレスバーに検索語を入力中の場合や、chrome:// のような内部ページは読み取りません。\n· 読み取れないブラウザーでは、アドレスをコピー(Ctrl+L、Ctrl+C)して、アドレス欄に貼り付けてください。\n· アドレスはこのコンピューター内でのみ読み取られ、どこにも送信されません。",
        "브라우저에서 주소를 읽는 중...":
            "ブラウザーからアドレスを読み取り中...",
        "비밀번호":
            "パスワード",
        "비밀번호 보기":
            "パスワードを表示",
        "비밀번호 복사":
            "パスワードをコピー",
        "비밀번호 숨기기":
            "パスワードを隠す",
        "비밀번호 확인":
            "パスワードの確認",
        "비밀번호(이 OS에서는 자동 채움 미지원)":
            "パスワード (このOSでは自動入力は非対応)",
        "비밀번호가 변경되었습니다.":
            "パスワードを変更しました。",
        "비밀번호가 일치하지 않습니다.":
            "パスワードが一致しません。",
        "비밀번호가 틀렸거나 손상된 백업 파일입니다.":
            "パスワードが間違っているか、破損したバックアップファイルです。",
        "비밀번호가 틀렸습니다.":
            "パスワードが間違っています。",
        "비밀번호는 8자 이상 입력하세요.":
            "パスワードは8文字以上で入力してください。",
        "비밀번호를 5회 틀려 종료합니다.":
            "パスワードを5回間違えたため終了します。",
        "빈 사이트 추가":
            "空のサイトを追加",
        "사용법\tF1":
            "使い方\tF1",
        "사용자 '{0}' 를 등록했습니다.\n지금 이 사용자로 로그인할까요?":
            "ユーザー「{0}」を登録しました。\n今このユーザーでログインしますか?",
        "사용자 '{0}' 를 삭제했습니다.\n(data\\_deleted 폴더에 보관됨)":
            "ユーザー「{0}」を削除しました。\n(data\\_deleted フォルダーに保管されています)",
        "사용자 '{0}' 와(과) 저장된 모든 사이트 정보를 삭제합니다.\n\n파일은 data\\_deleted 폴더로 옮겨지며, 필요하면 그곳에서 되살릴 수 있습니다.\n계속할까요?":
            "ユーザー「{0}」と、保存されているすべてのサイト情報を削除します。\n\nファイルは data\\_deleted フォルダーに移動され、必要であればそこから元に戻せます。\n続行しますか?",
        "사용자 추가·전환·삭제":
            "ユーザーの追加・切り替え・削除",
        "사용자를 만들 수 없습니다.\n{0}":
            "ユーザーを作成できません。\n{0}",
        "사용할 수 없는 그룹 이름입니다.":
            "使用できないグループ名です。",
        "사용할 수 없는 그룹 이름입니다.\n(같은 위치에 같은 이름의 그룹이 있거나, / \\ 문자가 들어 있습니다)":
            "使用できないグループ名です。\n(同じ場所に同じ名前のグループがあるか、/ \\ が含まれています)",
        "사이트 {0}개":
            "サイト{0}件",
        "사이트 설명":
            "サイトの説明",
        "사이트 열기":
            "サイトを開く",
        "사이트 정보가 없습니다.":
            "サイト情報がありません。",
        "사이트 정보가 있습니다.  [{0}]":
            "サイト情報があります。  [{0}]",
        "사이트 추가":
            "サイトを追加",
        "사이트 추가\tCtrl+N":
            "サイトを追加\tCtrl+N",
        "사이트 추가·수정·삭제":
            "サイトの追加・編集・削除",
        "사이트가 많아지면 그룹으로 묶어서 정리할 수 있습니다. 그룹 안에 그룹을 만들 수도 있습니다. (예: 업무 ▸ 은행)\n\n■ 그룹 만들기\n· 메인 목록에서 오른쪽 클릭 → '그룹 추가' / '하위 그룹 추가'\n· 사이트 추가 창의 '그룹명' 옆 [새 그룹] 버튼으로 바로 만들 수 있습니다.\n\n■ 사이트를 그룹으로 옮기기 (3가지 방법)\n1. 끌어서 놓기: 메인 목록에서 사이트를 마우스로 끌어 원하는 그룹 위에 놓습니다.\n   (그룹을 다른 그룹 위에 놓으면 그 안으로 들어갑니다. 놓을 수 있는 곳은 파란색으로 표시됩니다)\n2. 사이트에서 오른쪽 클릭 → '그룹으로 이동' 에서 그룹을 고릅니다.\n3. 사이트 [수정] → '그룹명'을 바꿉니다.\n\n■ 여러 개를 한꺼번에 묶기\n[목록관리] 창에서 Ctrl 또는 Shift 를 누른 채 사이트를 여러 개 고른 다음 오른쪽 클릭\n· '새 그룹으로 묶기': 새 그룹을 만들면서 한 번에 담기\n· '그룹으로 이동': 이미 있는 그룹으로 한 번에 옮기기\n\n■ 그룹 관리\n· 이름 변경 / 다른 그룹 안으로 이동 / 삭제: 메인 목록의 오른쪽 클릭 메뉴, 또는 [목록관리] 창에서\n   그룹 오른쪽의 [수정]을 눌러 팝업에서 바꿉니다.\n· 그룹 이름 옆 숫자는 안에 든 사이트 수(하위 그룹 포함)입니다.\n· 그룹을 삭제해도 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.\n· 맨 위 '최상위' 또는 관리 메뉴에서 '모두 펼치기 / 모두 접기'를 할 수 있습니다.\n\n■ 목록관리 창 (관리대장)\n· 왼쪽: 그룹 목록 / 오른쪽: 선택한 그룹의 사이트 목록\n· 각 줄 오른쪽의 [수정]을 누르면 팝업이 열립니다. 사이트는 설명·주소·아이디·비밀번호·그룹(경로)을,\n   그룹은 이름과 위치(어느 그룹 안에 둘지)를 바꿀 수 있습니다. 사이트 줄의 [삭제]는 그 사이트를 지웁니다.\n· 위쪽: [사이트 추가] [그룹 추가], 검색칸 (사이트 설명, 주소, 키워드, 아이디로 전체 검색 · 검색 중에는 모든 그룹에서 찾음)\n· 사이트를 여러 개 골라 오른쪽 클릭: 비밀번호 복사 / 그룹으로 이동 / 새 그룹으로 묶기 / 삭제 (Ctrl+A 로 전체 선택)":
            "サイトが増えてきたら、グループにまとめて整理できます。グループの中にグループを作ることもできます。(例: 業務 ▸ 銀行)\n\n■ グループの作成\n· メイン一覧で右クリック → 「グループを追加」 / 「サブグループを追加」\n· サイト追加ウィンドウの「グループ名」の横にある[新しいグループ]ボタンですぐに作成できます。\n\n■ サイトをグループへ移動する (3つの方法)\n1. ドラッグ＆ドロップ: メイン一覧でサイトをマウスでドラッグし、目的のグループの上にドロップします。\n   (グループを別のグループの上にドロップすると、その中に入ります。ドロップできる場所は青色で表示されます)\n2. サイトで右クリック → 「グループへ移動」でグループを選びます。\n3. サイトの[編集] → 「グループ名」を変更します。\n\n■ 複数をまとめてグループ化\n[一覧管理]ウィンドウで Ctrl または Shift を押しながらサイトを複数選び、右クリック\n· 「新しいグループにまとめる」: 新しいグループを作成しながら一度に入れる\n· 「グループへ移動」: すでにあるグループへ一度に移動する\n\n■ グループの管理\n· 名前の変更 / 別のグループの中へ移動 / 削除: メイン一覧の右クリックメニュー、または[一覧管理]ウィンドウで\n   グループの右にある[編集]を押して、ポップアップで変更します。\n· グループ名の横の数字は、中に含まれるサイト数(サブグループを含む)です。\n· グループを削除してもサイトは削除されず、上位のグループに移動されます。\n· 最上部の「最上位」または管理メニューから、「すべて展開 / すべて折りたたむ」ができます。\n\n■ 一覧管理ウィンドウ (管理台帳)\n· 左: グループ一覧 / 右: 選択したグループのサイト一覧\n· 各行の右にある[編集]を押すと、ポップアップが開きます。サイトは説明・アドレス・ID・パスワード・グループ(パス)を、\n   グループは名前と場所(どのグループの中に置くか)を変更できます。サイト行の[削除]は、そのサイトを削除します。\n· 上部: [サイトを追加] [グループを追加]、検索欄 (サイトの説明、アドレス、キーワード、IDで全体検索 · 検索中はすべてのグループから探します)\n· サイトを複数選んで右クリック: パスワードをコピー / グループへ移動 / 新しいグループにまとめる / 削除 (Ctrl+A ですべて選択)",
        "사이트를 먼저 선택하세요.":
            "先にサイトを選択してください。",
        "삭제":
            "削除",
        "삭제하지 못했습니다.\n{0}":
            "削除できませんでした。\n{0}",
        "삭제할 그룹을 선택하세요.":
            "削除するグループを選択してください。",
        "삭제할 사용자를 먼저 선택하세요.":
            "削除するユーザーを先に選択してください。",
        "삭제할 사이트를 먼저 선택하세요.":
            "削除するサイトを先に選択してください。",
        "새 그룹":
            "新しいグループ",
        "새 그룹 이름:":
            "新しいグループ名:",
        "새 그룹으로 묶기...":
            "新しいグループにまとめる...",
        "새 버전 {0} 이(가) 있습니다. (업데이트 메뉴 → 업데이트 확인)":
            "新バージョン {0} があります。(アップデートメニュー → アップデートを確認)",
        "새 버전이 있습니다: {0}   (현재 v{1})":
            "新バージョンがあります: {0}   (現在 v{1})",
        "새 비밀번호 (8자 이상):":
            "新しいパスワード (8文字以上):",
        "새 비밀번호 확인:":
            "新しいパスワードの確認:",
        "새 사용자 추가...":
            "新規ユーザーを追加...",
        "새 사용자(N)":
            "新規ユーザー(N)",
        "생성":
            "生成",
        "선택한 사이트 {0}개를":
            "選択した{0}件のサイトを",
        "선택한 사이트 {0}개를 묶을 새 그룹 이름:\n('{1}' 안에 만들어집니다)":
            "選択した{0}件のサイトをまとめる新しいグループ名:\n(「{1}」の中に作成されます)",
        "선택한 사이트 {0}개를 옮길 그룹을 고르세요.":
            "選択した{0}件のサイトの移動先グループを選んでください。",
        "선택한 폴더 안에 '{0}' 폴더를 만들어 저장합니다.":
            "選択したフォルダーの中に「{0}」フォルダーを作成して保存します。",
        "설정":
            "設定",
        "수정":
            "編集",
        "수정 (이름·위치)":
            "編集 (名前・場所)",
        "수정할 사이트를 먼저 선택하세요.":
            "編集するサイトを先に選択してください。",
        "시작하기":
            "はじめに",
        "실제 저장 위치: {0}":
            "実際の保存場所: {0}",
        "아이디":
            "ID",
        "아이디 기억(A)":
            "IDを記憶(A)",
        "아이디 복사":
            "IDをコピー",
        "아이디가 일치하지 않아 삭제를 취소했습니다.":
            "IDが一致しないため、削除を中止しました。",
        "아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요.":
            "IDは、ハングル、英字、数字、_ . - のみを使用し、32文字以内で入力してください。",
        "아이디와 비밀번호를 입력해 주세요.":
            "IDとパスワードを入力してください。",
        "아직 백업 위치가 설정되지 않았습니다.\n지금 설정할까요?":
            "バックアップ先がまだ設定されていません。\n今すぐ設定しますか?",
        "아직 백업 위치로 백업한 기록이 없습니다.":
            "バックアップ先へのバックアップの記録がまだありません。",
        "암호화 백업 (.mpbak) — 권장":
            "暗号化バックアップ (.mpbak) — 推奨",
        "언어 (Language)":
            "言語 (Language)",
        "언어를 바꿨습니다: {0}":
            "言語を変更しました: {0}",
        "업데이트 서버 오류 ({0})":
            "アップデートサーバーエラー ({0})",
        "업데이트 설정...":
            "アップデート設定...",
        "업데이트 확인":
            "アップデートを確認",
        "업데이트(U)":
            "アップデート(U)",
        "업데이트를 확인하는 중...":
            "アップデートを確認しています...",
        "업데이트를 확인할 GitHub 저장소가 설정되어 있지 않습니다.\nmypass.py 맨 위의 UPDATE_REPO 에 '계정/저장소'를 넣고 다시 만드세요.":
            "アップデートを確認する GitHub リポジトリが設定されていません。\nmypass.py の先頭にある UPDATE_REPO に「アカウント/リポジトリ」を入れて、再ビルドしてください。",
        "여기에 사이트 추가":
            "ここにサイトを追加",
        "여러 개 선택(Ctrl/Shift) 후 오른쪽 클릭: 이동 · 묶기 · 삭제":
            "複数選択(Ctrl/Shift)後に右クリック: 移動 · まとめる · 削除",
        "연동할 브라우저 창을 찾지 못했습니다. 브라우저를 한 번 사용한 뒤 다시 눌러 보세요.":
            "連携するブラウザーのウィンドウが見つかりません。ブラウザーを一度使用してから、もう一度押してみてください。",
        "올바른 백업 파일이 아닙니다.":
            "正しいバックアップファイルではありません。",
        "올바른 보관함 파일이 아닙니다.":
            "正しい保管庫ファイルではありません。",
        "옮길 그룹을 선택하세요.":
            "移動先のグループを選択してください。",
        "옮길 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "移動するサイトを先に選択してください。(Ctrl/Shift で複数選択)",
        "옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)":
            "移動できません。(移動先に同じ名前のグループがあります)",
        "위치":
            "場所",
        "이 백업을 만들 당시의 마스터 비밀번호를 입력하세요:":
            "このバックアップ作成時のマスターパスワードを入力してください:",
        "이 주소 키워드를 수동 사이트로 설정(M)":
            "このアドレスキーワードを手動サイトに設定(M)",
        "이 폴더는 프로그램 데이터(data 폴더)와 같은 드라이브(또는 같은 USB)에 있습니다.\n그 장치가 고장 나거나 분실되면 원본과 백업이 함께 사라집니다.\n\n다른 장치(다른 드라이브·클라우드 등)의 폴더를 권장합니다.\n그래도 이 폴더를 사용할까요?":
            "このフォルダーは、プログラムのデータ(data フォルダー)と同じドライブ(または同じUSB)にあります。\nそのデバイスが故障したり紛失したりすると、元データとバックアップが一緒に失われます。\n\n別のデバイス(別のドライブ・クラウドなど)のフォルダーをおすすめします。\nそれでもこのフォルダーを使用しますか?",
        "이름을 바꿀 그룹을 선택하세요.":
            "名前を変更するグループを選択してください。",
        "이미 '{0}' 사용자가 있습니다. 백업 내용으로 덮어쓸까요?\n(기존 파일은 data\\_deleted 폴더에 보관됩니다)":
            "ユーザー「{0}」はすでに存在します。バックアップの内容で上書きしますか?\n(既存のファイルは data\\_deleted フォルダーに保管されます)",
        "이미 등록된 아이디입니다.":
            "すでに登録されているIDです。",
        "인터넷에 연결할 수 없어 확인하지 못했습니다.":
            "インターネットに接続できないため、確認できませんでした。",
        "일치하지 않습니다.":
            "一致しません。",
        "입력하신 정보는 암호화되어 이 컴퓨터에만\n저장되며 인터넷으로 전송되지 않습니다.\n처음이시면 [새 사용자]를 눌러 등록하세요.":
            "入力された情報は暗号化されて、このコンピューターにのみ\n保存され、インターネットで送信されることはありません。\nはじめての場合は、[新規ユーザー]を押して登録してください。",
        "자동 백업 시점: 로그인할 때 · 정보를 바꾼 뒤 · 프로그램을 종료할 때":
            "自動バックアップのタイミング: ログイン時 · 情報を変更した後 · プログラム終了時",
        "자동 백업 폴더 열기":
            "自動バックアップフォルダーを開く",
        "자주 묻는 질문":
            "よくある質問",
        "저장":
            "保存",
        "저장된 아이디와 비밀번호를 브라우저의 로그인 칸에 자동으로 입력합니다. (Windows 전용)\n\n■ 사용 순서\n1. 사이트를 열어 로그인 페이지를 띄웁니다.\n2. 이 프로그램에서 해당 사이트 정보를 선택합니다. (주소가 맞으면 자동으로 선택됩니다)\n3. 브라우저의 아이디 입력칸을 클릭해 커서를 둡니다.\n4. 마이패스의 [채움] 버튼을 누릅니다.\n→ 아이디 입력 → Tab → 비밀번호 입력 순서로 자동 입력됩니다.\n\n■ 자동 로그인\n환경설정 메뉴의 '채움 후 Enter 키 입력' 을 켜면 입력 끝에 Enter 까지 눌러 줍니다.\n\n■ 안 될 때\n· 로그인 칸이 '아이디 → 비밀번호' 순서가 아니거나 중간에 다른 칸이 있으면 어긋날 수 있습니다.\n   이럴 땐 값을 더블클릭해 아이디와 비밀번호를 각각 복사해서 붙여넣으세요.\n· 아이디와 비밀번호를 따로 입력받는 사이트(2단계 로그인)도 복사해서 붙여넣는 방법을 쓰세요.\n· 비밀번호는 복사 후 20초가 지나면 클립보드에서 자동으로 지워집니다.":
            "保存されたIDとパスワードを、ブラウザーのログイン欄に自動で入力します。(Windows 専用)\n\n■ 使用手順\n1. サイトを開いて、ログインページを表示します。\n2. このプログラムで該当するサイト情報を選択します。(アドレスが一致していれば自動で選択されます)\n3. ブラウザーのID入力欄をクリックして、カーソルを置きます。\n4. MyPass の[入力]ボタンを押します。\n→ ID入力 → Tab → パスワード入力の順に自動入力されます。\n\n■ 自動ログイン\n環境設定メニューの「入力後にEnterキーを押す」をオンにすると、入力の最後に Enter まで押してくれます。\n\n■ うまくいかないとき\n· ログイン欄が「ID → パスワード」の順でない場合や、途中に別の欄がある場合は、ずれることがあります。\n   そのときは、値をダブルクリックしてIDとパスワードをそれぞれコピーし、貼り付けてください。\n· IDとパスワードを別々に入力するサイト(2段階ログイン)でも、コピーして貼り付ける方法を使ってください。\n· パスワードはコピーしてから20秒経つと、クリップボードから自動的に消去されます。",
        "저장된 정보를 찾는 기준 단어입니다. 주소창의 주소 안에 이 키워드가 들어 있으면 해당 사이트 정보가 나타납니다.\n\n■ 예시\n· NAVER.COM → mail.naver.com, cafe.naver.com 등 네이버 전체에 적용\n· MAIL.NAVER.COM → 네이버 메일 주소에만 적용\n· 같은 사이트에 키워드가 둘 이상 맞으면 더 긴(구체적인) 키워드가 위에 나옵니다.\n\n■ 자동 생성\n주소를 넣으면 키워드가 자동으로 만들어집니다. (www. 는 제외, co.kr 같은 주소도 처리)\n키워드 칸의 목록에서 범위를 고를 수 있습니다.\n\n■ 직접 정하고 싶을 때\n'이 주소 키워드를 수동 사이트로 설정' 을 체크하면 키워드를 마음대로 적을 수 있습니다.":
            "保存された情報を探すための基準となる単語です。アドレスバーのアドレスの中にこのキーワードが含まれていると、該当するサイト情報が表示されます。\n\n■ 例\n· NAVER.COM → mail.naver.com、cafe.naver.com など NAVER 全体に適用\n· MAIL.NAVER.COM → NAVER メールのアドレスにのみ適用\n· 同じサイトでキーワードが2つ以上一致する場合は、より長い(具体的な)キーワードが上に表示されます。\n\n■ 自動生成\nアドレスを入れると、キーワードが自動で作成されます。(www. は除外、co.kr のようなアドレスにも対応)\nキーワード欄の一覧から範囲を選べます。\n\n■ 自分で決めたいとき\n「このアドレスキーワードを手動サイトに設定」にチェックを入れると、キーワードを自由に入力できます。",
        "저장소 이름을 '계정/저장소' 형식으로 입력하세요.":
            "リポジトリ名を「アカウント/リポジトリ」の形式で入力してください。",
        "저장소 주소는 프로그램(mypass.py 맨 위 UPDATE_REPO)에 미리 넣어 두는 값을 씁니다. 비공개 저장소일 때만 'Fine-grained 토큰(이 저장소 하나, Contents: Read-only)'을 입력하세요. 토큰은 이 컴퓨터의 data 폴더에만 저장되며 외부로 전송되지 않습니다. (data 폴더를 다른 사람과 공유하지 마세요) 공개 저장소면 비워 두세요.":
            "リポジトリのアドレスは、プログラム(mypass.py の先頭にある UPDATE_REPO)にあらかじめ入れておいた値を使います。非公開リポジトリの場合のみ、「Fine-grained トークン(このリポジトリのみ、Contents: Read-only)」を入力してください。トークンはこのパソコンの data フォルダーにのみ保存され、外部に送信されることはありません。(data フォルダーを他人と共有しないでください) 公開リポジトリの場合は空のままにしてください。",
        "토큰 붙여넣기":
            "トークンを貼り付け",
        "고급 설정 (비공개 저장소용 토큰)":
            "詳細設定(非公開リポジトリ用トークン)",
        "저장소·릴리스를 찾을 수 없거나 토큰 권한이 부족합니다. (오류 {0})":
            "リポジトリ・リリースが見つからないか、トークンの権限が不足しています。(エラー {0})",
        "저장소·릴리스를 찾을 수 없습니다. (오류 {0})\n비공개(private) 저장소라면 읽기 전용 토큰이 필요합니다.":
            "リポジトリ・リリースが見つかりません。(エラー {0})\n非公開(private)リポジトリの場合は、読み取り専用のトークンが必要です。",
        "저장하지 못했습니다.\n{0}":
            "保存できませんでした。\n{0}",
        "정보":
            "バージョン情報",
        "종료":
            "終了",
        "주소":
            "アドレス",
        "주소 키워드":
            "アドレスキーワード",
        "주소 키워드가 비어 있습니다.\n주소를 확인하거나 수동으로 입력하세요.":
            "アドレスキーワードが空です。\nアドレスを確認するか、手動で入力してください。",
        "주소 키워드는 저장된 로그인 정보를 찾는 기준입니다.\n주소창의 주소에 이 키워드가 들어 있으면 이 사이트 정보가 표시됩니다.\n\n예) NAVER.COM → mail.naver.com, cafe.naver.com 모두 적용\n    MAIL.NAVER.COM → 메일 주소에만 적용\n\n'수동 사이트로 설정'을 체크하면 키워드를 직접 입력할 수 있습니다.":
            "アドレスキーワードは、保存されたログイン情報を探すための基準です。\nアドレスバーのアドレスにこのキーワードが含まれていると、このサイト情報が表示されます。\n\n例) NAVER.COM → mail.naver.com、cafe.naver.com のどちらにも適用\n    MAIL.NAVER.COM → メールのアドレスにのみ適用\n\n「手動サイトに設定」にチェックを入れると、キーワードを直接入力できます。",
        "주소 키워드란?":
            "アドレスキーワードとは?",
        "주소를 입력하세요.":
            "アドレスを入力してください。",
        "지금 백업":
            "今すぐバックアップ",
        "지금 백업 위치에 백업":
            "今すぐバックアップ先にバックアップ",
        "지정한 폴더를 찾을 수 없습니다.\n경로가 맞는지, 드라이브·USB·클라우드 프로그램이 연결되어 있는지 확인하세요.":
            "指定したフォルダーが見つかりません。\nパスが正しいか、ドライブ・USB・クラウドプログラムが接続されているかを確認してください。",
        "창 크기 초기화":
            "ウィンドウサイズを初期化",
        "창 크기를 기본값으로 되돌렸습니다. (목록관리·도움말 창은 다음에 열 때 적용)":
            "ウィンドウサイズを初期値に戻しました。(一覧管理・ヘルプウィンドウは次回開いたときに適用)",
        "창 크기와 위치":
            "ウィンドウのサイズと位置",
        "찾아보기":
            "参照",
        "채우는 중... 브라우저의 아이디 입력칸에 커서가 있어야 합니다.":
            "入力中... ブラウザーのID入力欄にカーソルがある必要があります。",
        "채울 사이트 정보가 없습니다.":
            "入力するサイト情報がありません。",
        "채움":
            "入力",
        "채움 (자동 입력)":
            "入力 (自動入力)",
        "채움 후 Enter 키 입력(자동 로그인)":
            "入力後にEnterキーを押す(自動ログイン)",
        "최상위":
            "最上位",
        "최상위 ({0})":
            "最上位 ({0})",
        "최신 버전입니다. (v{0})":
            "最新バージョンです。(v{0})",
        "추가":
            "追加",
        "취소":
            "キャンセル",
        "취소(C)":
            "キャンセル(C)",
        "클라우드 찾기":
            "クラウドを探す",
        "클라우드 폴더를 자동으로 찾지 못했습니다.\n[찾아보기]로 직접 고르세요.":
            "クラウドフォルダーを自動で見つけられませんでした。\n[参照]で直接選んでください。",
        "토큰 (비공개일 때만)":
            "トークン (非公開の場合のみ)",
        "토큰":
            "トークン",
        "팁: %USERPROFILE%\\OneDrive 처럼 환경변수 경로를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.":
            "ヒント: %USERPROFILE%\\OneDrive のように環境変数のパスを使うと、コンピューターごとにユーザー名が違っても一度の設定で済みます。",
        "파일(F)":
            "ファイル(F)",
        "하위 그룹 추가":
            "サブグループを追加",
        "한 컴퓨터에서 여러 사람(또는 용도별)이 각자의 보관함을 따로 쓸 수 있습니다.\n\n■ 새 사용자 추가\n· 로그인 창의 [새 사용자(N)] 또는 파일 메뉴 '새 사용자 추가'\n· 아이디와 8자 이상의 비밀번호를 정합니다. 인터넷 회원가입은 필요 없습니다.\n\n■ 다른 사용자로 로그인\n파일 메뉴 '다른 사용자로 로그인'. 사용자마다 사이트 정보가 완전히 분리됩니다.\n\n■ 사용자 삭제\n· 로그인 상태: 파일 메뉴 '현재 사용자 삭제' (마스터 비밀번호 확인 필요)\n· 보안을 위해 로그인 창에는 삭제·복원 버튼이 없습니다. 아이디나 비밀번호를 잊은 사용자는 복구할 수 없으며,\n   정리하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 직접 지우세요.\n· 안전장치: 삭제 전 확인을 거치며, 파일은 data\\_deleted 폴더로 옮겨질 뿐 지워지지 않습니다.\n   되살리려면 그 파일을 data 폴더로 옮기고 이름에서 날짜 부분(_20xxxxxx-xxxxxx)만 지우세요.\n   (예: aaa_20261009-135500.dat → aaa.dat)\n\n■ 마스터 비밀번호 변경\n파일 메뉴 '마스터 비밀번호 변경' (현재 비밀번호 확인 필요)":
            "1台のコンピューターで、複数の人(または用途別)がそれぞれの保管庫を別々に使えます。\n\n■ 新規ユーザーの追加\n· ログインウィンドウの[新規ユーザー(N)]、またはファイルメニューの「新規ユーザーを追加」\n· IDと8文字以上のパスワードを決めます。インターネットでの会員登録は不要です。\n\n■ 別のユーザーでログイン\nファイルメニューの「別のユーザーでログイン」。ユーザーごとにサイト情報は完全に分離されます。\n\n■ ユーザーの削除\n· ログイン状態で: ファイルメニューの「現在のユーザーを削除」(マスターパスワードの確認が必要)\n· セキュリティのため、ログインウィンドウには削除・復元ボタンがありません。IDやパスワードを忘れたユーザーは復旧できず、\n   整理するにはプログラムを終了してから、data フォルダー内の該当する「ID.dat」ファイルを直接削除してください。\n· 安全対策: 削除前に確認を行い、ファイルは data\\_deleted フォルダーに移動されるだけで削除はされません。\n   元に戻すには、そのファイルを data フォルダーに移動し、名前から日付部分(_20xxxxxx-xxxxxx)だけを削除してください。\n   (例: aaa_20261009-135500.dat → aaa.dat)\n\n■ マスターパスワードの変更\nファイルメニューの「マスターパスワードの変更」(現在のパスワードの確認が必要)",
        "항상 위에 표시":
            "常に手前に表示",
        "현재 로그인한 사용자를 복원했습니다. 다시 로그인합니다.":
            "現在ログインしているユーザーを復元しました。再度ログインします。",
        "현재 마스터 비밀번호:":
            "現在のマスターパスワード:",
        "현재 비밀번호가 틀렸습니다.":
            "現在のパスワードが間違っています。",
        "현재 사용자 삭제...":
            "現在のユーザーを削除...",
        "현재 주소로 사이트 추가":
            "現在のアドレスでサイトを追加",
        "확인":
            "OK",
        "확인 대상 저장소":
            "確認対象のリポジトリ",
        "확인(O)":
            "OK(O)",
        "확인을 위해 아이디 '{0}' 를 그대로 입력하세요:":
            "確認のため、ID「{0}」をそのまま入力してください:",
        "환경설정(S)":
            "環境設定(S)",
        "[지금 업데이트]를 누르면 새 버전을 받아 자동으로 바꿔 넣고 다시 시작합니다. data 폴더는 그대로 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "[今すぐアップデート]を押すと新しいバージョンを自動的にダウンロードして入れ替え、再起動します。dataフォルダはそのまま保持されます。(入れ替え前に「バックアップを作成」をおすすめします)",
        "{0} - 업데이트 적용":
            "{0} - アップデート適用",
        "다운로드에 실패했습니다: {0}":
            "ダウンロードに失敗しました: {0}",
        "업데이트 다운로드 중... {0}%":
            "アップデートをダウンロード中... {0}%",
        "업데이트 적용에 실패했습니다: {0}":
            "アップデートの適用に失敗しました: {0}",
        "업데이트를 적용합니다. 프로그램이 곧 다시 시작됩니다.":
            "アップデートを適用します。まもなくプログラムが再起動します。",
        "이 방식으로는 자동 업데이트를 적용할 수 없습니다. (exe 로 실행 중일 때만 가능)\n다운로드 페이지에서 새 exe 를 받아 직접 바꿔 넣어 주세요.":
            "この方法では自動アップデートを適用できません。(exeで実行している場合のみ可能)\nダウンロードページから新しいexeを取得し、ご自身で置き換えてください。",
        "지금 업데이트":
            "今すぐアップデート",
    },
    "zh": {
        "글자 크기":
            "文字大小",
        "글자 굵게 표시":
            "以粗体显示",
        "글자 크기를 바꿨습니다.":
            "已更改文字大小。",
        "굵게 표시 설정을 바꿨습니다.":
            "已更改粗体显示设置。",
        "작은 글자":
            "小号文字",
        "보통 글자":
            "正常文字",
        "큰 글자":
            "大号文字",
        "아주 큰 글자":
            "特大文字",
        "강조 색상...":
            "强调色...",
        "버튼·테두리 등에 쓸 강조 색을 골라 주세요.":
            "请选择用于按钮、边框等的强调色。",
        "직접 선택...":
            "自定义选择...",
        "강조 색상 직접 선택":
            "自定义强调色",
        "강조 색상을 바꿨습니다.":
            "已更改强调色。",
        "딥 틸 (기본)":
            "深青绿色（默认）",
        "네이비":
            "藏青色",
        "자두색":
            "梅紫色",
        "포레스트 그린":
            "森林绿",
        "슬레이트 블루":
            "石板蓝",
        "테라코타":
            "赤陶色",
        "차콜":
            "炭灰色",
        "버건디":
            "酒红色",
        "매우 약함":
            "非常弱",
        "약함":
            "弱",
        "보통":
            "一般",
        "강함":
            "强",
        "매우 강함":
            "非常强",
        "오래 안 쓴 사이트 ({0})":
            "长期未使用的网站 ({0})",
        " (오래 안 쓴 사이트)":
            " (长期未使用的网站)",
        "주요 기능":
            "主要功能",
        " · 오래 안 씀":
            " · 长期未使用",
        "검색 결과 {0}개":
            "搜索结果 {0} 个",
        "  ·  오래 안 쓴 사이트 {0}개":
            "  ·  长期未使用的网站 {0} 个",
        "■ 보관함과 사용자\n· 한 대의 컴퓨터에서 여러 사람(또는 용도별)이 각자 독립된 보관함을 쓸 수 있습니다. (서로의 정보는 볼 수 없습니다)\n· 저장한 사이트는 '그룹(폴더)'으로 나눠서 정리할 수 있고, 마우스로 끌어다 옮길 수 있습니다.\n\n■ 브라우저 연동과 채움\n· 지원하는 브라우저(Chrome·Edge·Whale 등)의 주소창을 읽어서, 지금 보고 있는 사이트의 저장된 정보를 자동으로 찾아줍니다. (Windows 전용)\n· [채움] 버튼 하나로 아이디·비밀번호를 브라우저 입력칸에 자동으로 넣어 줍니다.\n\n■ 검색\n· 메인 창에서 Ctrl+F(또는 돋보기 버튼)를 누르면 검색창이 열립니다. 사이트 설명·주소·키워드·아이디로 모든 그룹을 한 번에 찾아 줍니다.\n· 검색 중에도 그룹(폴더) 구조는 그대로 보이며, 찾은 사이트가 들어 있는 그룹만 펼쳐서 보여 줍니다.\n\n■ 비밀번호 강도 표시\n· 새 비밀번호를 만들 때(회원가입, 사이트 추가/수정) 길이와 문자 종류를 보고 '매우 약함~매우 강함'을 막대와 글자로 바로 보여 줍니다.\n\n■ 안 쓰는 사이트 알림\n· 오랫동안(기본 180일) [채움]이나 비밀번호 복사로 쓰지 않은 사이트는 목록에 주황색으로 '오래 안 씀' 표시가 붙습니다.\n· 로그인하면 오래 안 쓴 사이트가 몇 개인지 요약으로 알려 줍니다. 더 안 쓰는 계정은 정리하거나 비밀번호를 새로 바꾸는 걸 권장합니다.\n· [목록관리] 창 왼쪽의 '오래 안 쓴 사이트'를 누르면 그룹과 상관없이 오래 안 쓴 사이트만 한 번에 모아서 볼 수 있습니다. (오래 쓴 순서대로 정렬)\n\n■ 백업\n· 로그인할 때마다 자동으로 백업됩니다.\n· 원하는 위치(USB, 클라우드 동기화 폴더 등)에 자동 또는 수동으로 백업하도록 설정할 수 있습니다.\n· 기본은 암호화된 백업이며, 필요하면 암호화되지 않은 CSV로도 내보낼 수 있습니다 (내보낼 때 경고가 표시됩니다).\n\n■ 들고 다니기 (USB)\n· exe 파일 옆에 생기는 'data' 폴더만 있으면 되므로, 둘을 함께 USB에 넣어 다른 컴퓨터에서도 바로 쓸 수 있습니다.\n\n■ 업데이트\n· 새 버전이 나오면 알려 주고, [지금 업데이트]를 누르면 새 exe로 자동 교체 · 재시작됩니다.\n\n■ 여러 언어\n· 한국어 · English · 日本語 · 简体中文을 지원합니다. 환경설정에서 언제든 바꿀 수 있습니다.":
            "■ 保险库和用户\n· 一台电脑上可以有多个用户(或按用途)各自使用独立的保险库。(彼此的信息互不可见)\n· 保存的网站可以按'分组(文件夹)'整理，并可以用鼠标拖动移动。\n\n■ 浏览器联动与自动填充\n· 读取支持的浏览器(Chrome·Edge·Whale 等)的地址栏，自动查找当前所浏览网站的已保存信息。(仅限 Windows)\n· 点一下[填充]按钮即可自动将账号·密码填入浏览器输入框。\n\n■ 搜索\n· 在主窗口按 Ctrl+F(或点击放大镜按钮)即可打开搜索框，可按网站名称·网址·关键词·账号一次性搜索所有分组。\n· 搜索时分组(文件夹)结构依然保留，只会展开含有匹配结果的分组。\n\n■ 密码强度显示\n· 创建新密码时(注册、添加/编辑网站)，会根据长度和字符种类即时用进度条和文字显示'非常弱~非常强'。\n\n■ 长期未使用网站提醒\n· 长时间(默认180天)未通过[填充]或复制密码使用过的网站，会在列表中以橙色标注'长期未使用'。\n· 登录后会在状态栏提示有多少个长期未使用的网站，建议整理或更换这些账号的密码。\n· 点击[列表管理]窗口左侧的'长期未使用的网站'，即可不分分组、一次性查看所有长期未使用的网站(按未使用时间从长到短排序)。\n\n■ 备份\n· 每次登录都会自动备份。\n· 可以设置自动或手动备份到您指定的位置(USB、云同步文件夹等)。\n· 默认是加密备份，如有需要也可以导出未加密的 CSV(导出时会显示警告)。\n\n■ 随身携带 (USB)\n· 只需要 exe 文件旁生成的 'data' 文件夹，把两者一起放进 U 盘，就能在其他电脑上直接使用。\n\n■ 更新\n· 有新版本时会通知您，点击[立即更新]即可自动替换新 exe 并重启。\n\n■ 多语言\n· 支持韩语·English·日本語·简体中文，可以随时在设置中更改。",
        "■ 내 정보는 어떻게 보호되나요? (쉽게 설명)\n· 모든 정보는 '암호화'되어 저장됩니다. 암호화란, 마스터 비밀번호가 없으면 아무도 — 프로그램을 만든 사람도 — 내용을 읽을 수 없도록 뒤섞어 두는 것입니다.\n   (전문 용어로는 AES-256-GCM 방식입니다. 지금의 기술로는 사실상 풀 수 없다고 알려진 수준의 암호화 방식이라고 이해하시면 됩니다)\n· 마스터 비밀번호 자체는 어디에도 그대로 저장되지 않습니다. 비밀번호를 아주 여러 번 복잡한 계산을 거쳐 '잠금을 푸는 열쇠'로 바꾼 뒤, 그 열쇠로만 보관함을 엽니다.\n   (전문 용어로는 scrypt 방식입니다. 이렇게 하면 누군가 비밀번호를 무작위로 하나씩 맞혀 보려고 해도, 한 번 시도하는 데 시간이 오래 걸려서 사실상 불가능해집니다)\n· 정보는 이 컴퓨터의 data 폴더에만 저장됩니다. 인터넷 어디로도 보내지지 않습니다.\n· 인터넷에 연결되는 경우는 '새 버전이 나왔는지' 확인할 때뿐이며, 이때도 저장된 아이디·비밀번호는 전혀 전송되지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ 我的信息是如何被保护的? (通俗解释)\n· 所有信息都会被'加密'后保存。加密的意思是，没有主密码任何人——包括程序的作者——都无法读取其中内容，相当于把内容打乱重排。\n   (专业术语是 AES-256-GCM 方式。可以理解为以目前的技术水平事实上无法破解的加密方式)\n· 主密码本身不会以原始形式保存在任何地方。密码会经过多次复杂运算转换成'解锁用的密钥'，只有这把密钥才能打开保险库。\n   (专业术语是 scrypt 方式。这样一来，即使有人想逐一猜测密码，每次尝试都要花很长时间，实际上几乎不可能破解)\n· 信息只保存在这台电脑的 data 文件夹中，不会通过互联网发送到任何地方。\n· 唯一需要联网的情况是检查'是否有新版本'，此时也完全不会发送已保存的账号·密码。\n\n■ 自动保护功能\n· 10分钟内没有操作会自动返回登录窗口。\n· 复制的密码会在20秒后从剪贴板中清除。\n· 密码在屏幕上默认以 ●●● 遮挡显示。\n· 登录时密码连续输错5次，程序会自动退出。\n\n■ 注意事项\n· 主密码无法找回，请在其他地方妥善记下并保管好。\n· 如果这台电脑感染病毒，任何密码管理软件都无法保证安全，请及时更新杀毒软件。\n· 在公用电脑上使用后请务必退出登录。",
        "'{0}' 그룹으로 {1}개 사이트를 묶었습니다.":
            "已将 {1} 个网站合并到分组 '{0}'。",
        "'{0}' 로 옮겼습니다.":
            "已移至 '{0}'。",
        "'{0}' 사이트 정보를":
            "网站 '{0}' 的信息",
        "'{0}' 사이트 정보를 삭제할까요?":
            "要删除网站 '{0}' 的信息吗?",
        "'{0}' 안에 만들 새 그룹 이름:":
            "在 '{0}' 中新建的分组名称:",
        "'{0}' 의 마스터 비밀번호를 입력하세요:":
            "请输入 '{0}' 的主密码:",
        "'위치'는 이 그룹을 어느 그룹 안에 둘지입니다. 그룹을 삭제해도 안에 있던 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.":
            "'位置'指此分组放在哪个分组内。删除分组后,其中的网站不会被删除,而是移至上级分组。",
        "({0}초 후 클립보드 삭제)":
            "({0}秒后清除剪贴板)",
        "(검색 결과)":
            "(搜索结果)",
        "(설정되지 않음)":
            "(未设置)",
        "8자 이상 입력하세요.":
            "请至少输入8个字符。",
        "CSV (표 파일) — 암호화되지 않음":
            "CSV (表格文件) — 未加密",
        "CSV 가져오기":
            "导入 CSV",
        "CSV 가져오기·내보내기":
            "CSV 导入·导出",
        "CSV 내보내기 (암호화 안 됨)":
            "导出 CSV (未加密)",
        "CSV 데이터가 없습니다.":
            "没有 CSV 数据。",
        "CSV 백업은 암호화되지 않습니다.\n\n모든 사이트의 아이디와 비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다.\n\n그래도 CSV로 백업할까요?\n(권장: 암호화 백업)":
            "CSV 备份不会加密。\n\n所有网站的账号和密码都将以明文保存。如果该文件夹位于云端或他人可以查看的位置,内容将全部暴露。\n\n仍要以 CSV 备份吗?\n(建议: 加密备份)",
        "CSV(암호화 안 됨) 백업 완료: {0}":
            "CSV (未加密) 备份完成: {0}",
        "GitHub 저장소의 최신 Release 를 확인해서 새 버전이 있으면 알려 드립니다. 자동으로 설치하지는 않으며, 다운로드 페이지만 열어 줍니다. (새 exe 로 바꿔도 data 폴더의 정보는 그대로 유지됩니다)":
            "检查 GitHub 仓库的最新 Release,如有新版本会通知您。不会自动安装,只会打开下载页面。(更换为新的 exe 后,data 文件夹中的信息仍会保留)",
        "INFO : 입력하신 정보는 암호화되어 사용자의\n컴퓨터에 저장되며 인터넷으로 전송되지\n않으므로 회원가입이 필요 없습니다.\n\n※ 비밀번호를 잊으면 복구할 수 없습니다.":
            "INFO : 您输入的信息经加密后保存在\n您的电脑中,不会通过互联网传输,\n因此无需注册会员。\n\n※ 忘记密码将无法找回。",
        "Q. [채움]을 눌러도 입력이 안 돼요.\nA. ① 브라우저 아이디 입력칸을 먼저 클릭했는지, ② 관리자 권한으로 실행된 창이 아닌지 확인하세요.\n   일부 사이트는 보안 키패드를 써서 자동 입력이 막힙니다. 이때는 값을 복사해서 입력하세요.\n\nQ. 브라우저 주소가 자동으로 안 들어와요.\nA. ① 환경설정 메뉴의 '브라우저 주소 자동 연동'이 켜져 있는지, ② 지원 브라우저인지 확인하세요.\n   ↻ 버튼(F5)으로 즉시 읽기를 시도해 보고, 안 되면 주소를 직접 붙여넣으세요.\n\nQ. 마스터 비밀번호를 잊었어요.\nA. 복구할 방법이 없습니다. 이전 백업의 비밀번호가 기억난다면 백업에서 복원해 보세요.\n   포기하고 새로 시작하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 지우고(또는 다른 곳으로 옮기고)\n   새 사용자를 만드세요.\n\nQ. 프로그램을 다시 설치/이동하면 정보가 사라지나요?\nA. 정보는 프로그램 옆의 data 폴더에 있습니다. 프로그램(exe)을 옮길 때 data 폴더도 같이 옮기세요.\n\nQ. 다른 드라이브나 클라우드에 자동으로 백업하고 싶어요.\nA. 파일 메뉴 '백업 위치 설정'에서 폴더를 고르세요. 클라우드라면 그 서비스의 동기화 폴더를 고르면 됩니다.\n   (도움말 '백업과 복원' 참고. 암호화 백업을 권장합니다)\n\nQ. 다른 컴퓨터에서도 쓰고 싶어요.\nA. 'CSV'는 위험하니 쓰지 말고, '백업 만들기'로 저장한 파일을 새 컴퓨터에서 '백업에서 복원' 하세요.\n   (data 폴더를 통째로 복사해도 됩니다)\n\nQ. 백신이 exe 파일을 의심해요.\nA. 개인이 만든 프로그램은 서명이 없어 오탐이 생기기도 합니다. 특히 [채움]이 키보드 입력을 대신 하기 때문입니다.\n   소스(mypass.py)를 직접 확인하거나 예외 목록에 등록하세요.\n\nQ. 알패스에서 쓰던 정보를 옮기고 싶어요.\nA. 알패스가 정보를 CSV 등으로 내보낼 수 있다면 'CSV 가져오기'를 쓰세요. 없다면 직접 입력해야 합니다.":
            "Q. 点击 [填充] 后没有输入内容。\nA. 请确认: ① 是否已先点击浏览器中的账号输入框;② 浏览器窗口是否是以管理员权限运行的。\n   部分网站使用安全键盘,会阻止自动输入。此时请复制数值后手动输入。\n\nQ. 浏览器地址没有自动填入。\nA. 请确认: ① 设置菜单中的'自动关联浏览器地址'是否已开启;② 是否为支持的浏览器。\n   可点击 ↻ 按钮(F5)立即尝试读取,如果仍不行,请直接粘贴地址。\n\nQ. 我忘记了主密码。\nA. 无法找回。如果记得以前备份的密码,可以尝试从备份恢复。\n   如果决定放弃并重新开始,请关闭程序后,在 data 文件夹中删除(或移到别处)对应的 '账号.dat' 文件,\n   然后创建新用户。\n\nQ. 重新安装/移动程序后信息会丢失吗?\nA. 信息保存在程序旁边的 data 文件夹中。移动程序(exe)时,请一并移动 data 文件夹。\n\nQ. 我想自动备份到其他磁盘或云端。\nA. 在文件菜单的'设置备份位置'中选择文件夹。如果是云端,选择该服务的同步文件夹即可。\n   (参见帮助中的'备份与恢复'。建议使用加密备份)\n\nQ. 我想在其他电脑上也使用。\nA. 'CSV'有风险,请不要使用。请将通过'创建备份'保存的文件,在新电脑上通过'从备份恢复'来恢复。\n   (也可以整个复制 data 文件夹)\n\nQ. 杀毒软件怀疑 exe 文件有问题。\nA. 个人制作的程序没有签名,有时会出现误报。尤其是 [填充] 会代替键盘进行输入。\n   请自行检查源码(mypass.py),或将其添加到排除列表。\n\nQ. 我想迁移在 ALPass 中使用的信息。\nA. 如果 ALPass 可以将信息导出为 CSV 等格式,请使用'导入 CSV'。否则需要手动输入。",
        "{0}  v{1}\n\n아이디·비밀번호·사이트 정보를 암호화해서\n보관하는 개인용 비밀번호 관리 프로그램":
            "{0}  v{1}\n\n加密保存账号、密码和网站信息的\n个人密码管理程序",
        "{0} - 그룹 수정":
            "{0} - 编辑分组",
        "{0} - 그룹 이동":
            "{0} - 移动分组",
        "{0} - 그룹으로 이동":
            "{0} - 移至分组",
        "{0} - 도움말":
            "{0} - 帮助",
        "{0} - 로그인":
            "{0} - 登录",
        "{0} - 목록관리":
            "{0} - 列表管理",
        "{0} - 백업 위치 설정":
            "{0} - 设置备份位置",
        "{0} - 사이트 {1}":
            "{0} - 网站{1}",
        "{0} - 새 버전":
            "{0} - 新版本",
        "{0} - 새 사용자 등록":
            "{0} - 注册新用户",
        "{0} - 업데이트 설정":
            "{0} - 更新设置",
        "{0} - 정보":
            "{0} - 关于",
        "{0} 복사됨":
            "已复制{0}",
        "{0} 삭제할까요?":
            "要删除{0}吗?",
        "{0}개 사이트를 '{1}' 로 옮겼습니다.":
            "已将 {0} 个网站移至 '{1}'。",
        "{0}개 사이트를 가져왔습니다.":
            "已导入 {0} 个网站。",
        "{0}곳을 찾았습니다. 입력칸 오른쪽 ▼ 에서 고르세요.":
            "找到 {0} 处。请在输入框右侧的 ▼ 中选择。",
        "{0}님 로그인":
            "{0} 登录",
        "· 암호화: AES-256-GCM / scrypt\n· 정보는 이 컴퓨터에만 저장되며 인터넷으로 전송되지 않습니다.\n· (인터넷은 업데이트 확인에만 사용하며, 정보는 보내지 않습니다)\n· 데이터 폴더:\n   {0}":
            "· 加密: AES-256-GCM / scrypt\n· 信息仅保存在此电脑中,不会通过互联网传输。\n· (互联网仅用于检查更新,不会发送任何信息)\n· 数据文件夹:\n   {0}",
        "■ 가져오기\n· 파일 메뉴 'CSV 가져오기'. 엑셀에서 만든 표나 다른 프로그램에서 내보낸 파일을 읽습니다.\n· 첫 줄(제목줄)에 다음 이름이 있으면 자동으로 인식합니다.\n   그룹(폴더) / 사이트 설명(사이트명, name) / 주소(url) / 주소 키워드 / 아이디(id) / 비밀번호(password)\n· 주소가 없는 줄은 건너뜁니다. 주소 키워드가 비어 있으면 자동으로 만듭니다.\n· '그룹' 칸에 업무/은행 처럼 적으면 그룹이 자동으로 만들어집니다. ('폴더'라는 제목도 인식합니다)\n\n■ 내보내기\n· 파일 메뉴 'CSV 내보내기'. 엑셀로 열 수 있습니다.\n· ※ 내보낸 CSV는 암호화되어 있지 않습니다. 비밀번호가 그대로 보이므로 사용 후 반드시 지우세요.\n· 백업 용도라면 CSV 대신 '백업 만들기'를 사용하세요.":
            "■ 导入\n· 文件菜单'导入 CSV'。可读取用 Excel 制作的表格或其他程序导出的文件。\n· 如果第一行(标题行)中有以下名称,将被自动识别。\n   分组(文件夹) / 网站说明(网站名, name) / 地址(url) / 地址关键字 / 账号(id) / 密码(password)\n· 没有地址的行将被跳过。如果地址关键字为空,会自动生成。\n· 在'分组'列中填写如 工作/银行 时,会自动创建分组。(也能识别标题为'文件夹'的列)\n\n■ 导出\n· 文件菜单'导出 CSV'。可用 Excel 打开。\n· ※ 导出的 CSV 未加密。密码会直接显示,使用后请务必删除。\n· 如果是用于备份,请使用'创建备份',不要使用 CSV。",
        "■ 기본 크기\n처음 열 때는 화면 배율(125%, 150% 등)에 맞춰 보정한 기본 크기로 열립니다. 어느 컴퓨터에서나 같은 모양으로 나옵니다.\n\n■ 마음대로 조절\n창 가장자리를 끌어 크기를 자유롭게 줄이고 늘릴 수 있고, 옮겨 둔 위치도 기억합니다.\n메인 창, 목록관리 창, 도움말 창이 각각 따로 기억됩니다. 너무 작아지지 않도록 최소 크기는 정해져 있습니다.\n\n■ 되돌리기\n환경설정 메뉴 → '창 크기 초기화' 를 누르면 기본 크기로 돌아갑니다.\n(모니터를 바꾸는 등으로 저장된 위치가 화면 밖이 되면 자동으로 기본 위치에서 열립니다)":
            "■ 默认大小\n首次打开时,会按屏幕缩放比例(125%、150% 等)校正为默认大小。在任何电脑上外观都一致。\n\n■ 自由调整\n拖动窗口边缘即可自由缩小或放大,也会记住移动后的位置。\n主窗口、列表管理窗口、帮助窗口会分别记忆。为避免过小,设有最小尺寸。\n\n■ 恢复\n点击设置菜单 → '重置窗口大小' 即可恢复为默认大小。\n(如果因更换显示器等原因导致已保存的位置超出屏幕,将自动在默认位置打开)",
        "■ 메인 창\nF1          도움말\nF5          브라우저 주소 지금 가져오기\nCtrl+N      사이트 추가\nCtrl+F      검색창 열기/닫기 (설명·주소·키워드·아이디로 전체 검색, Esc 로 닫기)\nEnter       (주소 칸에서) 사이트 열기\n더블클릭    (아이디/비밀번호 값) 복사 · (목록의 사이트) 열기\n끌어서 놓기 (메인 목록) 사이트·그룹을 다른 그룹 위에 끌어 이동\nCtrl+A      (목록관리 창) 사이트 전체 선택\n오른쪽 클릭 (값/목록) 메뉴\n\n■ 로그인 창\nEnter / Alt+O   확인\nAlt+C           취소\nAlt+N           새 사용자\n\n■ 모든 창\nEsc             창 닫기(취소)":
            "■ 主窗口\nF1          帮助\nF5          立即获取浏览器地址\nCtrl+N      添加网站\nCtrl+F      打开/关闭搜索框 (按名称·网址·关键词·账号全局搜索，按 Esc 关闭)\nEnter       (在地址栏中) 打开网站\n双击        (账号/密码值) 复制 · (列表中的网站) 打开\n拖放        (主列表) 将网站·分组拖到其他分组上进行移动\nCtrl+A      (列表管理窗口) 全选网站\n右键单击    (值/列表) 菜单\n\n■ 登录窗口\nEnter / Alt+O   确定\nAlt+C           取消\nAlt+N           新用户\n\n■ 所有窗口\nEsc             关闭窗口(取消)",
        "■ 어떻게 보호되나요?\n· 모든 정보는 AES-256-GCM 으로 암호화되어 저장됩니다.\n· 마스터 비밀번호에서 암호화 키를 만들 때 scrypt 방식을 써서 비밀번호 대입 공격을 어렵게 합니다.\n· 정보는 이 컴퓨터(data 폴더)에만 저장되고, 인터넷으로 전송되지 않습니다.\n· 인터넷은 업데이트 확인(GitHub 에서 최신 버전 번호 조회)에만 쓰이며, 저장된 정보는 전혀 보내지 않습니다.\n\n■ 자동 보호 기능\n· 10분 동안 조작이 없으면 로그인 창으로 돌아갑니다.\n· 복사한 비밀번호는 20초 뒤 클립보드에서 지워집니다.\n· 비밀번호는 화면에서 기본적으로 ●●● 로 가려집니다.\n· 로그인에서 비밀번호를 5번 틀리면 프로그램이 종료됩니다.\n\n■ 주의하실 점\n· 마스터 비밀번호는 복구할 수 없습니다. 다른 곳에 안전하게 적어 두세요.\n· 이 컴퓨터가 바이러스에 감염되면 어떤 비밀번호 관리자도 안전하지 않습니다. 백신을 최신으로 유지하세요.\n· 공용 컴퓨터에서는 사용 후 반드시 종료하세요.":
            "■ 如何保护?\n· 所有信息均使用 AES-256-GCM 加密后保存。\n· 从主密码生成加密密钥时采用 scrypt 方式,使暴力破解密码变得困难。\n· 信息仅保存在此电脑(data 文件夹)中,不会通过互联网传输。\n· 互联网仅用于检查更新(从 GitHub 查询最新版本号),绝不会发送已保存的信息。\n\n■ 自动保护功能\n· 10分钟内没有任何操作,将返回登录窗口。\n· 复制的密码会在20秒后从剪贴板中清除。\n· 密码在屏幕上默认以 ●●● 隐藏显示。\n· 登录时密码输错5次,程序将退出。\n\n■ 注意事项\n· 主密码无法找回。请另外安全地记录在其他地方。\n· 如果这台电脑感染病毒,任何密码管理器都不安全。请保持杀毒软件为最新。\n· 在公用电脑上使用后,请务必退出程序。",
        "■ 자동 백업 (아무것도 안 해도 됩니다)\n· 로그인할 때마다 data\\backup 폴더에 '아이디_날짜.mpbak' 사본이 만들어집니다. (하루 1개, 최근 10개 보관)\n· 저장할 때마다 같은 폴더에 '아이디.dat.bak' (직전 상태)도 만들어집니다.\n\n■ 직접 백업\n파일 메뉴 '백업 만들기' → 원하는 위치(USB, 클라우드 폴더 등)에 저장합니다.\n백업 파일은 암호화되어 있어 남이 열어볼 수 없습니다.\n\n■ 복원\n· 로그인한 뒤 파일 메뉴 '백업에서 복원' (로그인 창에는 복원 버튼이 없습니다)\n· 새 컴퓨터라면: 로그인 창에서 [새 사용자]로 임시 사용자를 만들어 로그인 → '백업에서 복원' →\n   복원이 끝나면 '다른 사용자로 로그인'으로 복원한 사용자에 들어갑니다. (임시 사용자는 '현재 사용자 삭제'로 정리)\n· 백업 파일 선택 → 백업 당시의 마스터 비밀번호 입력 → 복원할 아이디 입력\n· 같은 아이디가 있으면 덮어쓸지 묻고, 기존 파일은 data\\_deleted 에 보관됩니다.\n· 복원 후에는 백업 당시의 마스터 비밀번호로 로그인합니다.\n\n■ 백업 위치 (내가 정한 폴더에 자동 백업)\n· 파일 메뉴 '백업 위치 설정'에서 백업을 저장할 폴더를 지정합니다. 로그인할 때, 정보를 바꾼 뒤, 종료할 때\n   그 폴더의 MyPass_backup 안에 자동으로 백업합니다. (위의 data\\backup 자동 백업과는 별개입니다)\n· 폴더는 어디든 됩니다: 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS),\n   또는 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더. [클라우드 찾기]로 흔한 클라우드 폴더를 찾을 수 있습니다.\n· 클라우드에 직접 로그인하지 않습니다. 이 컴퓨터에 클라우드 프로그램이 설치·로그인되어 있어야 하며, 올리는 일은 그 프로그램이 합니다.\n· 프로그램 데이터와 같은 드라이브(같은 USB)를 고르면 함께 사라질 수 있다고 알려 줍니다. 다른 장치를 권장합니다.\n· 경로에 %USERPROFILE%\\OneDrive 처럼 환경변수를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.\n· 기본은 '암호화 백업(.mpbak)'입니다. 마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 되살립니다.\n   (아이디_latest.mpbak = 최신본, 아이디_날짜.mpbak = 날짜별 사본)\n· 'CSV' 형식도 고를 수 있지만 암호화되지 않아 비밀번호가 글자 그대로 저장됩니다. 꼭 필요할 때만 쓰세요.\n   (아이디_latest.csv 한 파일만 덮어쓰며, 되살릴 때는 'CSV 가져오기'를 사용)\n· 설정한 폴더가 그 컴퓨터에 없으면(다른 PC, USB 미연결 등) 백업을 건너뛰고 상태줄에 알려 줍니다.\n· [지금 백업] 또는 파일 메뉴 '지금 백업 위치에 백업'으로 바로 실행할 수 있고, 마지막 결과는 설정 창에 표시됩니다.\n· 이 설정은 모든 사용자에게 공통이며, 백업 파일 이름에 사용자 아이디가 들어갑니다.\n\n■ 권장 습관\n중요한 정보라면 가끔 '백업 만들기'로 다른 저장 장치에도 사본을 두세요.\n컴퓨터가 고장 나면 data 폴더도 함께 사라집니다.":
            "■ 自动备份 (无需任何操作)\n· 每次登录时,会在 data\\backup 文件夹中生成 '账号_日期.mpbak' 副本。(每天1个,保留最近10个)\n· 每次保存时,也会在同一文件夹中生成 '账号.dat.bak' (上一次的状态)。\n\n■ 手动备份\n文件菜单'创建备份' → 保存到所需位置(USB、云端文件夹等)。\n备份文件已加密,他人无法打开。\n\n■ 恢复\n· 登录后,在文件菜单选择'从备份恢复' (登录窗口中没有恢复按钮)\n· 如果是新电脑: 在登录窗口通过 [新用户] 创建临时用户并登录 → '从备份恢复' →\n   恢复完成后,通过'以其他用户登录'进入已恢复的用户。(临时用户可通过'删除当前用户'清理)\n· 选择备份文件 → 输入备份时的主密码 → 输入要恢复的账号\n· 如果已有相同账号,会询问是否覆盖,原有文件将保存在 data\\_deleted 中。\n· 恢复后,请使用备份时的主密码登录。\n\n■ 备份位置 (自动备份到我指定的文件夹)\n· 在文件菜单'设置备份位置'中指定保存备份的文件夹。登录时、修改信息后、退出时,\n   会自动备份到该文件夹的 MyPass_backup 中。(与上述 data\\backup 自动备份相互独立)\n· 文件夹可以是任意位置: 其他磁盘、移动硬盘·USB、网络驱动器(NAS),\n   或 OneDrive·Google 云端硬盘·Dropbox·NAVER MYBOX 等云端同步文件夹。可通过 [查找云端] 找到常见的云端文件夹。\n· 不会直接登录云端。此电脑上需要已安装并登录云端程序,上传工作由该程序完成。\n· 如果选择与程序数据相同的磁盘(同一个 USB),会提示可能一起丢失。建议使用其他设备。\n· 路径中使用 %USERPROFILE%\\OneDrive 之类的环境变量时,即使每台电脑的用户名不同,也只需设置一次。\n· 默认为'加密备份(.mpbak)'。没有主密码无法打开,可通过'从备份恢复'还原。\n   (账号_latest.mpbak = 最新备份,账号_日期.mpbak = 按日期的副本)\n· 也可以选择 'CSV' 格式,但它不加密,密码会以明文保存。仅在确有必要时使用。\n   (只会覆盖 账号_latest.csv 这一个文件,恢复时请使用'导入 CSV')\n· 如果设置的文件夹在该电脑上不存在(其他电脑、未连接 USB 等),将跳过备份并在状态栏提示。\n· 可通过 [立即备份] 或文件菜单'立即备份到备份位置'直接执行,最近一次的结果会显示在设置窗口中。\n· 此设置对所有用户通用,备份文件名中包含用户账号。\n\n■ 推荐习惯\n如果信息很重要,请偶尔通过'创建备份'在其他存储设备中也保留一份副本。\n电脑损坏时,data 文件夹也会一并丢失。",
        "■ 처음 사용할 때\n1. 프로그램을 실행하면 로그인 창이 나옵니다. [새 사용자(N)]를 눌러 아이디와 마스터 비밀번호를 등록합니다.\n2. 등록한 아이디와 비밀번호로 로그인합니다.\n3. 메인 창의 [추가] 버튼으로 자주 쓰는 사이트의 주소, 아이디, 비밀번호를 저장합니다.\n\n■ 마스터 비밀번호란?\n저장한 모든 정보를 잠그는 열쇠입니다. 8자 이상으로 정하고 꼭 기억해 두세요.\n잊어버리면 누구도 복구할 수 없습니다. (프로그램 제작자도 마찬가지입니다)\n\n■ 화면 구성\n· 위쪽 버튼: 목록관리 / 추가(▾ 메뉴) / 수정 / 삭제\n· 주소 칸: 주소를 입력하거나 브라우저에서 자동으로 가져옵니다.\n   ➜ 사이트 열기,  ↻ 브라우저 주소 지금 가져오기\n· 사이트 정보 표시줄: 저장된 정보가 있으면 초록 ✔, 없으면 회색 표시\n· 아이디·비밀번호 칸과 [채움] 버튼\n· 아래 목록: 그룹과 저장된 사이트 (끌어서 그룹으로 이동)\n· 맨 아래 상태줄: 현재 로그인한 사용자와 안내 메시지":
            "■ 首次使用\n1. 运行程序后会出现登录窗口。点击 [新用户(N)],注册账号和主密码。\n2. 使用注册的账号和密码登录。\n3. 通过主窗口的 [添加] 按钮,保存常用网站的地址、账号和密码。\n\n■ 什么是主密码?\n它是锁定所有已保存信息的钥匙。请设置为8个字符以上,并务必牢记。\n一旦忘记,任何人都无法找回。(程序作者也一样)\n\n■ 界面构成\n· 顶部按钮: 列表管理 / 添加(▾ 菜单) / 编辑 / 删除\n· 地址栏: 输入地址,或从浏览器自动获取。\n   ➜ 打开网站,  ↻ 立即获取浏览器地址\n· 网站信息栏: 有已保存的信息时显示绿色 ✔,没有时显示灰色\n· 账号·密码输入框和 [填充] 按钮\n· 下方列表: 分组和已保存的网站 (拖动到分组即可移动)\n· 最下方状态栏: 当前登录的用户和提示信息",
        "■ 추가\n[추가] 버튼 → 주소, 아이디, 비밀번호를 입력하고 [확인].\n· 주소 칸에 이미 주소가 들어 있으면 그 주소로 창이 열립니다.\n· [추가] 옆 ▾ 에서 '빈 사이트 추가', '그룹 추가'도 고를 수 있습니다.\n· 비밀번호 옆 [생성] 버튼은 16자리 무작위 비밀번호를 만들어 줍니다. [보기]로 확인하세요.\n· 가입할 때 쓴 비밀번호를 그대로 저장하세요. 생성한 비밀번호는 사이트에도 같이 바꿔 주어야 합니다.\n\n■ 수정 / 삭제\n· 목록에서 사이트를 고르고 [수정] 또는 [삭제].\n· 목록의 사이트를 더블클릭하면 주소가 채워지고 사이트가 열립니다.\n· 목록에서 오른쪽 클릭하면 사이트 열기 / 수정 / 삭제 메뉴가 나옵니다.\n\n■ 같은 사이트에 계정이 여러 개일 때\n같은 주소로 사이트를 여러 개 저장하면, 주소가 맞을 때 주소 칸 아래 작은 목록에 모두 나타납니다. 쓸 계정을 고르세요.":
            "■ 添加\n[添加] 按钮 → 输入地址、账号、密码,然后点击 [确定]。\n· 如果地址栏中已有地址,则会以该地址打开窗口。\n· 在 [添加] 旁的 ▾ 中,还可以选择'添加空网站'、'添加分组'。\n· 密码旁的 [生成] 按钮会生成16位随机密码。请通过 [显示] 确认。\n· 请原样保存注册时使用的密码。生成的密码也需要在网站上同步修改。\n\n■ 编辑 / 删除\n· 在列表中选择网站,然后点击 [编辑] 或 [删除]。\n· 双击列表中的网站,会填入地址并打开该网站。\n· 在列表中右键单击,会出现 打开网站 / 编辑 / 删除 菜单。\n\n■ 同一网站有多个账号时\n如果用相同地址保存了多个网站,当地址匹配时,它们都会显示在地址栏下方的小列表中。请选择要使用的账号。",
        "⚠ 모든 아이디·비밀번호가 글자 그대로 저장됩니다. 그 폴더가 클라우드이거나 다른 사람이 볼 수 있는 곳이면 전부 노출됩니다. 엑셀로 바로 열어 볼 수 있다는 점이 장점입니다.":
            "⚠ 所有账号·密码都将以明文保存。如果该文件夹位于云端或他人可以查看的位置,内容将全部暴露。优点是可以直接用 Excel 打开查看。",
        "✎ 수정":
            "✎ 编辑",
        "✔ 성공":
            "✔ 成功",
        "✕ 삭제":
            "✕ 删除",
        "✖ 실패":
            "✖ 失败",
        "값을 더블클릭하면 복사됩니다 · 오른쪽 클릭: 메뉴":
            "双击数值即可复制 · 右键单击: 菜单",
        "개 (암호화 백업만 · 최신본은 항상 따로 저장)":
            "份 (仅限加密备份 · 最新备份始终单独保存)",
        "검색":
            "搜索",
        "관리(T)":
            "管理(T)",
        "그룹":
            "分组",
        "그룹 '{0}' 을(를) 넣을 그룹을 고르세요.":
            "请选择要放入分组 '{0}' 的目标分组。",
        "그룹 삭제":
            "删除分组",
        "그룹 이름":
            "分组名称",
        "그룹 이름 변경":
            "重命名分组",
        "그룹 이름:":
            "分组名称:",
        "그룹 이름을 입력하세요.":
            "请输入分组名称。",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.":
            "分组名称为空,或已存在同名分组。",
        "그룹 이름이 비었거나, 같은 이름의 그룹이 이미 있습니다.\n(/ \\ 문자는 사용할 수 없습니다)":
            "分组名称为空,或已存在同名分组。\n(不能使用 / \\ 字符)",
        "그룹 추가":
            "添加分组",
        "그룹과 목록관리":
            "分组与列表管理",
        "그룹과 하위 그룹을 삭제합니다.\n안에 있던 사이트 정보는 상위 그룹으로 옮겨집니다.\n(사이트는 지워지지 않습니다) 계속할까요?":
            "将删除该分组及其子分组。\n其中的网站信息将移至上级分组。\n(网站不会被删除) 要继续吗?",
        "그룹명":
            "分组名",
        "그룹으로 이동":
            "移至分组",
        "그룹으로 이동...":
            "移至分组...",
        "나중에":
            "稍后",
        "날짜별 사본 보관:":
            "按日期保留副本:",
        "내 드라이브":
            "我的云端硬盘",
        "내보내기 완료":
            "导出完成",
        "내보낸 CSV는 암호화되지 않습니다.\n사용 후 반드시 안전하게 삭제하세요.\n계속할까요?":
            "导出的 CSV 不会加密。\n使用后请务必安全删除。\n要继续吗?",
        "다른 그룹 안으로 이동":
            "移入其他分组",
        "다른 사용자로 로그인":
            "以其他用户登录",
        "로그아웃":
            "登出",
        "자동 잠금 시간":
            "自动锁定时间",
        "자동 잠금 시간을 바꿨습니다: {0}":
            "已更改自动锁定时间：{0}",
        "5분":
            "5分钟",
        "10분":
            "10分钟",
        "15분":
            "15分钟",
        "30분":
            "30分钟",
        "사용 안 함":
            "不使用",
        "다운로드 페이지 열기":
            "打开下载页面",
        "다운로드 페이지에서 새 exe 를 받아, 지금 쓰는 exe 파일만 바꿔 넣으세요. data 폴더는 그대로 두면 정보가 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "请在下载页面获取新的 exe,只替换当前使用的 exe 文件。保持 data 文件夹不变,信息就会保留。(替换前建议先'创建备份')",
        "다음 주소에 대한 사이트 정보를 수정합니다.":
            "编辑以下地址对应的网站信息。",
        "다음 주소에 대한 사이트 정보를 추가합니다.":
            "添加以下地址对应的网站信息。",
        "단축키":
            "快捷键",
        "닫기":
            "关闭",
        "데이터 폴더 열기":
            "打开数据文件夹",
        "도움말(H)":
            "帮助(H)",
        "등록되었습니다. 비밀번호를 입력하고 로그인하세요.":
            "注册成功。请输入密码并登录。",
        "등록되지 않은 아이디입니다.\n[새 사용자]로 먼저 등록하세요.":
            "该账号未注册。\n请先通过 [新用户] 注册。",
        "로그인":
            "登录",
        "로그인할 때 하루 한 번 자동으로 확인":
            "登录时每天自动检查一次",
        "마스터 비밀번호 변경":
            "更改主密码",
        "마스터 비밀번호 없이는 열 수 없고, '백업에서 복원'으로 바로 되살릴 수 있습니다.":
            "没有主密码无法打开,可通过'从备份恢复'直接还原。",
        "마이패스 백업":
            "MyPass 备份",
        "마지막 백업: {0}  {1}\n{2}":
            "最近一次备份: {0}  {1}\n{2}",
        "모두 접기":
            "全部折叠",
        "모두 펼치기":
            "全部展开",
        "모든 그룹 접기":
            "折叠所有分组",
        "모든 그룹 펼치기":
            "展开所有分组",
        "모든 파일":
            "所有文件",
        "목록관리":
            "列表管理",
        "묶을 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "请先选择要合并的网站。(按 Ctrl/Shift 可多选)",
        "백업 만들기...":
            "创建备份...",
        "백업 완료: {0}":
            "备份完成: {0}",
        "백업 위치 백업 실패: {0}":
            "备份到备份位置失败: {0}",
        "백업 위치 설정...":
            "设置备份位置...",
        "백업 위치 자동 백업을 껐습니다.":
            "已关闭自动备份到备份位置。",
        "백업 위치 자동 백업을 켰습니다. 지금 백업하는 중...":
            "已开启自动备份到备份位置。正在立即备份...",
        "백업 위치가 지정되지 않았습니다.":
            "尚未指定备份位置。",
        "백업 위치로 자동 백업 사용":
            "启用自动备份到备份位置",
        "백업 위치에 백업 완료 ({0})":
            "已备份到备份位置 ({0})",
        "백업 파일 저장":
            "保存备份文件",
        "백업 파일을 자동으로 저장할 폴더를 정하세요. 이 컴퓨터의 다른 드라이브, 외장하드·USB, 네트워크 드라이브(NAS)는 물론 OneDrive·구글 드라이브·Dropbox·네이버 MYBOX 같은 클라우드 동기화 폴더도 됩니다.\n(클라우드는 계정에 직접 로그인하지 않으며, 이 컴퓨터의 클라우드 프로그램이 파일을 올려 줍니다)":
            "请指定自动保存备份文件的文件夹。可以是此电脑的其他磁盘、移动硬盘·USB、网络驱动器(NAS),也可以是 OneDrive·Google 云端硬盘·Dropbox·NAVER MYBOX 等云端同步文件夹。\n(不会直接登录云端账号,而是由此电脑上的云端程序上传文件)",
        "백업 폴더":
            "备份文件夹",
        "백업 폴더 선택":
            "选择备份文件夹",
        "백업 폴더를 지정하세요.":
            "请指定备份文件夹。",
        "백업 폴더를 찾을 수 없습니다. (드라이브·USB·클라우드 프로그램이 연결되어 있지 않거나, 이 컴퓨터에 없는 경로)":
            "找不到备份文件夹。(磁盘·USB·云端程序未连接,或该路径在此电脑上不存在)",
        "백업 폴더에 예전에 저장해 둔 CSV 파일(암호화 안 됨)이 남아 있습니다.\n지금 삭제할까요?\n\n{0}":
            "备份文件夹中残留有以前保存的 CSV 文件(未加密)。\n要现在删除吗?\n\n{0}",
        "백업 형식":
            "备份格式",
        "백업과 복원":
            "备份与恢复",
        "백업에서 복원...":
            "从备份恢复...",
        "백업하지 못했습니다.\n{0}":
            "备份失败。\n{0}",
        "백업하지 못했습니다: {0}":
            "备份失败: {0}",
        "백업했습니다.\n백업 파일은 암호화되어 있으며, 복원할 때 지금의 마스터 비밀번호가 필요합니다.":
            "备份完成。\n备份文件已加密,恢复时需要当前的主密码。",
        "변경":
            "更改",
        "보관함 파일이 올바르지 않아 백업하지 않았습니다.":
            "密码库文件无效,未进行备份。",
        "보관함을 열 수 없습니다.\n{0}":
            "无法打开密码库。\n{0}",
        "보기":
            "显示",
        "보안 안내":
            "安全说明",
        "복원하지 못했습니다.\n{0}":
            "恢复失败。\n{0}",
        "복원할 백업 파일 선택":
            "选择要恢复的备份文件",
        "복원할 사용자 아이디:":
            "要恢复的用户账号:",
        "복원했습니다.\n아이디 '{0}' 와(과) 백업 당시의 마스터 비밀번호로 로그인하세요.":
            "恢复完成。\n请使用账号 '{0}' 和备份时的主密码登录。",
        "브라우저 주소 가져오기":
            "获取浏览器地址",
        "브라우저 주소 연동":
            "浏览器地址关联",
        "브라우저 주소 연동은 Windows에서만 사용할 수 있습니다.":
            "浏览器地址关联仅可在 Windows 中使用。",
        "브라우저 주소 연동을 사용할 수 없습니다.":
            "无法使用浏览器地址关联。",
        "브라우저 주소 연동을 사용할 수 없습니다.\n(Windows 전용이며 uiautomation 구성 요소가 필요합니다)":
            "无法使用浏览器地址关联。\n(仅限 Windows,且需要 uiautomation 组件)",
        "브라우저 주소 연동을 사용할 수 없습니다. (uiautomation 구성 요소 없음)":
            "无法使用浏览器地址关联。(缺少 uiautomation 组件)",
        "브라우저 주소 자동 연동":
            "自动关联浏览器地址",
        "브라우저 주소 지금 가져오기\tF5":
            "立即获取浏览器地址\tF5",
        "브라우저 주소: {0}":
            "浏览器地址: {0}",
        "브라우저 주소를 읽는 중 오류가 났습니다.":
            "读取浏览器地址时出错。",
        "브라우저 주소를 읽지 못했습니다.":
            "无法读取浏览器地址。",
        "브라우저 주소를 읽지 못했습니다. (검색어 입력 중이거나 지원하지 않는 화면)":
            "无法读取浏览器地址。(正在输入搜索词,或为不支持的页面)",
        "브라우저 주소창의 주소를 자동으로 읽어 주소 칸에 넣어 줍니다. (Windows 전용)\n브라우저에서 사이트를 이동할 때마다 저장된 정보가 자동으로 나타납니다.\n\n■ 지원 브라우저\n크롬, 엣지, 웨일, 파이어폭스, 브레이브, 오페라, 비발디 등\n\n■ 사용법\n· 환경설정 메뉴의 '브라우저 주소 자동 연동' 이 켜져 있으면 자동으로 동작합니다.\n· 마이패스 창을 브라우저 옆에 두고 '항상 위에 표시' 를 켜면 가장 편합니다.\n· 바로 읽고 싶으면 ↻ 버튼 또는 F5 키를 누르세요. (직전에 사용한 브라우저에서 읽어옵니다)\n\n■ 참고\n· 마이패스 창을 클릭해도 마지막으로 읽은 주소는 그대로 유지됩니다.\n· 주소창에 검색어를 입력 중이거나, chrome:// 같은 내부 페이지는 읽지 않습니다.\n· 읽히지 않는 브라우저는 주소를 복사(Ctrl+L, Ctrl+C)해서 주소 칸에 붙여넣으세요.\n· 주소는 이 컴퓨터 안에서만 읽히며 어디로도 전송되지 않습니다.":
            "自动读取浏览器地址栏中的地址并填入地址栏。(仅限 Windows)\n每当在浏览器中切换网站时,已保存的信息会自动显示。\n\n■ 支持的浏览器\nChrome、Edge、Whale、Firefox、Brave、Opera、Vivaldi 等\n\n■ 使用方法\n· 设置菜单中的'自动关联浏览器地址'开启后会自动运行。\n· 将 MyPass 窗口放在浏览器旁边并开启'窗口置顶',最为方便。\n· 想立即读取时,请点击 ↻ 按钮或按 F5 键。(从上一次使用的浏览器读取)\n\n■ 参考\n· 即使点击 MyPass 窗口,最近读取的地址也会保持不变。\n· 正在地址栏输入搜索词时,或 chrome:// 之类的内部页面不会被读取。\n· 对于无法读取的浏览器,请复制地址(Ctrl+L, Ctrl+C)并粘贴到地址栏。\n· 地址仅在此电脑内读取,不会传输到任何地方。",
        "브라우저에서 주소를 읽는 중...":
            "正在从浏览器读取地址...",
        "비밀번호":
            "密码",
        "비밀번호 보기":
            "显示密码",
        "비밀번호 복사":
            "复制密码",
        "비밀번호 숨기기":
            "隐藏密码",
        "비밀번호 확인":
            "确认密码",
        "비밀번호(이 OS에서는 자동 채움 미지원)":
            "密码(此操作系统不支持自动填充)",
        "비밀번호가 변경되었습니다.":
            "密码已更改。",
        "비밀번호가 일치하지 않습니다.":
            "密码不一致。",
        "비밀번호가 틀렸거나 손상된 백업 파일입니다.":
            "密码错误,或备份文件已损坏。",
        "비밀번호가 틀렸습니다.":
            "密码错误。",
        "비밀번호는 8자 이상 입력하세요.":
            "密码请至少输入8个字符。",
        "비밀번호를 5회 틀려 종료합니다.":
            "密码已输错5次,程序即将退出。",
        "빈 사이트 추가":
            "添加空网站",
        "사용법\tF1":
            "使用方法\tF1",
        "사용자 '{0}' 를 등록했습니다.\n지금 이 사용자로 로그인할까요?":
            "已注册用户 '{0}'。\n要现在以该用户登录吗?",
        "사용자 '{0}' 를 삭제했습니다.\n(data\\_deleted 폴더에 보관됨)":
            "已删除用户 '{0}'。\n(已保存在 data\\_deleted 文件夹中)",
        "사용자 '{0}' 와(과) 저장된 모든 사이트 정보를 삭제합니다.\n\n파일은 data\\_deleted 폴더로 옮겨지며, 필요하면 그곳에서 되살릴 수 있습니다.\n계속할까요?":
            "将删除用户 '{0}' 及其所有已保存的网站信息。\n\n文件会被移至 data\\_deleted 文件夹,如有需要可从那里恢复。\n要继续吗?",
        "사용자 추가·전환·삭제":
            "添加·切换·删除用户",
        "사용자를 만들 수 없습니다.\n{0}":
            "无法创建用户。\n{0}",
        "사용할 수 없는 그룹 이름입니다.":
            "该分组名称不可用。",
        "사용할 수 없는 그룹 이름입니다.\n(같은 위치에 같은 이름의 그룹이 있거나, / \\ 문자가 들어 있습니다)":
            "该分组名称不可用。\n(同一位置已有同名分组,或包含 / \\ 字符)",
        "사이트 {0}개":
            "{0} 个网站",
        "사이트 설명":
            "网站说明",
        "사이트 열기":
            "打开网站",
        "사이트 정보가 없습니다.":
            "没有网站信息。",
        "사이트 정보가 있습니다.  [{0}]":
            "有网站信息。  [{0}]",
        "사이트 추가":
            "添加网站",
        "사이트 추가\tCtrl+N":
            "添加网站\tCtrl+N",
        "사이트 추가·수정·삭제":
            "添加·编辑·删除网站",
        "사이트가 많아지면 그룹으로 묶어서 정리할 수 있습니다. 그룹 안에 그룹을 만들 수도 있습니다. (예: 업무 ▸ 은행)\n\n■ 그룹 만들기\n· 메인 목록에서 오른쪽 클릭 → '그룹 추가' / '하위 그룹 추가'\n· 사이트 추가 창의 '그룹명' 옆 [새 그룹] 버튼으로 바로 만들 수 있습니다.\n\n■ 사이트를 그룹으로 옮기기 (3가지 방법)\n1. 끌어서 놓기: 메인 목록에서 사이트를 마우스로 끌어 원하는 그룹 위에 놓습니다.\n   (그룹을 다른 그룹 위에 놓으면 그 안으로 들어갑니다. 놓을 수 있는 곳은 파란색으로 표시됩니다)\n2. 사이트에서 오른쪽 클릭 → '그룹으로 이동' 에서 그룹을 고릅니다.\n3. 사이트 [수정] → '그룹명'을 바꿉니다.\n\n■ 여러 개를 한꺼번에 묶기\n[목록관리] 창에서 Ctrl 또는 Shift 를 누른 채 사이트를 여러 개 고른 다음 오른쪽 클릭\n· '새 그룹으로 묶기': 새 그룹을 만들면서 한 번에 담기\n· '그룹으로 이동': 이미 있는 그룹으로 한 번에 옮기기\n\n■ 그룹 관리\n· 이름 변경 / 다른 그룹 안으로 이동 / 삭제: 메인 목록의 오른쪽 클릭 메뉴, 또는 [목록관리] 창에서\n   그룹 오른쪽의 [수정]을 눌러 팝업에서 바꿉니다.\n· 그룹 이름 옆 숫자는 안에 든 사이트 수(하위 그룹 포함)입니다.\n· 그룹을 삭제해도 사이트는 지워지지 않고 상위 그룹으로 옮겨집니다.\n· 맨 위 '최상위' 또는 관리 메뉴에서 '모두 펼치기 / 모두 접기'를 할 수 있습니다.\n\n■ 목록관리 창 (관리대장)\n· 왼쪽: 그룹 목록 / 오른쪽: 선택한 그룹의 사이트 목록\n· 각 줄 오른쪽의 [수정]을 누르면 팝업이 열립니다. 사이트는 설명·주소·아이디·비밀번호·그룹(경로)을,\n   그룹은 이름과 위치(어느 그룹 안에 둘지)를 바꿀 수 있습니다. 사이트 줄의 [삭제]는 그 사이트를 지웁니다.\n· 위쪽: [사이트 추가] [그룹 추가], 검색칸 (사이트 설명, 주소, 키워드, 아이디로 전체 검색 · 검색 중에는 모든 그룹에서 찾음)\n· 사이트를 여러 개 골라 오른쪽 클릭: 비밀번호 복사 / 그룹으로 이동 / 새 그룹으로 묶기 / 삭제 (Ctrl+A 로 전체 선택)":
            "网站增多后,可以按分组进行整理。分组中还可以创建分组。(例如: 工作 ▸ 银行)\n\n■ 创建分组\n· 在主列表中右键单击 → '添加分组' / '添加子分组'\n· 也可以通过添加网站窗口中'分组名'旁的 [新建分组] 按钮直接创建。\n\n■ 将网站移至分组 (3种方法)\n1. 拖放: 在主列表中用鼠标将网站拖到所需分组上放下。\n   (将分组放到其他分组上,会进入该分组内。可放置的位置会以蓝色显示)\n2. 在网站上右键单击 → 在'移至分组'中选择分组。\n3. 网站 [编辑] → 更改'分组名'。\n\n■ 一次合并多个网站\n在 [列表管理] 窗口中按住 Ctrl 或 Shift 选择多个网站,然后右键单击\n· '合并到新分组': 创建新分组的同时一次性放入\n· '移至分组': 一次性移到已有的分组\n\n■ 分组管理\n· 重命名 / 移入其他分组 / 删除: 通过主列表的右键菜单,或在 [列表管理] 窗口中\n   点击分组右侧的 [编辑],在弹出窗口中更改。\n· 分组名称旁的数字是其中的网站数(含子分组)。\n· 删除分组后,网站不会被删除,而是移至上级分组。\n· 可通过最上方的'顶层'或管理菜单中的'全部展开 / 全部折叠'进行操作。\n\n■ 列表管理窗口 (管理台账)\n· 左侧: 分组列表 / 右侧: 所选分组的网站列表\n· 点击每行右侧的 [编辑] 会打开弹出窗口。网站可更改说明·地址·账号·密码·分组(路径),\n   分组可更改名称和位置(放在哪个分组内)。网站行的 [删除] 会删除该网站。\n· 顶部: [添加网站] [添加分组],搜索框 (按网站说明、地址、关键字、账号全面搜索 · 搜索时会在所有分组中查找)\n· 选择多个网站后右键单击: 复制密码 / 移至分组 / 合并到新分组 / 删除 (按 Ctrl+A 全选)",
        "사이트를 먼저 선택하세요.":
            "请先选择网站。",
        "삭제":
            "删除",
        "삭제하지 못했습니다.\n{0}":
            "删除失败。\n{0}",
        "삭제할 그룹을 선택하세요.":
            "请选择要删除的分组。",
        "삭제할 사용자를 먼저 선택하세요.":
            "请先选择要删除的用户。",
        "삭제할 사이트를 먼저 선택하세요.":
            "请先选择要删除的网站。",
        "새 그룹":
            "新建分组",
        "새 그룹 이름:":
            "新分组名称:",
        "새 그룹으로 묶기...":
            "合并到新分组...",
        "새 버전 {0} 이(가) 있습니다. (업데이트 메뉴 → 업데이트 확인)":
            "有新版本 {0}。(更新菜单 → 检查更新)",
        "새 버전이 있습니다: {0}   (현재 v{1})":
            "有新版本: {0}   (当前 v{1})",
        "새 비밀번호 (8자 이상):":
            "新密码 (至少8个字符):",
        "새 비밀번호 확인:":
            "确认新密码:",
        "새 사용자 추가...":
            "添加新用户...",
        "새 사용자(N)":
            "新用户(N)",
        "생성":
            "生成",
        "선택한 사이트 {0}개를":
            "所选的 {0} 个网站",
        "선택한 사이트 {0}개를 묶을 새 그룹 이름:\n('{1}' 안에 만들어집니다)":
            "用于合并所选 {0} 个网站的新分组名称:\n(将创建在 '{1}' 中)",
        "선택한 사이트 {0}개를 옮길 그룹을 고르세요.":
            "请选择要移入所选 {0} 个网站的分组。",
        "선택한 폴더 안에 '{0}' 폴더를 만들어 저장합니다.":
            "将在所选文件夹中创建 '{0}' 文件夹并保存。",
        "설정":
            "设置",
        "수정":
            "编辑",
        "수정 (이름·위치)":
            "编辑 (名称·位置)",
        "수정할 사이트를 먼저 선택하세요.":
            "请先选择要编辑的网站。",
        "시작하기":
            "开始使用",
        "실제 저장 위치: {0}":
            "实际保存位置: {0}",
        "아이디":
            "账号",
        "아이디 기억(A)":
            "记住账号(A)",
        "아이디 복사":
            "复制账号",
        "아이디가 일치하지 않아 삭제를 취소했습니다.":
            "账号不一致,已取消删除。",
        "아이디는 한글, 영문, 숫자, _ . - 만 사용해 32자 이내로 입력하세요.":
            "账号只能使用汉字、英文、数字和 _ . -,且不超过32个字符。",
        "아이디와 비밀번호를 입력해 주세요.":
            "请输入账号和密码。",
        "아직 백업 위치가 설정되지 않았습니다.\n지금 설정할까요?":
            "尚未设置备份位置。\n要现在设置吗?",
        "아직 백업 위치로 백업한 기록이 없습니다.":
            "尚无备份到备份位置的记录。",
        "암호화 백업 (.mpbak) — 권장":
            "加密备份 (.mpbak) — 推荐",
        "언어 (Language)":
            "语言 (Language)",
        "언어를 바꿨습니다: {0}":
            "已切换语言: {0}",
        "업데이트 서버 오류 ({0})":
            "更新服务器错误 ({0})",
        "업데이트 설정...":
            "更新设置...",
        "업데이트 확인":
            "检查更新",
        "업데이트(U)":
            "更新(U)",
        "업데이트를 확인하는 중...":
            "正在检查更新...",
        "업데이트를 확인할 GitHub 저장소가 설정되어 있지 않습니다.\nmypass.py 맨 위의 UPDATE_REPO 에 '계정/저장소'를 넣고 다시 만드세요.":
            "尚未设置用于检查更新的 GitHub 仓库。\n请在 mypass.py 顶部的 UPDATE_REPO 中填入 '账户/仓库',然后重新生成。",
        "여기에 사이트 추가":
            "在此添加网站",
        "여러 개 선택(Ctrl/Shift) 후 오른쪽 클릭: 이동 · 묶기 · 삭제":
            "多选(Ctrl/Shift)后右键单击: 移动 · 合并 · 删除",
        "연동할 브라우저 창을 찾지 못했습니다. 브라우저를 한 번 사용한 뒤 다시 눌러 보세요.":
            "找不到可关联的浏览器窗口。请先使用一次浏览器,然后再点击。",
        "올바른 백업 파일이 아닙니다.":
            "不是有效的备份文件。",
        "올바른 보관함 파일이 아닙니다.":
            "不是有效的密码库文件。",
        "옮길 그룹을 선택하세요.":
            "请选择要移动到的分组。",
        "옮길 사이트를 먼저 선택하세요. (Ctrl/Shift 로 여러 개 선택)":
            "请先选择要移动的网站。(按 Ctrl/Shift 可多选)",
        "옮길 수 없습니다. (이동할 곳에 같은 이름의 그룹이 있습니다)":
            "无法移动。(目标位置已有同名分组)",
        "위치":
            "位置",
        "이 백업을 만들 당시의 마스터 비밀번호를 입력하세요:":
            "请输入创建此备份时的主密码:",
        "이 주소 키워드를 수동 사이트로 설정(M)":
            "将此地址关键字设为手动网站(M)",
        "이 폴더는 프로그램 데이터(data 폴더)와 같은 드라이브(또는 같은 USB)에 있습니다.\n그 장치가 고장 나거나 분실되면 원본과 백업이 함께 사라집니다.\n\n다른 장치(다른 드라이브·클라우드 등)의 폴더를 권장합니다.\n그래도 이 폴더를 사용할까요?":
            "此文件夹与程序数据(data 文件夹)位于同一磁盘(或同一个 USB)。\n如果该设备损坏或丢失,原始数据和备份将一同丢失。\n\n建议使用其他设备(其他磁盘·云端等)中的文件夹。\n仍要使用此文件夹吗?",
        "이름을 바꿀 그룹을 선택하세요.":
            "请选择要重命名的分组。",
        "이미 '{0}' 사용자가 있습니다. 백업 내용으로 덮어쓸까요?\n(기존 파일은 data\\_deleted 폴더에 보관됩니다)":
            "用户 '{0}' 已存在。要用备份内容覆盖吗?\n(原有文件将保存在 data\\_deleted 文件夹中)",
        "이미 등록된 아이디입니다.":
            "该账号已被注册。",
        "인터넷에 연결할 수 없어 확인하지 못했습니다.":
            "无法连接互联网,检查失败。",
        "일치하지 않습니다.":
            "不一致。",
        "입력하신 정보는 암호화되어 이 컴퓨터에만\n저장되며 인터넷으로 전송되지 않습니다.\n처음이시면 [새 사용자]를 눌러 등록하세요.":
            "您输入的信息经加密后仅保存在\n此电脑中,不会通过互联网传输。\n首次使用请点击 [新用户] 进行注册。",
        "자동 백업 시점: 로그인할 때 · 정보를 바꾼 뒤 · 프로그램을 종료할 때":
            "自动备份时机: 登录时 · 修改信息后 · 退出程序时",
        "자동 백업 폴더 열기":
            "打开自动备份文件夹",
        "자주 묻는 질문":
            "常见问题",
        "저장":
            "保存",
        "저장된 아이디와 비밀번호를 브라우저의 로그인 칸에 자동으로 입력합니다. (Windows 전용)\n\n■ 사용 순서\n1. 사이트를 열어 로그인 페이지를 띄웁니다.\n2. 이 프로그램에서 해당 사이트 정보를 선택합니다. (주소가 맞으면 자동으로 선택됩니다)\n3. 브라우저의 아이디 입력칸을 클릭해 커서를 둡니다.\n4. 마이패스의 [채움] 버튼을 누릅니다.\n→ 아이디 입력 → Tab → 비밀번호 입력 순서로 자동 입력됩니다.\n\n■ 자동 로그인\n환경설정 메뉴의 '채움 후 Enter 키 입력' 을 켜면 입력 끝에 Enter 까지 눌러 줍니다.\n\n■ 안 될 때\n· 로그인 칸이 '아이디 → 비밀번호' 순서가 아니거나 중간에 다른 칸이 있으면 어긋날 수 있습니다.\n   이럴 땐 값을 더블클릭해 아이디와 비밀번호를 각각 복사해서 붙여넣으세요.\n· 아이디와 비밀번호를 따로 입력받는 사이트(2단계 로그인)도 복사해서 붙여넣는 방법을 쓰세요.\n· 비밀번호는 복사 후 20초가 지나면 클립보드에서 자동으로 지워집니다.":
            "将已保存的账号和密码自动输入到浏览器的登录框中。(仅限 Windows)\n\n■ 使用步骤\n1. 打开网站,显示登录页面。\n2. 在本程序中选择对应的网站信息。(地址匹配时会自动选中)\n3. 点击浏览器的账号输入框,让光标停留在其中。\n4. 点击 MyPass 的 [填充] 按钮。\n→ 按 输入账号 → Tab → 输入密码 的顺序自动输入。\n\n■ 自动登录\n开启设置菜单中的'填充后按 Enter 键(自动登录)'后,输入结束时会再按一下 Enter。\n\n■ 无法使用时\n· 如果登录框不是'账号 → 密码'的顺序,或中间还有其他输入框,可能会错位。\n   此时请双击数值,分别复制账号和密码并粘贴。\n· 分别输入账号和密码的网站(两步登录),也请使用复制粘贴的方法。\n· 密码在复制 20 秒后会自动从剪贴板中清除。",
        "저장된 정보를 찾는 기준 단어입니다. 주소창의 주소 안에 이 키워드가 들어 있으면 해당 사이트 정보가 나타납니다.\n\n■ 예시\n· NAVER.COM → mail.naver.com, cafe.naver.com 등 네이버 전체에 적용\n· MAIL.NAVER.COM → 네이버 메일 주소에만 적용\n· 같은 사이트에 키워드가 둘 이상 맞으면 더 긴(구체적인) 키워드가 위에 나옵니다.\n\n■ 자동 생성\n주소를 넣으면 키워드가 자동으로 만들어집니다. (www. 는 제외, co.kr 같은 주소도 처리)\n키워드 칸의 목록에서 범위를 고를 수 있습니다.\n\n■ 직접 정하고 싶을 때\n'이 주소 키워드를 수동 사이트로 설정' 을 체크하면 키워드를 마음대로 적을 수 있습니다.":
            "这是用于查找已保存信息的依据词。如果地址栏的地址中包含此关键字,就会显示对应的网站信息。\n\n■ 示例\n· NAVER.COM → 适用于 mail.naver.com、cafe.naver.com 等整个 NAVER\n· MAIL.NAVER.COM → 仅适用于 NAVER 邮箱地址\n· 同一网站匹配到多个关键字时,更长(更具体)的关键字会排在前面。\n\n■ 自动生成\n输入地址后会自动生成关键字。(不含 www.,也能处理 co.kr 之类的地址)\n可在关键字栏的列表中选择范围。\n\n■ 想自行设定时\n勾选'将此地址关键字设为手动网站'后,可以随意填写关键字。",
        "저장소 이름을 '계정/저장소' 형식으로 입력하세요.":
            "请按 '账户/仓库' 的格式输入仓库名称。",
        "저장소 주소는 프로그램(mypass.py 맨 위 UPDATE_REPO)에 미리 넣어 두는 값을 씁니다. 비공개 저장소일 때만 'Fine-grained 토큰(이 저장소 하나, Contents: Read-only)'을 입력하세요. 토큰은 이 컴퓨터의 data 폴더에만 저장되며 외부로 전송되지 않습니다. (data 폴더를 다른 사람과 공유하지 마세요) 공개 저장소면 비워 두세요.":
            "仓库地址使用预先填入程序中的值(mypass.py 顶部的 UPDATE_REPO)。仅私有仓库需要输入 'Fine-grained 令牌(仅限此仓库,Contents: Read-only)'。令牌仅保存在本机的 data 文件夹中,不会发送到任何外部。(请勿与他人共享 data 文件夹) 公开仓库请留空。",
        "토큰 붙여넣기":
            "粘贴令牌",
        "고급 설정 (비공개 저장소용 토큰)":
            "高级设置(私有仓库令牌)",
        "저장소·릴리스를 찾을 수 없거나 토큰 권한이 부족합니다. (오류 {0})":
            "找不到仓库·Release,或令牌权限不足。(错误 {0})",
        "저장소·릴리스를 찾을 수 없습니다. (오류 {0})\n비공개(private) 저장소라면 읽기 전용 토큰이 필요합니다.":
            "找不到仓库·Release。(错误 {0})\n如果是私有(private)仓库,需要只读令牌。",
        "저장하지 못했습니다.\n{0}":
            "保存失败。\n{0}",
        "정보":
            "关于",
        "종료":
            "退出",
        "주소":
            "地址",
        "주소 키워드":
            "地址关键字",
        "주소 키워드가 비어 있습니다.\n주소를 확인하거나 수동으로 입력하세요.":
            "地址关键字为空。\n请检查地址或手动输入。",
        "주소 키워드는 저장된 로그인 정보를 찾는 기준입니다.\n주소창의 주소에 이 키워드가 들어 있으면 이 사이트 정보가 표시됩니다.\n\n예) NAVER.COM → mail.naver.com, cafe.naver.com 모두 적용\n    MAIL.NAVER.COM → 메일 주소에만 적용\n\n'수동 사이트로 설정'을 체크하면 키워드를 직접 입력할 수 있습니다.":
            "地址关键字是用于查找已保存登录信息的依据。\n如果地址栏的地址中包含此关键字,就会显示此网站的信息。\n\n例) NAVER.COM → mail.naver.com、cafe.naver.com 均适用\n    MAIL.NAVER.COM → 仅适用于邮箱地址\n\n勾选'设为手动网站'后,可以直接输入关键字。",
        "주소 키워드란?":
            "什么是地址关键字?",
        "주소를 입력하세요.":
            "请输入地址。",
        "지금 백업":
            "立即备份",
        "지금 백업 위치에 백업":
            "立即备份到备份位置",
        "지정한 폴더를 찾을 수 없습니다.\n경로가 맞는지, 드라이브·USB·클라우드 프로그램이 연결되어 있는지 확인하세요.":
            "找不到指定的文件夹。\n请确认路径是否正确,以及磁盘·USB·云端程序是否已连接。",
        "창 크기 초기화":
            "重置窗口大小",
        "창 크기를 기본값으로 되돌렸습니다. (목록관리·도움말 창은 다음에 열 때 적용)":
            "窗口大小已恢复为默认值。(列表管理·帮助窗口将在下次打开时生效)",
        "창 크기와 위치":
            "窗口大小与位置",
        "찾아보기":
            "浏览",
        "채우는 중... 브라우저의 아이디 입력칸에 커서가 있어야 합니다.":
            "正在填充... 浏览器的账号输入框中必须有光标。",
        "채울 사이트 정보가 없습니다.":
            "没有可填充的网站信息。",
        "채움":
            "填充",
        "채움 (자동 입력)":
            "填充 (自动输入)",
        "채움 후 Enter 키 입력(자동 로그인)":
            "填充后按 Enter 键(自动登录)",
        "최상위":
            "顶层",
        "최상위 ({0})":
            "顶层 ({0})",
        "최신 버전입니다. (v{0})":
            "已是最新版本。(v{0})",
        "추가":
            "添加",
        "취소":
            "取消",
        "취소(C)":
            "取消(C)",
        "클라우드 찾기":
            "查找云端",
        "클라우드 폴더를 자동으로 찾지 못했습니다.\n[찾아보기]로 직접 고르세요.":
            "未能自动找到云端文件夹。\n请通过 [浏览] 手动选择。",
        "토큰 (비공개일 때만)":
            "令牌 (仅私有仓库需要)",
        "토큰":
            "令牌",
        "팁: %USERPROFILE%\\OneDrive 처럼 환경변수 경로를 쓰면, 컴퓨터마다 사용자 이름이 달라도 한 번만 설정하면 됩니다.":
            "提示: 使用 %USERPROFILE%\\OneDrive 这样的环境变量路径,即使每台电脑的用户名不同,也只需设置一次。",
        "파일(F)":
            "文件(F)",
        "하위 그룹 추가":
            "添加子分组",
        "한 컴퓨터에서 여러 사람(또는 용도별)이 각자의 보관함을 따로 쓸 수 있습니다.\n\n■ 새 사용자 추가\n· 로그인 창의 [새 사용자(N)] 또는 파일 메뉴 '새 사용자 추가'\n· 아이디와 8자 이상의 비밀번호를 정합니다. 인터넷 회원가입은 필요 없습니다.\n\n■ 다른 사용자로 로그인\n파일 메뉴 '다른 사용자로 로그인'. 사용자마다 사이트 정보가 완전히 분리됩니다.\n\n■ 사용자 삭제\n· 로그인 상태: 파일 메뉴 '현재 사용자 삭제' (마스터 비밀번호 확인 필요)\n· 보안을 위해 로그인 창에는 삭제·복원 버튼이 없습니다. 아이디나 비밀번호를 잊은 사용자는 복구할 수 없으며,\n   정리하려면 프로그램을 끈 뒤 data 폴더에서 해당 '아이디.dat' 파일을 직접 지우세요.\n· 안전장치: 삭제 전 확인을 거치며, 파일은 data\\_deleted 폴더로 옮겨질 뿐 지워지지 않습니다.\n   되살리려면 그 파일을 data 폴더로 옮기고 이름에서 날짜 부분(_20xxxxxx-xxxxxx)만 지우세요.\n   (예: aaa_20261009-135500.dat → aaa.dat)\n\n■ 마스터 비밀번호 변경\n파일 메뉴 '마스터 비밀번호 변경' (현재 비밀번호 확인 필요)":
            "在一台电脑上,多个人(或按用途)可以各自单独使用自己的密码库。\n\n■ 添加新用户\n· 登录窗口的 [新用户(N)] 或文件菜单'添加新用户'\n· 设定账号和8个字符以上的密码。无需在互联网上注册会员。\n\n■ 以其他用户登录\n文件菜单'以其他用户登录'。每个用户的网站信息完全独立。\n\n■ 删除用户\n· 登录状态下: 文件菜单'删除当前用户' (需要确认主密码)\n· 出于安全考虑,登录窗口中没有删除·恢复按钮。忘记账号或密码的用户无法找回,\n   如需清理,请关闭程序后,在 data 文件夹中直接删除对应的 '账号.dat' 文件。\n· 安全措施: 删除前会进行确认,文件只会被移至 data\\_deleted 文件夹,并不会被彻底删除。\n   如需恢复,请将该文件移回 data 文件夹,并只删除名称中的日期部分(_20xxxxxx-xxxxxx)。\n   (例: aaa_20261009-135500.dat → aaa.dat)\n\n■ 更改主密码\n文件菜单'更改主密码' (需要确认当前密码)",
        "항상 위에 표시":
            "窗口置顶",
        "현재 로그인한 사용자를 복원했습니다. 다시 로그인합니다.":
            "已恢复当前登录的用户。将重新登录。",
        "현재 마스터 비밀번호:":
            "当前主密码:",
        "현재 비밀번호가 틀렸습니다.":
            "当前密码错误。",
        "현재 사용자 삭제...":
            "删除当前用户...",
        "현재 주소로 사이트 추가":
            "以当前地址添加网站",
        "확인":
            "确定",
        "확인 대상 저장소":
            "检查的目标仓库",
        "확인(O)":
            "确定(O)",
        "확인을 위해 아이디 '{0}' 를 그대로 입력하세요:":
            "为确认,请原样输入账号 '{0}':",
        "환경설정(S)":
            "设置(S)",
        "[지금 업데이트]를 누르면 새 버전을 받아 자동으로 바꿔 넣고 다시 시작합니다. data 폴더는 그대로 유지됩니다. (바꾸기 전에 '백업 만들기'를 권장합니다)":
            "点击【立即更新】会自动下载新版本并替换当前程序后重启。data 文件夹内容保持不变。(建议替换前先“创建备份”)",
        "{0} - 업데이트 적용":
            "{0} - 应用更新",
        "다운로드에 실패했습니다: {0}":
            "下载失败：{0}",
        "업데이트 다운로드 중... {0}%":
            "正在下载更新... {0}%",
        "업데이트 적용에 실패했습니다: {0}":
            "应用更新失败：{0}",
        "업데이트를 적용합니다. 프로그램이 곧 다시 시작됩니다.":
            "正在应用更新，程序即将重新启动。",
        "이 방식으로는 자동 업데이트를 적용할 수 없습니다. (exe 로 실행 중일 때만 가능)\n다운로드 페이지에서 새 exe 를 받아 직접 바꿔 넣어 주세요.":
            "无法以此方式自动更新。(仅在以 exe 方式运行时可用)\n请在下载页面获取新的 exe 文件后自行替换。",
        "지금 업데이트":
            "立即更新",
    },
}
