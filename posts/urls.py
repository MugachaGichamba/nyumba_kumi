from django.urls import path
from . import views
from hood import views as hood_views

urlpatterns = [
    path('new_post/', views.ProjectCreateView.as_view(), name='project-create'),
    path('new_biz/<int:hood_id>/', hood_views.BusinessCreateView.as_view(), name='biz-create'),
    path('', views.PostListView.as_view(), name="home"),
    # path('', views.ProjectListView.as_view(), name="home"),
    # # path('rate_post/(?P<class>\d+)/$', CreateSessionsView.as_view(), name='create_sessions')
    # path('rate_project/<int:project_id>/', views.RateProjectCreateView.as_view(), name='rate_project'),
    # path('project_detail/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    # path('view_ratings/<int:project_id>/', views.ViewRatings.as_view(), name='view_ratings'),

]
