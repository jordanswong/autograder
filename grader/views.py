from django.shortcuts import render
from grading_algo import knn_model

# Create your views here.

'shows page to upload essay (copy and paste)'


def grader_view(request):

    return render(request, "upload.html", {})

'shows page to view your score'


def score_view(request):

    s_essay = request.POST["subEssay"]
    grade = knn_model.grade_essay(s_essay)
    return render(request, "grade.html", {"EssayScore": grade})
