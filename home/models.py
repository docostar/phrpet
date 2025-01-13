from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="categories/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    description = models.TextField(blank=True, null=True)
    composition = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    packing = models.CharField(max_length=100, blank=True, null=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")  # Link to Product
    image = models.ImageField(upload_to="products/images/", max_length=255)
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Optional alt text for SEO and accessibility

    def __str__(self):
        return f"Image for {self.product.name}"
