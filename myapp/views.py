from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Client, Project
from admin_auth.models import AdminBoard
from .forms import ClientForms
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from admin_auth.forms import ProjectForm

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ProjectUpdate(StaffRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'myapp/project_form.html'
    success_url = '/'


class ProjectDelete(StaffRequiredMixin, DeleteView):
    model = Project
    template_name = 'myapp/project_confirm_delete.html'
    success_url = '/'

class Home(ListView, View):
    model = AdminBoard
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # include work samples/projects for the work samples tab
        ctx['projects'] = Project.objects.all().order_by('-date')
        return ctx

class Detail(DetailView):
    model = Client
    template_name = 'myapp/details.html'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'myapp/project_detail.html'


# ----------------CRUD------------------
# --------------------------------------
# --------------------------------------

# --------Create

def create_C(request):
    error_message = None
    name_exists = None
    form = ClientForms()
    if request.method == 'POST':
        firstname = request.POST.get('firstname').lower()
        lastname = request.POST.get('lastname').lower()
        form = ClientForms(request.POST)

        if Client.objects.filter(firstname=firstname.lower(), lastname=lastname).exists():
            name_exists = 'Full Name Already existes! '
        elif form.is_valid():
            form.save()
            return redirect('home')
        else:
            error_message = 'Phone Number Not Valid or Already Existed!'

    else:
        form = ClientForms()

    context = {
        'form': form,
        'error_message': error_message,
        'name_exists': name_exists,
    }



    return render(request, 'myapp/create.html', context)


