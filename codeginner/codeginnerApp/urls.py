from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from codeginnerApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('PythonCourse/', views.python, name='python'),
    path('CourseContent/', views.courseContent, name='courseContent'),
    path('login_user/' ,views.login_user, name="login_user"),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('Account/', views.userAccount, name='userAccount'),
    path('AdminPanel/',views.adminPanel,name='adminPanel'),
    path('Editor/',views.editor, name="editor"),
    path('chapterContent/',views.chapterContent,name='chapterContent'),
    path('Exercises/',views.exercises,name='exercises'),
    path('<int:id>',views.details, name='details'),
    path('<int:id>',views.previousPage, name='previousPage'),
    path('<int:id>',views.nextPage, name='nextPage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)