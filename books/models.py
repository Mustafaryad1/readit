from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField("Author", related_name="books")
    review = models.TextField(blank=True, null=True)
    reviewed_by = models.ForeignKey(User, blank=True, null=True, related_name='reviews')
    date_review = models.DateField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name='Favorite?')

    # verbose_name name that appear to admin user

    def __str__(self):
        return "{} by {}".format(self.title, self.list_author())

    def list_author(self):
        return ",".join([author.name for author in self.authors.all()])

    def save(self, *args, **kwargs):
        if self.review and self.date_review is None:
            self.date_review = now()

        super(Book, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=70, unique=True, help_text=' use pen name, not real name  ')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-details', kwargs={'pk', self.pk})
