from django.contrib import admin
from .models import Asesor, Product, Pagina, Comment, Video, Promo

# Register your models here.
admin.site.register(Asesor)
admin.site.register(Product)
admin.site.register(Pagina)
admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Promo)