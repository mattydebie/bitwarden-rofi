# BitWarden Rofi Menu

This is a work in progress to get the BitWarden cli functionality in an easy Rofi menu.
On selecting an entry, the password is copied to your clipboard for 5 seconds. During those 5 seconds, a notification is shown indicating which password you are copying at that time.

![bitwarden-rofi](img/screenshot1.png)

## Install
To install this script, put the `bwmenu` in your `bin` folder and grant it the `+x` permission

```bash
cp bwmenu "$HOME/bin/bwmenu"
chmod +x "$HOME/bin/bwmenu"
```

You can either execute the script from a terminal or by binding it to a key combination in your window manager.

## Usage

```
bwmenu 0.1

Usage:
  bwmenu [options]

Options:
  --help
      Show this help text and exit.

  --version
      Show version information and exit.

  -c <SECONDS>, --clear <SECONDS>, --clear=<SECONDS>
      Clear password from clipboard after this many seconds.
      Defaults: 5 seconds.

  -C, --no-clear
      Don't automatically clear the password from the clipboard. This disables
      the default --clear option.

  --show-password
      Show the first 4 characters of the copied password in the notification.

  --state-path <PATH>, --state-path=<PATH>
      Store the Bitwarden session information in this file. This file makes it
      possible to reuse your session multiple times and keep you from having to
      enter your master password over and over again.
      Default: "/home/mange/.bwhash".

      NOTE: The "~" character will not be expanded properly unless you put a
      space between the argument and the value.

Examples:
  # Default options work well
  bwmenu

  # Tilde can be used when you put space in arguments.
  bwmenu -c 10 --state-path ~/.cache/bwmenu
  bwmenu -c 10 --state-path=/home/mange/.cache/bwmenu

  # XDG-compatible state location
  bwmenu --state-path=${XDG_RUNTIME_DIR}/bwmenu-state
```

## Functions

  - *Alt+r*: sync bitwarden
  - *Alt+u*: search on url
  - *Alt+n*: search on names
  - *Alt+f*: show folders

## Dependencies

- bitwarden-cli
- jq
- xclip or xsel
