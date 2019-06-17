#!/usr/bin/env bash

# This is to make sure double stars ** works
shopt -s globstar

#command to convert all notebooks
jupyter nbconvert **/*.ipynb
