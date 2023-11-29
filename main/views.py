from curses.ascii import CR, HT
from dataclasses import field
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import CheckForm
from django.contrib import messages
from .models import Sites


title = 'Gatka'


def home_view(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        print(form.data)
        if form.is_valid():
            domain_name = form.cleaned_data.get('domain_form')
            site = Sites.objects.filter(domain=domain_name).first()
            if str(site) == domain_name:
                if site.is_scam:
                    messages.error(request, f'{domain_name} является поддельным сайтом')
                else:
                    messages.success(request, f'Хорошие новости!  {domain_name} является оффициальным сайтом!')
            elif site is None:
                messages.warning(request, f'{domain_name} не занесен в базу данных, и скорее всего является поддельным')
    else:
        form = CheckForm()

    context = {
        'form': form,
        'title': title,
        'subtitle': 'home',
        'name': cut_name(request)
    }
    return render(request, 'main/home.html', context)


def blog(request):
    context = {
            'posts': Post.objects.all(),
            'title': title,
            'subtitle': 'context',
            'name': cut_name(request)
        }
    return render(request, 'main/blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 6


class UserListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': title,
        'subtitle': 'about',
        'name': cut_name(request)

    }
    return render(request, 'main/about.html', context)


def cut_name(request):
    nameuser = request.user.username
    if len(nameuser) > 10:
        return nameuser[:8] + '..'
