from django.urls import path
from .views import HomeView,CategoryView,CategoryUpdateView,CategoryDeleteView,CategoryCreateView

app_name ="blog"

urlpatterns = [
    path('', HomeView, name='home'),
    path('category/', CategoryView, name='category'),
    path('category/<int:pk>/update/', CategoryUpdateView, name='category-update'),
    path('category/<int:pk>/delete/',CategoryDeleteView, name='category-delete'),
    path('category/add/',CategoryCreateView, name='category-create')
]
