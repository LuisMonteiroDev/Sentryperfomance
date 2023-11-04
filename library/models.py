from django.db import models
from adminUsibras.models import Companys
from users.models import Users
from adminUsibras.models import Books


class Librarys(models.Model):
    owner_library = models.ForeignKey(Users, verbose_name='Dono', related_name='owner_library', on_delete=models.CASCADE, null=True)
    name = models.CharField('Nome da livraria', max_length=100)
    address = models.CharField('Endereço', max_length=50)
    street = models.CharField('Rua', max_length=50)
    number = models.CharField('Número', max_length=50)
    cep = models.CharField('Cep', max_length=12)
    partner_companies = models.ManyToManyField(Companys, verbose_name='Companhias parceiras', related_name='library_partner_companies')
    books_for_sale = models.ManyToManyField(Books, verbose_name='Livros à venda', related_name='library_books_for_sale')
    delivery = models.BooleanField('Faz entrega?', default=True)
    minimum_delivery = models.IntegerField('Tempo minímo de entrega', default=0, blank=True, null=True)
    maximum_delivery = models.IntegerField('Tempo máximo de entrega', default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.address}"

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'
