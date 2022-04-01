from django.urls import path

from newsletter.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='articles')

]
