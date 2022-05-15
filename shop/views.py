from django.db.models import Q, Count
from django.http import HttpResponseForbidden
from django.shortcuts import reverse, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Product, Category, Contact
from django.views.generic import ListView, DetailView, TemplateView, FormView, View
from django.contrib import messages
from .forms import ContactForm, CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        if self.kwargs.get('slug'):
            context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
            context['products'] = Product.objects_available.filter(category=context['category'])
        return context


class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        view = ProductDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProductComment.as_view()
        return view(request, *args, **kwargs)


class ProductDisplay(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['cart_product_form'] = CartAddProductForm()
        return context


class ProductComment(SingleObjectMixin, FormView):
    model = Product
    form_class = CommentForm
    template_name = 'shop/product_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProductComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.project = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "A comment has been sent.")
        return reverse('shop:product_detail', kwargs={'id': self.object.id,
                                                      'slug': self.object.slug})


class ContactCreate(CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        messages.success(self.request, "The message was sent to the admin.")
        return reverse("contact")


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects_available.all()[:12]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        messages.success(self.request, "پیام شما برای ادمین فرستاده شد.")
        return reverse("contact")


class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'
    context_object_name = 'search_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects_available.filter(Q(name__contains=query) | Q(description__contains=query))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(SearchResultsView, self).get_context_data(*args, **kwargs)
        context['search_word'] = self.request.GET.get('q')
        return context
