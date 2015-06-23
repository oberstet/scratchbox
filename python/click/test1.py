import click

@click.command()
@click.option('--name', prompt='Your name please')
def hello(name):
    #click.clear()
    click.echo(click.style('Hello, {}!'.format(name), bg='blue', fg='white'))
    #click.launch('http://crossbar.io/')


if __name__ == '__main__':
    if click.confirm("Are you sure?"):
        hello()
