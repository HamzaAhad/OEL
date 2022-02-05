

import book_db
import member_db


#########################################################START OF HOME_SCREEN###########################################################
class home_screen():
    def __init__(self):
        print("YOU HAVE TWO OPTIONS TO CHOOSE FROM\n1.ADMIN\n2.MEMBER\n3.EXIT")
        choice=input("ENTER: ")
        if choice=="1":
            print("MOVING TO ADMIN BLOCK")
            a=admin()
            
        elif choice=='2':
            print("MOVING TO MEMBER BLOCK")
            m=member()
            
        else:
            quit()
            
#########################################################END OF HOME_SCREEN########################################################### 
          
#########################################################START OF ADMIN BLOCK###########################################################
class admin():
    def __init__(self):
        print("YOU ARE IN ADMIN BLOCK")
        self.option()
    def option(self):
        print("WHAT YOU WANT TO DO? ")
        print("1.BOOK_FUNCTIONALITY\n| ADD | REMOVE | MODIFY |")
        print("2.SEARCH CATALOG")
        print("3.WORKING ON MEMBERSHIPS")
        print("4.GO BACK")
        opt= input("ENTER PICK ONE: ")
        if opt == "1":
            print("BOOK_FUNCTIONALITY")
            b=book_functions()
        elif opt == "2":
            print("SEARCH CATALOG")
            s=search_catalog()
        elif opt =="3":
            print("MEMBERSHIPS")
            m=membership()
        elif opt=="4":
            h=home_screen()
        else:
            print("INPUT VALID OPTION")
            self.option()
            
            
class search_catalog():
    def __init__(self):
        self.search()
               
    def search(self):
        print("NAME THE CATAGORY THROUGH WHICH YOU WANT TO FIND THE BOOK: ")
        print("title\nauthor\nsub\npub_date")
        x=input("CATAGORY: ")
        Value=input("ENTER VALUE OF THAT CATAGORY W.R.T WHICH YOU WANT THE BOOK: ")
        book_db.book_lookup(x,Value)
        while True:
            opt=input("WHAT YOU WANT TO DO?\n1.CONTINUE\n2.BACK")
            if opt=="1":
                self.search()
                break
            elif opt=="2":
                a=admin()
                break
            else:
                print("ENTER VALID CHOICE")  
            
class book_functions():
    def __init__(self):
        try:
            print("CHOOSE FROM THE OPTIONS PROVIDED: ")
            print("1.ADD DATA")
            print("2.DELETE DATA")
            print("3.MODIFY DATA")
            print("4.BACK TO ADMIN")
            option=input("ENTER NO: ")
            if option=="1":
                self.add_book()
            elif option=="2":
                self.delete_book()
            elif option=="3":
                self.modify_detail()
            else:
                a=admin()
        except Exception as error:
            print("Some error occured",error)
            
            
    
    def add_book(self):
        
        choice=int(input("ENTER THE NO OF RECORDS YOU WANT TO INSERT"))
        print("GIVE THE DETAIL INFO OF THE BOOK YOU WANT TO ADD SUCH AS")
        if choice == 1:
            title=input("title: ")
            author=input("author: ")
            sub=input("subject: ")
            pub_date=input("pubication date: ")
            book_db.add_one(title,author,sub,pub_date)
        else:
            lst=[]
            for i in range(choice):
                title=input("title: ")
                author=input("author: ")
                sub=input("subject: ")
                pub_date=input("pubication date: ")
                lst.append((title,author,sub,pub_date,"AVAILABLE","NO"))
            book_db.add_many(lst)
            lst=[]
        self.__init__()
    def delete_book(self):
        book_db.display()
        book_id=int(input("Enter BOOK_ID: "))
        book_db.delete_one(book_id)
        self.__init__()
        #calling func of book_db
        
    def modify_detail(self):
        book_db.display()
        field=input("ENTER THE FIELD WHERE YOU WANT TO UPDATE: ")
        id=input("ENTER THE BOOK_ID NUMBER WHERE YOU WANT TO UPDATE: ")
        item=input("ENTER THE UPDATED ITEM: ")
        book_db.update(field,item,id)
        self.__init__()
              
class membership():
    
    def __init__(self):
        self.option()
        
    def option(self):
        print('WHAT YOU WANT DO? ')
        opt=input("1.ADD MEMBER\n2.CANCEL MEMBERSHIP\n3.GO BACK\nPICK: ")
        if opt=="1":
            self.add_member()
        elif opt=="2":
            self.remove_member()
        elif opt=="3":
            a=admin()
        else:
            print("ENTER VALID INPUT")
            self.option() 
            
    def add_member(self):
        
        x=int(input("HOW MANY MEMBERS YOU WANT TO ADD ?"))
        try:    
            if x==1:
                member_name=input("Member Name:")
                member_db.add_one(member_name)
            else:
                lst=[]
                for i in range(x):
                    member_name=input("Member Name:")
                    lst.append((member_name,"NO","NO"))
                member_db.add_many(lst)
                lst=[]                     
        except:
            print("SOMME ERROR OCCURED")
            self.add_member()
        self.option()
                
    
    def remove_member(self):
        member_db.display()
        try:
            x=input("ENTER THE MEMBER_ID OF THE MEMBER: ")
            member_db.delete_one(x)
        except:
            print('Some thing went wrong')
            self.remove_member()
        self.option()
                   
                   
#########################################################END OF ADMIN BLOCK###########################################################

#########################################################START OF MEMBER BLOCK###########################################################

class member():
    
    def __init__(self):
        
        
        x=input("CHOOSE ONE \n1.EXPLORE MEMBERSHIP OPTIONS: \n2.GO BACK: \nPICK: ")
        if x=="1":
            self.dic_book=book_db.get_book_details()
            self.dic_mem=member_db.get_member_details()
            self.option()
        else:
            w=home_screen()
    def option(self):
        
        mem_id=int(input("ENTER MEMBER ID: "))
        print("WHAT YOU WNAT TO DO? ")
        x=input("1.CHECKOUT\n2.RENEW\n3.RESERVE\n4.RETURN\nPICK: ")
        
        if x=="1":
            print("CHECKING OUT")
            self.check_out(mem_id)
        elif x=="2":
            self.renew(mem_id)
        elif x=="3":
            self.reserve(mem_id)
        elif x=="4":
                self.return_book(mem_id)
    def check_out(self,mem_id):
        
            #first checking out that is there any book that this member have already issued
            check_m_db=member_db.check_checkout(self.dic_mem,mem_id)
            if check_m_db == True:
                print("PICK ONE OF THE FOLLOWING BOOK")
                #display book
                book_db.display()
                book_id = int(input("ENTER BOOK ID OF THE BOOK YOU WANT: "))
                #checking availability of book and checking that book isn't 
                check_b_db=book_db.check_availability(self.dic_book,book_id)
                res_b_db=book_db.check_reservation(self.dic_book,book_id)
                print(check_b_db)
                print(res_b_db)
                if check_b_db==True and (True in res_b_db):
                    print("CHECKING OUT THE BOOK FOR YOU")
                    #modifying the check_out field in book_db
                    self.dic_book=book_db.dic_update(self.dic_book,book_id,"0",mem_id)
                    self.dic_mem=member_db.dic_update(self.dic_mem,mem_id,"0",book_id)
                    
                else:
                    print("BOOK NOT AVAILABLE")
                    x=input("DO YOU WANT TO RESERVE THIS BOOK[Y/N]: ")
                    if x=="Y" or x=="y":
                        r=self.reserve()
                    
                    
            else:
                print("You have already checked_out a book")
            
            opt=input("YOU WANT TO CONTINUE [Y/N]")
            if opt=="Y":
                self.option()
            else:
                #save that update data of dictionary to database
                self.save()
                self.__init__()
                
                
         
            
    def renew(self):
            print('DO YOU WANT TO RENEW THE BOOK') 
            print("THE BOOK IS AGAIN ISSUED TO YOU FOR A WEEK")  
            #there is no need to make any change in the dictionary 
            opt=input("YOU WANT TO CONTINUE [Y/N]")
            if opt=="Y":
                self.option()
            else:
                self.save()
                self.__init__()
            
    def reserve(self,mem_id):
        #first checking out that is there any book that this member have already made reservation
        res_m_db=member_db.check_reservation(self.dic_mem,mem_id)
        if res_m_db == True:
                print("PICK ONE OF THE FOLLOWING BOOK")
                #display book
                book_db.display()
                book_id = int(input("ENTER BOOK ID OF THE BOOK YOU WANT: "))
                #checking availability of book and checking that book is reserved
                check_b_db=book_db.check_availability(self.dic_book,book_id)
                res_b_db=book_db.check_reservation(self.dic_book,book_id)
                print("check_b_db:",check_b_db)
                print("res_b_db",res_b_db)
                if check_b_db==False and (True in res_b_db):
                    print("RESERVING THE BOOK FOR YOU")
                    #modifying the check_out field in book_db
                    self.dic_book=book_db.dic_update(self.dic_book,book_id,"1",mem_id)
                    self.dic_mem=member_db.dic_update(self.dic_mem,mem_id,"1",book_id)
                    print("final:",self.dic_book)
                    print("final",self.dic_mem)
                else:
                    if check_b_db==True:
                        print("THIS BOOK IS ALREADY AVAILABLE FOR CHECK OUT\nWE DONT HAVE TO POLICY OF MAIKING\nRESERVATION OF ALREADY AVAILABLE BOOKS")
                    elif res_b_db==False:
                        print("RESERVED ALREADY") 
                        
                    
        else:
                print("You have already reserved a book")
            
        opt=input("YOU WANT TO CONTINUE [Y/N]\n")
        if opt=="Y":
                self.option()
        else:
                self.save()
                self.__init__()
    def return_book(self,mem_id):
        #Taking book_id from member
        book_id=self.dic_mem[mem_id][0]
        self.dic_mem=member_db.dic_update(self.dic_mem,mem_id,"0","NO")
        
        #FILLING THE BOOK IN THE SLOT
        self.dic_book=book_db.dic_update(self.dic_book,book_id,"0","AVAILABLE")
        
        #CHECKING IF ANY RESERVATION BEING MADE IN THE NAME OF THIS BOOK
        
        #BOOK WILL BE CHECKED_OUT TO THE MEMBER_ID THAT MADE RESERVATION
        #IF YES THE RESERVATION WILL BECOME NO
        res_b_db=book_db.check_reservation(self.dic_book,book_id)
        print(res_b_db)
        if (False in res_b_db):
            res_mem_id=res_b_db[1]
            #checking_out book to that person
            self.dic_mem=member_db.dic_update(self.dic_mem,res_mem_id,"0",book_id)
            self.dic_mem=member_db.dic_update(self.dic_mem,res_mem_id,"1","NO")
            self.dic_book=book_db.dic_update(self.dic_book,book_id,"0",res_mem_id)
            self.dic_book=book_db.dic_update(self.dic_book,book_id,"1","NO")
            print("final:",self.dic_mem)
            print("final:",self.dic_book)
        else:
            pass
            
        opt=input("YOU WANT TO CONTINUE [Y/N]\n:")
        if opt=="Y":
                self.option()
        else:
                self.save()
                self.__init__()
                
    def save(self):
        dic_book=self.dic_book
        dic_mem=self.dic_mem
        
        # calling update_col function of book_db and mem_db respectively
        book_db.update_col(dic_book)
        member_db.update_col(dic_mem)
        
        print("DATA UPDATED")
        
        opt=input("YOU WANT TO CONTINUE [Y/N]\n:")
        if opt=="Y":
                self.option()
        else:
                self.save()
                self.__init__()
    
#########################################################END OF MEMBER BLOCK#############################################################
h=home_screen()