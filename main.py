import qrcode
img = qrcode.make(str(input('URL: ')))
type(img)
filename = str(input('File name: '))
img.save('export/' + filename + '.png')

