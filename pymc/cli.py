from typing import Optional

import typer
import yaml
import os 


from pymc import __app_name__, __version__

app = typer.Typer()
dir_path = os.path.dirname(os.path.realpath(__file__))


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def version(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def init(
) -> None:
    """
    Creates pymc.yaml file
    """
    with open(os.path.join(dir_path, 'preset.yaml'), 'r') as preset:
        preset = yaml.safe_load(preset)
    with open('pymc.yaml', 'w') as file:
        # boiler-plate code
        yaml.dump(preset, file)