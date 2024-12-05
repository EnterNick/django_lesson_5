from django.views.generic import FormView, ListView, DetailView
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model

from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Comments


class CreatePostView(FormView):
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = '..'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if type(request.user) is get_user_model():
            return super().get(request, *args, **kwargs)
        return HttpResponseForbidden('Для входа на эту страницу необходимо войти в аккаунт!')

    def get_form_kwargs(self):
        return {**super().get_form_kwargs(), 'initial': {'request': self.request}}


class CreateCommentView(FormView):
    form_class = CreateCommentForm
    template_name = 'create_comment.html'
    success_url = '..'

    def get(self, request, *args, **kwargs):
        if type(request.user) is get_user_model():
            return super().get(request, *args, **kwargs)
        return HttpResponseForbidden('Для входа на эту страницу необходимо войти в аккаунт!')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        return {
            **super().get_form_kwargs(),
            'initial': {
                'request': self.request,
                'post': Post.objects.get(pk=self.kwargs['pk']),
            },
        }


class PostsView(ListView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        if type(request.user) is get_user_model():
            return super().get(request, *args, **kwargs)
        return HttpResponseForbidden('Для входа на эту страницу необходимо войти в аккаунт!')


class PostView(DetailView):
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        if type(request.user) is get_user_model():
            return super().get(request, *args, **kwargs)
        return HttpResponseForbidden('Для входа на эту страницу необходимо войти в аккаунт!')

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes += 1
        post.save()
        return self.get(request, pk=pk)

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(**kwargs), 'comments': Comments.objects.filter(post_id=self.kwargs['pk'])}
