from django.contrib.auth.admin import User, Group
from django.contrib.gis.db import models
from cloudinary.models import CloudinaryField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    userImg = models.ImageField(upload_to='users/customers', blank=True, null=True)  # icon
    address = models.CharField(max_length=255, blank=True, null=True)
    phoneNum = models.CharField(max_length=9, blank=True, null=True)
    dni = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Informacion Usuarios"

###############################################


class Categories(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150, blank=True, null=True)
    icon_host = models.ImageField(upload_to='storeMaster/icons', blank=True, null=True)  # icon
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True,
                            help_text='Unique value for product page URL, created from name.')
    react_icon = models.ImageField(upload_to='storeMaster/banners', blank=True, null=True)  # icon
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['pk']
        verbose_name_plural = "Categoria de Tienda"

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store')
    title = models.CharField(max_length=150, unique=True)
    short_description = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=300)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_match')
    logo_host = models.ImageField(upload_to='stores/logos', default='shorturl.at/bqsGJ')  # authorImg
    description = models.TextField(blank=True, null=True)
    payments = models.CharField(max_length=2, choices=choice_payment, default=EFECTIVO, blank=True, null=True)
    ruc = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phoneNum = models.CharField(max_length=9, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    whatsapp = models.CharField(max_length=9, blank=True, null=True)
    img1host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
    img2host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
    img3host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
    img4host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
    img5host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
    img6host = models.ImageField(upload_to='stores/banner', blank=True, null=True)
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
        verbose_name_plural = "Tiendas"

    def __str__(self):
        return self.title


class CategoriesProd(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    cate_top = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='cateTop_match')
    store_top = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True, related_name='storeTop_match')
    icon_host = models.ImageField(upload_to='stores/categories', blank=True, null=True)  # icon
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True,
                            help_text='Unique value for product page URL, created from name.')
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'catStores'
        ordering = ['pk']
        verbose_name_plural = "Categoria de Producto"

    def __str__(self):
        return self.title


class ProductStore(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="store_match")
    cate_prod = models.ForeignKey(CategoriesProd, on_delete=models.CASCADE, related_name="catego_match")
    brand = models.CharField(max_length=50, blank=True, null=True)
    material = models.CharField(max_length=55, blank=True, null=True)
    colors = models.CharField(max_length=150, blank=True, null=True)
    sizes = models.CharField(max_length=150, blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    img1host = models.ImageField(upload_to='stores/productos', blank=True, null=True)
    img2host = models.ImageField(upload_to='stores/productos', blank=True, null=True)
    img3host = models.ImageField(upload_to='stores/productos', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name_plural = "Agregue un Proucto"

    def __str__(self):
        return self.title


class Ubicacion(models.Model):
    point = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='point_match')
    point_prod = models.ManyToManyField(ProductStore, related_name='point_prod_match')
    location = models.PointField()

    class Meta:
        verbose_name_plural = "Ubicacion de Tienda"

    def __str__(self):
        return str(self.location)
