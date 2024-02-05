from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Variant(TimestampedModel):
    title = models.CharField(max_length=40)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(TimestampedModel):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class ProductImage(TimestampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()

    def __str__(self):
        return self.product.title

class ProductVariant(TimestampedModel):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title

class ProductVariantPrice(TimestampedModel):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

