from django.shortcuts import render
from django.views.generic import (
    View, TemplateView, ListView, DetailView, CreateView, UpdateView,
    DeleteView
)
from django.http import HttpResponse
from basic_app import models
from django.core.urlresolvers import reverse_lazy

# Create your views here.
#instead of defining function below, we will create class based view
# Method 1: using a function and rendering a template
# def index(request):
#     return render(request, 'basic_app/index.html')

# Method 2: using a class based view and rendering a HttpResponse
class CBView(View):
    def get(self, request):
        return HttpResponse('CLASS BASED VIEWS ARE WAY COOL!!')

# Method 3: using a templateView
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    #The ListView will return by default school_list(It will lowercase
    # the name of the model (in this case school) and appends _list)
    # If you want to override this name provide the context_object_name

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # The DetailView will return by default the model name in lowercase
    # in our case school. If you want to override this name provide
    # the context_object_name

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')
