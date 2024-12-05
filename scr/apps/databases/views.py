from django.views.generic import FormView, ListView, DetailView

from .forms import CreatePostForm, CreateCommentForm
from .models import Post, Comments


class CreatePostView(FormView):
    form_class = CreatePostForm
    template_name = 'create_post.html'
    success_url = '..'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        return {**super().get_form_kwargs(), 'initial': {'request': self.request}}


class CreateCommentView(FormView):
    form_class = CreateCommentForm
    template_name = 'create_comment.html'
    success_url = '..'

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


class PostView(DetailView):
    queryset = Post.objects.all()

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes += 1
        post.save()
        return self.get(request, pk=pk)

    def get_context_data(self, **kwargs):
        return {**super().get_context_data(**kwargs), 'comments': Comments.objects.filter(post_id=self.kwargs['pk'])}
