## rpgPromoBot ##
# W/B: Danni Sunne
# 10/13/17 ~ xx/xx/17
## ----------- ##
# Queues promo posts based on previously written +
# created descriptions and graphics.
# User commands bot to queue posts inserted into code.
## ----------- ##
import oauth2
import pytumblr

version = 1.0
# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'MkCwzRfL5SW3ooufSpinjalJrQqrXoCcn2bawAhaR8IBkRExgo',
  '6jW73AI9szmBivFAOMp1CtgUD4OW2cidGUB4QzHxW2xRe06gGS',
  'DsW052lnGbJtGKCs4o4kFHgEda87X09pSpK7iueKjqn6DCOKK0',
  'Prw2Ydi6rfte27UXAdIFNIDg1awaGrGRUnw1EZM7FFpZhJvGbe'
)

# Make the request
client.info()

from PostArchive import ALLPOSTS

# Console Interface
def main() :
    userInput = ""
    postI = 0
    noOfQ = 0
    print("Posts available to Queue:")
    for i, val in enumerate(ALLPOSTS) :
        print(str(i) + ": " + val['postName'])
    print("")
    postI = input("What post would you like to queue?" + "\n"
                  + "Use the number to the left of the post name." + "\n"
                  + "Enter nothing to quit." + "\n")
    if(postI == "") :
        print("Goodbye.")
        return
    else :
        postI = int(postI)
    
    printPost(ALLPOSTS[postI])
    userInput = input("Are you sure you want to queue this post? (y/n)" + "\n")
    if(userInput == "y") :
        noOfQ = int(input("How many copies of this post do you want to queue? Please use digits." + "\n"))
        while(noOfQ != 0) :
            queuePost(ALLPOSTS[postI])
            print("Print: " + str(noOfQ))
            noOfQ -= 1
    elif(userInput == "n") :
        # do nothing
        print("")
    else :
        print("wtf happen???")
    
    main()
    
def queuePost(post) :
    global client
    client.create_photo(post['blogName'], state = post['state'],
                        tags = post['tags'], source = post['imgSource'],
                        caption = post['caption'])

def printPost(post) :
    print(post['postName'])
    print(post['blogName'])
    print(post['state'])
    print(post['tags'])
    print(post['caption'])

# run stuff
print("rpgPromoBot by Danni Sunne")
print("version " + str(version))
print("https://github.com/SunneDog/rpgPromoBot" + "\n")
main()
