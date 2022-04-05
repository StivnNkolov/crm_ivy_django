from django.db import models


class Customer(models.Model):
    NAME_MAX_LEN = 200
    PHONE_MAX_LEN = 200

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=PHONE_MAX_LEN,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    NAME_MAX_LEN = 200
    CATEGORY_CHOICES = ['Indoor', 'Out Door']

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    price = models.FloatField(
        null=True,
        blank=True,
    )
    category = models.CharField(
        max_length=max(len(el) for el in CATEGORY_CHOICES),

        choices=((el, el) for el in CATEGORY_CHOICES),
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    tags = models.ManyToManyField(
        Tag,
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_CHOICES = ['Pending', 'Out for delivery', 'Delivered']
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    status = models.CharField(
        max_length=max(len(el) for el in ORDER_CHOICES),
        choices=((el, el) for el in ORDER_CHOICES),
        null=True,
        blank=True,
    )
    products = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL,
    )
    customer = models.ForeignKey(
        Customer,
        null=True,
        on_delete=models.SET_NULL,
    )

