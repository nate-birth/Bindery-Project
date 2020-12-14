from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField(upload_to='shop_pics')
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def string_price(self):
        return f"${round(self.price, 2)}"

class Order(models.Model):
    email = models.EmailField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    items = models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        total=0
        for item in self.items:
            total += (item.qty * item.product.price)
        return round(total,2)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="ordered", on_delete=models.CASCADE)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    address1 = models.CharField(max_length=125)
    address2 = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    state = models.CharField(max_length=125)
    zipcode = models.CharField(max_length=125)
    order = models.ForeignKey(Order, related_name="address", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
