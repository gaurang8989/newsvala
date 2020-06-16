from django.shortcuts import render
from.models import Home
# Create your views here.
def index(request):

    homes  = Home.objects.all()

    return render(request,'index.html',{'homes':homes})