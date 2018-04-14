#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup
import time

#getting author's category name 
with open('0-commons-book-authors-list.csv', 'r') as commonsAuthorsList:
    reader = csv.reader(commonsAuthorsList,delimiter='~')
    for row in reader:
#   if len(row) == 1:
        authorCatName = row[0]
    #authorCatName = 'பேராசிரியர் அ. ச. ஞானசம்பந்தன்'

        #creating the commons author category url
        rUrl  = u'https://commons.wikimedia.org/wiki/Category:'+authorCatName
        #print('\n'+rUrl+'\n')

        #getting all the data from above the category url
        rData = requests.get(rUrl)
        soup = BeautifulSoup(rData.content, 'lxml')

        #extracting the above category's name from the soup
        for authorCat in soup.find('h1'):
            print(authorCat+'\n')
	
        #cleaning the commons category's name
        booksAuthor = authorCat.replace('Category:','')
        #print(booksAuthor+'\n')

        #getting books name only
        for item in soup.find_all('div', class_='gallerytext'):
            bookTags = item.a
            #print(bookTags)

            #print(bookTags['title'])  # or print(a_tag['href']) if you want the link

            #converting the commons file names for wikisource indexes
            indexTitle = bookTags['title'].replace('File','Index')

            #print(bookIndex)
            bookIndexAuthor = indexTitle+'~'+booksAuthor+'~'#+info
        #   printing the index name and the author one by one
        #   WAIT_TIME = 5    
            print(bookIndexAuthor)
        #   time.sleep(WAIT_TIME)

        #   if you want to writedown the bookIndexAuthor, remove the hash from the next 2 lines and rerun.
        #   with open('0-bookIndexAuthor.csv', 'a') as bookIndexDataAll:
        #   writer = bookIndexDataAll.write(bookIndexAuthor+'\n')


            bookUrl= 'https://commons.wikimedia.org/wiki/' + indexTitle.replace('அட்டவணை','File').replace('Index','File')
            print ('\n'+ bookUrl+'\n')

        #   getting the book's content for the bs4
            bookContent = requests.get(bookUrl).content

        #   getting the content with clean html tags
            bookSoup = BeautifulSoup(bookContent,'lxml')
        #   print (bookSoup)
		
        #   extracting specific content from the soup
            bookdataList = bookSoup.find(id='mw-content-text')
            for item in bookdataList.find_all('div',class_='fullMedia'):
                bookTags = item.span

                bookInfo = bookTags.text.replace('(','').replace(')','').replace(' pixels,',' pixels~').replace(' file size:','').replace(' MB,','MB~').replace(' KB,','KB~').replace('pdf,','pdf~').replace('~ ','~').replace(' pages','pages')
                bookTag = item.a
                downloadURL = bookTag['href']
                indexBookInfoAll = indexTitle+'~'+booksAuthor+'~'+bookInfo
                WAIT_TIME = 5
                print (indexBookInfoAll+'\n')
                time.sleep(WAIT_TIME)
                print(downloadURL)
                downloadURLclean = downloadURL[:52]
                downloadURLcleanTitle = indexTitle+'~'+downloadURLclean+'~'+downloadURL
                
                print('The fileURL = '+ bookUrl+'~'+'The downloadURL-clean = '+downloadURLcleanTitle+'~'+'The downloadURL-unclean = '+downloadURL)

                with open(booksAuthor+'-books-info.csv', 'a') as bookIndexs2:
                    writer = bookIndexs2.write(indexBookInfoAll+'\n')

                with open(booksAuthor+'-down-info.csv', 'a') as bookIndexs3:
                    writer = bookIndexs3.write(downloadURLcleanTitle+'\n')
