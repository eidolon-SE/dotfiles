import os, pathlib

home_path = pathlib.Path(os.getenv('HOME'))
config_path = home_path / '.config'

path_list = [
    ('alacritty/alacritty.toml', config_path / 'alacritty/alacritty.toml', False),
    ('neovim', config_path / 'nvim', True),
]

for (source, link, is_dir) in path_list:
    source_path = pathlib.Path(source).absolute()
    link_path = pathlib.Path(link).absolute()
    

    if not link_path.exists():
        if not link_path.parent.exists():
            print(f'Directory {link_path.parent} does not exist, creating directory.')
            link_path.parent.mkdir(parents=True)

        print(f'Symlinking {link_path} to {source_path}.')
        link_path.symlink_to(source_path, target_is_directory=is_dir)
    else:
        if link_path.is_symlink():
            print(f'Path {link_path} is already a symlink to {link_path.readlink()}.')
        else:
            print(f'Path {link_path} already exists.')
        print(f'To create symlink, {link_path} must be deleted.')
