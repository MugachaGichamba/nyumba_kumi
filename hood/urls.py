from django.urls import path
from . import views

urlpatterns = [
    # path('new_project/', views.ProjectCreateView.as_view(), name='project-create'),
    path('all', views.BusinessListView.as_view(), name="biz-all"),
    path('hood', views.HoodListView.as_view(), name="hood-all"),
    # # path('rate_post/(?P<class>\d+)/$', CreateSessionsView.as_view(), name='create_sessions')
    # path('rate_project/<int:project_id>/', views.RateProjectCreateView.as_view(), name='rate_project'),
    # path('project_detail/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    # path('view_ratings/<int:project_id>/', views.ViewRatings.as_view(), name='view_ratings'),

]
