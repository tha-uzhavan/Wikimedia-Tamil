#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import time

#getting author's category name 
with open('2015-tva-commons-pdf-author-s-list.csv', 'r') as commonsAuthorsList:
    reader = csv.reader(commonsAuthorsList,delimiter='~')
    for row in reader:
#   if len(row) == 2:
        authorCatName = row[0]

        #creating the commons author category url
        rUrl  = u'https://commons.wikimedia.org/wiki/Category:'+authorCatName
        print('\n'+rUrl+'\n')
        
        #getting all the data from above the category url
        rData = requests.get(rUrl)
        soup = BeautifulSoup(rData.content, 'lxml')

        #extracting the above category's name from the soup
        for authorCat in soup.find('h1'):
            print(authorCat+'\n')

        #cleaning the commons category's name
        booksAuthor = authorCat.replace('Category:','')
        print(booksAuthor+'\n')
        
        #getting all files name only
        #for item in soup.find_all(class_='gallerytext'):
            #bookTags = item.a
            #print(bookTags['title'])  # or print(a_tag['href']) if you want the link

        #getting pdfs name only
        for books in soup.find_all(class_='galleryfilename'):
            if '.pdf' in books.get('title'):
                booksTitle = books['title']
                #print(booksTitle)

                #converting the commons file names for wikisource indexes
                indexTitle = booksTitle.replace('File','Index')
                #print(indexTitle)

                bookIndexAuthor = indexTitle+'~'+booksAuthor+'~'#+info
                #   printing the index name and the author one by one
                #WAIT_TIME = 10    
                print(bookIndexAuthor)
                #time.sleep(WAIT_TIME)

             #if you want to writedown the bookIndexAuthor, remove the hash from the next 2 lines and rerun.
                #with open('0-bookIndexAuthor.csv', 'a') as bookIndexDataAll:
                    #writer = bookIndexDataAll.write(bookIndexAuthor+'\n')

                #creating a book's url to get the book info
                bookUrl= 'https://commons.wikimedia.org/wiki/' + indexTitle.replace('அட்டவணை','File').replace('Index','File')
                print ('\n'+ bookUrl+'\n')

                #getting the book's content for the bs4
                bookContent = requests.get(bookUrl).content

                #getting the content with clean html tags
                bookSoup = BeautifulSoup(bookContent,'lxml')
                #print (bookSoup)

                #extracting specific content from the soup
                bookdataList = bookSoup.find(id='mw-content-text')
                for item in bookdataList.find_all('div',class_='fullMedia'):
                    bookTags2 = item.span

                    bookInfo = bookTags2.text.replace('(','').replace(')','').replace(' pixels,',' pixels~').replace(' file size:','').replace(' MB,','MB~').replace(' KB,','KB~').replace('pdf,','pdf~').replace('~ ','~').replace(' pages','pages')
                    bookTag = item.a
                    downloadURL = bookTag['href']
                    indexBookInfoAll = indexTitle+'~'+booksAuthor+'~'+bookInfo
                    WAIT_TIME = 15
                    print (indexBookInfoAll+'\n')
                    time.sleep(WAIT_TIME)

                    downloadURLclean = downloadURL[:52]
                    downloadURLcleanTitle = indexTitle+'~'+downloadURLclean+'~'+downloadURL

                    print('The fileURL = '+ bookUrl+'~'+'The downloadURL-clean = '+downloadURLcleanTitle+'~'+'The downloadURL-unclean = '+downloadURL)

                    #with open(booksAuthor+'-books-info.csv', 'a') as bookIndexs2:
                    #writer = bookIndexs2.write(indexBookInfoAll+'\n')

                    #with open(booksAuthor+'-down-info.csv', 'a') as bookIndexs3:
                    #   writer = bookIndexs3.write(downloadURLcleanTitle+'\n')

                    with open('2015-tva-commons-pdf-books-all-info.csv', 'a') as bookIndexs4:
                        writer = bookIndexs4.write(indexBookInfoAll+'\n')

                    #with open('2015-tva-commons-pdf-down-info.csv', 'a') as bookIndexs5:
                    #   writer = bookIndexs5.write(downloadURLcleanTitle+'\n')
