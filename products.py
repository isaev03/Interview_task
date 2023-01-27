from django.db import models

class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, validators=[validators.check_bad_symbols], unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)
    objects = models.Manager

def live_search(request):
    q = request.GET.get("q", "")
    products = Product.objects.filter(sku__icontains="q") | Product.objects.filter(name__icontains="q") | Product.objects.filter(description__icontains="q")
    with open('data.json', 'w', encoding='utf-8') as wf:
        json.dump(products, wf, default=str)
