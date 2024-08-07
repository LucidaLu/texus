# PYTHON_ARGCOMPLETE_OK

import argcomplete, argparse
import os
from pathlib import Path


def create(name, template, recipe):
    template_home = Path.home() / ".texus/templates"
    recipe_home = Path.home() / ".texus/recipes"
    os.system(f"cp -r {template_home}/{template} {name}")
    os.chdir(name)
    os.mkdir(".vscode")
    os.system(f"cp {recipe_home}/{recipe} .vscode/settings.json")
    os.system(f"code .")


temps = sorted(os.listdir(Path.home() / ".texus/templates"))
recipes = sorted(os.listdir(Path.home() / ".texus/recipes"))


def main():
    parser = argparse.ArgumentParser(prog="texus")

    opers = ["create", "sync"]
    parser.add_argument(
        "operation",
        choices=opers,
        help="The operation to be applied. Supported: %s"
        % ", ".join(map(lambda x: '"%s"' % (x), opers)),
        metavar="operation",
    )

    parser.add_argument(
        "name",
        help="Project name.",
        metavar="name",
    )

    parser.add_argument(
        "-t",
        "--template",
        choices=temps,
        help="Specify the document type. Supported: %s"
        % ", ".join(map(lambda x: '"%s"' % (x), temps)),
        metavar="template",
    )

    parser.add_argument(
        "-r",
        "--recipe",
        choices=recipes,
        help="Choose the compilation recipe for vscode. Supported: %s"
        % ", ".join(map(lambda x: '"%s"' % (x), recipes)),
        metavar="recipe",
    )

    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if args.operation == "create":
        create(args.name, args.template, args.recipe)


if __name__ == "__main__":
    main()
