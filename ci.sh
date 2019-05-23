#!/usr/bin/env bash
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda_latest.sh
bash Miniconda_latest.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
rm Miniconda_latest.sh
conda config --set always_yes yes --set show_channel_urls yes
conda update conda
conda config --add channels conda-forge
conda create -qy -n testenv python=3.7 pytest nbval termcolor
source activate testenv
which python
python --version

#conda install <optional dependencies>


# run all notebooks in current folder and subfolders
jupyter nbconvert --ExecutePreprocessor.kernel_name=python3 --execute --inplace --allow-errors **/[^_^.]*.ipynb

# pytest all notebooks in current folder and subfolders
pytest --current-env --verbose --capture=no --nbval **/[^_^.]*.ipynb

# convert all notebooks in current folder and subfolders to html
jupyter nbconvert **/[^_^.]*.ipynb
