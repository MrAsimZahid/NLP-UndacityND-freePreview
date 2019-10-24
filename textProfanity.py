import urllib

def read_text():
    quotes = open("File path")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(textToCheck):
    connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+textToCheck)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("No Profanity Alert.")
    else
        print("Document not scaned properly")

read_text()
