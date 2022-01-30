from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    html = """
    
   <!DOCTYPE html>
    <html lang="en">
     <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
     </head>
    <link
    rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
    crossorigin="anonymous"
     />
    <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only"></span></a>
            <a class="nav-link" href="about"
              >About <span class="sr-only"></span
            ></a>
            <a class="nav-link" href="contact"
              >Contact Us <span class="sr-only"></span
            ></a>
          </li>
                        </ul>
             </div>
            </nav>
            <h1>WELCOME</h1>
        </body>
        </html>
            """
    return HttpResponse(html)
def about(request):
    return render(request,'pages/about.html')
def contact (request):
    return render(request,'pages/contact.html')