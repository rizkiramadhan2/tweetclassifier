#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:05:02 2018

@author: localuser
"""
from .NB import NB as nb
import sys
from .google_search import gs as gs
from .cos_sim import cosim as cos
#data = pp.Pre_processing('data/data2/80_20/fakta/','data/data2/80_20/hoax/','data/data2/80_20/no_stem_raw_tf.csv','data/data2/80_20/no_stem_term_unik.csv')
#data = pp.Pre_processing('data/data2/80_20/fakta/','data/data2/80_20/hoax/','data/data2/bigram/raw_tf.csv','data/data2/bigram/term_unik.csv')
#data = pp.Pre_processing('data/data2/80_20/fakta/','data/data2/80_20/hoax/','data/data2/80_20/raw_tf.csv','data/data2/80_20/term_unik.csv')

class Classification:
	
	
	

	#10 fold cross validation
	def cross_validation():
	    akurasi =0
	    for i in range(10):
	        dat = nb('web/data/data2/cv/'+str(i+1)+'/fakta/','web/data/data2/cv/'+str(i+1)+'/hoax/','web/data/data2/cv/'+str(i+1)+'/raw_tf.csv','web/data/data2/cv/'+str(i+1)+'/term_unik.csv')
	        # dat.process()
	        akurasi+=dat.testing('web/data/data2/cv/'+str(i+1)+'/test/','web/lbl')[0]
	    print(akurasi/10)

	def classify(a,b=''):
		i=6
		data =  nb('web/data/data2/cv/'+str(i)+'/fakta/','web/data/data2/cv/'+str(i)+'/hoax/','web/data/data2/cv/'+str(i)+'/raw_tf.csv','web/data/data2/cv/'+str(i)+'/term_unik.csv')
		return data.testing(a,b,True)

	#classify('data/data2/cv/1/test/','lbl')
	#cross_validation()
	

	
	def get_relevance(a):
		# cos.test()
	    return cos.similarity(a)


#preprocess
#count=1
#for i in data.fact_doc:
#    r = data.preprocessing([i])[0]
#    s=''
#    for j in r:
#        s+=' '+j
#    filename = 'data/data2/stem/fakta/'
#    file = open(filename+str(count)+'.txt','w')
#    file.write(s)
#    file.close
#    print(str(count)+'.txt saved in fakta')
#    count+=1
    
#count = 1    
#for i in data.hoax_doc:
#    r = data.preprocessing([i])[0]
#    s=''
#    for j in r:
#        s+=' '+j
#    filename = 'data/data2/stem/hoax/'
#    file = open(filename+str(count)+'131.txt','w')
#    file.write(s)
#    file.close
#    print(str(count)+'.txt saved in hoax')
#    count+=1

#data.process()
#data.process_bigram()
#data.classify('test','lbl')
#data.classify(sys.argv[1],sys.argv[2])