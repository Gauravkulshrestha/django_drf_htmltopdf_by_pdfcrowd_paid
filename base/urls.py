from django.contrib import admin
from django.urls import path
from pdf_convert.views import HTML_to_PDFView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf-api/', HTML_to_PDFView.as_view()), 
]