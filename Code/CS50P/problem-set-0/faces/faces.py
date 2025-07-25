#defining convert function
def convert(text):
    #convert :)
    h_emoji = text.replace(":)", "🙂")

    #convert :(
    emoji = h_emoji.replace(":(", "🙁")

    #return emoji
    return (emoji)

#defining main function
def main ():
    #get text message from user
    text = input ()

    #sending user message to convert
    emoji = convert (text)

    #print converted text
    print (emoji)

main ()
