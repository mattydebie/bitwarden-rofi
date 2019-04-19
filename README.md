# BitWarden Rofi Menu

This is a work in progress to get the BitWarden cli functionality in an easy Rofi menu.
On selecting an entry, the password is copied to your clipboard for 5 seconds.
During those 5 seconds, a notification is shown indicating which password you
are copying at that time.

![bitwarden-rofi](img/screenshot1.png)

## Usage

You can either execute the script from a terminal or by binding it to a key
combination in your window manager.

```
bwmenu 0.3

Usage:
  bwmenu [options] -- [rofi options]

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
      Default: "~/.bwhash".

      NOTE: The "~" character will not be expanded properly unless you put a
      space between the argument and the value.

Examples:
  # Default options work well
  bwmenu

  # Tilde can be used when you put space in arguments.
  bwmenu -c 10 --state-path ~/.cache/bwmenu
  bwmenu -c 10 --state-path=$HOME/.cache/bwmenu

  # XDG-compatible state location
  bwmenu --state-path=${XDG_RUNTIME_DIR}/bwmenu-state

  # Place rofi on top of screen, like a Quake console
  bwmenu -- -location 2
```


### Functions

  - <kbd>Alt</kbd>+<kbd>r</kbd>: Resync Bitwarden
  - <kbd>Alt</kbd>+<kbd>u</kbd>: Search on url
  - <kbd>Alt</kbd>+<kbd>n</kbd>: Search on names
  - <kbd>Alt</kbd>+<kbd>c</kbd>: Select folder to search in

### Auto Typing
You can use bitwarden-rofi to auto type your *username*, *password* or *both* by using xdotool to autofill forms.
  - <kbd>Alt</kbd>+<kbd>1</kbd>: Type username and password
  - <kbd>Alt</kbd>+<kbd>2</kbd>: Type only the username
  - <kbd>Alt</kbd>+<kbd>3</kbd>: Type only the password


## Install

### Via package managers

<a href="https://repology.org/metapackage/bitwarden-rofi/versions">
  <img src="https://repology.org/badge/vertical-allrepos/bitwarden-rofi.svg" alt="Packaging status" align="right">
</a>

#### Arch Linux (AUR)

Install the `bitwarden-rofi` AUR package for the latest release or the `bitwarden-rofi-git` for the current master.  
For copying or autotyping, install:
- *xorg*: `xclip`,`xsel` and/or `xdotool` 
- *wayland*: `wl-clipboard`

### Via source

Install these **required** dependencies:

- bitwarden-cli
- jq

**Optionally** install these requirements:
- xclip, xsel, or wl-clipboard
- xdotool

Then download the script file and place it somewhere on your `$PATH` and grant it
the `+x` permission.

```bash
# Install for all users
sudo install -D --mode=755 --group=root --owner=root bwmenu /usr/local/bin/bwmenu

# Install for yourself
mkdir -p ~/.local/bin && \
  cp bwmenu ~/.local/bin/bwmenu && \
  chmod +x ~/.local/bin/bwmenu
```

## License

Released under the GNU General Public License, version 3. See `LICENSE` file.

Copyright © 2018-2019
  * Matthias De Bie
  * Magnus Bergmark
  * Jonathan Raphaelson.
