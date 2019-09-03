from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home_page(request):
    #if request.method == 'POST':
    #    return HttpRequest(request.POST['item_text'])
    return render(request, 'home.html', {
        'new_item_text':request.POST.get('item_text',''),
    })