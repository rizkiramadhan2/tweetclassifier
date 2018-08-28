#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:49:27 2018

@author: localuser
"""
import csv
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import os
class NB:
    
    
    def __init__(self,filename_fact,filename_hoax,raw_tf_filename,fitur_filename):
        self.filename_fact = filename_fact
        self.filename_hoax = filename_hoax
        
                
        text=[]
        t1=[]
        
        for filename in os.listdir(self.filename_fact):
            file = open(self.filename_fact+filename, 'r', encoding="utf8")
            x = file.read().lower()
            reg = r"http.*"
            t1.append(re.sub(reg, '', x))
        self.fact_doc = t1
        
        data_fakta =''
        for news in t1:
            data_fakta+=' '+news
        text.append(data_fakta)
        
        
        t2=[]
        for filename in os.listdir(self.filename_hoax):
            file = open(self.filename_hoax+filename, 'r', encoding="utf8")
            x = file.read().lower()
            reg = r"http.*"
            t2.append(re.sub(reg, '', x))
        self.hoax_doc = t2
        
        data_hoax =''
        for news in t2:
            data_hoax+=' '+news
        text.append(data_hoax)

        temp = []
        for i in text:
            temp.append(i.split())
            
        text = temp
        temp=''
        
        self.jml_fakta = len(t1)
        self.jml_hoax = len(t2)
        self.text=text
        self.raw_tf_filename=raw_tf_filename
        self.fitur_filename=fitur_filename
        
        #fitur setelah information gain
        file = open('web/fitur2.txt','r', encoding="utf8")
        ff = file.read()
        file.close()
        self.ig_fitur = ff.split() 
              
        
    #tokenisasi
    @staticmethod
    def tokenisasi(sentence):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        stem = stemmer.stem(sentence)
        reg = r'[a-z0-9]+|\d+\.?\,?\d+'
        token = re.findall(reg, stem)
        return token
    @staticmethod
    def tokenisasi_no_stem(sentence):
        reg = r'[a-z0-9]+|\d+\.?\,?\d+'
        token = re.findall(reg, sentence)
        return token
    
    #menghilangkan list stopword
    @staticmethod
    def clean_stopword(token):
        stopwords = []
        file = open('web/stopword.txt')
        for line in file:
            stopwords.append(line.strip())
        token_filter = []
        for i in token:
            if i not in stopwords:
                token_filter.append(i)
        return token_filter
    
    #preprocessing teks
    def preprocessing(self, text):
        token = []
        for i in text:
            token.append(self.tokenisasi(i)) 
        
        token_filtered = []
        for i in token:
            token_filtered.append(self.clean_stopword(i))
        return token_filtered
    
    def preprocessing_no_stem(self, text):
        token = []
        for i in text:
            token.append(self.tokenisasi_no_stem(i)) 
        
        token_filtered = []
        for i in token:
            token_filtered.append(self.clean_stopword(i))
        return token_filtered
    
    
    def preprocessing_bi(self, text):
        token = []
        for i in text:
            token.append(self.tokenisasi(i)) 
        
        token_filtered = []
        for i in token:
            token_filtered.append(self.clean_stopword(i))
        bigram = []    
        for i in token_filtered:
            temp=[]
            for  j in range(1,len(i)):
                temp.append(i[j-1]+' '+i[j])
            bigram.append(temp)
        return bigram
    
    #list term unik
    @staticmethod
    def list_term(token):
        term_unik= []
        for i in range(0, len(token)):
            for j in range(0, len(token[i])):
                if str(token[i][j]) not in term_unik:
                    term_unik.append(token[i][j])
        return term_unik
       
    
    #kemunculan kata
    @staticmethod
    def frekuen_kata(term, token):
        frekuensi_kata = []
        for k in range(len(term)):
            frekuensi_dokumen = []
            for i in range(len(token)):
                counter = 0
                for j in range(len(token[i])):
                    if term[k] == token[i][j]:
                        counter += 1
                frekuensi_dokumen.append(counter)
            frekuensi_kata.append(frekuensi_dokumen)
        return frekuensi_kata
    #
    #log-tf
    @staticmethod
    def term_freq(term):
        tf = []
        for i in term:
            if i > 0:
                tf.append(1 + math.log(i, 10))
            else:
                tf.append(0)
        return tf
    
    @staticmethod
    def transpose(list):
        t = []
        for i in range(len(list[0])):
            t_row = []
            for j in range(len(list)):
                t_row.append(list[j][i])
            t.append(t_row)
        return t
    
    def process(self):
#        token = self.preprocessing(self.text)
#        term = self.list_term(token)
        token = self.text
        term = self.ig_fitur #self.list_term(token)
        
        frekuensi_kata = self.frekuen_kata(term, token)
        
        with open(self.fitur_filename, 'w') as output:
            wr = csv.writer(output, lineterminator='\n')
            for t in term:
                wr.writerow([t]) 
        with open(self.raw_tf_filename, 'w') as csvfile:
            wr = csv.writer(csvfile, lineterminator='\n')
            wr.writerows(frekuensi_kata)
            
    def process_bigram(self):
        token = self.preprocessing_bi(self.text)
        term = self.list_term(token)
        
        frekuensi_kata = self.frekuen_kata(term, token)
        
        with open(self.fitur_filename, 'w') as output:
            wr = csv.writer(output, lineterminator='\n')
            for t in term:
                wr.writerow([t]) 
        with open(self.raw_tf_filename, 'w') as csvfile:
            wr = csv.writer(csvfile, lineterminator='\n')
            wr.writerows(frekuensi_kata)
            
            
    def testing(self, filename,filename2='',record=False):
    
            
        testing_list=[]
        sentence = False
        if os.path.isdir(filename):
            
            for name in os.listdir(filename):
                file = open(filename+name, 'r', encoding="utf8")
                x = file.read().lower()
                reg = r"http.*"
                testing_list.append(re.sub(reg, '', x))
            file=open(filename2, 'r', encoding="utf8")
            x = file.read()
            file.close()
            label = x.split('\n')
            total = len(label)
        else:
            sentence = True
            testing_list.append(filename)

#        file = open(filename, 'r')
#        x = file.read().lower()
#        reg = r"http.*"
#        file.close()
#        testing = re.sub(reg, '', x)
#        testing_list = testing.split('\n')
        

        
        
        missed=0
        counter=0
        list_sim = []
        file = open(self.fitur_filename)
        fitur = file.read()
        file.close()
        
        frek = open(self.raw_tf_filename)
        fr = frek.read()
        frek.close()
        list_fr =[]
        for i in fr.split('\n'):
            temp=[]
            for j in i.split(','):
                temp.append(j)
            list_fr.append(temp)
            
        list_kata=[]
        fit=fitur.split()
        for i in range(len(fit)):
            list1=[fit[i]]
            list2=[list_fr[i]]
            list_kata.append(list1+list2)
     
            
        total_f_fact=0
        total_f_hoax=0
        
        for i in list_fr[:-1]:
           total_f_fact+=int(i[0])
           total_f_hoax+=int(i[1])
        
        hsl=[]
        for tweet in testing_list:
            #tweet = ['Hoax, Lowongan Kerja di Garuda Indonesia Tersebar Viral ']
            #print('preprocessing query..')
            tw = tweet.split()
            token = self.preprocessing([tweet])
            query = self.list_term(token)
            print(query)
            p_fakta=self.jml_fakta/(self.jml_fakta+self.jml_hoax)
            p_hoax=self.jml_hoax/(self.jml_fakta+self.jml_hoax)
            #print(p_hoax)
            #print(total_f_hoax)
            lis = []
            for i in query:
                for j in list_kata:
                    if i == j[0]:
                        #print(j[0])
                        p_fakta += math.log10((int(j[1][0])+1)/(total_f_fact+len(fit)))
                        p_hoax += math.log10((int(j[1][1])+1)/(total_f_hoax+len(fit)))
                                            
            lis.append([p_fakta])
            lis.append([p_hoax])
            # print(lis)

            if max(lis)==lis[1]:
                hasil = 'HOAX'
            else:
                hasil = 'FAKTA'
            if sentence:
                if float(max(lis)[0]) == float(0.5):
                    hasil = 'Maaf, tidak dapat dideteksi'
                if record == True:
                    print(str(counter+1)+' '+hasil +' '+str(lis))
                return hasil
            hsl.append(hasil)
#            sim=''
   
                
            #similarity 
#            if hasil == 'hoax':
#                sim=cos.similarity(tweet)
#                if sim[0]<0.8:
#                    content=sim[1]
#                    s=''
#                    for i in content:
#                        s+='\n'+i.lower()
#                    if 'hoax' in s or 'hoaks' in s:
#                        hasil ='hoax'
#                        print(str(counter+1)+' '+tweet+' '+colored(hasil, 'red')+' '+str(sim[0]))
#                    else:
#                        hasil ='fakta'
#                        print(str(counter+1)+' '+tweet+' '+colored(hasil, 'green')+' '+str(sim[0]))
#                else:
#                    print(str(counter+1)+' '+tweet+' '+colored(hasil, 'red'))
#                    
#            else:
#                print(str(counter+1)+' '+tweet+' '+colored(hasil, 'green'))
#            print('\n')
#                
#            list_sim.append(sim)
#            print(hasil+' '+str(sim))
#            print(hasil+' '+str(max(lis)))
##            
#        
            
                
            if hasil.lower() != label[counter]:
                missed+=1
            counter+=1
            #break
        acc = ((total-missed)/total)*100
        res =[]
        res.append(acc)
        res.append(hsl)
        print('akurasi : '+str(acc))
        return res
        
    

    
    