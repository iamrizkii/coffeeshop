from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES = (
    ('Aceh', 'Aceh'),
    ('Sumatera Utara', 'Sumatera Utara'),
    ('Sumatera Barat', 'Sumatera Barat'),
    ('Riau', 'Riau'),
    ('Jambi', 'Jambi'),
    ('Sumatera Selatan', 'Sumatera Selatan'),
    ('Bengkulu', 'Bengkulu'),
    ('Lampung', 'Lampung'),
    ('Kepulauan Bangka Belitung', 'Kepulauan Bangka Belitung'),
    ('Kepulauan Riau', 'Kepulauan Riau'),
    ('DKI Jakarta', 'DKI Jakarta'),
    ('Jawa Barat', 'Jawa Barat'),
    ('Jawa Tengah', 'Jawa Tengah'),
    ('DI Yogyakarta', 'DI Yogyakarta'),
    ('Jawa Timur', 'Jawa Timur'),
    ('Banten', 'Banten'),
    ('Bali', 'Bali'),
    ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
    ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
    ('Kalimantan Barat', 'Kalimantan Barat'),
    ('Kalimantan Tengah', 'Kalimantan Tengah'),
    ('Kalimantan Selatan', 'Kalimantan Selatan'),
    ('Kalimantan Timur', 'Kalimantan Timur'),
    ('Kalimantan Utara', 'Kalimantan Utara'),
    ('Sulawesi Utara', 'Sulawesi Utara'),
    ('Sulawesi Tengah', 'Sulawesi Tengah'),
    ('Sulawesi Selatan', 'Sulawesi Selatan'),
    ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
    ('Gorontalo', 'Gorontalo'),
    ('Sulawesi Barat', 'Sulawesi Barat'),
    ('Maluku', 'Maluku'),
    ('Maluku Utara', 'Maluku Utara'),
    ('Papua Barat', 'Papua Barat'),
    ('Papua', 'Papua'),
    ('Papua Tengah', 'Papua Tengah'),
    ('Papua Pegunungan', 'Papua Pegunungan'),
    ('Papua Selatan', 'Papua Selatan'),
    ('Papua Barat Daya', 'Papua Barat Daya'),
)


CATEGORY_CHOICES = (
    ('CR', 'Espresso'),
    ('ML', 'Americano'),
    ('LS', 'Latte'),
    ('MS', 'Cappuccino'),
    ('PN', 'Mocha'),
    ('GH', 'Macchiato'),
    ('CZ', 'Flat White'),
    ('IC', 'Cold Brew'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    default_address = models.BooleanField(default=False)  # Tambahan kolom

    def __str__(self):
        return f"{self.name} - {self.locality}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
