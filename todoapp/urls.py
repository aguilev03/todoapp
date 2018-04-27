from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/complete/$', views.TaskListView.as_view(), name='task_complete_list'),
    url(r'^$',views.TaskActiveListView.as_view(), name='task_list'),
    url(r'^task/(?P<pk>\d+)$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^task/new/$',views.CreateTaskView.as_view(), name='task_new'),
    url(r'^task/(?P<pk>\d+)/edit/$',views.TaskUpdateView.as_view(), name='task_edit'),
    url(r'^task/(?P<pk>\d+)/remove/$',views.TaskDeleteView.as_view(), name='task_remove'),
    url(r'^task/(?P<username>[\w.@+-]+)/$',views.TaskUserListView.as_view(), name='task_user_list'),
    url(r'^task/(?P<pk>\d+)/note/$',views.add_note_to_task, name='add_note_to_task'),
    url(r'^note/(?P<pk>\d+)/remove/$',views.note_remove, name='note_remove'),
    
    ]