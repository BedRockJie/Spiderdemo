# -*- coding: utf-8 -*-#
#!/usr/bin/env python
# @Time    : 2020-5-8 12:09
# @Author  : BedRock_Jie
# @Site    : 
# @File    : u校园.py
# @Software: PyCharm

import requests
import json

url = "http://106.13.207.124/api/getUserScore.php"

heards = { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',}

data = 'token=' + 'ac38b4608296952fb3e9eb72055060ad'

text = requests.post(url,heards)

print(text.text)