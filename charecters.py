def match_words(words):
    ctr=0
    list=[]
    for word in words :
        if len(word)>1 and word[0]==word[-1]:
            ctr=1
            list.append(words)
    print("list of words with first and last charecter same\n",list)
    return ctr

count=match_words(['aga','tht','ohy','787'])
print("Number of words with first and last charecters same\n",count)
