
from django.contrib import admin
from django.urls import path, include
from django.http import StreamingHttpResponse
from camera import VideoCamera, gen

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("OTP.urls")),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
                                                     content_type='multipart/x-mixed-replace; boundary=frame')),
]
