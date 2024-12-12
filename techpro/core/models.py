from django.db import models

#slider section
class Slider(models.Model):
    title = models.CharField(max_length=200)  # Title of the section
    description = models.TextField()          # Description text
    image = models.ImageField(upload_to='slider/')  # Image upload
    highlighted_title = models.CharField(max_length=100, default='Default')

    def __str__(self):
        return self.title


# About section
class About(models.Model):
    title = models.CharField(max_length=200)  # Title of the section
    description = models.TextField() 
    point1 = models.TextField(default='Default')
    point2 = models.TextField(default='Default')
    point3 = models.TextField(default='Default')         # Description text
    image = models.ImageField(upload_to='about/')  # Image upload

    def __str__(self):
        return self.title

# service section
class Service(models.Model):
    title = models.CharField(max_length=200)  # Title of the section
    description = models.TextField()          # Description text
    image = models.ImageField(upload_to='service/')  # Image upload

    def __str__(self):
        return self.title

# why_choose_us section
class Why_choose_us(models.Model):
    title = models.CharField(max_length=200)  # Title of the section
    description = models.TextField()          # Description text
    point1 = models.TextField(default='Default')
    point2 = models.TextField(default='Default')
    point3 = models.TextField(default='Default')
    point4 = models.TextField(default='Default')
    image = models.ImageField(upload_to='why_choose_us/')  # Image upload

    def __str__(self):
        return self.title

# blog section
class Blog(models.Model):
    title = models.CharField(max_length=200)  # Title of the section
    description = models.TextField()          # Description text
    image = models.ImageField(upload_to='blog/')  # Image upload
    date = models.DateField(auto_now_add=True) # Date field for when the blog is posted

    def __str__(self):
        return self.title

# Contact Information Section
class Contact(models.Model):
    address = models.TextField()               # Address
    phone_number = models.CharField(max_length=15)  # Phone number
    email = models.EmailField()                # Email address

    def __str__(self):
        return self.email