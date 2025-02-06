import sys, os

#Робим функцію для пошуку абсолютного шляху
def search_path(file_name : str):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(os.path.join(".", "_internal", *file_name.split("/")))
    else:
        path = os.path.abspath(os.path.join(".", *file_name.split("/")))

    return path