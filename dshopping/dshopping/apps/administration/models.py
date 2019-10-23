from django.db import models


# Create your models here.

class categories(models.Model): 
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    status = models.BooleanField('Status', default=True)

class gender(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    status = models.BooleanField('Status', default=True)

class country(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    abbreviation = models.CharField('Abbrevation', max_length=100)
    status = models.BooleanField('Status', default=True)

class products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    id_category = models.ForeignKey(categories, on_delete=models.CASCADE)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    photo = models.ImageField('Image', upload_to='photo/', max_length=200)
    quantity = models.IntegerField('Quantity', default=0)
    status = models.BooleanField('Status', default=True)

class clients(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField('Firstname', max_length=150)
    lastname = models.CharField('Lastname', max_length=150)
    id_gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=100)
    email = models.EmailField('E-mail', max_length=200)
    password = models.CharField('Password', max_length=200)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    photo = models.ImageField('Image', upload_to='photo/', max_length=200)
    credit_card_number = models.CharField('Credit card number', max_length=200)
    status = models.BooleanField('Status', default=True)

class shopping(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(products, on_delete=models.CASCADE)
    id_client = models.ForeignKey(clients, on_delete=models.CASCADE)
    shopping_date = models.DateField('Date shopping', auto_now=True, auto_now_add=False)
    





























    

    



