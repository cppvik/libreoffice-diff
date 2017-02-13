LODIFF - set of utilities for using LibreOffice as git-diff and git-difftool.

Use installer.sh to install some scripts and global git configuration; you should give it a directory on your `PATH`, for example:

```
./installer.sh ~/bin
```

Use `lodiff-config-repo.sh DIRECTORY` to enable features for a git repository in `DIRECTORY` (it defaults to the current directory): this sets `lodiff.py` as git-difftool and [`odt2txt`][1] as text converter for git-diff. (`odt2txt` is available in many distributions too.)

[1]: https://github.com/dstosberg/odt2txt

Inspired by TortoiseSVN
_____________________________________________________________

LODIFF - набор утилит для использования LibreOffice в качестве git-difftool

Для установки скриптов в /usr/bin запустите installer.sh (требуются права администратора).
После этого можно использовать комнаду difftool -t lodiff для файлов odt, ods, doc/docx, xls/xlsx.

Для установки lodiff в качестве утилиты по умолчанию для репозитория в /path/to/repo,
                            запустите config_repo.sh /path/to/repo
Идея, алгоритм: difftool	- TortoiseSVN
        diff		- Git-Book
