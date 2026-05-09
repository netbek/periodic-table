{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:
{
  env.DEVENV_TASKS_QUIET = 1;

  packages = with pkgs; [
    nixfmt
    pre-commit
    ripgrep
    zlib
  ];

  languages = {
    javascript = {
      enable = true;
      package = pkgs.nodejs_24;
      npm = {
        enable = true;
        install = {
          enable = true;
        };
      };
    };

    python = {
      enable = true;
      uv = {
        enable = true;
        sync = {
          enable = true;
          allExtras = true;
          allGroups = true;
        };
      };
    };
  };

  dotenv = {
    disableHint = true;
  };

  enterShell = ''
    VENV_PATH="${config.env.DEVENV_STATE}/venv"

    if [ -d "$VENV_PATH" ]; then
      ln -sfn "$VENV_PATH" venv
      source "$VENV_PATH/bin/activate"
    else
      echo "$VENV_PATH not found"
      exit 1
    fi

    if [ -d ".git" ]; then
      pre-commit install --overwrite > /dev/null 2>&1
    fi
  '';
}
