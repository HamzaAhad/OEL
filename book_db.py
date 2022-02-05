# from itertools import count
# from re import I, X
import sqlite3
# from turtle import title


#Query the data and return ALL records
def show_all():
    conn = sqlite3.connect("book.db")
    #create a cursor
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM books")
    items =cursor.fetchall()
    for item in items:
        print(item)
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
#ADD NEW RECORD
def add_one(title,author,sub,pub_date,check_out="AVAILABLE",reserved="NO"):
    conn = sqlite3.connect("book.db")
    #create a cursor
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO books (title,author,sub,pub_date,check_out,reserved) VALUES (?,?,?,?,?,?)",(title,author,sub,pub_date,check_out,reserved))  
     #commit our command
    conn.commit()
    #close our connection
    conn.close()
#Delete func
def delete_one(book_id):
    try:
        conn = sqlite3.connect("book.db")
        #create a cursor
        cursor = conn.cursor()   
        
        cursor.execute("DELETE from books WHERE book_id= (?)",(book_id,))
        # cursor.execute("DELETE from books WHERE book_id = (?)",book_id) 
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
     
     #commit our command
    conn.commit()
    #close our connection
    conn.close()
#Add amny
def add_many(list):
    conn = sqlite3.connect("book.db")
    #create a cursor
    cursor = conn.cursor()   
    cursor.executemany("INSERT INTO books (title,author,sub,pub_date,check_out,reserved) VALUES (?,?,?,?,?,?)",(list))  
     #commit our command
    conn.commit()
    #close our connection
    conn.close()

#looking with Where
def book_lookup(x,name):
    try:
        catagory=x
        print(x)
        name=name
        print(name)
        query="SELECT * from books WHERE "+catagory+"= (?)"
        conn = sqlite3.connect("book.db")
        #create a cursor
        cursor = conn.cursor()  
        cursor.execute(query,(name,))
        
        # cursor.execute("SELECT * from books WHERE sub= (?)",(name,))
        items =cursor.fetchall()
        display_pattern(items)
        #commit our command``
        conn.commit()
        #close our connection
        conn.close()
    except Exception as error:
        print("SOME ERROR OCCURED",error)
    
def display():
    conn = sqlite3.connect("book.db")
    #create a cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    items = cursor.fetchall()
    #first calling sorting algo 
    new_items=search_algo(items)
    display_pattern(new_items)

        

    print("command executed successfully")
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
    
def update(field,item,id):
    conn = sqlite3.connect("book.db")
    #create a cursor
    cursor = conn.cursor()
    #update records:

    # cursor.execute("""UPDATE books SET title ='big' WHERE rowid = 2""")
    field=field
    item=item
    item="'"+item+"'"
    id=str(id)
    query="UPDATE books SET "+field+"="+item+"  WHERE booK_id = "+id
    cursor.execute(query)
    conn.commit()
    #query the database
    print("command executed successfully")
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
    

def display_pattern(items):
    fields=["book_id: ","title: ","author: ","sub: ","pub_date: ","check_out: ","reserved: "]
    count=0
    for item in items:
        print("-"*20)
        for value in item:
           print(fields[count],value)
           count+=1 
        print("-"*20)
        count=0
        
def check_availability(dic_book,book_id):
        dic_book=dic_book
        count=0
        check=None
        for key,value in dic_book.items():
            if key==book_id:
                check=value[0]
                count+=1
        
        if count==0:
            print("NO SUCH BOOK PRESENT") 
        count=0
        if check == "AVAILABLE":
            return True
        else:
            return False
        
def check_reservation(dic_book,book_id):
        res=None
        dic_book=dic_book
        count=0
        for key,value in dic_book.items():
            if key==book_id:
                res=value[1]
                count+=1
        if count==0:
            print("NO SUCH BOOK PRESENT")            
        count=0
        if res == "NO":
            return [True,res]
        else:
            return [False,res]
        
def get_book_details():
        dic_book={}
        conn = sqlite3.connect("book.db")
        
        #create a cursor
        cursor = conn.cursor()  
        
        cursor.execute("SELECT * from books")
        items =cursor.fetchall()
        for item in items:
            dic_book[item[0]]=[item[5],item[6]]
            
        #commit our command``
        conn.commit()
        #close our connection
        conn.close()
        
        return dic_book
        
def dic_update(dic,id,loc,change):
    loc=int(loc)
    for key,value in dic.items():
        if key==id:
            value[loc]=change
    
    return dic        


def search_algo(items):
    search_lst=[]
    search_dic={}
    new_items=[]
    for item in items:
        #add to dic
        x=item[1]
        # print(x)

        # search_dic[item[0]]=item[1]
        #add to lst
        
        search_lst.append(x)
        
    # print(search_dic)
    #converting to ascii
    # print(search_lst)
    
    search_lst=quicksort(search_lst)
    # print(search_lst)
    for i in search_lst:
        for j in items:
            if i==j[1]:
                new_items.append(j)
                
    # print(new_items)
    
    return new_items
    



def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))
    
def update_col(dic_book):
    conn = sqlite3.connect("book.db")
    
    #create a cursor
    cursor = conn.cursor()
    #update records:

    #update check_out
    for key,value in dic_book.items():
    
        field="check_out"
        item=str(value[0])
        item="'"+item+"'"
        id=str(key)
        query="UPDATE books SET "+field+"="+item+"  WHERE book_id = "+id
        cursor.execute(query)
        conn.commit()
        
    for key,value in dic_book.items():
    
        field="reserved"
        item=str(value[1])
        item="'"+item+"'"
        id=str(key)
        query="UPDATE books SET "+field+"="+item+"  WHERE book_id = "+id
        cursor.execute(query)
        conn.commit()
    
 
    #query the database
    print("command executed successfully")
    #commit our command
   
    #close our connection
    conn.close()

    
