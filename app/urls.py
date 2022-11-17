from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.LoginUserApi.as_view(), name='api_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='api_register'),

    path('checklist/', views.checklist_list, name='checklist_list'),
    path('checklist/create/', views.checklist_create, name='checklist_create'),
    path('checklist/<int:pk>', views.checklist_delete, name='checklist_delete'),
    path('checklist/<int:checklistid>/item/', views.checklist_item_list, name='checklist_item_list'),
    path('checklist/<int:checklistid>/item/create/', views.checklist_item_create, name='checklist_item_create'),
    path('checklist/<int:checklistid>/item/<int:checklistitemid>', views.checklist_item_detail, name='checklist_item_detail'),
    path('checklist/<int:checklistid>/item/<int:checklistitemid>/update/', views.checklist_item_update, name='checklist_item_update'),
    path('checklist/<int:checklistid>/item/<int:checklistitemid>/delete/', views.checklist_item_delete, name='checklist_item_delete'),
    path('checklist/<int:checklistid>/item/rename/<int:checklistitemid>', views.checklist_update, name='checklist_update'),
]

