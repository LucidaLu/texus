# $\TeX \mathrm{us}$ : a helper for working with latex using vscode

## Functionality

### `create`
Create a new latex project using given template and vscode recipe. Example:
```
texus create 'Demo Project' -t article -r xelatex
```

## Installation
```
pip install .
activate-global-python-argcomplete --user
eval "$(register-python-argcomplete texus)"
```

And then, put your templates in `~/.texus/templates` and your vscode recipes in `~/.texus/recipes`. You may refer to my templates and recipes in the `assets` branch of this repo. Or if you want to use them, just run the following commands:
```
rm -rf ~/.texus
git clone -b assets https://github.com/LucidaLu/texus.git ~/.texus
```
