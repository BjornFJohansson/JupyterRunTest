#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pathlib
import sys
import nbformat
from nbconvert import HTMLExporter

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

html_exporter = HTMLExporter()

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
        body, resources = html_exporter.from_filename(str(pth))
        open(pth.with_suffix(".html"), mode='w', encoding='utf-8').write(body)
        print(colored(dirpath,"blue"), colored(file_,"green"), "OK")
    break