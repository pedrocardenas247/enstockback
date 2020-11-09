from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    react_icon = models.CharField(max_length=20, null=True, blank=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class store(models.Model):
    EFECTIVO = 'EF'
    TARJETA = 'TC'
    TRANSFERENCIA = 'TR'
    YAPE = 'YP'
    PLIM = 'PL'
    payment = (
        (EFECTIVO, 'En Efectivo'),
        (TARJETA, 'Tarjeta de Credito o Debito'),
        (TRANSFERENCIA, 'Transferencia Bancaria'),
        (YAPE, 'Yape'),
        (PLIM, 'Plim'),
    )
    title = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category_match')
    authorImg = models.ImageField(upload_to='statics/img/customer')
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length = 254)
    number = models.CharField(max_length=9)
    website = models.CharField(max_length=200)
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    img1 = models.ImageField(upload_to='statics/img/customer')
    img2 = models.ImageField(upload_to='statics/img/customer')
    img3 = models.ImageField(upload_to='statics/img/customer')
    img4 = models.ImageField(upload_to='statics/img/customer')
    img5 = models.ImageField(upload_to='statics/img/customer')
    img6 = models.ImageField(upload_to='statics/img/customer')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    activate = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for store page URL, created from name.')

    class Meta:
        db_table = 'stores'
        ordering = ['pk']

    def __str__(self):
        return self.name