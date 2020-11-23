from pathlib import Path


def get_plugins(plugin_path: Path):
    plugin_packages = list()
    source_files = list(plugin_path.glob(f'*py'))
    for sf in source_files:
        # plugin_packages.append(f"{plugin_path.stem}.{sf.stem}")
        plugin_packages.append(f"{sf.stem}")
    return plugin_packages