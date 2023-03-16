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

    if not os.path.exists('pymc.yaml') or overwrite:
        try:
            with open(os.path.join(dir_path, 'preset.yaml'), 'r') as preset:
                preset = yaml.safe_load(preset)
        except:
            typer.echo('Failed reading from preset.')
            raise typer.Exit(code=1)

        try:
            with open('pymc.yaml', 'w') as file:
                # boiler-plate code
                yaml.dump(preset, file)
            
            typer.echo('pymc file created.')
        except:
            typer.echo('Failed creating pymc.yaml')
            raise typer.Exit(code=1)
    else:
        typer.echo('pymc file already exists (use -o to overwrite)')
        raise typer.Exit(code=1)

@app.command()
def build() -> None:
    """
    Creates class files from the pymc.yaml preset
    """
    with open('./pymc.yaml', 'r') as file:
        classes = yaml.safe_load(file)

    for classname in classes:

        filename = classname + '.py'

        if not os.path.exists(filename):
            with open(filename, 'w') as classfile:
                classfile.write('class ' + classname + ':\n\n')
                classfile.write('\tdef __init__(self):\n\n')

                for variable in classes[classname]:
                    classfile.write(f'\t\tself.{variable} = {classes[classname][variable]}\n')

                for variable in classes[classname]:
                    if variable[0] == '_':
                        classfile.write(f'\n\tdef get{ (str(variable).replace("_", "").capitalize()) }(self):\n')
                        classfile.write(f'\t\t return self.{variable}\n')
                  