#!/usr/bin python3

from datetime import datetime
import sys


now = datetime.now()
date_string = now.strftime("%Y/%m/%d %H:%M:%S +0000")

title = sys.argv[1]

categorias = sys.argv[2].split(":")
if(len(categorias)>2):
    print("Maximo 2 categorias")
    exit

tags = sys.argv[3].split(":")

header = f"""---
title: {title}
author: Ismael Delgado
date: {date_string}
categories: {categorias}
tags: {tags}
render_with_liquid: false
---"""

with open("./_posts/"+date_string.split(" ")[0].replace("/","-")+"-"+title.replace(" ","-")+".md", "w") as f:
    f.write(header)

print(header)


print("Uso: new_post.py 'nombre del articulo' 'categoria1:categoria2' 'tag1:tag2...' ")

