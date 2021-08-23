from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path('', views.Home_View, name='home'),
   path('signUp/', views.sign_up_view, name='signIn'),
   path('userLogin/', views.login_view, name='login'),
   path('userLogout', views.user_logout, name='logout'),
   path('blogtopic/<str:title>', views.filter_topic, name='topic' ),
   path('blogtopic/<str:title>/<int:id>', views.blog_view, name='view_blog'),
   path('posts/',views.post_view,name='postview'),
   path('dashboardView/', views.dashboard_view, name='dashboard'),
   path('editPostView/<int:id>', views.edit_view, name='editPost'),
   path('addComment/<int:id1>/<int:id>', views.addComment_view, name='addComments'),
   path('viewComment/<str:name>/<int:id>', views.viewComment_view, name='viewComments'),
   path('changepassword/', views.password_change_view, name='changepassword'),
   path('categoryadd/', views.add_category, name='categoryAdd'),
   path('catDelete/<int:id>', views.del_cat,name='deleteCat'),
   path('deleteBlog/<int:id>', views.blog_delete, name='delete_blog'),
   path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
