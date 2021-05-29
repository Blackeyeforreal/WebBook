from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm,pdfform
import os
from .models import Document, pdfDocument
from .pythonfiles.docxreqd import docx1
from friendship.models import FriendshipRequest

from django.contrib.auth.decorators import login_required
import operator
import django.dispatch



def makedirec(dirname):
    os.mkdir(os.path.join(f'../books/{dirname}', ''))

@login_required
def index(request):

    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        formpdf = pdfform(request.POST, request.FILES)

        if form.is_valid() and  "documentsent" in request.POST:
            bbb = form.save(commit=False)
            bbb.duser = request.user
            bbb.save()
            document2= Document.objects.filter(duser=request.user)
            document2 = sorted(document2, key=operator.attrgetter('uploaded_at'))
           # makedirec(document2.document.name)
            k =request.FILES['document']
            d =docx1(k.name,request.POST["Name"])
            d.automation()

            return redirect('/home', {'books': document2,'text':"yeah"})


        elif formpdf.is_valid() and  "button2" in request.POST:
            formpdf.save()
            documentpdf= pdfDocument.objects.all();
            document2 = Document.objects.filter(duser=request.user)
            document2 = sorted(document2, key=operator.attrgetter('uploaded_at'))
           # makedirec(document2.document.name)

            return redirect('/home', {'pdf': documentpdf,'text':"yeah",'books': document2})

    else:


        try:
           t = docx1()
           k  = t.oncalledit(int(request.GET["page_no"]),"../notes/notes/pdf_words.docx")


        except:
            k = "wanna dance honey"
        form = DocumentForm()
        formpdf = pdfform()
    documentpdf = pdfDocument.objects.all();
    document2 = Document.objects.filter(duser=request.user)
    document2 = sorted(document2, key=operator.attrgetter('uploaded_at'))
    return render(request, 'index.html', {

        'form': form,'books': document2,'pdfform':pdfform, 'pdf': documentpdf, 'formpdf':formpdf
    })



def test(request):

    return render(request,'post_wall.html')



def getpdf(request,pk,pk2,pk3):
    document2 = Document.objects.all();
    with open(f'media/{pk}/{pk2}/{pk3}', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')

        return response
    pdf.closed

def getdocx(request,pk,pk2,pk3):
    document2 = Document.objects.all();
    with open(f'media/{pk}/{pk2}/{pk3}', 'rb') as docx:
        response = HttpResponse(docx.read(), content_type='application/docx')

        return response
    pdf.closed



def model_form_upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:

        form = DocumentForm()
    return render(request, 'index.html', {
        'form': form,'text':"yeah"
    })



def right_index(request):
    return render(request,'left side bar', {'text':"yeah"})

def bele(request):
    if request.method == 'GET':
        book_id = request.GET['book_id']
        Document.objects.filter(id=book_id).delete()
        return HttpResponse("thank you")

def test_sum(request, value):
    documentpdf = pdfDocument.objects.all();
    value = Document.objects.get(id = value)
    document2 = Document.objects.filter(duser=request.user)
    document2 = sorted(document2, key=operator.attrgetter('uploaded_at'))



    return render(request, 'bokk_pre.html',{

        'books': document2,  'pdf': documentpdf, 'book':value
    })

def edi_change(request):
    doc = Document.objects.get(pk= request.POST["nid"])
    doc.summary = request.POST["edi_tt"]
   # Document.objects.get(pk= request.POST.get("nid")).update(summary = request.POST.get("edi_tt"))
    return HttpResponse("done")

