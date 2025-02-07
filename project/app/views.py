from django.shortcuts import render,HttpResponse,get_object_or_404
from . models import details

# Create your views here.
def home(request):
    return render(request,"app/index.html")


def user_form_submission(request):
    if request.method == "POST":
        # Retrieve the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a new instance of the Details model (assuming 'Details' is the model name)
        user = details(name=name, email=email, password=password)
        
        # Save the user to the database
        user.save()
        
       
        return HttpResponse(f"Successfully registered: {name}")
    else:
      
        return render(request, "app/index.html")
    
def user_read(request):
    users=details.objects.all()
    for i in users:
        print(i.name)
    return render(request,"app/read.html",{'users': users})

def fuser(request,user_id):
    
    user=get_object_or_404(details,id=user_id)
    user_list = f"{user.name} - {user.email}"
    return HttpResponse(user_list)




def update_user(request, user_id):
    # Retrieve the user object using the provided user ID
    user = get_object_or_404(details, id=user_id)

    # Handle form submission
    if request.method == 'POST':
        # Update the user fields with data from the form
        user.name = request.POST.get('name')  # Update the name field
        user.email = request.POST.get('email')  # Update the email field
        user.password = request.POST.get('password')  # Update the password field
        
        # Save the updated user object to the database
        user.save()
        user_list = f"{user.name}"
        # Redirect to a different page (e.g., user details or success page)
        return HttpResponse(user_list)

    # Render the update form, pre-filling it with the current user data
    return render(request, 'app/update.html', {'user': user})

def delete_user(request,user_id):
     user = get_object_or_404(details, id=user_id)
     user.delete()
     return HttpResponse(f"{user.name} details deleted sucessfully")

        
    

    
