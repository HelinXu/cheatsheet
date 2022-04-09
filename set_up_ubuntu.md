1. [VPN set up](https://www.cfmem.com/2021/09/linux-clash-for-windows-vpnv2ray.html)
2. chrome
    1. sync!
3. vscode
    1. sync!
4. [configure touchpad](https://ubuntuhandbook.org/index.php/2021/06/multi-touch-gestures-ubuntu-20-04/)
5. Chinese???
6. [Change Ubuntu theme!](https://www.youtube.com/watch?v=IPwF4OzylTs) WhiteSur-light-solid, WhiteSur-dark
7. install [zsh!](https://www.sitepoint.com/zsh-tips-tricks/#:~:text=%24(which%20bash)%20.-,Linux,the%20changes%20to%20take%20effect.)
    1. install zsh
    2. install oh-my-zsh
    3. change theme
    4. add plugins
8. anaconda installation
    1. will init conda in .zshrc
9. git config
10. set up alias


```shell
alias myip="curl http://ipecho.net/plain; echo"
alias mkcd='foo(){ mkdir -p "$1"; cd "$1" }; foo '
alias hs='history | grep'
alias vpnrun='cd ~/Downloads/Clash/; ./cfw' # run my vpn
alias cdcd='cd ~/Code/'


plugins=(
    git
    zsh-syntax-highlighting # git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
    zsh-autosuggestions # git clone https://github.com/zsh-users/zsh-autosuggestions.git
    conda-zsh-completion # git clone https://github.com/esc/conda-zsh-completion.git
    )


ZSH_THEME="ys"
```
