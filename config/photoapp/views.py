from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .models import Photo

class PhotoListView(ListView):

    model =Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):

    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'

class PhotoCreateView(CreateView):

    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photoapp/create.html'
    success_url = reverse_lazy('photo:list')

class PhotoUpdateView( UpdateView):

    template_name = 'photoapp/update.html'
    model = Photo
    fields = ['title', 'description' ]
    success_url = reverse_lazy('photo:list')

class PhotoDeleteView( DeleteView):

    template_name = 'photoapp/delete.html'
    model = Photo
    success_url = reverse_lazy('photo:list')      