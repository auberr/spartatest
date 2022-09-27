from django.db import models

# Create your models here.

class AccessLog(models.Model):
    '''class Meta가 뭔지 찾아보기'''
    # class Meta:
    #     db_table = "user"
    

    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("수정 시간", max_length=50)

    def __str__(self):
        return f"{self.created_at} / {self.location}"