import os
from pathlib import Path

home_path = Path(os.getenv("HOME"))
config_path = home_path / ".config"

paths = [
    ("alacritty/alacritty.toml", config_path / "alacritty/alacritty.toml", False),
    ("neovim", config_path / "nvim", True),
]

for target, link, is_dir in paths:
    target_path = Path(target).absolute()
    link_path = Path(link).absolute()

    if not target_path.exists():
        print(f"Path {target_path} does not exist.")
    else:
        if not link_path.exists():
            if not link_path.parent.exists():
                print(
                    f"Directory {link_path.parent} does not exist, creating directory."
                )
                link_path.parent.mkdir(parents=True)

            print(f"Symlinking {link_path} to {target_path}.")
            link_path.symlink_to(target_path, target_is_directory=is_dir)
        else:
            if link_path.is_symlink():
                print(
                    f"Path {link_path} is already a symlink to {link_path.readlink()}."
                )
            else:
                print(f"Path {link_path} already exists.")
            print(f"To create symlink, {link_path} must be deleted.")
