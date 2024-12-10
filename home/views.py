from django.shortcuts import render
from .models import PhotoUploads

# Create your views here.
def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        photo = PhotoUploads(image=uploaded_file)
        photo.save()
        return render(request, 'success.html', {'photo': photo})
    return render(request, 'home.html')
