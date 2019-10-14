
        
TwitterCharacterLimit = 280

if __name__=="__main__":

    text = "This is a text."
    text = text * 20

    length = len(text)

    print(length)

    tweet01 = text[:TwitterCharacterLimit]
    # tweet02 = 


    print(tweet01)
    print(len(tweet01))
    # print(text[:TwitterCharacterLimit])