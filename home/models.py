from django.db import models
from PIL import Image  # Import Pillow's Image class
import os

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

class FAQ(models.Model):
    question = models.CharField(max_length=255, unique=True)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)  # To toggle visibility
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']  # Newest FAQs first

    def __str__(self):
        return self.question

class Testimonial(models.Model):
    picture = models.ImageField(upload_to='testimonials/', blank=True, null=True)  # Upload picture
    description = models.TextField()  # Testimonial description
    doctor_name = models.CharField(max_length=255)  # Doctor's name
    clinic_name = models.CharField(max_length=255)  # Clinic name
    doctor_city = models.CharField(max_length=100)  # Doctor's city
    is_active = models.BooleanField(default=True)  # To toggle visibility
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at']  # Newest testimonials first

    def __str__(self):
        return f"{self.doctor_name} - {self.clinic_name} ({self.doctor_city})"

    def save(self, *args, **kwargs):
        # Save the object
        super().save(*args, **kwargs)

        # Resize the uploaded image
        if self.picture:
            picture_path = self.picture.path  # Get the file path of the uploaded image
            with Image.open(picture_path) as img:
                # Resize the image to 89x89 while maintaining quality
                img = img.resize((89,89), resample=Image.Resampling.LANCZOS)
                img.save(picture_path)  # Save the resized image back to the same path
