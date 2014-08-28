from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import VideoFragment
from .forms import VideoUploadForm

def buy(request, where, vidid):
    frag = VideoFragment.objects.get(pk=int(vidid))
    if not frag:
        return HttpResponse(status=404)

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/')

    else:
        form = VideoUploadForm()

    return render(request, "buy.html", {'form': form})


