from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.db.models import Q



class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AboutView(DetailView):
        model = Post
        template_name = 'about.html'



class SearchResultsView(ListView):
    model = Post
    template_name = 'search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Post.title.filter(
            Q(question__startswith=query))

        return object_list

# def Search_Post(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#
#         return render(request, 'search.html', {'searched': searched})
#     else:
#         return  render(request, 'search.html', 'searched': searched})