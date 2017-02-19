def get_html(target_url):
    
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
    headers = {'User-Agent': agent}
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='cookies')

    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("Cookie 未能加载")
    
    try:
        r = session.get(target_url, headers=headers)
        if r.status_code == 200:
            print "target URL is sucessfully loaded"
    except:
        print "loading failed"
    html = r.content#.decode('utf-8')
    session.cookies.save()
    return html
    
get_html("http://wwdsadasw.baiddsdsadasdasu.com")