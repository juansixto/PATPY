import xlrd

corpora_text = []




def loadCorpora():
    corpora = xlrd.open_workbook("./Corpora/Corpus01.xls")
    print "The number of worksheets is ", corpora.nsheets
    for sheet in corpora.sheets():
        nrows = sheet.nrows
        ncols = sheet.ncols
        for i in range(nrows):
            if(sheet.cell_value(i,15) == 'es'):
                text = sheet.cell_value(i,ncols-1).encode('utf-8')
                print text
                corpora_text.append(text)
    print 'Corpus finalizado con ' + str(len(corpora_text)) + ' entradas'


loadCorpora()
