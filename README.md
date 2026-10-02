# Miscellaneous Scripts Collection

This repository contains scripts I have written to automate repetitive tasks in my daily development work. I tend to script a task whenever I think I might need to repeat it. I originally created this collection to avoid duplicating utility scripts across my project repositories. Most scripts are written in Bash, with others written in Perl, Python, and Lua.

The scripts mainly support build automation for modern projects, static code analysis, and toolchain setup. Some are also useful for debugging.
Most scripts run natively on Linux, macOS, and Windows. Some require additional tools to be installed; required dependencies are documented where applicable.

I am not actively working on this repository unless a new issue comes up or a new script needs to be added, so some bugs may be present. Feel free to open an issue; I will address it as soon as I can.

## Copyrights

Some scripts are based on or copied from other open-source repositories, and some have been modified. License notices are included at the top of each script. Where applicable, a separate copyright file is included in the same directory.

## Setup

You can include this repository in your project as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Add the submodule to your project repository, git will record its configuration in the `.gitmodules` file.

A sample entry can be added to the top level of your repository:

```sh
[submodule "tools"]
	path = tools
	url = https://github/wissem01chiha/tools.git
```

## Contributing

I am always looking for awesome small automation and helper scripts from open-source repositories to add to my collection. Contributions of new scripts, tools, documentation, and comments are very welcome.
See the [contribution guide](/CONTRIBUTING.md) for more informations.

## Ressources

- [aselvan/scripts](https://github.com/aselvan/scripts) Collection of shell scripts
- [rm1984/Scripts](https://github.com/rm1984/Scripts) A collection of personal useful scripts (in Bash and Python) for Unix and GNU/Linux systems
- [krlmlr/scriptlets](https://github.com/krlmlr/scriptlets) A collection of tiny but helpful shell scripts and config files for personal use. Tested on Ubuntu
- [holman/dotfiles](https://github.com/holman/dotfiles)  holman does dotfiles

## License

See [LICENSE](LICENSE).



