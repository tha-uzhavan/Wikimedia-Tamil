#-*- coding: utf-8 -*-

#bringing the needed library modules
import csv,pywikibot,time

WAIT_TIME = 10
with open('now-cat-clean.csv', 'r') as csvfile:
	reader = csv.reader(csvfile,delimiter="~")
	count = 0
	for row in reader:
	#if len(row) == 8: உயிரியல்
	# if not 'booktitle' in row:   
		wiktHeader = row[0]#.decode('utf-8')
		print ()
		print (wiktHeader)
		
		site1 = pywikibot.Site('ta', 'wiktionary')
		page = pywikibot.Page(site1, wiktHeader)
#		print (page.text)
#		findCategory = ''#.decode('utf-8')
		if 'துப்புரவு செய்ய வேண்டியவை' in page.text:
			page.text = page.text.replace('துப்புரவு செய்ய வேண்டியவை','மேம்படுத்த வேண்டியன-தமிழ்')
		print (page.text)
		if 'thumb' or 'gallery>' in page.text:
			if not '{{படம்' or '[[பகுப்பு:படங்களுள்ளவை]]' in page.text:
				page.text = page.text +'\n'+'[[பகுப்பு:தமிழ்-படங்களுள்ளவை]]'
				print (page.text)
#		page.text = page.text
		catSummary = '''- [[பகுப்பு:மேம்படுத்த வேண்டியன-தமிழ்|பகுப்பு மாற்றம்]]'''#.decode('utf-8')
		page.save(summary= catSummary)
		time.sleep(WAIT_TIME)