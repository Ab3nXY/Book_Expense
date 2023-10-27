from django.shortcuts import render
from matplotlib import pyplot as plt
from io import BytesIO
import base64
from .models import Book 

# Create your views here.

def index(request):

    # Page from the theme 
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'pages/dashboard.html', context)


