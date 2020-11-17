from django.db import models
from google.cloud import storage


class Categories(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150, blank=True, null=True)
    icon_up = models.ImageField(upload_to='img/categories', blank=True, null=True)  # icon
    icon_host = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True,
                            help_text='Unique value for product page URL, created from name.')
    react_icon = models.CharField(max_length=20, null=True, blank=True)
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['pk']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Store(models.Model):
    EFECTIVO = 'EF'
    TARJETA = 'TC'
    TRANSFERENCIA = 'TR'
    YAPE = 'YP'
    PLIM = 'PL'
    choice_payment = (
        (EFECTIVO, 'En Efectivo'),
        (TARJETA, 'Tarjeta de Credito o Debito'),
        (TRANSFERENCIA, 'Transferencia Bancaria'),
        (YAPE, 'Yape'),
        (PLIM, 'Plim'),
    )
    title = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=300)
    lat = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    lon = models.DecimalField(max_digits=15, decimal_places=8, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_match')
    logo = models.ImageField(upload_to='img/stores', default='shorturl.at/bqsGJ')  # authorImg
    logo_host = models.CharField(max_length=350, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    payments = models.CharField(max_length=2, choices=choice_payment, default=EFECTIVO, blank=True, null=True)
    ruc = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=50)
    phoneNum = models.CharField(max_length=9, blank=True, null=True)
    owner = models.CharField(max_length=150, blank=True, null=True)
    dni = models.CharField(max_length=9, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    whatsapp = models.CharField(max_length=9, blank=True, null=True)
    img1 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img1host = models.CharField(max_length=300, blank=True, null=True)
    img2 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img2host = models.CharField(max_length=300, blank=True, null=True)
    img3 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img3host = models.CharField(max_length=300, blank=True, null=True)
    img4 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img4host = models.CharField(max_length=300, blank=True, null=True)
    img5 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img5host = models.CharField(max_length=300, blank=True, null=True)
    img6 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img6host = models.CharField(max_length=300, blank=True, null=True)
    video = models.CharField(max_length=250, blank=True, null=True)
    is_bestseller = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for store page URL, created from name.')

    class Meta:
        db_table = 'stores'
        ordering = ['pk']
        verbose_name_plural = "Stores"

    def __str__(self):
        return self.title


class CategoriesProd(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    icon_up = models.ImageField(upload_to='img/categories', blank=True, null=True)  # icon
    icon_host = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True,
                            help_text='Unique value for product page URL, created from name.')
    react_icon = models.CharField(max_length=20, null=True, blank=True)
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'catStores'
        ordering = ['pk']
        verbose_name_plural = "Category Product"

    def __str__(self):
        return self.title


class ProductStore(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=55, blank=True, null=True)
    colors = models.CharField(max_length=150, blank=True, null=True)
    sizes = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    img1 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img1host = models.CharField(max_length=300, blank=True, null=True)
    img2 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img2host = models.CharField(max_length=300, blank=True, null=True)
    img3 = models.ImageField(upload_to='img/banner', blank=True, null=True)
    img3host = models.CharField(max_length=300, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default="get_default_store", related_name="store_match")
    cate_prod = models.ForeignKey(CategoriesProd, on_delete=models.CASCADE, related_name="catego_match")

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name_plural = "Product Store"

    def __str__(self):
        return self.title


class Customer(models.Model):
    firstname = models.CharField(max_length=255, unique=True)
    lastname = models.CharField(max_length=255, unique=True)
    userImg = models.ImageField(upload_to='img/categories', blank=True, null=True)  # icon
    userImgHost = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=255)
    phoneNum = models.CharField(max_length=9)
    is_active = models.BooleanField(default=True, help_text='True Moroso')
    document = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer'
        ordering = ['pk']
        verbose_name_plural = "Customers"

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

