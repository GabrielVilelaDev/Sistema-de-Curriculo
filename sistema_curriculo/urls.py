from django.urls import path

from. import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('candidato/', views.candidato, name='candidato'),
    path('recrutador/', views.recrutador, name='recrutador'),
    path('do_login/', views.do_login, name='do_login'),
    path('do_logout/', views.do_logout_user, name='do_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('cadastro_curriculo/', views.cadastro_curriculo, name='cadastro_curriculo'),
    path('recrutador_candidato/', views.recrutador_candidato, name='recrutador-candidato'),
    path('', views.home, name='home'),
]