import click
from click_default_group import DefaultGroup
from subprocess import Popen, PIPE
from keyctl import Keyctl


@click.group(cls=DefaultGroup, default='open', default_if_no_args=True)
@click.option("-v", "--version", help="Show version information and exit.")
@click.option("-l", "--auto-lock", type=int, default=900, show_default=True, help="Automatically lock the Vault "
                                                                                  "<SECONDS> seconds after last "
                                                                                  "unlock. "
                                                                                  "Use 0 to lock immediatly. "
                                                                                  "Use -1 to disable.")
@click.option("-c", "--clear", type=int, default=5, show_default=True, help="Clear password from clipboard after this "
                                                                            "many seconds.")
@click.option("-C", "--no-clear", is_flag=True, help="Don't automatically clear the password from the clipboard. "
                                                     "This disables the default --clear option.")
@click.option("--show-password", is_flag=True, help="Show the first 4 characters of the copied password in the "
                                                    "notification.")
def cli(version, auto_lock, clear, no_clear, show_password):
    pass


@cli.command()
@click.argument("url")
def server(url):
    """Set the Bitwarden Server"""
    click.echo('setting server to {}'.format(url))
    ps = Popen(['bw', 'config', 'server', url], stdout=PIPE, stderr=PIPE)
    click.echo(ps.communicate())


@cli.command()
def sync():
    """Sync the Bitwarden database"""
    click.echo(Popen(['bw', 'sync'], stdout=PIPE, stderr=PIPE).communicate())


@cli.command()
def open():
    """Open the menu"""
    session = None
    try:
        session = Keyctl().get()
    except ValueError:
        session = "session needs to be requested"

    click.echo(session)


@cli.command()
def close():
    Keyctl().purge()

@cli.command()
@click.argument("_pass")
def test(_pass):
    Keyctl().set(_pass)
