from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import MyUserCreationForm

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = "registration.html"
    form_class = MyUserCreationForm
    # success_url = reverse_lazy("webapp:product_list_view")

    def form_valid(self, form):
        user = form.save()
        # Profile.objects.create(user=user)
        login(self.request, user)
        return redirect("webapp:product_list_view")
        # return super().form_valid()
        # return redirect(self.get_success_url())

    # def get_success_url(self):
    #     next_url = self.request.GET.get('next')
    #     if not next_url:
    #         next_url = self.request.POST.get('next')
    #     if not next_url:
    #         next_url = reverse('webapp:index')
    #     return next_url