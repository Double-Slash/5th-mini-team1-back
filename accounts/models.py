from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager


class Interest(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # written_posts = models.ManyToManyField('postings.Posting')
    # bookmarked_posts = models.ManyToManyField('postings.Posting',
    #                                         related_name='bookmarked_by',
    #                                         blank=True)
    birthday = models.DateField(null=True)
    location = models.CharField(max_length=100, null=True)
    interests = models.ManyToManyField(Interest, blank=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.username

# 유저:
# pk
# 유저네임(이메일)
# 페스워드(해시값)
# (소셜 로그인에 필요한 것들)
# 쓴 포스트( 포스트 외래키, on_delete=cascade)
# 북마크한 포스트들 (포트스 외래키, on_delete= 가만히)
# 생년월일
# 지역
# 관심분야

# class UserManager(BaseUserManager):

#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError('Users must have an email address.')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password):

#         if password is None:
#             raise TypeError('Superusers must have a password.')

#         user = self.create_user(email, password)
#         user.is_admin = True
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user