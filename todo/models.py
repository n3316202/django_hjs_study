from pyexpat import model
import time
from typing import Iterable
from django.db import models
from django.forms import DateField

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=20,null=True,blank=True)
    birth_at = models.DateTimeField(null=True,blank=True)
    gender = models.CharField(
            max_length=1,
            choices=(
                ('f', 'female'),
                ('m', 'male'),
            ),null=True,blank=True)
    
    #def __str__(self):
    #    return self.id
    


# Create your models here.
class Todo(models.Model):
    #user.todos 이런식으로 가능 -> Todo.objects.filter(user=user)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="todos")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    complete_at = models.DateTimeField(null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) # 최초 등록시에만 저장, 갱신되지 않는 정보
    updated_at = models.DateTimeField(auto_now=True) #최종수정일자 - 수정시 갱신 
    

    def __str__(self):
        return self.name
    
    def save(self, *args,**kwargs):
        
        if self.complete and self.complete_at is None:
            self.complete_at = time.now()
        
        if not self.complete and self.complete_at is not None:
            self.complete_at = None

        return super().save()
    
#10. null=True 와 blank=True 의 차이가 무엇인가요?
#null 과 blank 는 둘 다 기본값이 False 입니다. 이 두 설정은 모두 필드(열) 수준에서 동작합니다. 
# 즉, 필드(열)를 비워두는 것을 허용할 것인지를 설정합니다.

#null=True 는 필드의 값이 NULL(정보 없음)로 저장되는 것을 허용합니다. 결국 데이터베이스 열에 관한 설정입니다.

#null, blank의 디폴트 값은 False !
#null과 blank는 모두 디폴트 값이 false입니다. 즉, null값을 허용하지 않습니다.
#그렇기 때문에 null = True와 blank = True는 공백값(null, "")이 저장되는 것을 허용합니다.
#이 경우의 DB 해당 column은 null 혹은 ""로 저장됩니다.


 


