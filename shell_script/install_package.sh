#!/bin/bash
#!/usr/bin/php
# 使用conda命令安装包，在conda install不可用的情况下，使用pip
# 或者conda install --yes --file requirements.txt
# 或者pip install -r requirements.txt
while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
