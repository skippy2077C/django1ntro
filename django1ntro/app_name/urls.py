from django.urls import path
from .views import index, page1, page2, page3, page4, page5

urlpatterns = [
    path('', index, name='home'),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('page4/', page4, name='page4'),
    path('page5/', page5, name='page5'),
]
