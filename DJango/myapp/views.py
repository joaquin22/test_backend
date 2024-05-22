from django.urls import reverse
from django.views.generic import CreateView, ListView
from .forms import UserForm
from .models import Product

# Create your views here.


class UserRegisterView(CreateView):
    template_name = "userForm.html"
    context_object_name = "producto"
    form_class = UserForm

    def get_success_url(self):
        return reverse("user_register", kwargs={})


class ProductListView(ListView):

    model = Product
    template_name = "product_list.html"
    paginate_by = 10
    context_object_name = "products"
