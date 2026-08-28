import webbrowser
#decorator daet sdelat` functional do i posle functii
def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Neverny url")
    return wrapper #vozvrat func bez skobok

@validator #decorator
#mozno podryad kuchu decoratorov
def open_url(a):
    webbrowser.open(a)

open_url("https://pypi.org/project/cowsay/")


def validator(func):
    def wrapper():
        print("do vipoln")
        func()
        print("Posle vipoln")
    return wrapper
#defoult