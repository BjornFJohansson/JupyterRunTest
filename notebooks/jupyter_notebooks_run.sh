#!/usr/bin/env bash

# This is to make sure double stars ** works
shopt -s globstar

# command to run all notebooks
jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors **/*.ipynb
