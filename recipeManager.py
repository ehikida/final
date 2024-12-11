import click

from ingredients import addIngredient

@click.group()
def recipeManager():
    pass

@recipeManager.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Recipe name',
              help='The recipe name.')

def addRecipe(count, name):
    
    for x in range(count):
        click.echo(f"Hello {name}!")


# @recipeManager.command()
# @click.option('--recipe_name', prompt='Recipe name:', help='The recipe to add this ingrdient to')
# @click.option('--ingredient', prompt='Ingredient name:', help='The ingredient to add')
# def addIngredient(recipe_name):
#     click.echo(f"added ingredient to {recipe_name}")

recipeManager.add_command(addIngredient)

if __name__ == '__main__':
    recipeManager()