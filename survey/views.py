from django.shortcuts import render

# Create your views here.
from django.views import csrf
from django.views.decorators.csrf import csrf_exempt

from survey.models import Survey, Answer


def surveyList(request):
    #select * from survey_survey where statud='y'order by survey_idx desc limit 1;
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    print('survey question =>',survey.question)
    return render(request,"survey/surveyList.html",{'survey':survey})

@csrf_exempt
def save_survey(request):
    survey_idxv = request.POST['survey_idx']
    survey = Survey.objects.get(survey_idx=survey_idxv)
    print(type(survey_idxv))
    print(survey_idxv)
    numv = request.POST['num']
    dto = Answer(num=numv,survey_idx=survey) #survey_idx가 pk 이므로 survey객체를 던져주면 알아서 참조값인 survey_idxv의 값을 가져온다.
    dto.save()
    return render(request,'survey/success.html',{'survey_idx':survey_idxv})

def show_result(request):
    idx = request.GET['survey_idx']
    #select * from survey where survey_idx = 1
    ans = Survey.objects.get(survey_idx=idx)
    answer = [ans.ans1,ans.ans2,ans.ans3,ans.ans4]
    surveyList = Survey.objects.raw('''
        select survey_idx, num, count(num) sum_num,
        round((select count(*) from survey_answer 
        where survey_idx = a.survey_idx and num = a.num) * 100.0 / 
        (select count(*) from survey_answer where survey_idx = a.survey_idx),1)
        rate 
        from survey_answer a where survey_idx=%s
        group by survey_idx, num 
        order by num
        ''', idx)
    surveyList = zip(surveyList,answer)
    return render(request,'survey/surveyResult.html',{'surveyList':surveyList})



################ 0118 chart 웹 시각화
def chartdemo1(request):
    return render(request,"survey/chartDemo2.html")

def chartpractice1(request):
    return render(request,"survey/chartPractice.html")