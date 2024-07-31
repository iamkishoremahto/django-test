from django.shortcuts import render
from django.db.models import Q
from . import models
def home(request):

    q = request.GET.get('q','')

    
    books = models.Book.objects.filter(Q(title__icontains = q) | Q (authors__icontains = q))
    total_books = books.count()





    return render(request, 'home.html', {'books': books.values(), 'total_books':total_books})


