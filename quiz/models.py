from django.db import models
import uuid
import random

# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True
        
class Category(BaseModel):
    category_name=models.CharField(max_length=200,verbose_name="Category Name")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    
    def __str__(self) -> str:
        return self.category_name

class SubCategory(BaseModel):
    category_name=models.CharField(max_length=200,verbose_name="Category Name")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_category",verbose_name="Category")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categorys'
    
    def __str__(self) -> str:
        return self.category_name

class Question(BaseModel):
    category=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_category",verbose_name="Category")
    question=models.TextField(max_length=5000)
    mark=models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question

    def get_answer(self):
        answer_objs=list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correct
            })
        return data

class Answer(BaseModel):
    question=models.ForeignKey(Question,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_question")
    answer=models.CharField(max_length=500)
    is_correct=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer
    