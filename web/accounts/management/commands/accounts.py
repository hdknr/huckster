from django.utils import translation 
from oauth2_provider.models import Application
import djclick as click
from logging import getLogger


logger = getLogger()
translation.activate('ja')


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.option('--app', '-a', default=None)
@click.pass_context
def oauth2_provider(ctx, app):
    '''OAuth2 Provider'''
    query = {'name': app} if app  else {}
    app = Application.objects.filter(**query).first()
    click.echo(f"{app.client_id},{app.client_secret}")