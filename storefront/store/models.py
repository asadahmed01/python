from django.db import models
# Create your models here.

########     COLLECTION ###########

class Collection (models.Model):
  title = models.CharField(max_length=255)

########     PRODUCT ###########
class Product (models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)


########     CUSTOMER    ###########
class Customer (models.Model):
  MEMBERSHIP_BRONZE = 'B'
  MEMBERSHIP_SILVER = 'S'
  MEMBERSHIP_GOLD = 'G'
  MEMBERSHIP_CHOICES = [(MEMBERSHIP_BRONZE, 'Bronze'), (MEMBERSHIP_SILVER, 'Silver'), (MEMBERSHIP_GOLD, 'Gold')]
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phoneNumber = models.CharField(max_length=255)
  birth_date = models.DateField(null=True)
  membership = models.CharField(max_length=1, choices = MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
  


########     ORDER     ###########
class Order (models.Model):
  PAYMENT_STATUS_PENDING = 'P'
  PAYMENT_STATUS_COMPLETE = 'C'
  PAYMENT_STATUS_FAILED = 'F'
  PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'), 
    (PAYMENT_STATUS_COMPLETE, 'Complete'), 
    (PAYMENT_STATUS_FAILED, 'Failed')
  ]
  placed_at = models.DateTimeField(auto_now_add=True)
  payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

########     ADDRESS     ###########

class Address (models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
  #One-to-many relationship
  #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)