print("Welcome to Jungle.")
print("Your mission is to find map parts in order to find way to come back.") 
c= input("First part is in the cave of bear. You prefer to enter when he'sleep's or when he'go out':  \n")
c1=c.lower()
if c1=="go out":
  h=input("Second part in the top of hill. You will continue 'right' or 'left':\n ")
  h1=h.lower()
  if h1=="right":
    n=input("It is alost night. You prefer to 'sleep' or 'continue' to search:\n ")
    n1=n.lower()
    if n1=="sleep":
      print("Be ready for long travel at early morning. \nHere is your map:\n")
      print('''                   ____    ,~~`/
   ,'`/  (,| \         ________________/    \,-`   /
 ,'   |NT |Qld \      |                           /
( WA  |----|____\     |                      .Tamworth
 \   ,|_,SA|NSW /     |.Broken Hill               ./Newcastle
  (_/    `^|`~,/      |            N.S.W.       |
           `-^'Vic    |                       */Sydney
             __       |__                     /
             \/Tas       `,'\_               /
                              '\_,~~~,      /
 Kevin Griffey                        \_   /
                                        \_|''')
    else:
        print("In the night time you can not find. You should sleep!")
        
       
  else:
   print("Why left? It was in the right! Change direction to right")
      
else:
  print("No! Dont try. Bear will be angry! He dont ready to accomodate new guests. Wait him go out")


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

