# -*- coding: utf-8 -*-
"""
New project

Date: 13/08/2023

Name of project: Krill lotin bot

Creater: Sardorbek Khamrakulov
"""
from transliterate import to_cyrillic, to_latin

print("Kiritilgan matnni lotindan krill alifbosiga,\n"
      "yoki krilldan lotin alifbosiga o'zgartiruvchi dastur!")
matn = input("Matn kiriting: ")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))
    