
# 
import click

@click.group()
def cli():
    click.echo("Hello, World!")

@click.command()
@click.option('--generate', '-g', help='Generate something')
@click.option('--revision', '-r', help='List something')
@click.argument('name')
@click.argument("value")
def sub_command1(name, value, generate, revision):
    click.echo("argument: " + name + " generate: " + generate + " list: " + revision + " value: " + value)

@click.command()
@click.option('--delete', '-d', default=False, help='Delete something')
def sub_command2(delete):
    click.echo(f"delete something, {delete}")
    
cli.add_command(sub_command1)
cli.add_command(sub_command2)

if __name__ == '__main__':
    cli()