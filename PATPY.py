# -*- coding: utf-8 -*-
import xlrd
import matplotlib.pyplot as plt
corpora_text = []
words_freq = {}
bigrams_freq = {}
top_words = {}
spanish_stopwords = ["a","acá","ahí","ajena","ajenas","ajeno","ajenos","al","algo","algún","alguna","algunas","alguno","algunos","allá","alli","allí","ambos","ampleamos","ante","antes","aquel","aquella","aquellas","aquello","aquellos","aqui","aquí","arriba","asi","atras","aun","aunque","bajo","bastante","bien","cabe","cada","casi","cierta","ciertas","cierto","ciertos","como","cómo","con","conmigo","conseguimos","conseguir","consigo","consigue","consiguen","consigues","contigo","contra","cual","cuales","cualquier","cualquiera","cualquieras","cuan","cuán","cuando","cuanta","cuánta","cuantas","cuántas","cuanto","cuánto","cuantos","cuántos","de","dejar","del","demás","demas","demasiada","demasiadas","demasiado","demasiados","dentro","desde","donde","dos","el","él","ella","ellas","ello","ellos","empleais","emplean","emplear","empleas","empleo","en","encima","entonces","entre","era","eramos","eran","eras","eres","es","esa","esas","ese","eso","esos","esta","estaba","estado","estais","estamos","estan","estar","estas","este","esto","estos","estoy","etc","fin","fue","fueron","fui","fuimos","gueno","ha","hace","haceis","hacemos","hacen","hacer","haces","hacia","hago","hasta","incluso","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","jamás","junto","juntos","la","largo","las","lo","los","mas","más","me","menos","mi","mía","mia","mias","mientras","mio","mío","mios","mis","misma","mismas","mismo","mismos","modo","mucha","muchas","muchísima","muchísimas","muchísimo","muchísimos","mucho","muchos","muy","nada","ni","ningun","ninguna","ningunas","ninguno","ningunos","no","nos","nosotras","nosotros","nuestra","nuestras","nuestro","nuestros","nunca","o","os","otra","otras","otro","otros","para","parecer","pero","poca","pocas","poco","pocos","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","por","por qué","porque","primero","primero desde","puede","pueden","puedo","pues","que","qué","querer","quien","quién","quienes","quienesquiera","quienquiera","quiza","quizas","sabe","sabeis","sabemos","saben","saber","sabes","se","segun","ser","si","sí","siempre","siendo","sin","sín","sino","so","sobre","sois","solamente","solo","somos","soy","sr","sra","sres","sta","su","sus","suya","suyas","suyo","suyos","tal","tales","también","tambien","tampoco","tan","tanta","tantas","tanto","tantos","te","teneis","tenemos","tener","tengo","ti","tiempo","tiene","tienen","toda","todas","todo","todos","tomar","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","tú","tu","tus","tuya","tuyo","tuyos","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","usted","ustedes","va","vais","valor","vamos","van","varias","varios","vaya","verdad","verdadera","vosotras","vosotros","voy","vuestra","vuestras","vuestro","vuestros","y","ya","yo"]
twitter_words = ["rt", "…", "q"]
R = corpora_text
Extracts = []
Attributes = []
Values = []
Templates = []
Umbral = 0


def loadCorpora():
    corpora = xlrd.open_workbook("./Corpora/Corpus03.xls")
    print "The number of worksheets is ", corpora.nsheets
    for sheet in corpora.sheets():
        nrows = sheet.nrows
        ncols = sheet.ncols
        for i in range(nrows):
            if(sheet.cell_value(i,15) == 'es'):
                text = sheet.cell_value(i,ncols-1).encode('utf-8')
                for word in text.split():
                    if word.startswith( 'http:'):
                        text = text.replace(word, "")
                if not text in corpora_text:
                    corpora_text.append(text)
                    print text
    print 'Corpus finalizado con ' + str(len(corpora_text)) + ' entradas'

def sentenceFilter(sentence):
    sentence = sentence.lower()
    for word in spanish_stopwords:
        sentence = sentence.replace(" "+word+" ", " ")
    for word in twitter_words: 
        sentence = sentence.replace(" "+word+" "," ")
    return sentence
    

def bigramsFrecuency():
    for text in corpora_text:
        words = sentenceFilter(text)
        words = words.split()
        for n in range(1,len(words)-1):
            if len(words[n]) > 1 and len(words[n+1]) > 1:
                biKey = str(words[n].lower().replace(",","")) + "_" + str(words[n+1].lower().replace(",",""))
                biKey =  unicode(biKey, errors='replace')
                if biKey in bigrams_freq:
                    bigrams_freq[biKey] += 1
                else:
                    bigrams_freq[biKey] = 1
    for key, value in sorted(bigrams_freq.iteritems(), key=lambda (k,v): (v,k)):
        if value > 300:
                top_words[key] = value
                print "%s: %s" % (key, value)

                   
            
            
            

def wordFrecuency():
    for text in corpora_text:
        words = text.split()
        for word in words:
            word = word.replace(",","")
            word = word.lower()
            if word not in spanish_stopwords+twitter_words:
                if word in words_freq:
                    words_freq[word] += 1
                else:
                    words_freq[word] = 1
    for key, value in sorted(words_freq.iteritems(), key=lambda (k,v): (v,k)):
        if value > 300:
                top_words[key.decode('utf-8')] = value
                print "%s: %s" % (key, value)




def drawPlot(): 
    D = top_words
    plt.bar(range(len(D)), D.values(), align='center')
    plt.xticks(range(len(D)), D.keys())

    plt.show()

def paInit():
    global Templates, Umbral, Extracts, R
    Templates = []
    Umbral = 6
    R = corpora_text
    Extracts = [("gobierno", "malo"), ("gobierno", "bueno"), ("gobierno", "triste")]

def templateInduction(R):
    global Extracts
    print Extracts
    for r in R:
        for e in Extracts:
            print e[0]
            if e[0] in r:
                print r
                if e[1] in r:
                    print r

def paRun(R):
    templateInduction(R)

def patternAlgorithm():
    paInit()
    paRun(R)        


    
loadCorpora()
bigramsFrecuency()
drawPlot()

