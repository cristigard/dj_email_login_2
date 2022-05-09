
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Equipment, Manufacturer, Category, Error
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ManufacturerForm



# Create your views here.

class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'knowledge/manufacturer-update.html'
    context_object_name = "manufacturer"


class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'knowledge/manufacturer-delete.html'
    context_object_name = 'manufacturer'
    success_url = reverse_lazy('manufacturer-list')
    success_message = "Manufacturer deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'knowledge/manufacturer-list.html'
    context_object_name = "manufacturers"


class ManufacturerCreateView(SuccessMessageMixin,CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'knowledge/manufacturer-create.html'
    success_url = reverse_lazy('manufacturer-create')
    success_message = "Manufacturer %(name)s was created successfully"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

































# def manufacturer_view(request):
#     form = ManufacturerForm()
#     manufacturers = Manufacturer.objects.all()
#     if request.method == "POST":
#         form = ManufacturerForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data['created_by'] = request.user
#             form.save()
#             form = ManufacturerForm()
#             return render(request,'knowledge/manufacturer-create.html',{"form":form, "manufacturers":manufacturers})
#     return render(request,'knowledge/manufacturer-create.html', {"form":form, "manufacturers":manufacturers})
