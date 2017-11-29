PREFIX ?= /usr
BINDIR ?= $(PREFIX)/bin

default:
	@echo "dmenu-setxkbmap is a shell script, so there is nothing to do." \
	      "Try \"make install\" instead."

install:
	@install -v -d "$(BINDIR)"
	@install -m 0755 -v src/dmenu-setxkbmap.sh "$(BINDIR)/dmenu-setxkbmap"

uninstall:
	@rm -vf "$(BINDIR)/dmenu-setxkbmap"
