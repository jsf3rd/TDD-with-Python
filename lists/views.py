from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm
from lists.models import Item, List

NO_EMPTY_ITEM = "빈 아이템을 등록할 수 없습니다"

def new_list(request):

    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
        
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list':list_,"form": form})
        
    
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})