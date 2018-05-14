#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv
import pywikibot
import time
import re

WAIT_TIME = 15
with open('pdfInfo.csv', 'r') as csvfile:
	reader = csv.reader(csvfile,delimiter="~")
	for row in reader:
	#if len(row) == 8:
	# if not 'booktitle' in row:
#if you use other PAWS,remove the hash to decode well
		wikiPage1 = row[0].replace('File','Index')#.decode('utf-8')
		bookAuthor = row[1]
		bookSize = row[3].replace('MB','')
		indexPages = row[5].replace('pages','')
		print (wikiPage1)
		print (bookAuthor)
		print (indexPages)
		print (bookSize)
		
		site = pywikibot.Site('ta', 'wikisource')
		page1 = pywikibot.Page(site, wikiPage1)
		
		res1 = re.compile('\|Number of pages=*(\d+)').search(page1.text)
		if res1:
			print("number of pages is already assign to %s" % res1.group(1))
		else:
			page1.text = page1.text.replace('|Number of pages=','|Number of pages='+indexPages)
			page1.save(summary='+ கோப்பளவு =' + bookSize+ ', நூற்பக்கங்கள் = '+indexPages) 

		res2 = re.compile('\|File size= *(\d+)').search(page1.text)
		if res2:
			print("File size is already assign to %s" % res2.group(1))
		else:
			page1.text = page1.text.replace('|File size=','|File size='+bookSize)

			page1.save(summary='+ கோப்பளவு =' + bookSize+ ', நூற்பக்கங்கள் = '+indexPages) 

		time.sleep(WAIT_TIME)
