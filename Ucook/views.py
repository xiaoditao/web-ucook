from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.core import serializers
from Ucook.forms import LoginForm, RegisterForm,EditForm,ProfileForm,PostForm,CommentForm
from Ucook.models import *
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.

def login_action(request):
    context={}
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, "Ucook/1login.html", context)

    form = LoginForm(request.POST)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'Ucook/1login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    return redirect(reverse('welcome'))


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))

def register_action(request):

    context = {}
    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, "Ucook/1register.html", context)

    form = RegisterForm(request.POST)
    context['form'] =form

    if not form.is_valid():
        return render(request, "Ucook/1register.html", context)

    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email']
                                        )
    new_user.save()

    # new_user_profile = Profile(user=new_user)
    # new_user_profile.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    return redirect(reverse('home'))

def welcome_action(request):
    context={}
    if request.method == 'GET':
        return render(request,"Ucook/footer-1.html",context)

def profile_action(request):
    context={}
    if request.method == 'GET':
        return render(request,"Ucook/1profile.html",context)

def detail_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1detail.html", context)

def mypost_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1mypost.html", context)

def explorehost_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1explore-host.html", context)

def explorenonhost_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1explore-nonhost.html", context)

def iAmHost_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1posthost.html", context)

def iAmNonHost_action(request):
    context={}
    if request.method == 'GET':
        return render(request, "Ucook/1postnonhost.html", context)


# @ensure_csrf_cookie
# @login_required
# def post_action(request):
#
#     errors =[]
#     context = {}
#
#     if request.method == 'GET':
#         forms = PostForm()
#         posts = Post.objects.all().order_by('-time', 'id')
#         comments = Comment.objects.all().order_by('post_id', '-time')
#         context = {'posts':posts,'comments':comments,"forms":forms}
#         return render(request,"Ucook/globalstream.html",context)
#
#     form = PostForm(request.POST)
#     time_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     if not form.is_valid():
#         context['form'] = form
#     # if request.method =='GET':
#     #     form = PostForm()
#     #     context['forms'] = form
#
#     #     return render(request,"Ucook/globalstream.html",context)
#     # elif 'post' not in request.POST or not request.POST['post']:
#     #     errors.append("You must enter an item to post.")
#     else:
#         # time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
#         # time_format = parse_datetime(time)
#         # print(time)
#         new_post = Post(text = form.cleaned_data['text'],
#                         user = request.user,
#                         time = time_str,
#                         username = request.user.first_name+" "+request.user.last_name,
#                         )
#         new_post.save()
#         context['last_time'] = new_post.time
#     context['forms'] = PostForm()
#     comments = Comment.objects.all().order_by('post_id', '-time')
#     context['comments'] = comments
#     context['errors'] = errors
#     posts = Post.objects.all().order_by('-time', 'id')
#     context['posts'] = posts
#
#
#     return render(request,"Ucook/globalstream.html",context)
#
#
# @login_required
# def comment_action(request,id):
#     context={}
#     if not 'comment' in request.POST or not request.POST['comment']:
#         message = 'You must enter an item to add.'
#         json_error = '{ "error": "'+message+'" }'
#         return HttpResponse(json_error, content_type='application/json')
#     form = CommentForm(request.POST)
#     post = Post.objects.get(id =id)
#     time_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#     # print("dd")
#     newtime=parse_datetime(time_str)
#     # print(time_str)
#     # if not form.is_valid():
#     #     context['commentform'] = form
#     # else:
#     #     new_comment = Comment(text = form.cleaned_data['text'],
#     #                           user = request.user,
#     #                           time = timezone.localtime(),
#     #                           post = post
#     #                           )
#     #     new_comment.save()
#     new_comment = Comment(text = request.POST['comment'],
#                           username = request.user.first_name+" "+request.user.last_name,
#                           user = request.user,
#                           time = newtime,
#                           post = post)
#     new_comment.save()
#     # print(new_comment.time)
#     # context['commentform'] = form
#     comments = Comment.objects.all().order_by('-time','id')
#     context['comments'] = comments
#     context['last_time'] = new_comment.time
#
#     response_text = serializers.serialize('json', [new_comment,])
#
#     # print(response_text)
#     return HttpResponse(response_text, content_type='application/json')
#
#     # return render(request,"Ucook/globalstream.html",context)
#
# def refresh_global_action(request):
#
#     if request.method == 'GET':
#         last_refresh= request.GET['last_refresh']
#         print("last_refresh:"+last_refresh)
#
#     try:
#         last_refresh_time = parse_datetime(last_refresh)
#         print(Post.objects.filter(time__gt=last_refresh_time).count())
#         posts = Post.objects.filter(time__gt=last_refresh_time).order_by("-time").values()
#
#         # response_text[posts] = serializers.serialize('json', posts)
#         comments = Comment.objects.filter(time__gt=last_refresh_time).order_by("post_id","-time").values()
#
#         combine = {'posts':list(posts),'comments':list(comments)}
#
#     # response_text = serializers.serialize('json', combine)
#     # json = serializers.serialize('json', combined)
#     # print(response_text)
#
#     # response_text = serializers.serialize('json', comments)
#     # response_text = JsonResponse(combine)
#     # return HttpResponse(response_text, content_type='application/json')
#     except:
#         print("error")
#     return JsonResponse(combine)
#
#
# def refresh_follower_action(request):
#
#     if request.method == 'GET':
#         last_refresh= request.GET['last_refresh']
#
#     print("last_refresh:"+last_refresh)
#     last_refresh_time = parse_datetime(last_refresh)
#     print(Comment.objects.filter(time__gt=last_refresh_time).count())
#     # user= User.objects.filter(user = request.user)
#     profile = Profile.objects.filter(user_id=request.user.id).last()
#     followers = profile.followers.all()
#     if followers:
#         posts = Post.objects.filter(user__in = followers,time__gt=last_refresh_time).order_by("-time").values()
#         print(posts)
#         comments = Comment.objects.filter(user__in = followers,time__gt=last_refresh_time).order_by("post_id", "-time").values()
#         print(followers)
#     # print(user.length())
#
#     # posts = Post.objects.filter(time__gt=last_refresh_time).filter(user=user)
#         # .exclude(user_id = request.user.id).order_by("-time").values()
#
#     # response_text[posts] = serializers.serialize('json', posts)
#     # comments = Comment.objects.filter(time__gt=last_refresh_time).order_by("post_id","-time").values()
#         combine = {'posts':list(posts),'comments':list(comments)}
#     else:
#         combine = {'posts': list(), 'comments': list()}
#     return JsonResponse(combine)
#
#     # response_text = serializers.serialize('json', combine)
#     # json = serializers.serialize('json', combined)
#     # print(response_text)
#
#     # response_text[comments] = serializers.serialize('json', comments)
#     # response_text = JsonResponse(combine)
#     # return HttpResponse(response_text, content_type='application/json')
#     # except:
#     #     print("error")
#         # return JsonResponse(None)
#
#
#
#
#
# def profile_action(request,id):
#
#     context ={}
#     id = int(id)
#
#     if id != request.user.id:
#         followee_profile = Profile.objects.filter(user_id=id).last()
#         request_user_profile = Profile.objects.filter(user_id=request.user.id).last()
#
#         context['followee_profile']=followee_profile
#         context['user_profile'] = request_user_profile
#         try:
#             context['followers'] = request_user_profile.followers.all()
#         except:
#             context['followers'] =None
#         return render(request,"Ucook/follower.html",context)
#
#     new_profile = Profile.objects.filter(user_id=request.user.id).last()
#     form = ProfileForm(request.POST,request.FILES)
#         # request.POST, request.FILES, instance=new_profile)
#
#     if not form.is_valid():
#         context['form'] = form
#         # temp = Profile.objects.all()
#         try:
#             # stuck by this!!!:
#             # objects.get() can only get one qualified,so if there many same user, it will failed
#             # So I use filter which can get all qualified user, and choose the last one which updated recently
#             context['profile']=Profile.objects.filter(user=request.user).last()
#             context['followers'] = new_profile.followers.all()
#
#         except:
#             context['followers'] = None
#
#         return render(request, "Ucook/profile.html", context)
#
#     else:
#         # Must copy content_type into a new model field because the model
#         # FileField will not store this in the database.  (The uploaded file
#         # is actually a different object than what's return from a DB read.)
#         context['form'] = form
#         pic = form.cleaned_data['profile_picture']
#         print('Uploaded picture: {} (type={})'.format(pic, type(pic)))
#         new_profile.profile_picture = pic
#         new_profile.content_type = form.cleaned_data['profile_picture'].content_type
#         new_profile.bio_text = request.POST['bio_text']
#         new_profile.save()
#         context['profile'] = new_profile
#         context['followers'] = new_profile.followers.all()
#     return render(request, "Ucook/profile.html", context)
#         # new_profile = form.save(commit = False)
#         # new_profile.user = request.user
#         # new_profile.save()
#         # context['message'] = 'Item #{0} saved.'.format(new_profile.id)
#         # context['form'] = ProfileForm()
#     # context['profile'] = Profile.objects.get(id=new_profile.id)
#     # profiles= Profile.objects.all()
#     # for profile in profiles:
#     #     if profile.id != new_profile.id or profile.id is None:
#     #         profile.delete()
#     # context['profiles'] = profiles
#
#     # p=Profile.objects.all()
#
#     # try :
#     #     context['profile'] = Profile.objects.get(user_id=request.user.id)
#     # except:
#     #     context['profile'] = None
#
#
#
#
# def get_photo(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     print('Picture #{} fetched from db: {} (type={})'.format(id, profile.profile_picture, type(profile.profile_picture)))
#
#     # Maybe we don't need this check as form validation requires a picture be uploaded.
#     # But someone could have delete the picture leaving the DB with a bad references.
#     if not profile.profile_picture:
#         raise Http404
#     return HttpResponse(profile.profile_picture, content_type=profile.content_type)
#
#
#
#
# def follow_action(request,id):
#     context ={}
#     followee = User.objects.get(id=id)
#     followee_profile = Profile.objects.filter(user_id=id).last()
#     try:
#         request_user_profile = Profile.objects.filter(user=request.user).last()
#     except:
#         request_user_profile = None
#     # if followee not in request_user_profile.followers:
#     request_user_profile.followers.add(followee)
#     request_user_profile.save()
#     # request_user_profile.save()
#     follower= request_user_profile.followers.all()
#     # if followee in user:
#     #     print("t")
#     # else:
#     #     pass
#
#     followee_profile = Profile.objects.filter(user_id=id).last()
#     context={'user_profile':request_user_profile,'followee_profile':followee_profile,'followers':follower}
#
#     return render(request,"Ucook/follower.html", context)
#
# def unfollow_action(request, id):
#     context = {}
#     followee = User.objects.get(id=id)
#     followee_profile = Profile.objects.filter(user_id=id).last()
#     try:
#         request_user_profile = Profile.objects.filter(user=request.user).last()
#     except:
#         request_user_profile = None
#
#     request_user_profile.followers.remove(followee)
#     request_user_profile.save()
#     follower = request_user_profile.followers.all()
#
#     followee_profile = Profile.objects.filter(user_id=id).last()
#     context = {'user_profile': request_user_profile, 'followee_profile': followee_profile, 'followers': follower}
#
#     return render(request, "Ucook/follower.html", context)
#
#
# def followStream_action(request):
#
#     errors = []
#     context = {}
#     # if request.method == 'GET':
#     #     forms = PostForm()
#     #     profiles = Profile.objects.filter(user = request.user).last()
#     #     print(profiles)
#     #     users = profiles.followers.all().values()
#     #     print(users)
#     #     if users:
#     #         # posts = users.post.objects.all()
#     #         posts = Post.objects.filter(user = users.id).order_by('-time')
#     #     print(posts)
#     #     comments = Comment.objects.all().order_by('post_id', '-time')
#     #     context = {'posts':posts,'comments':comments,"forms":forms}
#     #     return render(request,"Ucook/globalstream.html",context)
#
#     followers_posts=[]
#     request_user_profile = Profile.objects.filter(user = request.user).last()
#
#     followers = request_user_profile.followers.all()
#     comments = Comment.objects.all().order_by('-time','id')
#
#     posts=Post.objects.all().order_by('-time', 'id')
#     for post in posts:
#         if post.user in followers:
#             followers_posts.append(post)
#
#     context['posts'] = followers_posts
#     context['comments'] = comments
#
#     return render(request, "Ucook/followerstream.html", context)
