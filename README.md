`dmenu-setxkbmap` is a simple dmenu wrapper for setxkbmap,
which allows to set X11 keyboard layouts.

### Install
``make install``

### Usage
Run ``LAYOUTS=$'us\nfr\nfr bepo' dmenu-setxkbmap``, select your layout then press the Return key.

The script arguments are forwarded to dmenu.
Please refer to the [dmenu manual][man dmenu] for listing all available options.

[man dmenu]: https://man.cx/dmenu

### User-defined layouts
The listed layouts can be customized in the ``LAYOUTS`` environment variable.
Entries must be newline-separated and valid regarding setxkbmap.  
