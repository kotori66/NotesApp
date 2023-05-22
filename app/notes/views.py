from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import Notes
from .utils import DataMixin


class HomeNotes(DataMixin, ListView):
    model = Notes
    template_name = 'notes/index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return super().get_queryset().filter(user_key=self.request.user.id).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заметки')
        return dict(list(context.items()) + list(c_def.items()))


class AddNotes(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNoteForm
    template_name = 'notes/add.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user_key = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить заметку')
        return dict(list(context.items()) + list(c_def.items()))


class ViewNote(DataMixin, DetailView):
    model = Notes
    template_name = 'notes/view.html'
    slug_url_kwarg = 'note_slug'
    context_object_name = 'note'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заметка - ' + str(context['note']))
        return dict(list(context.items()) + list(c_def.items()))


class UpdateNote(DataMixin, UpdateView):
    form_class = UpdateNoteForm
    model = Notes
    template_name = "notes/update.html"
    slug_url_kwarg = 'note_slug'
    context_object_name = 'note'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заметка - ' + str(context['note']))
        return dict(list(context.items()) + list(c_def.items()))


class DeleteNote(DataMixin, DeleteView):
    model = Notes
    slug_url_kwarg = 'note_slug'
    template_name = 'notes/delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Заметка - ' + str(context['note']))
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'notes/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'notes/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class About(DataMixin, TemplateView):
    template_name = 'notes/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):
    logout(request)
    return redirect('login')

# def index(request):
#     notes = Notes.objects.all()
#     context = {
#         'notes': notes,
#         'title': menu[0]['title'],
#         'menu': menu
#     }
#     return render(request, 'notes/index.html', context=context)
# def add(request):
#     if request.method == 'POST':
#         form = AddNoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#
#     else:
#         form = AddNoteForm()
#
#     context = {
#         'title': menu[2]['title'],
#         'menu': menu,
#         'form': form
#     }
#     return render(request, 'notes/add.html', context=context)
# def show_note(request, note_slug):
#     note = get_object_or_404(Notes, slug=note_slug)
#
#     context = {
#         'note': note,
#         'menu': menu,
#         'title': 'Просмотр заметки'
#     }
#     return render(request, 'notes/view.html', context=context)
