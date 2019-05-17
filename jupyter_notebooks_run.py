#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://nbconvert.readthedocs.io/en/stable/execute_api.html

import os
import pathlib
import sys
import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor

try:
    filter_files = sys.argv[1:]
except IndexError:
    filter_files = None

try:
    from termcolor import colored
except ImportError:
    def colored(text, color): 
        return text

try:
    thisdir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
except NameError:
    thisdir = pathlib.Path(os.getcwd())

exit_=0

notebooks_w_errors = []

for dirpath, dirnames, filenames in os.walk(thisdir):
    if dirpath.startswith(('.','_')): 
        continue
    for file_ in filenames:
        if filter_files and not filter_files in file_:
            continue
        if not file_.endswith(".ipynb"): 
            continue
        pth = pathlib.Path(os.path.join(dirpath, file_))
        if any( [f for f in pth.parts if f.startswith(("_","."))] ): 
            continue
        
        os.chdir(dirpath)

        pp = ExecutePreprocessor()
        pp.timeout = 120 # seconds
        pp.interrupt_on_timeout = True
        
        with open(pth, 'r', encoding='utf-8') as f: 
            nb = nbformat.read(f, 4)
    
        from nbconvert.preprocessors import CellExecutionError
        
        try:
            nb_executed, resources = pp.preprocess(nb, resources={})
        except CellExecutionError as err:
            print(colored(dirpath,"red"), colored(file_,"red"), "CellExecutionError")
            notebooks_w_errors.append(pth) 
            exit_=1
        else:
            print(colored(dirpath,"blue"), colored(file_,"green"), "OK")
        finally:
            nbformat.write(nb, str(pth))

print("run_all.py finished with exit code {}".format(exit_))

if notebooks_w_errors:
    print("These notebooks executed with errors".format(exit_))
    for nb in notebooks_w_errors:
        print(colored(nb,"red"))
else:
    print("These notebooks executed without errors")

sys.exit(exit_)
