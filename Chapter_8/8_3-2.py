def user_music (artist, album):
    user = f"{artist} , {album}"
    return user
while True:
    print("\n Please tell me your favorate artist and album:")
    print("enter 'q' at any time to quit")
    art = input("artist: ")
    if art == "q":
        break
    alb = input("album: ")
    if alb == "q":
        break

    fave = user_music(art , alb)
    print (f"\n I see your favorate album and artist is: {fave}")

