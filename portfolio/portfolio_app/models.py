from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length= 256)

    project_resume = models.CharField(
        max_length= 256)

    UTL_CHOICES = [
        ("Acura", "Acura"),
        ("Alfa Romeo", "Alfa"),
        ("Audi", "Audi"),
        ("Bentley", "Bentley"),
        ("BMW", "BMW"),
        ("Buick", "Buick"),
        ("Cadillac", "Cad"),
        ("Chevrolet", "Chev"),
        ("Chrysler", "Chrysler"),
        ("Citroen", "Citroen"),
        ("Dacia", "Dacia"),
        ("Dodge", "Dodge"),
        ('CSS', "CSS"),
        ('JS', "Java Script"),
        ('DK', 'Docker'),
        ('DJ', "Django"),
        ('JSON', "JSON"),
        ('HT ', "HTML"),
        ('TK ', "TKInter"),
        ('SQ', "SQlite"),
        ('API', "API"),
        ('WS', "Web Scraping"),
        ('GT', "Git"),
        ('GH', "GitHub")]
    UTL_CHOICES2 = [
        ("bak","bak")]
    Gamintojas = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    Marke = models.CharField(
        max_length=50,
        choices=UTL_CHOICES,
        blank=True)

    Variklis = models.CharField(
        max_length=20,
        choices=UTL_CHOICES2,
        blank=True)

    Galia = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    Spalva = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl5 = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl6 = models.CharField(
        max_length=20,
        choices=UTL_CHOICES,
        blank=True)

    utl7 = models.CharField(
        max_length=20,
        choices = UTL_CHOICES,
        blank=True)

    project_start_date = models.DateField(
        blank=False
    )
    project_image = models.ImageField(upload_to='images/', blank=True)

    PSTATUS_CHOICES = [
        ('K', "Kuriamas"),
        ('U', "Užbaigtas")]

    project_status = models.CharField(
        max_length= 1,
        choices= PSTATUS_CHOICES,
        blank=False
        )
    c_remarks = models.CharField(max_length=256, verbose_name='Pastabos', default='-')
    c_created_at = models.DateTimeField(auto_now_add=True)
    c_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title}, {self.project_resume}, {self.project_start_date}"
