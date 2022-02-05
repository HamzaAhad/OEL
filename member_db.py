
import sqlite3

from book_db import update_col



#Query the data and return ALL records
def show_all():
    conn = sqlite3.connect("member.db")
    #create a cursor
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM members")
    items =cursor.fetchall()
    for item in items:
        print(item)
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
#ADD NEW RECORD
def add_one(member_name,check_out=None,reserved=None):
    conn = sqlite3.connect("member.db")
    #create a cursor
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO members (member_name,check_out,reserved) VALUES (?,?,?)",(member_name,check_out,reserved))  
     #commit our command
    conn.commit()
    #close our connection
    conn.close()
#Delete func
def delete_one(member_id):
    try:
        conn = sqlite3.connect("member.db")
        #create a cursor
        cursor = conn.cursor()   
        
        cursor.execute("DELETE from members WHERE member_id= (?)",(member_id,))
        # cursor.execute("DELETE from books WHERE book_id = (?)",book_id) 
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
     
     #commit our command
    conn.commit()
    #close our connection
    conn.close()
#Add many
def add_many(list):
    conn = sqlite3.connect("member.db")
    #create a cursor
    cursor = conn.cursor()   
    cursor.executemany("INSERT INTO members (member_name,check_out,reserved) VALUES (?,?,?)",(list))  
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
        query="SELECT * from members WHERE "+catagory+"= (?)"
        conn = sqlite3.connect("member.db")
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
    conn = sqlite3.connect("member.db")
    #create a cursor
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    items = cursor.fetchall()
    display_pattern(items)
    print("command executed successfully")
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
    
def update(field,item,id):
    conn = sqlite3.connect("member.db")
    #create a cursor
    cursor = conn.cursor()
    #update records:

    # cursor.execute("""UPDATE books SET title ='big' WHERE rowid = 2""")
    field=field
    item=item
    item="'"+item+"'"
    id=str(id)
    query="UPDATE members SET "+field+"="+item+"  WHERE member_id = "+id
    cursor.execute(query)
    conn.commit()
    #query the database
    print("command executed successfully")
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
    

def display_pattern(items):
    fields=["member_id: ","member_name: ","check_out: ","reserved: "]
    count=0
    for item in items:
        print("-"*20)
        for value in item:
           print(fields[count],value)
           count+=1 
        print("-"*20)
        count=0
        
def check_reservation(dic_mem,member_id):
        dic_mem=dic_mem
        count=0
        res=None
        for key,value in dic_mem.items():
            if key==member_id:
                res=value[1]
                count+=1
        if count==0:
            print("NO SUCH MEMBER PRESENT")            
        count=0
        if res == "NO":
            return True
        else:
            return res
        
def check_checkout(dic_mem,member_id):
        check=None
        dic_mem=dic_mem
        count=0
        for key,value in dic_mem.items():
            if key==member_id:
                check=value[0]
                count+=1
        
        if count==0:
            print("NO SUCH MEMBER PRESENT") 
        count=0
        if check == "NO":
            return True
        else:
            return check
        
def get_member_details():
        dic_mem={}
        conn = sqlite3.connect("member.db")
        
        #create a cursor
        cursor = conn.cursor()  
        # cursor.execute(query,(book_id,))
        cursor.execute("SELECT * from members")
        items =cursor.fetchall()
        for item in items:
            dic_mem[item[0]]=[item[2],item[3]]
            
        #commit our command``
        conn.commit()
        #close our connection
        conn.close()
        print(dic_mem)
        return dic_mem
        
def dic_update(dic,id,loc,change):
    loc=int(loc)
    for key,value in dic.items():
        if key==id:
            value[loc]=change
    print(dic)
    return dic

def update_col(dic_mem):
    conn = sqlite3.connect("member.db")
    
    #create a cursor
    cursor = conn.cursor()
    #update records:

    #update check_out
    for key,value in dic_mem.items():
    
        field="check_out"
        item=str(value[0])
        item="'"+item+"'"
        id=str(key)
        query="UPDATE members SET "+field+"="+item+"  WHERE member_id = "+id
        cursor.execute(query)
        conn.commit()
        
    for key,value in dic_mem.items():
    
        field="reserved"
        item=str(value[1])
        item="'"+item+"'"
        id=str(key)
        query="UPDATE members SET "+field+"="+item+"  WHERE member_id = "+id
        cursor.execute(query)
        conn.commit()
    
 
    #query the database
    print("command executed successfully")
    #commit our command
   
    #close our connection
    conn.close()
    


    
        
