from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import ProfileForm, ImageForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image = Image.objects.all()
    return render(request, 'all-grammy/index.html',{'image':image})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    uploadform= ImageForm
    image = Image.objects.all()
    profile = User.objects.get(username=username)
   
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} View photos and videos'

    return render(request, 'all-grammy/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images,'uploadform':uploadform,'image':image})
    '''
    editing user profile fillform & submission
    '''
@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('index_page')
    else:
        form = ProfileForm()
    return render(request, 'all-grammy/edit_profile.html', {'form':form})
    '''
    logs out current user from account
    '''
def logout(request):
    return render(request, 'index.html')

    '''
    returns all images uploaded
    '''
def view_image(request):
    image = Image.objects.all()
    return render(request, 'index.html',{"image":image})

    '''
    searching for profile
    '''
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profile = Profile.search_user(search_term)
        message = f'{search_term}'       
        return render(request, 'all-grammy/search.html',{'message':message, 'profiles':profile})
    else:
        message = 'Enter term to search'
        return render(request, 'all-grammy/search.html', {'message':message})

@login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        uploadform = ImageForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('profile', username=request.user)
    else:
        uploadform = ImageForm()
    
    return render(request, 'all-grammy/profile.html', {'uploadform':uploadform})

@login_required(login_url='/accounts/login')
def one_image(request,image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
    return redirect('index_page')
