from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
    
def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    dictionary={}

    for word in wordlist:
        if word in dictionary:
            #Add
            dictionary[word] += 1
        else:
            dictionary[word] = 1


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'dictionary':dictionary.items()})
