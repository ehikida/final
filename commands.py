import json
import click

from ingredients import Ingredient, Quantity
from instructions import Instruction
from recipe import Recipe
from recipeBook import RecipeBook

@click.command()
@click.option('--recipe_name', prompt='Recipe name', help='The name of the recipe you wish to create')
@click.pass_context
def addRecipe(ctx, recipe_name):
    recipe = Recipe(recipe_name)
    ctx.parent.book.recipe_list.append(recipe)
    ctx.parent.book.addRecipeToIndex(recipe_name, len(ctx.parent.book.recipe_list)-1)

    recipeBook = ctx.parent.book
    recipeBook.write_book()
    click.echo(f"added recipe {recipe.name} to book")


@click.command()
@click.option('--recipe_name', prompt='Recipe name', help='The name of the recipe you wish to add ingredients to')
@click.option('--ingredient_name', prompt='Ingredient name', help='The name of the ingredient to add')
@click.option('--amount', prompt='Amount of ingredient', help='Amount of ingredient to add')
@click.option('--quantifier', prompt='unit', help='Type of measurement ie. TBS, tsp, cup')
@click.pass_context
def addIngredient(ctx, recipe_name, ingredient_name, amount, quantifier):
    recipe_page_num = ctx.parent.book.index[recipe_name]
    recipe = Recipe(**ctx.parent.book.recipe_list[recipe_page_num])
    ingredient = Ingredient(ingredient_name, Quantity(amount, quantifier))
    recipe.add_ingredient(ingredient)
    recipeBook = ctx.parent.book
    recipeBook.write_book()
    click.echo(f"added ingredient {ingredient_name} to {recipe_name}")

@click.command()
@click.option('--recipe_name', prompt='Recipe name', help='The name of the recipe you wish to add ingredients to')
@click.option('--instruction', prompt='Instruction text', help='The instruction to add')
@click.pass_context
def addInstruction(ctx, recipe_name, instruction):
    recipe_page_num = ctx.parent.book.index[recipe_name]
    recipe = Recipe(**ctx.parent.book.recipe_list[recipe_page_num])
    instruction = Instruction(instruction, len(recipe.instructions))
    recipe.add_instruction(instruction)
    recipeBook = ctx.parent.book
    recipeBook.write_book()
    click.echo(f"added instruction to {recipe_name}")

@click.command()
@click.pass_context
def view(ctx):
    ctx.parent.book.view_book()