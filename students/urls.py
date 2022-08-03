from django.urls import path
from .views import index, view_one, create, delete, edit

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>',view_one, name='one'),
    path('create', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    # path('login', login_user, name='login'),
]
