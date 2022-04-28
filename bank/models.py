from django.db import models


class Accounts(models.Model):
    acc_no=models.CharField(max_length=5,blank=False,null=False)
    acc_type=models.CharField(max_length=5,blank=False,null=False)
    acc_id=models.CharField(max_length=5,blank=False,null=False)

    def __str__(self):
        return self.acc_no,self.acc_type,self.acc_id


class Customer(models.Model):
    cust_id=models.TextField(max_length=30,blank=True,null=False)
    cust_fname=models.TextField(max_length=30,blank=True,null=False)
    cust_sname=models.TextField(max_length=30,blank=True,null=False)
    cust_username=models.CharField(max_length=30,blank=True,null=False)
    acc_no=models.TextField(max_length=30,blank=True,null=True)
    def __str__(self):
        return self.cust_id


        





    