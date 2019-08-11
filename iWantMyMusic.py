import webbrowser

url = "https://drive.google.com/drive/folders/1YArvUWwJ2mUvOnk-A6APQ7QdtckXF6Vr"
url2 = "https://drive.google.com/drive/folders/1e6JqRoBB2roc3ssrqyADXULfURyAxyqP"
url3 = "https://drive.google.com/drive/folders/1gTivJD7wYgpE4NeXoavBn19Flq8NAIM1"

def getMyMusic():
    webbrowser.open_new(url)
    webbrowser.open_new_tab(url2)
    webbrowser.open_new_tab(url3)

getMyMusic()