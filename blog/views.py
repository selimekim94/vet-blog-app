from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Category


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    """
    DetailView will provide a context object we can use in our
    template called either object or the lowercased name of our model which would be 'post'
    """
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'category', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'category']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_new.html'
    fields = ['name', 'slug', 'parent']


class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'


class PostByCategoryView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category_id=self.kwargs['id'])
