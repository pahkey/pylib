import base64


def img_to_string(filename):
    ''' 파일명(filename)을 입력으로 받아 base64로 인코딩한 문자열을 리턴한다 '''
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read())


def string_to_img(s, filename):
    ''' base64로 인코딩된 문자열(s)과 파일명(filename)을 입력으로 받아 문자열을 파일로 저장한다. '''
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(s))


img_string = img_to_string('test.jpg')  # test.jpg 파일을 base64 문자열로 리턴
string_to_img(img_string, 'result.jpg')  # base64 문자열을 result.jpg 파일로 저장
