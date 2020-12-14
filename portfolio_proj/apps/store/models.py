from django.db import models
from django.conf import settings

import stripe

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
    email = models.EmailField(max_length=45, default="email@email.com")
    first_name = models.CharField(max_length=45, default="test")
    last_name = models.CharField(max_length=45, default="test")
    address1 = models.CharField(max_length=125)
    address2 = models.CharField(max_length=125)
    city = models.CharField(max_length=125)
    state = models.CharField(max_length=125)
    zipcode = models.CharField(max_length=125)
    order = models.ForeignKey(Order, related_name="address", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def charge(self, request, email, fee):
        # Set your secret key: remember to change this to your live secret key
        # in production. See your keys here https://manage.stripe.com/account
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create a Customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        # Save the Stripe ID to the customer's profile
        self.stripe_id = stripe_customer.id
        self.save()

        # Charge the Customer instead of the card
        stripe.Charge.create(
            amount=fee, # in cents
            currency="usd",
            customer=stripe_customer.id
        )

        return stripe_customer