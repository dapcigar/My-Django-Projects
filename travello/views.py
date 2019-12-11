from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    # dest1 = Destination()
    # dest1.name = 'Nigeria'
    # dest1.desc = 'The Cit that never sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 250
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.name = 'Ghana'
    # dest2.desc = 'Cape Coast'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 398
    # dest2.offer = True
    #
    # dest3 = Destination()
    # dest3.name = 'South Africa'
    # dest3.desc = 'Giant of Africa'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 1500
    # dest3.offer = False
    #
    # dests=[dest1, dest2, dest3]
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

    #return render(request,"index.html",{'dest':dest1, 'dest2': dest2,'dest3':dest3} )