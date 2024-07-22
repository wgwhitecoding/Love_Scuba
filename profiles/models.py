from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, default='default.jpg')
    is_pro_diver = models.BooleanField(default=False)
    qualifications = models.TextField(blank=True)
    dive_company = models.CharField(max_length=100, blank=True)
    dive_shop_location = models.CharField(max_length=100, blank=True)
    certifications = models.TextField(blank=True)  # For non-pro divers

    def __str__(self):
        return self.user.username
