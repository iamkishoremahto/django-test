from django.db import models

# title	authors	average_rating	isbn	isbn13	language_code	  num_pages	ratings_count	text_reviews_count	publication_date	publisher

class Book(models.Model):

    title = models.CharField(max_length = 255)
    authors = models.CharField(max_length = 255, db_index= True)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length = 255)
    isbn13 = models.IntegerField()
    language_code = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.CharField(max_length=150)
    publisher = models.TextField(max_length = 400)


    def __str__(self):
        return self.title












