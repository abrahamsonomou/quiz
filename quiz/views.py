from .models import *
import random
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect

def index(request):
    categorys=SubCategory.objects.all()
    context={
        'categorys':categorys
    }
    if request.GET.get('category'):
        return redirect(f"/home-quiz/quiz/?category={request.GET.get('category')}")

    return render(request,"pages/home.html",context)

def get_quiz(request):
    try:
        question_objs=Question.objects.all()

        if request.GET.get('category'):
            question_objs=question_objs.filter(category__category_name__icontains=request.GET.get('category'))
        
        question_objs=list(question_objs)
        data=[]
        random.shuffle(question_objs)

        for question_obj in question_objs:
            data.append({
                "category":question_obj.category.category_name,
                "question":question_obj.question,
                "mark":question_obj.mark,
                "answer":question_obj.get_answer()
            })
                
        payload={'status':True,'data':data}
        return JsonResponse(payload)
        
    except Exception as e:
        print(e)
    
    return HttpResponse("Something went wrong")

