from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Review(models.Model):
    user = models.ForeignKey(User, verbose_name="المستخدم", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    rating = models.IntegerField("التقييم", default=5)
    comment = models.TextField("التعليق", blank=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "تقييم"
        verbose_name_plural = "التقييمات"

    def __str__(self):
        return f"تقييم {self.rating} - {self.product.name} - {self.user.username}"
