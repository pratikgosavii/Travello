from django.shortcuts import render
from .models import Destination

# Create your views here.






def index(request):
   
   
    dests = Destination.objects.all()
   

    context= {

        
        'dests' : dests
    }
    
    return render(request, 'index.html', context)



def index1search(request):



    qs= ''
    
    searche= request.POST.get('search')

    if searche != '' and searche  is not None:
        qs= Destination.objects.filter(name__icontains=searche)


    dests= Destination.objects.filter(offer__icontains=True)

    print(searche)

    context= {

        'queryset' : qs,
        'dests' : dests
    }
    
    return render(request, 'search.html', context)