`dmenu-setxkbmap` is a simple dmenu wrapper for setxkbmap,
which allows to set X11 keyboard layouts.

### Usage
Run ``dmenu-setxkbmap.sh``, select your layout then press the Return key.

The script arguments are forwarded to dmenu.
Please refer to the [dmenu manual][man dmenu] for listing all available options.

[man dmenu]: https://man.cx/dmenu

### User-defined layouts
By default, `dmenu-setxkbmap` lists all available X11 layouts.

This behavior can be customized by defining the ``LAYOUTS`` variable.  
Entries must be newline-separated and valid regarding setxkbmap.  
For example, the following bash call only proposes the qwerty,
azerty and bépo layouts:

``` bash
LAYOUTS=$'us\nfr\nfr bepo' ./dmenu-setxkbmap.sh
```
