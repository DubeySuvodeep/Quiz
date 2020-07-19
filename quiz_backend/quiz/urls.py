from django.conf.urls import url 


from quiz.views import Questions, QuestionDetail, SubmitAnswer, AssessmentReport


urlpatterns = [
    url(r'^assessment-report/$', AssessmentReport.as_view(), name='AssessmentReport'),
    url(r'^question/$', Questions.as_view(), name='Questions'),
    url(r'^question/(?P<question_id>[0-9a-f\-]+)/$', QuestionDetail.as_view(), name='QuestionDetail' ),
    url(r'^submit-answer/$', SubmitAnswer.as_view(), name='SubmitAnswer'),
]