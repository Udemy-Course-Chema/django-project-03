from django.urls import path
from .views import PageListview, PageDetailView, PageCreateView

pages_patterns = ([
    path('', PageListview.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(), name="create"),
], 'pages')