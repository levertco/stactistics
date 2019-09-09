from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.forms.fields import CharField,ImageField,ChoiceField,MultiValueField

ONE=1
TWO=2
THREE=3
FOUR=4
FIVE=5
SIX=6
SEVEN=7
EIGHT=8
NINE=9
TEN=10
REVIEW_CHOICES=(
    (ONE,'1'),
    (TWO,'2'),
    (THREE,'3'),
    (FOUR,'4'),
    (FIVE,'5'),
    (SIX,'6'),
    (SEVEN,'7'),
    (EIGHT,'8'),
    (NINE,'9'),
    (TEN,'10')
)

class Review(models.Model):
    title= models.CharField(max_length=60)
    design = models.IntegerField(choices=REVIEW_CHOICES,default=ONE)
    usability= models.IntegerField(choices=REVIEW_CHOICES,default=ONE)
    content =  models.IntegerField(choices=REVIEW_CHOICES,default=ONE)
    site=models.ForeignKey('Website',on_delete=models.CASCADE)

    
    @classmethod
    def add(self,design,usability,content):
        return design + usability + content

    def __str__(self):
        return self.title

class Website(models.Model):
    owner = models.ForeignKey(User)
    screenshot=models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description= models.CharField(max_length=250)
    web_url=models.URLField(max_length=250)
    reviews = models.ManyToManyField('Review', related_name='websites' ,blank=True)

    @classmethod
    def update(self,user):
        return self.update(user)
    
    def review(self,username):
        reviews=self.objects.filter(reviews__user__username=username)
        return reviews

    def __str__(self):
        return self.owner.username

