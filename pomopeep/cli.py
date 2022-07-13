from typing import Optional
import typer
from pomopeep import __app_name__, __version__
from .functions import countdown

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
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


# Commands
@app.command()
def start(sessions: int, work_time: int = 25, break_time: int = 5):
    countdown(sessions, work_time, break_time)