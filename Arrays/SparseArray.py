def matchingStrings(stringList, queries):
    arr=[]
    for i in queries:
        count=0
        for j in stringList:
            if i==j:
                count+=1
        arr+=[count]
    return arr
