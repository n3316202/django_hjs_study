from pyexpat import model
from django.db import models
from django.forms import DateField

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    complete = models.BooleanField(default=False)
    exp = models.PositiveIntegerField(default=0)
    complete_at = models.DateTimeField(null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True) # 최초 등록시에만 저장, 갱신되지 않는 정보
    updated_at = models.DateTimeField(auto_now=True) #최종수정일자 - 수정시 갱신 
    

    def __str__(self):
        return self.name
    
#10. null=True 와 blank=True 의 차이가 무엇인가요?
#null 과 blank 는 둘 다 기본값이 False 입니다. 이 두 설정은 모두 필드(열) 수준에서 동작합니다. 
# 즉, 필드(열)를 비워두는 것을 허용할 것인지를 설정합니다.

#null=True 는 필드의 값이 NULL(정보 없음)로 저장되는 것을 허용합니다. 결국 데이터베이스 열에 관한 설정입니다.

#null, blank의 디폴트 값은 False !
#null과 blank는 모두 디폴트 값이 false입니다. 즉, null값을 허용하지 않습니다.
#그렇기 때문에 null = True와 blank = True는 공백값(null, "")이 저장되는 것을 허용합니다.
#이 경우의 DB 해당 column은 null 혹은 ""로 저장됩니다.


 


