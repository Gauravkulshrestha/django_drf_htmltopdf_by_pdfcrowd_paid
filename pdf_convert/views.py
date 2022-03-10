from rest_framework.views import APIView
from werkzeug import Response
from .serializers import Html_to_PDFSerializer
from django.http import HttpResponse
import pdfcrowd
import sys

class HTML_to_PDFView(APIView):
    serializer_class = Html_to_PDFSerializer

    def post(self, request, format=None):
        serializer = Html_to_PDFSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
                pdf = client.convertUrlToFile(self.request.data.get('url'), 'report.pdf')
                response = HttpResponse(pdf, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            except pdfcrowd.Error as why:
                sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
                raise
        return response