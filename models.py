from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ("Customer","Customer"),
        ("Admin","Admin"),
    ]
    
    user_type = models.CharField(choices=USER_TYPE, max_length=50, null=True)

    def __str__(self):
        return self.username
    
class CustomerProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)    
    address = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)    
    image = models.ImageField(upload_to='media/profile', null=True)

    def __str__(self):
        return self.name
    

class AdminProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    store_name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)
    store_address = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='media/profile', null=True)


    def __str__(self):
        return self.name
    
    
class CategoryModel(models.Model):
    user = models.ForeignKey(AdminProfileModel, on_delete=models.CASCADE)
    category_name = models.CharField(null=True, max_length=50)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.category_name
    
class ProductManagementModel(models.Model):
    user = models.ForeignKey(AdminProfileModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_name = models.CharField(null=True, max_length=50)
    price = models.FloatField(null=True)
    stock = models.FloatField(null=True)
    description = models.TextField(null=True)
    product_image = models.ImageField(upload_to='media/product', null=True)
    
    def __str__(self):
        return self.product_name
    
class ProductOrderModel(models.Model):
    
    payment_method =[
        ("COD","COD"),
        ("Online","Online"),
    ]
    order_status =[
        ("Pending","Pending"),
        ("In-Progress","In-Progress"),
        ("Shipped","Shipped"),
        ("Deliverd","Deliverd"),
    ]
    payment_status =[
        ("Paid","Paid"),
        ("Unpaid","Unpaid"),
    ]
    
    
    
    product = models.ForeignKey(ProductManagementModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfileModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    payment_method = models.CharField(choices=payment_method, max_length=50,null=True)
    payment_status = models.CharField(choices=payment_status, max_length=50,null=True,default='Unpaid')
    order_status = models.CharField(choices=order_status, max_length=50,null=True,default='Pending')
    
    def __str__(self):
        return f"self.product"
    
class ReviewModel(models.Model):
    product = models.ForeignKey(ProductManagementModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerProfileModel, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.review
     
    