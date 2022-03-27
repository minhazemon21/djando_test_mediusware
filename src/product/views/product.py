from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from product.models import Product, ProductVariant, ProductVariantPrice
from django.views.decorators.csrf import csrf_exempt
import json

from product.models import Variant

class CreateProductView(TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
	@@ -12,3 +16,23 @@ def get_context_data(self, **kwargs):
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class CreateProductAPIView(View):

    @method_decorator(csrf_exempt, name="post")
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        product_data = {
            "title": data.get("title", None),
            "sku": data.get("sku", None),
            "description": data.get("description", None),
        }
        a_product = Product.objects.create(**product_data)

        return JsonResponse({"data": "New Product is created"})