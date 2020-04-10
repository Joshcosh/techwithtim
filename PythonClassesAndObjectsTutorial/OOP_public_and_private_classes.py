import mod
# from mod import NotPrivate

test = mod.NotPrivate('tim')
test.display()
test._display()  # is allowed but against convention