{   pkgs ? import (
    fetchTarball "https://github.com/NixOS/nixpkgs/archive/19.03.tar.gz") {}
}:

let
  jobs = rec {
    dmenu_setxkbmap = pkgs.stdenv.mkDerivation rec {
      pname = "dmenu-setxkbmap";
      version = "0.3.0";

      buildInputs = with pkgs; [
        dmenu
        xorg.setxkbmap
        xorg.xmodmap
        python3
        which
      ];

      src = ./.;
      patchPhase = ''
        # Patch runtime process dependencies
        sed -iE "sW\"dmenu\"W\"$(which dmenu)\"W" src/dmenu-setxkbmap.py
        sed -iE "sW\"setxkbmap\"W\"$(which setxkbmap)\"W" src/dmenu-setxkbmap.py
        sed -iE "sW\"xmodmap\"W\"$(which xmodmap)\"W" src/dmenu-setxkbmap.py
      '';
      installPhase = "PREFIX=$out make install";
    };
  };
in
  jobs
