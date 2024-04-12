def main ():
    file_name = input("FIle name: ")
    extensions(file_name)

def extensions(x):
    if ".gif" in x:
        print("image/gif")
    elif ".jpg" in x:
        print("image/jpeg")
    elif ".jpeg" in x:
        print("image/jpeg")
    elif ".png" in x:
        print("image/png")
    elif ".pdf" in x.lower():
        print("application/pdf")
    elif ".txt" in x:
        print("text/plain")
    elif ".zip" in x:
        print("application/zip")
    else:
        print("application/octet-stream")

main()
