#!/usr/bin/env bash

#command to test all notebooks

pytest --current-env --capture=no --nbval notebooks/**/*.ipynb 
