from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# Automaticly create one to one object Using Signals
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The email must be set')
        if not password:
            raise ValueError('The password must be set')
        
        # no diffrence between abd@gmail.xom and ABC@gmail.com
        extra_fields.setdefault('is_teacher', False)
        user = self.model(email=self.normalize_email(email), **extra_fields)  #  user created here
        user.set_password(password)   # this is how we set a password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields): #  super just a simple user with extra permissions
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_teacher', True)  # if is_teacher does'nt exists in the fields set in to False

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superser mst have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superser mst have is_superuser=True')
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(ugettext_lazy('Staff Status'), default=False, help_text=ugettext_lazy('Designates wether the user can login in the site'))

    is_superuser = models.BooleanField(ugettext_lazy('SuperUser'), default=False)

    is_active = models.BooleanField(ugettext_lazy('Active'), default=True, help_text=ugettext_lazy('Designates wether the user be treated as active user'))

    is_teacher = models.BooleanField(ugettext_lazy('User Type (student or teacher)'), default=False, help_text=ugettext_lazy('Designates wether the user is student or teacher'))


    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='Student')
    cne = models.CharField(unique=True, null=True, max_length=45)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='account/images')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='Teacher')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            teacher = TeacherProfile.objects.create(user=instance)
            teacher.save()
        else:
            student = StudentProfile.objects.create(user=instance)
            student.save()


