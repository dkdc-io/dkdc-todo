# imports
import typer

# typer config
## default kwargs
default_kwargs = {
    "no_args_is_help": True,
    "add_completion": False,
    "context_settings": {"help_option_names": ["-h", "--help"]},
}

## main app
app = typer.Typer(help="dkdc-todo", **default_kwargs)


# commands
## servers
@app.command()
@app.command("g", hidden=True)
def gui(
    port: int = typer.Option(8008, help="port", show_default=True),
    prod: bool = typer.Option(False, help="prod?", show_default=True),
):
    """
    gui
    """
    from shiny import run_app as run_gui_app
    from dkdc_todo.ui.gui import app  # noqa

    if prod:
        run_gui_app(
            app=app,
            host="0.0.0.0",
            port=port,
        )
    else:
        run_gui_app(
            app="dkdc_todo.ui.gui:app",  # goofy! but needed to reload
            host="0.0.0.0",
            port=port,
            reload=True,
            launch_browser=True,
        )


# main
if __name__ == "__main__":
    typer.run(app)
