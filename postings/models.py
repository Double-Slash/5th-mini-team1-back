from django.db import models

class PostingType(models.Model):
    '''
    모집분야
    '''
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('accounts.CustomUser',
                                on_delete=models.DO_NOTHING,
                                related_name='postings') # on delete cascade?
    created_at = models.DateTimeField(auto_now=True)
    field = models.ForeignKey(PostingType,
                            related_name='Postings',
                            on_delete=models.DO_NOTHING,
                            null=True)
    deadline = models.DateTimeField(null=True)
    hashtags = models.ManyToManyField('hashtags.DefaultTag',
                                    related_name="postings",
                                    blank=True)
    image = models.ImageField(null=True)
    location = models.TextField(null=True)
    team_name = models.CharField(max_length=100, null=True)
    team_description = models.TextField(null=True)
    project_description = models.TextField(null=True)
    guide_text = models.TextField(null=True)
    qualifications = models.TextField(null=True)

    
class Contest(models.Model):
    title = models.CharField(max_length=100, null=True)
    deadline = models.DateTimeField(null=True)
    host = models.CharField(max_length=100,  null=True)
    host_info = models.CharField(max_length=100,  null=True)
    award = models.CharField(max_length=100,  null=True)
    detail = models.TextField()




    def __str__(self):
        return self.title


# 포스트:
# 작성자: (유저 외래키)
# 작성시간
# 모집타입 (공모전, 팀프로젝트, 등)
# 해쉬테그 (공모전 분야, 개발 언어)
# 마감기한



# 메세지:
# 보낸시간
# 읽음표시
# 내용
# 작성자: (유저)
# 수신자 (유저) (edited) 