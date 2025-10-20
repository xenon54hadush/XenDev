from django.shortcuts import render, redirect, get_object_or_404
from .forms import AdminForm, ProjectForm
from .models import AdminBoard
from myapp.models import Client, Project
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from functools import wraps


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin that restricts access to staff users only."""
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        # If user is not authenticated, let LoginRequiredMixin handle redirect to login.
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        # Authenticated but not staff -> show permission denied page.
        return render(self.request, 'admin_auth/permission_denied.html', status=403)


class AdminHome(StaffRequiredMixin, ListView, View):
    model = AdminBoard
    template_name = 'admin_auth/admin_view.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # include projects for quick access on the admin dashboard
        ctx['projects'] = Project.objects.all().order_by('-date')[:6]
        return ctx

class Orders(StaffRequiredMixin, ListView, View):
    model = Client
    template_name = 'admin_auth/orders.html'

class Details(DetailView):
    model = AdminBoard
    template_name = 'admin_auth/details.html'

@login_required
@user_passes_test(lambda u: u.is_staff, login_url='permission_denied')
def create_post(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'admin_auth/create_post.html', {'form':form})


@login_required
@user_passes_test(lambda u: u.is_staff, login_url='permission_denied')
def create_project(request):
    """Staff-only view to create a Project (work sample)."""
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    return render(request, 'admin_auth/create_project.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff, login_url='permission_denied')
def update_post(request, post_id):
    form = get_object_or_404(AdminBoard, post_id=post_id)
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AdminBoard()
    return render(request, 'admin_auth/create_post.html', {'form': form})


@login_required
@user_passes_test(lambda u: u.is_staff, login_url='permission_denied')
def delete_post(request, post_id):
    post = AdminBoard.objects.get(post_id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    
    return render(request, 'admin_auth/delete_confirm.html', {'post':post})


def permission_denied_view(request):
    """Simple view to render a friendly permission denied page."""
    return render(request, 'admin_auth/permission_denied.html', status=403)




