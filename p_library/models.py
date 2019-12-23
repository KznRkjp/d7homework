from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Friend(models.Model):
    full_name = models.TextField()

    def __str__(self):
        return self.full_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, null=True, on_delete=models.SET_NULL)
    copy_count = models.SmallIntegerField(default=1)
    price = models.FloatField()
    def __str__(self):
        return self.title






# class Inspiration(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     inspirer = models.ForeignKey(
#         Author,
#         on_delete=models.CASCADE,
#         related_name="inspired_works",
#     )
