from .models import Chats
# Кастомные переиспользуемые функции

def createMediaFileHTML(arr):
    videoExtentions = ["mp4", "webm"]
    imageExtentions = ["png", "jpeg", "jpg", "gif"]
    for el in arr:
        if el.file.url.find("False") == -1:
            if any(ext in el.file.url for ext in videoExtentions):
                el.mediaFileHTML = '<video controls><source src="/media/%s" type="video/mp4">Ваш браузер не поддреживает данный формат видео</video>' % el.file
            elif any(ext in el.file.url for ext in imageExtentions):
                el.mediaFileHTML = '<img src="/media/%s">' % el.file
            else:
                el.mediaFileHTML = '<a href="/media/%s" download><svg><use href="#attach"></use></svg></a>' % el.file