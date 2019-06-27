#-*- coding: utf-8 -*-
import csv, time, subprocess, re, pywikibot

#WAIT_TIME = 15
with open('000-ws-ta-pre-clean.csv', 'r') as csvfile:
	reader = csv.reader(csvfile,delimiter="~")
#	count = 0
	for row in reader:
#		subprocess.call("sed -i 1d 000-ws-ta-pre-clean.csv",shell=True)          
	#if len(row) == 8: 
	# if not 'booktitle' in row:   
		wikiPage = row[0]#.decode('utf-8')
		print (wikiPage)
		
		site1 = pywikibot.Site('ta', 'wikisource')
		page = pywikibot.Page(site1, wikiPage)
		existingText = page.text
#		print('-------------------------------------------       தற்போதுள்ள பக்க உள்ளடக்கம்       ---------------------------------------------')
#		print(type (existingText))
#		print('\n\n' + existingText)
#		print('\n\n' + '------------------------------        தற்போதுள்ள பக்க உள்ளடக்கம்   முடிவடைந்தது.       --------------------------------------------')
		search_pattern = re.compile("\<noinclude\>.*?\<\/noinclude>", re.DOTALL)
		tags = re.findall(search_pattern, existingText)
		
		headerTag1 = tags[0]
		footerTag  = tags[1]
		middleText = re.sub(search_pattern, '', existingText).strip()
		dotsLine = '............................................................'
		print ('\n' + dotsLine + 'header' + dotsLine + '\n' + headerTag1 + '\n')
		print ('\n' + dotsLine + 'middle' + dotsLine + '\n' + middleText + '\n')
		print ('\n' + dotsLine + 'footer' + dotsLine + '\n' + footerTag + '\n')
#		time.sleep(WAIT_TIME)
