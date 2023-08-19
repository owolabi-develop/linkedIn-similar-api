from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.conf import settings

# Create your models here.

class JobUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class JobUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = JobUserManager()

    USERNAME_FIELD = "email"
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    



class Industry(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry,on_delete=models.CASCADE)
    headquarters = models.CharField(max_length=255)
    website = models.URLField()


    def __str__(self) -> str:
        return self.name
    


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    location = models.CharField(max_length=200,default='remote')
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering =['created_at']


    def __str__(self) -> str:
        return self.title
    


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    banner = models.ImageField(upload_to='banners/')
    headline = models.CharField(max_length=255)
    about = models.TextField()
    skill = models.ManyToManyField('Skill',blank=True,through='UserSkill')
    certificate_image = models.FileField(upload_to='certificate/')  
    certificate_links = models.URLField()   

    def __str__(self) -> str:
        return self.headline
    

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class UserSkill(models.Model):
    User_profile  = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    endorsement_count = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.skill__name


   



class Application(models.Model):
    User_profile  = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    cover_latter = models.TextField()
    resume = models.FileField(upload_to='Applications/')



class Experience(models.Model):
    User_profile  = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_image = models.ImageField(upload_to='companyImage/')
    location = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date  = models.DateTimeField()
    status = models.BooleanField(default='present')


    def __str__(self) -> str:
        return self.company_name
    


    


