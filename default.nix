{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.virtualenv
  ];

  shellHook = ''
    if [ ! -d "venv" ]; then
      python -m venv venv
      source venv/bin/activate
      pip install --upgrade pip
      pip install -r requirements.txt
    else
      source venv/bin/activate
    python3 anna
    fi
  '';
}
