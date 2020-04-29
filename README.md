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
### Powerlevel10k
Follow instructions on [Powerlevel10k](https://github.com/romkatv/powerlevel10k).
Install [Meslo Nerd Font](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k) before configuring.
Type `p10k configure` to start the configuration wizard.

## Software

Set global .gitignore
```bash
git config --global core.excludesfile ~/dotfiles/gitignore_global
```

