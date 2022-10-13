# XXX https://github.com/nix-community/poetry2nix/pull/715
{
  # pkgs ? import <nixpkgs> {}
  pkgs ? import (fetchTarball https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz) { }
}:

let
  quasiApironEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    editablePackageSources = {
      bugwarrior = ./quasi_apiron.py;
    };
    overrides = pkgs.poetry2nix.overrides.withDefaults (self: super: {
      apiron = super.apiron.overridePythonAttrs (old: {
        buildInputs = old.buildInputs ++ [ self.setuptools ];
      });
    });
  };
in quasiApironEnv.env.overrideAttrs (oldAttrs: {
  buildInputs = [
    pkgs.poetry
  ];
})
