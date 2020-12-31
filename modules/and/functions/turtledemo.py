from turtle import forward, done, right
import shelve
import webbrowser

help(webbrowser)
chrome = webbrowser.get(using='google-chrome')
chrome.open_new_tab("https://www.python.org/")

forward(150)
right(250)
forward(150)
done()

print(dir())
for m in dir(__builtins__):
    print(m)

help(shelve)
