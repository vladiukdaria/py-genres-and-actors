import init_django_orm  # noqa: F401

from django.db.models import QuerySet


def main() -> QuerySet:
class Genre(models.Model)
name = models.CharFIeld(max_length=255)
def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
