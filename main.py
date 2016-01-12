#!/usr/bin/env python

import csv, re

file_name = "./doctomedia_nisman_old_application.csv"
output = "./doc2media_nisman.csv"

reader = csv.DictReader(open(file_name, "rb"))

fieldnamesD2M = ['page', 'title', 'description', 'media_type', 'media_src', 'media_text']
writer = csv.DictWriter(open(output, "wb"), fieldnames=fieldnamesD2M)
writer.writeheader()


for row in reader:
    if not row['media_src']:
        writer.writerow( 
            {
            'page': row['pagina'], 
            'title': row['titulo'], 
            'description': row['contenido'], 
            })
    
    else:
        for media_src in row['media_src'].split(","):
            try:
                media_src, media_text = media_src.strip().split(" ")
                
                if media_text:
                    media_text = re.sub("[\[\]]", "", media_text)
                    media_text = re.sub("p\.", "Pag. ", media_text)
                
                writer.writerow( 
                    {
                        'page': row['pagina'], 'title': row['titulo'], 'description': row['contenido'],
                        'media_type': 'audio',
                        'media_src':  media_src,
                        'media_text': media_text,
                    })
            except Exception, e:
                print e, media_src

