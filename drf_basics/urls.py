from django.conf.urls import url
from drf_basics import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'drf_basics'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('test/', views.test_deploy, name='test'),
    #path('login_new/',views.user_login, name='login_new'),
    #url(r'^register/$',views.register,name='register'),
    #url(r'^user_login/$',views.user_login,name='user_login'),
    # path('login/', views.user_login, name='login'),
    # #path('admin/validateLogin',views.validate_login,name='validate_login'),
    # path('predict/', views.predict, name='predict'),
    # path('hello/',views.hello_view,name='hello')

    #path('train/', views.train, name='train'),
    #path('add_photos/', views.add_photos, name='add-photos'),
    #url(r'^dashboard/$',views.dashboard,name='admin_dashboard'),

    
]