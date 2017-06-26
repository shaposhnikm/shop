from django.contrib import admin
from .models import Product
from .models import User
from .models import Category
from .models import Metal
from .models import Vstavka
from .models import Proba
from .models import BlogPost

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

class BlogPostAdmin(admin.ModelAdmin):   
	list_display = ("id", "title", "timestamp")

admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(Order, OrderAdmin)

admin.site.register(Metal)
admin.site.register(Vstavka)
admin.site.register(Proba)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Category)
