from django.db import models
from django.contrib.auth.models import User
import datetime as dt



        
class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 250)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()
    
    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = User.objects.filter(username__icontains = name)
        return userprof
# Create your models here.
class Image(models.Model):
    Image = models.ImageField(upload_to = 'images/')
    Image_name = models.CharField(max_length =30)
    Image_caption = models.TextField(max_length =100)
    Likes = models.CharField(max_length =20,blank =True)
    profile = models.ForeignKey(Profile, null = True,related_name='image')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    comment = models.ForeignKey
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def save_image(self):
        self.save()
    
    @classmethod
    def get_by_id(cls,id):
        image= Image.objects.get(user = id)
        return image

    @classmethod
    def get_images(cls, profile):
        image = Image.objects.filter(Profile__pk = profile)
        return image
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    @classmethod
    def find_image_id(cls, id):
        identity = Image.objects.get(pk=id)
        return identity

class Comment(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,null = True)
    image = models.ForeignKey(Image,related_name='comment')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def find_commentimage(cls,id):
        comments = Comments.objects.filter(image__pk = id)
        return comments