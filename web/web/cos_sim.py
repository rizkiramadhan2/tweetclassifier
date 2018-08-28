#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:01:14 2018

@author: localuser
"""
#from newsplease import NewsPlease
#article = NewsPlease.from_url('https://news.detik.com/berita/d-3922736/kementan-tegaskan-info-telur-palsu-hoax')
#print(dir(article))


from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
from .google_search import gs as gs
from .generate_data import gd as gd
import re
from .IR import ir as ir


class cosim:
    TAG_RE = re.compile(r'<[^>]+>')

    def remove_tags(text):
        return TAG_RE.sub('', text)


    def test():
        print('wawaw')

    # def get_content(url):
    # #    print('get content..')
    # #    with urllib.request.urlopen(url) as response:
    # #       html = response.read()
    #     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
    #     source_code = urlopen(req).read()
    #     soup = BeautifulSoup(source_code,"lxml")
    #     pre_text = soup.find_all(['title'])
    #     doc=""
    #     for s in pre_text:
    #         doc+=remove_tags(str(s))
    #     return doc

    def similarity(query):
        
       # print('query : '+ query)
    #    sent =''
    #    for w in query:
    #        sent+=' '+ w
        #q=['Kemkominfo Buat Help Desk Registrasi Kartu Prabayar, Itu Hoax via. @tempoekbis ']
        
        
    #    f=""
    #    for t in term:
    #        f+=' '+t
    #    if 'hoax' not in query:
    #        query+=' hoax'
        #content = gs.search_(query,10)
        #print(url)
        #content=[]
        g = gd()
        token = g.preprocessing([query])
    #    s=''
    #    for t in token[0]:
    #        s+=' '+t
        gresult = gs.search_(query)
        title = []

        for i in gresult:
            title.append(i[0])
        #term = g.list_term(token)
        #print(token)
     
        
    #    for u in url:
    #        content.append(get_content(u).lower())
    #    i=0
        #print(content)
    #    label = False
    #    s = ''
    #    print(content)
    #    for doc in content:
    ##        s+='\n'+doc
    #       file = open('google-result/'+str(i+1)+'.txt','w')
    #       file.write(doc)
    #       file.close()
    #       i+=1
    #    if 'hoax' not in s:
    #        label = True
    #    if label==True:
    #        return 'fakta'
    #    else:
    #        return 'hoax'
            
        g.run(title)
        i = ir()
        return i.sim(token[0],gresult)

    #print(similarity(['mk', 'cabut', 'pasal', 'uu', 'md3', 'mendagri']))

        #print(similarity(['mk', 'cabut', 'pasal', 'uu', 'md3', 'mendagri']))