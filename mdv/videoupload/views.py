from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import VideoFragment
from .forms import VideoUploadForm

def buy(request, where, vidid):
    frag = None
    if VideoFragment.objects.count() != 0:
        frag = VideoFragment.objects.get(pk=int(vidid))
        if not frag:
            return HttpResponse(status=404)

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            newfrag = form.save(commit=False)
            if not frag:
                newfrag.save()
                return HttpResponseRedirect('/')

            if where == "before":
                newfrag.prev_video = frag.prev_video
                newfrag.next_video = frag
                newfrag.save()
                frag.prev_video = newfrag
            elif where == "after":
                newfrag.next_video = frag.next_video
                newfrag.prev_video = frag
                newfrag.save()
                frag.next_video = newfrag
            frag.save()
            return HttpResponseRedirect('/')


    else:
        form = VideoUploadForm()

    return render(request, "buy.html", {'form': form})


