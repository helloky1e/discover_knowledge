from django.http import JsonResponse
from .models import Profile, BlogPost


def profile_view(request):
    profile = Profile.objects.first()
    if profile:
        data = {
            'name': profile.name,
            'introduction': profile.introduction,
            'contact': profile.contact,
            'work_experience': profile.work_experience,
        }
    else:
        data = {}
    return JsonResponse(data)


def blog_list(request):
    posts = list(BlogPost.objects.values('id', 'title', 'body', 'created_at'))
    return JsonResponse({'posts': posts})
