from django.http import HttpResponse, response
from django.shortcuts import render


def index(request):
    return render(request,"index.html")

def analyze(request):
    text = request.POST.get('text','default')
    punc = '''"<>?,./\|:;'[]}{+=_-!@#$%^&*)(~`€"'''
    rmpunc = request.POST.get('rmpunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    fulllower = request.POST.get('fulllower','off')
    extspc  = request.POST.get('extspc','off')
    charcount  = request.POST.get('charcount','off')


    analyzed_text = ""
    
    if rmpunc == "on":
        for i in text:
            if i not in punc:
                analyzed_text = analyzed_text + i
    
    elif fullcaps == "on":
        for i in text:
            analyzed_text = analyzed_text + i.upper()

    elif fulllower == "on":
        for i in text:
            analyzed_text = analyzed_text + i.lower()

    elif (extspc == "on"):
        analyzed_text = ""
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index+1] == " "):
                analyzed_text = analyzed_text + char
                
        para = {'analyze':analyzed_text}
        return render(request,"analyze.html",para)
    
    elif charcount == "on":
        count = 0
        for i in text:
            for j in i:
                count += 1

        analyzed_text = count

    else:
        return HttpResponse("Error")
    
    para = {'analyze':analyzed_text}
    return render(request,"analyze.html",para)
