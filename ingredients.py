import click

@click.command()
@click.option('--recipe_name', prompt='Recipe name', help='The recipe to add this ingrdient to')
@click.option('--ingredient', prompt='Ingredient name', help='The ingredient to add')
def addIngredient(recipe_name, ingredient):
    click.echo(f"added ingredient: {ingredient}, to {recipe_name}")