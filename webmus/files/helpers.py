from .models import UploadedFile


def get_files_by_tag(tag):
    return UploadedFile.objects.filter(tag__name=tag)
