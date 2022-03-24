#Ameer Faour 316540467
#qA:
def read_line(n, file):
    x='invalid input detected'
    ON_OFF = False
    if type(n)==str:
        return x
    else:
        try:
            teX = open(file, 'r')
        except FileNotFoundError :
            x="file not found"
            ON_OFF=True
        if ON_OFF==False:
            f_Lines = teX.readlines()
            if n > len(f_Lines):
                x = "line {num} doesn't exist".format(num=n)
                ON_OFF==True
            if ON_OFF==False:
                counter=0
                for word in f_Lines:
                    word=word.rstrip()
                    counter+=1
                    if counter==n:
                        x = word
                        break
        return x

#-------------------------------------------------
#q.B:
def longest_words(file):
    import re
    count=0
    ON_OFF=False
    freqList=[]
    try:
        myText = open(file, 'r')
    except FileNotFoundError:
        err = "file not found"
        ON_OFF = True
        return err
    if ON_OFF == False:
        f_Words = myText.read()
        f_Words_split=re.split('[\s+ . )]', f_Words)
        for word in f_Words_split:
            if word in freqList or '-' in word:
                continue
            else:
                freqList.append(word)
        freqList=sorted(freqList, key=len ,reverse=True)[:5]
        return freqList

