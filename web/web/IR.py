import csv
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import math
import operator


class ir:
    #tokenisasi
    def tokenisasi(self,sentence):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        stem = stemmer.stem(sentence)
        reg = r'[a-z0-9]+|\d+\.?\,?\d+'
        token = re.findall(reg, stem)
        return token

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

    ##
    def match(self,key, list_term):
        f = []
        for i in range(len(list_term)):
            c = 0
            for j in range(len(key)):
                if list_term[i] == key[j]:
                    c += 1
            f.append(c)
        return f

    #menghilangkan list stopword
    def clean_stopword(self,token):
        stopwords = []
        file = open('stopword.txt')
        for line in file:
            stopwords.append(line.strip())
        token_filter = []
        for i in token:
            if i not in stopwords:
                token_filter.append(i)
        return token_filter


    def transpose(self,list):
        t = []
        for i in range(len(list[0])):
            t_row = []
            for j in range(len(list)):
                t_row.append(list[j][i])
            t.append(t_row)
        return t

    def normalisasi(self,tf_idf):
        w = []
        counter = 0
        for i in tf_idf:
            counter += math.pow(i, 2)
        divider = math.sqrt(counter)
        for i in tf_idf:
            if divider == 0:
                w.append(0)
            else:
                w.append(i/divider)
        return w
    ##
    def cosim(self,a, b):
        counter = 0
        for i in range(len(a)):
            counter += a[i]*b[i]
        return counter



    def sim(self,query,content):
        term_unik = []
        with open('web/google-result/term_unik.csv', newline='') as csvfile:
            for row in csv.reader(csvfile):
                term_unik.append(row[0])
        list_idf = []
        with open('web/google-result/list_idf.csv', newline='') as csvfile:
            for row in csv.reader(csvfile):
                list_idf.append(float(row[0]))
        tf_idf = []
        with open('web/google-result/norm_tf.csv', newline='') as csvfile:
            for row in csv.reader(csvfile):
                tf_idf.append(row)
        for i in range(len(tf_idf)):
            for j in range(len(tf_idf[i])):
                tf_idf[i][j] = float(tf_idf[i][j])
        #query_token = tokenisasi(query)
        #new_query = clean_stopword(query_token)
        #print('hitung similarity')
        query_freq = self.match(query, term_unik)
        tf = self.term_freq(query_freq)
        tf_idf_query = []
        for i in range(len(tf)):
            tf_idf_query.append(tf[i]*list_idf[i])   
        new_tfidf = self.normalisasi(tf_idf_query)
        d = []
        trans_tfidf = self.transpose(tf_idf)
        for i in range(len(tf_idf[0])):
            d.append(self.cosim(trans_tfidf[i], new_tfidf))
        file = open('web/google-result/index.txt', 'r')
        index = file.read().split('\n')
        file.close()
        distance = {}
        for i in range(len(content)):
            distance[index[i]] = d[i]
        sort = sorted(distance.items(), key=operator.itemgetter(1), reverse=True)
        result = []

        for i in sort:
            result.append([content[int(i[0])-1][0],content[int(i[0])-1][1] ,str(i[1])])
    #    for i in range(0, 1):
    #         return int(sort[i][0])-1
    #    for i in range(0, 3):
        
    #        print('Dok ', i+1, ': ', sort[i][0], '. Similarity :', float(sort[i][1]))
        return result #[sort[0][1],sort[0][0]]