from os import environ
from django import template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context
from datetime import datetime
from .forms import DemandForm
from .models import Demand
from django.http import HttpResponseRedirect
from address.forms import AddressField
from address.models import AddressField
from django.db.models import Count
from django.conf import Settings, settings
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from delivery.models import Author
from django.contrib.auth.decorators import login_required
from phone_field import PhoneField
from django.template.loader import get_template, render_to_string 
import threading
from fpdf import FPDF,  HTMLMixin
import datetime
from templated_email import send_templated_mail




# Post delivery request view
@login_required(login_url='login')
def post_ads(request):
    if request.POST.get('action') == 'post-ads':
        # Get service type
        service = request.POST.get('service')
        # Get name
        name = request.POST.get('name')

         # Get user's phone
        phone = request.POST.get('phone')

        # Get adress 
        autocomplete = request.POST.get('autocomplete')

        # Get email
        email = request.POST.get('email')

        # Get ad description
        description = request.POST.get('description')
        

        # Create the request
        ads = Demand.objects.create(author=request.user.author, service=service, name=name, phone=phone, autocomplete=autocomplete, email=email, description=description)

        
        
        # Send email notificaton to Admin
        mail_subject = "New request submitted"
        sender_email = request.user.email
        sender_user = request.user.author
        message = f"Dear Clement, you received a new request from {sender_user} his email is {sender_email}"
        print(message)
        to_email = settings.NOTIF_EMAIL
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(
            mail_subject,
            message,
            from_email,
            to_list,
            fail_silently=False,
        )
        

        #send email notification to end customer
        mail_subject = "Notification de Livraison | Delivery notification"
        sender_email = request.user.email
        sender_user = ads.author.business_name
        customer = email
        customerName = name
        package_id = ads.id

        today = datetime.date.today()
        idx = (today.weekday() + 1) % 7
        dim = today - datetime.timedelta(idx)
        lun = today - datetime.timedelta(idx-1)
        mar = today - datetime.timedelta(idx-2)
        mer = today - datetime.timedelta(idx-3)
        jeu = today - datetime.timedelta(idx-4)
        ven = today - datetime.timedelta(idx-5)
        sam = today - datetime.timedelta(idx-6)
        heuredebut = datetime.time(1, 0)
        heurefin = datetime.time(17, 0)
        temps = datetime.datetime.now()
        temps = str(temps.strftime("%Y-%m-%d %H:%M:%S"))

        
        
        to_email = customer
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER

        # Monday
        lundate_hr1 = datetime.datetime.combine(lun, heuredebut)
        lundate_hrs1 =  str(lundate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        lundate_hr2 = datetime.datetime.combine(lun, heurefin)
        lundate_hrs2 =  str(lundate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

        # Tuesday
        mardate_hr1 = datetime.datetime.combine(mar, heuredebut)
        mardate_hrs1 =  str(mardate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        mardate_hr2 = datetime.datetime.combine(mar, heurefin)
        mardate_hrs2 =  str(mardate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

        # Wednesday
        merdate_hr1 = datetime.datetime.combine(mer, heuredebut)
        merdate_hrs1 =  str(merdate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        merdate_hr2 = datetime.datetime.combine(mer, heurefin)
        merdate_hrs2 =  str(merdate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

        # Thursday
        jeudate_hr1 = datetime.datetime.combine(jeu, heuredebut)
        jeudate_hrs1 =  str(jeudate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        jeudate_hr2 = datetime.datetime.combine(jeu, heurefin)
        jeudate_hrs2 =  str(jeudate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

         # Friday
        vendate_hr1 = datetime.datetime.combine(ven, heuredebut)
        vendate_hrs1 =  str(vendate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        vendate_hr2 = datetime.datetime.combine(ven, heurefin)
        vendate_hrs2 =  str(vendate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

        # Saturday
        samdate_hr1 = datetime.datetime.combine(sam, heuredebut)
        samdate_hrs1 =  str(samdate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        heurefinsam = datetime.time(13, 0)
        samdate_hr2 = datetime.datetime.combine(sam, heurefinsam)
        samdate_hrs2 =  str(samdate_hr2.strftime("%Y-%m-%d %H:%M:%S"))

        # Sunday
        dim = today - datetime.timedelta(idx)
        heuredim = datetime.time(0, 0)
        dimdate_hr1 = datetime.datetime.combine(dim, heuredim)
        dimdate_hrs1 =  str(dimdate_hr1.strftime("%Y-%m-%d %H:%M:%S"))
        

        # Notification for every morning to monday at saturday
        if lundate_hrs1 < temps and temps < lundate_hrs2 or  mardate_hrs1 < temps and temps < mardate_hrs2 or merdate_hrs1 < temps and temps < merdate_hrs2 or jeudate_hrs1 < temps and temps < jeudate_hrs2 or vendate_hrs1 < temps and temps < vendate_hrs2 or samdate_hrs1 < temps and temps < samdate_hrs2 :
            send_templated_mail(template_name='LoQQal', from_email=settings.EMAIL_HOST_USER, recipient_list=[customer],
            context={
            'customerName': customerName,
            'sender_user': sender_user,
            'package_id':package_id
            },)
        # Notification for every night to monday at friday
        elif lundate_hrs2 < temps and temps < mardate_hrs1 or  mardate_hrs2 < temps and temps < merdate_hrs1 or merdate_hrs2 < temps and temps < jeudate_hrs1 or jeudate_hrs2 < temps and temps < vendate_hrs1  or vendate_hrs2 < temps and temps < samdate_hrs1:
            send_templated_mail(template_name='LoQQal2', from_email=settings.EMAIL_HOST_USER, recipient_list=[customer],
            context={
            'customerName': customerName,
            'sender_user': sender_user,
            'package_id':package_id
            },)

        # Notification for saturday afternoon and sunday
        elif samdate_hrs2 < temps  or dimdate_hrs1 < temps :
            send_templated_mail(template_name='LoQQal3', from_email=settings.EMAIL_HOST_USER, recipient_list=[customer],
            context={
            'customerName': customerName,
            'sender_user': sender_user,
            'package_id':package_id
            },)

        else :
            print('Merci')

    
    return render(request, 'delivery/post-ads.html')



# Post delivery request view
@login_required(login_url='login')
def post_demands(request):
    if request.POST.get('action') == 'post-demands':

        # Get service type
        service = request.POST.get('service')
        # Get name
        name = request.POST.get('name')

         # Get user's phone
        phone = request.POST.get('phone')

        # Get adress 
        autocomplete = request.POST.get('autocomplete')

        # Get email
        email = request.POST.get('email')

        # Get ad description
        description = request.POST.get('description')
        

        # Create the request
        ads = Demand.objects.create(author=request.user.author, service=service, name=name, phone=phone, autocomplete=autocomplete, email=email, description=description)

        
        
        # Send email notificaton to Admin
        mail_subject = "New request submitted"
        sender_email = request.user.email
        sender_user = request.user.author
        message = f"Dear Clement, you received a new request from {sender_user} his email is {sender_email}"
        print(message)
        to_email = settings.NOTIF_EMAIL
        to_list = [to_email]
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(
            mail_subject,
            message,
            from_email,
            to_list,
            fail_silently=False,
        )
        

        
    return render(request, 'delivery/post-demands.html')



# Function to make and send client invoice 
# cid:client id
# prix: price of normal delivery
# prixE: price of express delivery
# business: business name
# adress: business adress
# c_email: business email on invoice
# receiver_email: business email

def facture(cid, prix, prixE, business, adress, c_email, receiver_email):
    threading.Timer(1800.0, facture,(cid, prix, prixE, business, adress, c_email, receiver_email,)).start()
    import datetime
    dt = datetime.datetime.now()

    wk = dt.isocalendar()[1] 
    #For normal delivery
    total_ads1 = str(Demand.objects.all().filter(author =cid, service='Normal').filter(published_date__week=wk).count())
    total_ads = int(total_ads1)
    #For Express delivery
    total_ads1E = str(Demand.objects.all().filter(author =cid, service='Express').filter(published_date__week=wk).count())
    total_adsE = int(total_ads1E)

    prix_total = (total_ads * prix) + (total_adsE * prixE)
    tax = int(prix_total) * 14.975/100
    prix_final = int(prix_total) + tax   
    today = datetime.date.today()
    idx = (today.weekday() + 1) % 7
    sat = today - datetime.timedelta(idx-6)
    num1 = str(today - datetime.timedelta(idx-6))
    num = num1.replace("-","", 2)
    Sun = today - datetime.timedelta(idx)
    entete = f'INVOICE OF {sat}'
    num1 = str(num)
    prix1 = str(prix)
    prix2 = str(prixE)
    prix_total1 = str(prix_total)
    tax = "{:.2f}".format(tax)
    tax1 = str(tax)
    prix_final = "{:.2f}".format(prix_final)
    prix_final1 = str(prix_final)
    
    #condition and date for invoice sending
    #send invoice every evening saturday
    today = datetime.date.today()
    idx = (today.weekday() + 1) % 7
    wed = today - datetime.timedelta(idx-6)
    heure = datetime.time(23, 30)
    date_hr = datetime.datetime.combine(wed, heure)
    date_hrs =  str(date_hr.strftime("%Y-%m-%d %H:%M:%S")) 
    temps = datetime.datetime.now()
    temps = str(temps.strftime("%Y-%m-%d %H:%M:%S"))

    #invoice
    sales = [
        
        { "item":"DESCRIPTION :", "amount":"Delivery"},
        { "item":"INVOICE No :", "amount": num1 },
        { "item":"PRICE (NORMAL DELIVERY):", "amount":f'$ {prix1}'},
        {"item":"QUANTITY (NORMAL DELIVERY):", "amount":total_ads1},
        { "item":"PRICE (EXPRESS DELIVERY):", "amount":f'$ {prix2}'},
        {"item":"QUANTITY (EXPRESS DELIVERY):", "amount":total_ads1E},
        { "item":"TOTAL :", "amount": f'$ {prix_total1}'},
        { "item":"TAX 14.975% :", "amount": f'$ {tax1}'},
        { "item":"GRAND TOTAL :",  "amount":f'$ {prix_final1}'},
        
    ]
    data = [
        {"item": "To :", "amount":business},
        {"item": "Address:", "amount":adress},
        {"item": "Email:", "amount": c_email},  
    ]

    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_line_width(0.0)
    pdf.line(5.0,5.0,205.0,5.0) # top one
    pdf.line(5.0,292.0,205.0,292.0) # bottom one
    pdf.line(5.0,5.0,5.0,292.0) # left one
    pdf.line(205.0,5.0,205.0,292.0) # right one
    pdf.image('logo.png', 10, 10, 10)
    pdf.set_font('helvetica', 'B', 15)
    pdf.cell(80)
    pdf.cell(70, 10, entete, 1, 0, 'C')
    pdf.cell(40, 10, '',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 13)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 6, 'From : LoQQal ' , 0, 1, 'L', True)
    pdf.set_font('courier', '', 13)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 6, 'Address: 5337 Sherbrooke Ouest' , 0, 1, 'L', True)
    pdf.set_font('courier', '', 13)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(0, 6, 'Email: info@loqqal.ca' , 0, 1, 'L', True)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', 'B', 12)
    pdf.cell(200, 8, f"{''.ljust(41)} {''.rjust(31)}", 0, 1)
    for line in data:
        pdf.cell(200, 8, f"{line['item'].ljust(41)} {line['amount'].rjust(31)}", 0, 1)
    pdf.set_font('courier', '', 13)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 4  
    pdf.line(10, 100, 200, 100)
    pdf.line(10, 108, 200, 108)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(40)} {line['amount'].rjust(27)}", 0, 1)
    pdf.ln(line_height)
    pdf.set_font('courier', '', 10)
    pdf.cell(40, 10, f'Date of Invoice: {sat}',0,1)
    pdf.set_font('courier', 'B', 10)
    pdf.cell(40, 10, 'A finance charge of 1.5% will be made on unpaid balances after 30 days.',0,1)
    
      
    if total_ads > 0 and  date_hrs < temps :
        pdf.output('invoice.pdf', 'F')
        template ='delivery/facturemail.html'
        content = render_to_string(template,  {'business': business, 'prix_final': prix_final})
        entete = f'INVOICE OF {sat}'
        email = EmailMessage(
        entete, content, settings.EMAIL_HOST_USER, [receiver_email])
        email.attach_file('invoice.pdf')
        email.send()


        
        
       
# make a function for every client like below function
# First parameter is client id (auhor id)
# Two parameter is price of normal delivery
# Three parameter is price of express delivery
# Foor parameter is client's business name
# Five parameter is client's business adress
# six parameter is client's business email on invoice
# Seven parameter is client's business email

facture('3', 5, 12, 'Fleur Sauvage-Aliments Naturels', '5561 Monkland ave', settings.CLIENT1_EMAIL, settings.CLIENT1_EMAIL)

