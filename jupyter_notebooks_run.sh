#!/usr/bin/env bash

# command to run all notebooks

jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors **/*.ipynb
