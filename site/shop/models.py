from django.db import models

from django.contrib.auth.models import User

from django.contrib import admin

class BlogPost(models.Model):   
    title = models.CharField(max_length=150)
    short_body = models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField()
    logo = models.ImageField(upload_to="static/")
    class Meta:
        ordering = ("-timestamp",)

class User(models.Model):
	name=models.ForeignKey(User,on_delete=models.CASCADE)
	sourname=models.CharField(max_length=250)
	telephone=models.CharField(max_length=250)
	adress=models.CharField(max_length=250)
	update=models.DateTimeField(auto_now=True,auto_now_add=False)
	create=models.DateTimeField(auto_now=False,auto_now_add=True)

	class Meta:
		verbose_name='Пользователь'
		verbose_name_plural= 'Пользователи'
		ordering=['-create']

	def __str__(self):
		return "%s %s" % (self.name, self.sourname)


class Category(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name='Категория товаров'
    	verbose_name_plural= 'Категории товаров'
    
    def __str__(self):
    	return self.name

class Category(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name='Категория товаров'
    	verbose_name_plural= 'Категории товаров'
    
    def __str__(self):
    	return self.name


class Metal(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name='Метал'
    	verbose_name_plural= 'Металы'
    
    def __str__(self):
    	return self.name


class Vstavka(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name='Вставка'
    	verbose_name_plural= 'Вставки'
    
    def __str__(self):
    	return self.name


class Proba(models.Model):
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)

    class Meta:
    	verbose_name='Проба'
    	verbose_name_plural= 'Пробы'
    
    def __str__(self):
    	return self.name



class Product(models.Model):
	best = models.BooleanField(default=False)
	category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
	metal = models.ForeignKey(Metal, default=None)
	vstavka = models.ForeignKey(Vstavka,default=None)
	proba = models.ForeignKey(Proba, default=None)
	size = models.CharField(max_length=200, default=None)
	name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='static/media/', blank=True, verbose_name="Изображение товара")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
	stock = models.PositiveIntegerField(verbose_name="На складе")
	available = models.BooleanField(default=True, verbose_name="Доступен")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name='Товар'
		verbose_name_plural= 'Товары'

class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Email')
    address =  models.CharField(verbose_name='Адрес', max_length=250)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)


    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

