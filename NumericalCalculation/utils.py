
def filename_from(params):
    filename = ""
    for key, value in params.items():
        filename += key+str(value).replace(".","_")
    return filename