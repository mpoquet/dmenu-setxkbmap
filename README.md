`dmenu-setxkbmap` is a simple dmenu wrapper for setxkbmap,
which allows to set X11 keyboard layouts.

### Usage
Run ``dmenu-setxkbmap.sh``, select your layout then press Return.

As arguments are forwarded to dmenu, the call can be customized.  
Please refer to the [dmenu manual][man dmenu] for a list of the available
options.

[man dmenu]: https://man.cx/dmenu

### User-defined layouts
`dmenu-setxkbmap` proposes all available X11 layouts by default.

This behavior can be customized by defining a list of newline-separated
`setxkbmap` entries in the LAYOUTS variable.  
For example, the following bash call only proposes the qwerty,
azerty and bépo layouts:

``` bash
LAYOUTS=$'us\nfr\nfr bepo' ./dmenu-setxkbmap.sh
```
