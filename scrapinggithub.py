# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:48:19 2022

@author: Yasir Itoo
"""

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/itooyasir"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)