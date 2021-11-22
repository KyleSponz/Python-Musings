'''
Taken from https://click.palletsprojects.com/en/8.0.x/
'''

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('--message',  help='What you wanna say') #For right now it works with no spacve Can click take whitespace?


def hello(count, name, message):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")
    c = click.get_current_context()
    message = c.params["message"]
    print("the message is " + message)




if __name__ == '__main__':
    hello()