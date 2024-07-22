from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy

urlpatterns = [
    path('', ItemListCreate.as_view(), name='item_list_create'),
    path('<int:pk>/', ItemRetrieveUpdateDestroy.as_view(), name='item_retrieve_update_destroy'),
]
