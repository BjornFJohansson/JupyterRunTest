#!/usr/bin/env bash

wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh


conda config --set always_yes yes --set show_channel_urls yes
conda update conda
conda env create -f environment.yml
source activate testenvironment
conda install pytest nbconvert nbval termcolor

shopt -s globstar


# command to run all notebooks in current folder and subfolders
jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors notebooks/**/[^_^.]*.ipynb

#command to test all notebooks in current folder and subfolders
pytest --current-env --verbose --capture=no --nbval notebooks/**/[^_^.]*.ipynb

#command to convert all notebooks in current folder and subfolders to html
jupyter nbconvert notebooks/**/[^_^.]*.ipynb
