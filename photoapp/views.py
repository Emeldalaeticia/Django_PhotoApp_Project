from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from django.core.exceptions import PermissionDenied

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy

from .forms import PhotoForm
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from .models import Photo

def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    user = request.user
    if user not in photo.likes.all():
        photo.likes.add(user)
    else:
        photo.likes.remove(user)
    return redirect('photo:detail', photo_id=photo_id)  

class PhotoListView(ListView):

    model =Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'

class PhotoDetailView(DetailView):

    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin, CreateView):


    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'photoapp/create.html'
    success_url = reverse_lazy('photo:list')
    def form_valid(self, form):

        form.instance.submitter = self.request.user

        return super().form_valid(form)

class UserIsSubmitter(UserPassesTestMixin):

    # Custom method
    def get_photo(self):
        return get_object_or_404(Photo, pk=self.kwargs.get('pk'))

    def test_func(self):

        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied('Sorry you are not allowed here')

class PhotoUpdateView(UserIsSubmitter, UpdateView):

    template_name = 'photoapp/update.html'
    model = Photo
    fields = ['title', 'description' ]
    success_url = reverse_lazy('photo:list')

class PhotoDeleteView(UserIsSubmitter, DeleteView):

    template_name = 'photoapp/delete.html'
    model = Photo
    success_url = reverse_lazy('photo:list')   

 