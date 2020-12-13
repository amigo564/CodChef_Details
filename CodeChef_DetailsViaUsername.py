import requests
from bs4 import BeautifulSoup

userName = input("If You don't have Internet this program will automatically shutDown\nEnter CodeChef UserName: ")


while(True):
    url = "https://www.codechef.com/users/"+userName
    html = requests.get(url)
    
    soup = BeautifulSoup(html.text,'html.parser')
    title = str(soup.title.string)
    orTitle=title.strip()

    if(str(orTitle) =="Competitive Programming | Participate & Learn | CodeChef"):
        print("Please Enter a valid username!!\n\n")
        userName = input("\n(If want to quit enter q else provide valid username) UserName: ")
        if(userName=='q'):
            break
    else:
        print("You have entered a valid username!!")
        #find all list element and parse them
        lis=soup.find_all('li')
        for li in lis:
            if(li.label!=None):
                if(li.span!=None and (li.label.string)!="Country:" and (li.label.string)!="Username:"):
                    print(str(li.label.string)+" "+str(li.span.string))
                if(str(li.label.string)=="Country:"):
                    print(str(li.label.string)+" "+str(li.span.span.string))
                if(str(li.label.string)=="Username:"):
                    print("Username: "+userName)

        #Getting User-Rating:
        temp = str(soup.find_all("div",class_='rating-number'))
        ntemp =[]
        ntemp+=temp
        rating=''
        if(len(ntemp)==39):
            newLis = ntemp[28:32]
            rating = ''.join(newLis)
        elif(len(ntemp)==36):
            rating='0'
            
        print("Your rating is: "+rating)
        userName = input("\n(If want to quit enter q else provide valid username) UserName: ")
        if(userName=='q' or userName=='Q'):
            break
        else:
            print("Continuing...\n")
            

