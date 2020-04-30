# Dotfiles
This repo primarily provides a basic configuration for zsh, tmux, and vim.

## Install

```bash
git clone --recurse-submodules -j8 https://github.com/ltriess/dotfiles.git ~/dotfiles
cd ~/dotfiles
./bootstrap
```

## Dependencies

Install with apt
```bash
sudo apt-get install zsh tmux vim-gnome python3-pip socat rxvt-unicode-256color xautomation xbindkeys
```

Install with pip
```bash
pip3 install thefuck
```

### Powerlevel10k
Follow instructions on [Powerlevel10k](https://github.com/romkatv/powerlevel10k).
Install [Meslo Nerd Font](https://github.com/romkatv/powerlevel10k#meslo-nerd-font-patched-for-powerlevel10k) before configuring.
Type `p10k configure` to start the configuration wizard.

