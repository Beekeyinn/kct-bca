from django.shortcuts import redirect, render
from django.urls import reverse
from post.models import Post
from post.forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get("page", 1)
        posts = Post.objects.all()
        paginator = Paginator(posts, 5)
        page_obj = paginator.get_page(page)
        print(page_obj.count)
        return render(
            request,
            "index.html",
            context={"posts": page_obj.object_list, "page": page_obj},
        )


class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get("page", 1)
        posts = Post.objects.filter(user=request.user)
        paginator = Paginator(posts, 5)
        page_obj = paginator.get_page(page)
        print(page_obj.count)
        return render(
            request,
            "post/list.html",
            context={"posts": page_obj.object_list, "page": page_obj},
        )


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "post/create.html")

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        Post.objects.create(
            title=data.get("title"),
            content=data.get("content"),
            author=request.user,
            image=files.get("image"),
        )
        return redirect(reverse("post-list"))


class PostEditView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        form = PostForm(instance=post)
        return render(request, "post/edit.html", {"form": form})

    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("post-list"))
        return render(request, "post/edit.html", {"form": form})


class PostDeleteView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=request.POST.get("id"))
        post.delete()
        return redirect(reverse("post-list"))


# Create your function based  views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", context={"posts": posts})


def create_post(request):
    if request.method == "GET":
        return render(request, "post/create.html")
    else:
        data = request.POST
        files = request.FILES

        Post.objects.create(
            title=data.get("title"),
            content=data.get("content"),
            author=data.get("author"),
            image=files.get("image"),
        )
        return redirect(reverse("post-list"))


def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, "post/edit.html", context={"form": form})
    else:
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("post-list"))
        return render(request, "post/edit.html", context={"form": form})


def post_delete(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST.get("id"))
        post.delete()
        return redirect(reverse("post-list"))
