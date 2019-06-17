#!/usr/bin/env bash

# This is to make sure double stars ** works
shopt -s globstar

#command to test all notebooks
pytest --current-env --capture=no --nbval **/*.ipynb 
