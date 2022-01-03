from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    meetups=[
        {
            "title":"A first meetUp",
            "location": "New York",
            "slug":"a-first-meetup"
        },
        {
            "title":"A second meetUp",
            "location":"Paris",
            "slug":"a-second-meetup"
        }
        
    ]
    return render(request,'meetups/index.html',{
        "show_meetups":True,
        "meetups":meetups
    })
    
def meetup_details(request,meetup_slug):
    selected_meetup={
        "title":"A first meetup",
        "description":"This is the first meetup!"
        }
    return render(request,"meetups/meetup-detail.html",{
        "meetup_title":selected_meetup["title"],
        "meetup_description":selected_meetup["description"]
    })
    