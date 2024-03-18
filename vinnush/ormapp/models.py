from django.db import models 
from django.contrib import admin 
class books_DB(models.Model): 
    refno=models.IntegerField(primary_key="refno");
    bookname=models.CharField(max_length=20); 
    email=models.EmailField();
    Doissued=models.DateField();
    reviews=models.CharField(max_length=20);
class books_DBAdmin(admin.ModelAdmin):
    list_display=("refno", "bookname", "email", "Doissued", "reviews");