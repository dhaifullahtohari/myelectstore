from django.db import models

class Category(models.Model):
    name = models.CharField("اسم القسم", max_length=100)

    class Meta:
        verbose_name = "قسم"
        verbose_name_plural = "الأقسام"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("اسم المنتج", max_length=200)
    description = models.TextField("الوصف", blank=True)
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("الكمية")
    category = models.ForeignKey(Category, verbose_name="القسم", on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField("الصورة", upload_to='product_images/', null=True, blank=True)
    is_active = models.BooleanField("نشط", default=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
