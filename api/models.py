from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    main_field = models.CharField(max_length=255)
    address = models.TextField(blank=False)

    def to_json(self):
        return{
            'id':self.pk,
            'name':self.name,
            'main_field':self.main_field,
            'city':self.city,
            'address':self.address
        }

    def __str__(self):
        return f"{self.name}, {self.city}, {self.main_field}, {self.address}"

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufaturers'
        ordering = ('-name','-city')


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def to_json(self):
        return{
            'id':self.pk,
            'name':self.name,
            'description':self.description,
        }

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-name','-description')


class Prodcut(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    cost = models.FloatField()
    rating = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def to_json(self):
        return{
            'id':self.pk,
            'name':self.name,
            'description':self.description,
            'cost':self.cost,
            'rating':self.rating,
            'manufacturer':self.manufacturer.to_json()
        }

    def __str__(self):
        return f"{self.name}, {self.description}, {self.cost}, {self.rating}, {self.manufacturer}, {self.category}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-name','-cost')


# class Comment(object):
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()

class Comment(models.Model):
    email = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.email}, {self.content}, {self.created}"

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ('-created','-email')

        # self.email = email
        # self.content = content
        # self.created = created or datetime.now()