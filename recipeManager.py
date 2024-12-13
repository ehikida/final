from pathlib import Path
import click
import json

from commands import addIngredient, addRecipe, addInstruction, view
from recipeBook import RecipeBook

@click.group(invoke_without_command=True, chain=True)
@click.pass_context
def recipeManager(ctx):
    book_file = Path("book.json")
    if book_file.is_file():
        with open("book.json", 'r') as data:
            json_string = json.load(data)
            book = json.loads(json_string)
            recipeBook = RecipeBook(**book)
            ctx.book = recipeBook
    else:
        recipeBook = RecipeBook()
        ctx.book = recipeBook
        recipeBook.write_book()


recipeManager.add_command(addRecipe)
recipeManager.add_command(addIngredient)
recipeManager.add_command(addInstruction)
recipeManager.add_command(view)


def main():
    recipeManager()
    
if __name__ == '__main__':
    main()