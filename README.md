LODIFF - set of utilities for using LibreOffice as a diff tool with Git and Mercurial.

Use installer.sh to install some scripts and global Git configuration; you should give it a directory on your `PATH`, for example:

```
./installer.sh ~/bin
```


Git
===

Use `lodiff-config-git-repo.sh DIRECTORY` to enable features for a git repository in `DIRECTORY` (it defaults to the current directory): this sets `lodiff.py` as git-difftool and [`odt2txt`][1] as text converter for git-diff. (`odt2txt` is available in many distributions too.)

[1]: https://github.com/dstosberg/odt2txt


Mercurial
=========

Configuring Mercurial is a manual process, but it can be done once and for all, by adding some lines to your user configuration file. Run the following command:

```
hg config --edit
```

If there is no line `[extensions]`, then add one at the bottom of the file, then add the following lines:

```
extdiff =

[extdiff]
cmd.lodiff = lodiff.py
```

to activate the required `extdiff` extension and configure a new command `lodiff`.

Then, when you want to use LibreOffice for a diff, run, for example:

```
hg lodiff -r 30 -r 31 foo.odt
```


Inspired by TortoiseSVN
_____________________________________________________________

LODIFF - набор утилит для использования LibreOffice в качестве git-difftool

Для установки скриптов в /usr/bin запустите installer.sh (требуются права администратора).
После этого можно использовать комнаду difftool -t lodiff для файлов odt, ods, doc/docx, xls/xlsx.

Для установки lodiff в качестве утилиты по умолчанию для репозитория в /path/to/repo,
                            запустите config_repo.sh /path/to/repo
Идея, алгоритм: difftool	- TortoiseSVN
        diff		- Git-Book
