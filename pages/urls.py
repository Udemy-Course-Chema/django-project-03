from django.urls import path
from .views import PageListview, PageDetailView, PageCreateView, PageUpdate, PageDelete

pages_patterns = ([
    path('', PageListview.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name="create"),
    path('update/<int:pk>/', PageUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', PageDelete.as_view(), name="delete"),
], 'pages')