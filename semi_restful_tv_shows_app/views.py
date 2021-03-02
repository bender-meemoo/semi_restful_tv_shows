from django.shortcuts import render, HttpResponse, redirect
from .models import TVshows
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "shows_DB": TVshows.objects.all()
    }
    return render(request, 'shows.html', context)

def showsnew(request):
    return render(request, 'showsnew.html')

def showscreate(request):
    errors = TVshows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
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
    print(showID)
    print('*******************')
    errors = TVshows.objects.basic_validator(request.POST)
    editTVShow = TVshows.objects.get(id = showID)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(showID)
        print('*******************')
        return redirect(f'/shows/{editTVShow.id}/edit')
    else:
        #editTVShow = TVshows.objects.get(id = showID)
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
