import csv
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math



class gd:
    #preprocessing teks

    def preprocessing(self,text):
        token = []
        for i in text:
            token.append(self.tokenisasi(i)) 
        
        token_filtered = []
        for i in token:
            token_filtered.append(self.clean_stopword(i))
        return token_filtered

    def preprocessing_no_stem(text):
        token = []
        for i in text:
            token.append(tokenisasi_no_stem(i)) 
        
        token_filtered = []
        for i in token:
            token_filtered.append(clean_stopword(i))
        return token_filtered
    #tokenisasi
    @staticmethod
    def tokenisasi(sentence):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        stem = stemmer.stem(sentence)
        reg = r'[a-z0-9]+|\d+\.?\,?\d+'
        token = re.findall(reg, stem)
        return token

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


    #list term unik
    def list_term(self,token):
        term_unik= []
        for i in range(0, len(token)):
            for j in range(0, len(token[i])):
                if token[i][j] not in term_unik:
                    term_unik.append(token[i][j])
        return term_unik

    #kemunculan kata
    def frekuen_kata(self,term, token):
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
    def term_freq(self,term):
        tf = []
        for i in term:
            if i > 0:
                tf.append(1 + math.log(i, 10))
            else:
                tf.append(0)
        return tf

    #normalisasi
    def norm_tf(self,tf_idf):
        t = self.transpose(tf_idf)
        d = []
        for i in range(len(t)):
            counter = 0
            for j in range(len(t[i])):
                counter += math.pow(t[i][j], 2)
            d.append(math.sqrt(counter))
        w = []
        for i in range(len(tf_idf)):
            row = []
            for j in range(len(tf_idf[i])):           
                row.append(tf_idf[i][j] / d[j])
            w.append(row)
        return w

    def transpose(self,lis):
        t = []
        for i in range(len(lis[0])):
            t_row = []
            for j in range(len(lis)):
                t_row.append(lis[j][i])
            t.append(t_row)
        return t

    #idf
    def idf(self,term_freq):
        idf = []
        for i in range(len(term_freq)):
            counter = 0
            for j in range(len(term_freq[i])):
                if term_freq[i][j] > 0:
                    counter += 1
            idf.append(1+math.log(len(term_freq[i]) / counter, 10))
        return idf

    #tf*idf
    def tfidf(self,tf, idf):
        tf_idf = []
        for i in tf:
            tf_idf.append(i * idf)
        return tf_idf


    def run(self,text):
        #print('preprocessing google search result..')
    #    text = []
    #    for i in range(0, 3):
    #        n = 'google-result/' + str(i+1) + '.txt'
    #        file = open(n, 'r')
    #        x = file.read().lower()
    #        text.append(x)
    #    print(text)   
        token = self.preprocessing(text)
        term = self.list_term(token)
    #    print(token)
    #    print(term)
        with open('web/google-result/term_unik.csv', 'w') as output:
            wr = csv.writer(output, lineterminator='\n')
            for t in term:
                wr.writerow([t])
                
        #menghitung frekuensi kata
        frekuensi_kata = self.frekuen_kata(term, token)

        #menghitung tf
        tf = []
        for i in frekuensi_kata:
            tf.append(self.term_freq(i))
      
        #menghitung idf
        idf_ = self.idf(frekuensi_kata)

        with open('web/google-result/list_idf.csv', 'w') as output:
            wr = csv.writer(output, lineterminator='\n')
            for i in idf_:
                wr.writerow([i])
        tf_idf = []
        for i in range(len(tf)):
            tf_idf.append(self.tfidf(tf[i], idf_[i]))
        norm = self.norm_tf(tf_idf)
        
        with open('web/google-result/norm_tf.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, lineterminator='\n')
            wr.writerows(norm)