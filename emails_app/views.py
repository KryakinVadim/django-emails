from django.urls import reverse_lazy
from django.views import generic
from . import models


class EmailListView(generic.ListView):
    model = models.UserEmail
    # template_name = 'emails_app/index.html'
    context_object_name = 'emails'


class EmailCreateView(generic.CreateView):
    model = models.UserEmail
    fields = ["email", "phone",
              "user", "text"]
    # template_name = 'emails_app/create.html'
    success_url = reverse_lazy('email_list')


class EmailDetailView(generic.DetailView):
    model = models.UserEmail
    # template_name = 'emails_app/detail.html'
    context_object_name = 'email'


class EmailUpdateView(generic.UpdateView):
    model = models.UserEmail
    fields = ["email", "phone",
              "user", "text"]
    # template_name = 'emails_app/update.html'
    success_url = reverse_lazy('email_list')


class EmailDeleteView(generic.DeleteView):
    model = models.UserEmail
    success_url = reverse_lazy('email_list')
