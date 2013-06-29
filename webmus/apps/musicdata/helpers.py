from .models import Album

def get_albums_by_year():
    result = []
    currentyear = None
    currentyearalbums = []
    for album in Album.objects.all().order_by('-year'):
        if album.year != currentyear:
            if currentyearalbums:
                result.append((currentyear, currentyearalbums))
                currentyearalbums = []
            currentyear = album.year
        currentyearalbums.append(album)
    if currentyearalbums:
        result.append((currentyear, currentyearalbums))
    return result
