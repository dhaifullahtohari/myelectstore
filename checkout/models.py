from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('paid', 'تم الدفع'),
        ('shipped', 'تم الشحن'),
        ('completed', 'تم التسليم'),
        ('canceled', 'ملغي'),
    )
    
    user = models.ForeignKey(User, verbose_name="المستخدم", on_delete=models.CASCADE)
    status = models.CharField("الحالة", max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="الطلب", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("الكمية", default=1)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلبات"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
