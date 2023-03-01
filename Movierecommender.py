import pandas as pd
import random
df = pd.read_csv("movies2006to2016.csv")
print("What is the movie genre that you want to watch")
answer = input()
df2 = df[df['Genre'].str.contains(answer)]
df2.set_index('Rating',inplace=True)
df2.sort_index(axis=0,ascending=False,inplace=True)
print("Here are movies which  has Metascore more than 75")
df3 = df2[df2['Metascore']>=75.0]
print(df3)

print(" if you cant choose DuraniMerdiOzalbı can choose for you. If you want so type'Yes'")

doyouwantmetochoose = input()
if doyouwantmetochoose == 'Yes':
    n = random.choice(range(df3.shape[0]))
    print(df3.iloc[n])
    print("Do you want me to tell you about this film if so type 'Yes' If you want another recommendation type 'No'")
    desc = input()
    if desc == 'Yes':
        print(df3.iloc[n,3])
        print("\n did you like it ")
        didlikeit = input()
        if didlikeit == 'No':
            while didlikeit == 'No':
                x = random.choice(range(df3.shape[0]))
                print(df3.iloc[x])
                print("\n did you like it")
                didlikeit = input()
                if didlikeit == 'Yes':
                    print("Do you want me to tell you about this film")
                    wantdescription = input()
                    if wantdescription == 'Yes':
                        print(df3.iloc[x,3])
                    else: print("IM TOO HAPPY THAT U USED ME ;)")
        else: print("BABY, BURN YOUR JO AND OPEN YOUR FILM")
    elif desc == 'No':
        while desc == 'No':
            m = random.choice(range(df3.shape[0]))
            print(df3.iloc[m])
            print("If you did not like it you can type 'No' So I can give you more if you like it type Yes to see the description")
            desc = input()
            if desc == 'Yes':
                print(df3.iloc[m,3])
                print("LET ME KNOW IF YOU LIKE IT OR NOT BY 'Yes' or 'No'")
                desc = input()
                if desc == 'Yes':
                    print("HAVE FUN I LOVE YOU FOR USING ME")


else:
    print("DO NOT FORGET TO BURN 1 OF YOUR JO's IT IS WORTH IT TRUST")




    



