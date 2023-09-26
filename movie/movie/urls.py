"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from film import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    path('',views.movielistview.as_view(),name="home"),
    # path('add',views.add,name='add'),
    path('createview',views.createview.as_view(),name="add"),
    # path('view/<int:p>/',views.view_movie,name="view"),
    path('detailview/<int:pk>/',views.detailview.as_view(),name="view"),
    # path('update/<int:p>/',views.update_movie,name="update"),
    # path('delete/<int:p>/',views.delete_movie,name="delete"),
    path('updateview/<int:pk>/',views.updateview.as_view(),name="update"),
    path('deleteview/<int:pk>/',views.deleteview.as_view(),name="delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
