from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
<<<<<<< HEAD
from django.urls import reverse_lazy
=======
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
>>>>>>> 6e27d18c5278645d8ceffc6576fee07b6e573d4f
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import BirthdayForm, CongratulationForm
from .models import Birthday, Congratulation
from .utils import calculate_birthday_countdown


class OnlyAuthorMixin(UserPassesTestMixin):

    def test_func(self):
        object = self.get_object()
        return object.author == self.request.user


class BirthdayListView(ListView):
    model = Birthday
    queryset = Birthday.objects.prefetch_related(
        'tags'
    ).select_related('author')
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayUpdateView(OnlyAuthorMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(OnlyAuthorMixin, DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        context['form'] = CongratulationForm()
        context['congratulations'] = (
            self.object.congratulations.select_related('author')
        )
        return context


class CongratulationCreateView(LoginRequiredMixin, CreateView):
    birthday = None
    model = Congratulation
    form_class = CongratulationForm

    def dispatch(self, request, *args, **kwargs):
        self.birthday = get_object_or_404(Birthday, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.birthday = self.birthday
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.birthday.pk})
