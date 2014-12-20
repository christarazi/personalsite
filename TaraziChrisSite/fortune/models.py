from django.db import models

# Create your models here.
'''
CREATE TABLE fortunes (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, filename TEXT, size INTEGER, aphorism TEXT);
CREATE INDEX filename_index ON fortunes (filename);
CREATE INDEX id_index ON fortunes (id);
CREATE INDEX size_index ON fortunes (size);
'''

class Fortune(models.Model):
    filename = models.CharField(max_length=200)
    size = models.IntegerField()
    aphorism = models.CharField(max_length=2150)
    def __str__(self):
        return self.aphorism