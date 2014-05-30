LODIFF - set of utilities for using LibreOffice as git-diff and git-difftool.

use installer.sh to install scripts to /usr/bin (requires root)
use config_repo.sh <dir> to enable features for git repository in <dir>:
	 sets lodiff.py as git-difftool and odf-to-txt as text converter for git-diff
Inspired by TortoiseSVN
_____________________________________________________________

LODIFF - набор утилит для использования LibreOffice в качестве git-difftool

Для установки скриптов в /usr/bin запустите installer.sh (требуются права администратора).
После этого можно использовать комнаду difftool -t lodiff для файлов odt, ods, doc/docx, xls/xlsx.

Для установки lodiff в качестве утилиты по умолчанию для репозитория в /path/to/repo,
							запустите config_repo.sh /path/to/repo
Идея, алгоритм: difftool	- TortoiseSVN
		diff		- Git-Book
