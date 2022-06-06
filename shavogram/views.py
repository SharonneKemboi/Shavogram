from django.shortcuts import render,redirect
from .models import Photo, Profile,identifiers,Comments,Follow
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponseRedirect
from .forms import PictureForm, ProfileForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url = "accounts/login")
def index(request):
    my_likes_list = []
    images = Photo.objects.all().order_by("-pub_date")
    for image in images:
        user = image.user
        followers = user.user_followers.all()
        arr_ = []
        for follower in followers:
            arr_.append(follower.followed_by.id)
        if request.user.id in arr_:
            image.user.is_following = True
        else: 
            image.user.is_following = False
        
        if image.user.id == request.user.id:
            user.myself = True
         
        else:
            user.myself = False

        if request.user in image.likes.all():
            image.my_likes = True
        else:
            image.my_likes = False
        

    return render(request,"index.html", {"images":images,"user":request.user})

@login_required(login_url = "/accounts/login/")
def feed(request):
    all_images = []
    following_arr = []
    for following in request.user.user_following.all():
        following_arr.append(following.user.id)

    for image in Photo.objects.all():
        if image.user.id in following_arr:
            all_images.append(image)

    for image in all_images:
        if request.user in image.likes.all():
            image.my_likes = True
        else:
            image.my_likes = False

    return render(request, "feed.html", {"images":all_images})    

def like(request):
    user = request.user
    images = Photo.objects.all()
    image_id = request.POST.get("id")
    if image_id != None:
        identifiers.objects.create(identifier = request.POST.get("id"))
    the_last = identifiers.objects.all()
    end = identifiers.objects.get(pk = the_last.count())
    image = Photo.objects.get(pk = end.identifier)
    to_red = None
    
    if user in image.likes.all():
        image.likes.remove(user)
        to_red = 0

    else:
        image.likes.add(user)
        to_red = 1
        
    likes = image.likes.all().count()
    data = {"likes":likes, "to_red": to_red}
    return JsonResponse(data) 

def comment(request):
    image_id = request.POST.get("id")
    photo = Photo.objects.get(pk = image_id)
    Comments.objects.create(user = request.user,  photo= photo, mycomments = request.POST.get("comment"))
    user = request.user.username
    comment = request.POST.get("comment")

    data = {"user":user, "comment":comment}

    return JsonResponse(data)     

def follow(request):
    image = Photo.objects.get(id = request.POST.get("id"))
    user = image.user
    followed = None
   
    if Follow.objects.filter(user = user, followed_by = request.user):
        Follow.objects.filter(user = user, followed_by = request.user).delete()
      
        followed = 0
    else:
        Follow.objects.create(user = user, followed_by = request.user)
    
        followed = 1
    data = {"hello":"hello", "followed":followed}
    return JsonResponse(data)   


def follow_in_profile(request):
    user = User.objects.get(id = request.POST.get("id"))
    followed = None
   
    if Follow.objects.filter(user = user, followed_by = request.user):
        Follow.objects.filter(user = user, followed_by = request.user).delete()
        followed = 0
        count = user.user_followers.all().count()
    else:
        Follow.objects.create(user = user, followed_by = request.user)
        followed = 1
        count = user.user_followers.all().count()
    data = {"hello":"hello", "followed":followed, "count":count}
    return JsonResponse(data)     


def add_picture(request):
    user = request.user
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = user
            image.save()
            return redirect("index")
    else:
        form = PictureForm()

    return render(request, "add_picture.html", {"form":form}) 

def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_bio = form.cleaned_data["bio"]
            new_picture = form.cleaned_data["picture"]
            profile = Profile.objects.get(user = request.user)
            profile.bio = new_bio
            profile.picture = new_picture
            profile.save()
            final_url = "/profile/" + str(request.user.id) + "/"
            return redirect(final_url)
    else:
        form = ProfileForm()
    return render(request, "update_profile.html", {"form":form})  



def search_user(request):
    if "user_search_term" in request.GET and request.GET["user_search_term"]:
        term = request.GET.get("user_search_term")
        users = Profile.search_user(term)
        print(users)
        return render(request, "search.html", {"users":users,"title":term})    


def my_profile(request):
    user = request.user
    return render(request, "my_profile.html", {"user":user, "current_user":request.user})        

def profile(request,id):
    user = User.objects.get(id = id)
    followers = user.user_followers.all()
    followers_arr = []
    for follower in followers:
        followers_arr.append(follower.followed_by.id)

    if request.user.id in followers_arr:
        is_following = True
    else:
        is_following = False

    if request.user.id == int(id):
        
       return redirect("my_profile")
    else:
       return render(request, "profile.html", {"user":user,"current_user":request.user, "is_following": is_following})
    
