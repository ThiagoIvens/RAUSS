from app.models import Portifolio, Projetos
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def homepage(request):
    portifolio = Portifolio.objects.all()
    projetos = Projetos.objects.all()
    return render(request, 'pages/home.html', {'portifolio':portifolio, 'projetos':projetos})


def page_Venda_Seu_Terreno(request):

    if request.method=="POST":
        subject = "Quero vender meu terreno!"
        nome = request.POST['nome']
        emailDoSolicitante = request.POST['email']
        telefone = request.POST['telefone']
        
        message = "Olá, meu nome é " + nome + ".\n" + ".\n Meu telefone: "+ telefone + "\nMeu Email: "+ emailDoSolicitante

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ['contato@rauss.com.br']

        send_mail(subject, message, email_from, recipient_list)

        portifolio = Portifolio.objects.all()
        return render(request, 'pages/home.html', {'portifolio':portifolio})

    return render(request, 'pages/venda_seu_terreno.html')