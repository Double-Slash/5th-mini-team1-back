from django.db import models

# Create your models here.
class Chat(models.Model):
    content = models.TextField()
    recipient = models.ForeignKey('accounts.CustomUser',
                            on_delete=models.DO_NOTHING,
                            related_name='received_messages') # on delete cascade?
    sender = models.ForeignKey('accounts.CustomUser',
                        on_delete=models.DO_NOTHING,
                        related_name='send_messages') # on delete cascade?


    def __str__(self):
        return self.content[:50]
