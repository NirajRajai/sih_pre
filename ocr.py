import tesserocr

with tesserocr.PyTessBaseAPI(lang='eng+chi_tra') as api:
    api.SetImageFile('download.jpg')
    print api.GetUTF8Text()