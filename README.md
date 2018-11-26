# BitWarden Rofi Menu

This is a work in progress to get the BitWarden cli functionality in an easy Rofi menu.  
On selecting an entry, the password is copied to your clipboard for 5 seconds. During those 5 seconds, a notification is shown indicating which password you are copying at that time.

![bitwarden-rofi](img/screenshot1.png)

## Install
To install this script, simply put the `bwmenu` in your `bin` folder (/home/{user}/bin) and grant it the +x permission
```bash
chmod +x bwmenu
```

You can either execute the script from a terminal or by binding it to a key combination in your window manager.

## Functions

  - *Alt+r*: sync bitwarden
  - *Alt+u*: search on url
  - *Alt+n*: search on names
  - *Alt+f*: show folders

## Dependencies

- bitwarden-cli
- jq
- xclip
