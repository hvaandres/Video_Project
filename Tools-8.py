import webbrowser as wb

google = ('Google search:')
tabs = ['tab1', 'tab2', 'tab3', 'tab4'] #using this you can add more tabs
i = 0
while i < len(tabs):
    print (wb.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google))
    i = i + 1