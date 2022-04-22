from django.contrib import admin
from .models import Product, Order

admin.site.site_header = "E-Commerce Admin Site"
admin.site.site_title = "E-Commerce Admin Site"
admin.site.index_title = "Manage E-Commerce Site"

class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category='Default')
    
    change_category_to_default.short_description = "Change to Default Category"

    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title', 'category')
    actions = ('change_category_to_default', )
    fields = ('title', 'category', 'description', 'image')
    list_editable = ('price', 'discount_price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
