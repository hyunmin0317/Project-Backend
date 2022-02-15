from django.urls import path, re_path
from django.views.static import serve

from config import settings
from .views import base_views, question_views, answer_views, comment_views, vote_views, db_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.indexs, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('list/', base_views.list, name='list'),
    path('list/<str:id>/', base_views.list_detail, name='list_detail'),
    path('category/<str:category>/', base_views.category, name='category'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),

    # db_views.py
    path('update/public', db_views.update_public, name='update_public'),
    path('update/seoul', db_views.update_seoul, name='update_seoul'),
    path('update/data', db_views.update_data, name='update_data'),
    path('delete/', db_views.delete, name='db_delete'),

    # elastic.py
    path('subway/', base_views.subway, name='subway'),
    path('seoul/', base_views.seoul, name='seoul'),
    path('covid19/', base_views.covid19, name='covid19'),
    path('bike/', base_views.bike, name='bike'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]