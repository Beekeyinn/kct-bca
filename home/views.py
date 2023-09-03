from django.shortcuts import render

# Create your views here.
def home(request):
    print("Request Method: ", request.method)
    print("Query Parameters: ", request.GET)
    # print("RESPONSE:    ",response)
    return render(request,
                  "index.html",
                  context={"params":request.GET.dict()}
                  )

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")