from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
   path('login/',views.login_view,name='login'),
   path('register/',views.register,name='register'),
   path('admin_home/',views.admin_home,name='admin_home'),
#    path('view_users/',views.view_users,name='view_users'),
   path('user_home/',views.user_home,name='user_home'),
   path('add_blog/',views.add_blog,name='add_blog'),
   path('my_blogs/',views.my_blogs,name='my_blogs'),
   path('edit_blog/<int:id>/',views.edit_blog,name='edit_blog'),
   path('delete_blog/<int:id>/',views.delete_blog,name='delete_blog'),
   path('view_blogs_admin/',views.view_blogs_admin,name='view_blogs_admin'),
   path('view_blogs_user/',views.view_blogs_user,name='view_blogs_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
