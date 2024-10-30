# myproject/urls.py
from django.urls import path
from srt_converter.views import upload_srt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_srt, name='upload_srt'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)