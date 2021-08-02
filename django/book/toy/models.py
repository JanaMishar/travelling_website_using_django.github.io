from django.db import models

class usr(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    pwd=models.CharField(max_length=50)

    class Meta:
        db_table="usr"


class usrs(models.Model):
    place=models.CharField(max_length=50)
    # email=models.EmailField()
    # pwd=models.CharField(max_length=50)

    class Meta:
        db_table="usrs"



        # 3rd


class contact(models.Model):
    name=models.CharField(max_length=50,primary_key=True)
    persons = models.CharField(max_length=50,default="")
    days = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")

    class Meta:
        db_table="contact"
   



class Chk(models.Model):
    uname=models.CharField(max_length=50,default="")
    pswd=models.CharField(max_length =50, default = "")
    def __str__(self):
        return f"{self.uname} : {self.pswd} "