from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all(): # Make sure a list belongs to the currently signed in user

        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get(f"c{str(item.id)}") == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    # response.user (can be used to get all info about the user for the back-end)
    if response.method == "POST":
        form = CreateNewList(response.POST) # this holds all the info from the form (saved as a dictionary)

        if form.is_valid():
            n = form.cleaned_data["name"] # Think of this just as grabbing a value out of a dictionary
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t) # This saves each to do list to a specifc user

        return HttpResponseRedirect(f"/{t.id}")

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})

def view(response):
    return render(response, "main/view.html", {})