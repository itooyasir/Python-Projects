# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:03:40 2022

@author: HP
"""

import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

number = "+917780874866"
number = ph.parse(number)
print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))
