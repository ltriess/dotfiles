# Dotfiles
This repo primarily provides a basic configuration for tmux, vim, and bash.

## Install notes
I recommend to clone it to a folder $HOME/dotfiles.

Make sure to checkout submodules:
```bash
$ git submodule update --init --recursive
$ cd ~/dotfiles/script
$ ./bootstrap
```

## Dependencies

```bash
sudo apt-get install zsh tmux vim-gnome python3-pip socat rxvt-unicode-256color xautomation xbindkeys
```

```bash
pip3 install thefuck
```

Powerline Python package
```bash
sudo -H pip3 install powerline-status
sudo -H pip3 install powerline-gitstatus
ln -s ~/dotfiles/config/powerline ~/.config/powerline
```

## Software

Set global .gitignore
```bash
git config --global core.excludesfile ~/dotfiles/gitignore_global
```
