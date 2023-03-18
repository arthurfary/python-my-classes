from typing import Optional

import typer
import yaml
import os 
import logging

from pymc.Writer import Writer

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
    overwrite: Optional[bool] = typer.Option(
        None,
        "--overwrite",
        "-o",
        help="Overwrites current pymc.yaml file with boiler-plate code"
    )
) -> None:
    """
    Creates pymc.yaml file
    """

    preset_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'preset.yaml')
    pymc_file = 'pymc.yaml'

    if not os.path.exists(pymc_file) or overwrite:
        try:
            with open(preset_file, 'r') as preset:
                preset = yaml.safe_load(preset)
        except FileNotFoundError as e:
            logger.error(f"Failed reading from preset: {e}")
            raise typer.Exit(code=1)

        try:
            with open(pymc_file, 'w') as file:
                yaml.dump(preset, file)
                typer.echo('pymc file created.')
        except OSError as e:
            logger.error(f"Failed creating pymc.yaml: {e}")
            raise typer.Exit(code=1)
    else:
        typer.echo('pymc file already exists (use -o to overwrite)')
        raise typer.Exit(code=1)


@app.command()
def build() -> None:
    """
    Creates class files from the pymc.yaml preset
    """
    try:
        with open('./pymc.yaml', 'r') as file:
            classes = yaml.safe_load(file)
        
        writer = Writer(classes)
        writer.write()
        
    except Exception as e:
        # VV descomentar VV se quiser que apareça o erro 
        # typer.echo(e) 
        raise typer.Exit(code=1)
