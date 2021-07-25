from django.shortcuts import render
from django.views import View
from .models import Blog, Team, Testimonial, Contact


class Home(View):
    def get(self, request, *args, **kwargs):
        context = {
            'testimonials': Testimonial.objects.all()
        }
        return render(request, 'core/index.html',context)


class About(View):
    def get(self, request):
        context = {
            'teams': Team.objects.all()
        }
        return render(request, 'core/about.html', context)

class Work(View):
    def get(self, request):
        return render(request, 'core/work.html')

class Journal(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'core/journal.html', {'blogs':blogs})

class ContactPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/contact.html')

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        

        if full_name and email and phone and message:
            Contact.objects.create(full_name = full_name, email = email, phone_number = phone, message = message)
            context = {'message': 'Message has been sent successfully', 'request' : 'success'}
            return render(request, 'core/contact.html',context)
        return render(request, 'core/contact.html')