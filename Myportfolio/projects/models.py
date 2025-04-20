from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='Category Name')

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category')
    title = models.CharField(max_length=200,verbose_name='Project Name')
    description = models.TextField(verbose_name='Description')
    technology = models.CharField(max_length=200,verbose_name='Technology Used')
    made_at = models.DateField(blank=True,verbose_name='Date of creation')
    image = models.ImageField(blank=True,upload_to='%Y/%m/%d',verbose_name='Image')
    github_link = models.URLField(blank=True,verbose_name='Github link')
    upload_date = models.DateTimeField(auto_now_add=True,verbose_name='Upload date')

    def __str__(self):
        return self.title
