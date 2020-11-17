##Generated file on own -Ayush Nanda

from django.http import HttpResponse          #while returning normal info return HttpResponse

from django.shortcuts import render           #while using templates

def index(request):
    return render(request, 'index.html')
   # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    
    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charactercount=request.POST.get('charactercount','off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext= analyzed     #for multi functioning
        #return render(request, 'analyse.html', params)
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext= analyzed     #for multi functioning
        #return render(request, 'analyse.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext= analyzed     #for multi functioning
        #return render(request, 'analyse.html', params)
    
    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext= analyzed     #for multi functioning

        # Analyze the text
        #return render(request, 'analyse.html', params)

    if(charactercount=='on'):
        analyzed=0
        for char in djtext:
            if char != ' ': #not counting the space as a character
                analyzed +=1


        params = {'purpose':'charactercount', 'analyzed_text':analyzed}
        djtext= analyzed     #for multi functioning
        
    if(removepunc != "on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on" and charactercount!="on"):
        return HttpResponse("please select any operation and try again")
        
    return render(request, 'analyse.html', params)




    #else:
        #return HttpResponse('Error')

def navigation(request):
    s= '''<h2> Navigation Bar </h2>
        <a href="https://www.youtube.com/">Youtube </a><br>
        <a href="https://www.google.com/webhp?authuser=3">Google </a><br>
        <a href="https://www.facebook.com/">Facebook</a> <br>'''
    return HttpResponse(s)
