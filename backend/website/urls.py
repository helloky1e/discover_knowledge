from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view),
    path('blog/', views.blog_list),
]
