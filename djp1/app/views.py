from django.shortcuts import render, HttpResponseRedirect
from .forms import BooksForm
from .models import Books
from django.views.generic import ListView, DetailView


# Create your views here.



def fun(request):
    b = Books.objects.all()
    '''i = 0
    s = {'number': []}
    for item in b:
        s['number'].append = {'item': i+1}'''
    form = BooksForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST)
        # if  form.is_valid():
        # return HttpResponseRedirect('/thanks/')
        new_form = form.save()

    return render(request, 'index.html', locals())


class BookList(ListView):
    template_name = 'book_list.html'
    model = Books
    #form = BooksForm(request.POST or None)
    '''form_class = BooksForm
    initial = {'key': 'value'}
    #context_object_name = 'book_list

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/publishers/')

        #return render(request, self.template_name, {'form': form})'''
