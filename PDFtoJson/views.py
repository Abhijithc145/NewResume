from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
# import ast,json,re 
# from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import IsAdminUser
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
import PyPDF2
# Create your views here.
# PdftoJson




class convert(APIView):
    def get(self,request):
        rsrcmgr = PDFResourceManager()

        retstr = StringIO()
        codec = 'utf-8'

        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = open('PDFtoJson/Arjun_Vijayan_Resume.pdf', 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()

        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()
        print(text,";;;;;;;;;;;;;;;;;;")

        fp.close()
        device.close()
        retstr.close()
        

            
        return Response(text,status=status.HTTP_200_OK)