# PYTHON_ARGCOMPLETE_OK

import argcomplete, argparse
import os
from pathlib import Path


def create(name, template, recipe):
    template_home = Path.home() / ".texus/templates"
    recipe_home = Path.home() / ".texus/recipes"
    os.mkdir(name)
    os.system(f"cp -r {template_home}/{template}/* '{name}'")
    os.chdir(name)
    os.mkdir(".vscode")
    os.system(f"cp {recipe_home}/{recipe} .vscode/settings.json")
    os.system(f"code .")


def sync(msg):
    os.system("git add .")
    if msg is None:
        os.system("git commit")
    else:
        os.system(f"git commit -m '{msg}'")
    os.system("git push")


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
        "-n",
        "--name",
        help="Project name (required for create).",
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

    parser.add_argument(
        "-m",
        "--message",
        help="Commit message for sync process.",
        metavar="message",
    )

    argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if args.operation == "create":
        create(args.name, args.template, args.recipe)
    elif args.operation == "sync":
        sync(args.message)


if __name__ == "__main__":
    main()
