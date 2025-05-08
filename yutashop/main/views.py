from django.views.generic import ListView,DetailView
from .models import Category, ClothingItems, Size
from django.db.models import Q


class CatalogView(ListView):
    model = ClothingItems
    template_name = 'main/product/list.html'
    context_object_name = 'clothing_items'


    def get_queryset(self):
        queryset = super().get_queryset()
        category_slugs = self.request.GET.getlist('category')
        size_names = self.request.GET.getlist('size')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')   
        print("Выбранные категории:", category_slugs)
 
    


        if category_slugs:
            queryset = queryset.filter(category__slug__in = category_slugs)  
        print("Отфильтрованные товары:", queryset)


        if size_names:
            queryset = queryset.filter(
            Q(sizes__name__in = size_names ) & Q(sizes__clothingitemsize__available = True)
            ).distinct()

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sizes'] = Size.objects.all()
        context['selected_categories'] = self.request.GET.getlist('category')
        context['selected_sizes'] = self.request.GET.getlist('size')
        context['min_price'] =  self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('min_price', '')

        return context
    
class ClothingItemDetailView(DetailView):
    model = ClothingItems
    template_name = 'main/product/details.html'
    context_object_name = 'clothing_item'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'




        
