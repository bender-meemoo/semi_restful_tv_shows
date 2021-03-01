from django.shortcuts import render, HttpResponse, redirect
from .models import TVshows

# Create your views here.

def shows(request):
    context = {
        "shows_DB": TVshows.objects.all()
    }
    return render(request, 'shows.html', context)

def showsnew(request):
    return render(request, 'showsnew.html')

def showscreate(request):
    newTVShow = TVshows.objects.create(title = request.POST['addtitle'], network = request.POST['addnetwork'], releaseDate = request.POST['addreleaseDate'], description = request.POST['adddescription'])
    return redirect(f'/shows/{newTVShow.id}')

def showsshow(request, showID):
    context = {
        "show": TVshows.objects.get(id = showID),
        "shows_DB": TVshows.objects.all()
    }
    return render(request, 'showsshow.html', context)

def showsedit(request, showID):
    context = {
        "show" : TVshows.objects.get(id = showID),
        "shows_DB": TVshows.objects.all()
    }
    return render(request, 'showsedit.html', context)

def showsedited(request, showID):
    editTVShow = TVshows.objects.get(id = showID)
    # editTVShow = TVshows.objects.update(title = request.POST['edittitle'], network = request.POST['editnetwork'], releaseDate = request.POST['editreleaseDate'], description = request.POST['editdescription']
    editTVShow.title = request.POST['edittitle']
    editTVShow.network = request.POST['editnetwork']
    editTVShow.releaseDate = request.POST['editreleaseDate']
    editTVShow.description = request.POST['editdescription']
    editTVShow.save()
    context = {
        "show" : TVshows.objects.get(id = showID),
        "show_DB": TVshows.objects.all()
    }
    return redirect(f'/shows/{showID}', context)

def showsdelete(request, showID):
    showToDelete = TVshows.objects.get(id = showID)
    showToDelete.delete()
    return redirect('/shows')
