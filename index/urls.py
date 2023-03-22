from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('login/staff-login', views.StaffLogin, name='staff-login'),
    path('student-portal/', views.StudentPortal, name='student-portal'),
    path('staff-portal/', views.StudentPortal, name='staff-portal'),
    path('results-page', views.ResultsPage, name='results-page'),
    path('registration', views.Registration, name='registration'),
    path('project', views.Project, name='project'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
