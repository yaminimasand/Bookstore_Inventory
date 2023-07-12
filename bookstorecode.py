import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='tanya',database='bookstore')
if conn.is_connected():
    print('successfully connected')
c=conn.cursor()
print('My Bookstore')
print('1. Bookstore Employee Login')
print('2. Exit')
choice=int(input('Enter your choice: '))
if choice==1:
    user_name=input('Enter your username: ')
    password=input('Enter your password: ')
    while user_name=='yamini' and password=='tamanna':
        print('connected successfully')

        print('1. Enter Book Details')
        print('2. Enter Customer Purchase Details')
        print('3. Enter Ordered Books Details')
        print('4. View All Book Details')
        print('5. View All Customer Purchase Details')
        print('6. View All Order Details')
        print('7. Extract Book Records')
        print('8. Extract Customer Purchase Records')
        print('9. Extract Ordered Books Records')
        #print('10.Pie Chart for Popular Book Categories')
        print('10. Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            isbn=input('Enter Book ISBN XXXX: ')
            bookname=input('Enter Book Name: ')
            author=input('Enter Author Name: ')
            price=float(input('Enter Book Price: '))
            category=input('Enter Book Category: ')
            qtyavailable=int(input('Enter Quantity Available: '))
            sql_insert="INSERT INTO bookdetails VALUES('"+isbn+"','"+bookname+"','"+author+"',"+str(price)+",'"+category+"',"+str(qtyavailable)+")"
            c.execute(sql_insert)
            conn.commit()
            print('1 Record Inserted')


        elif choice==2:
            purchaseid=input('Enter Purchase ID XXXX: ')
            customerid=input('Enter Customer ID XXXX: ')
            customername=input('Enter Customer Name: ')
            phonenumber=int(input('Enter Customer Phone Number XXXXXXXX: '))
            isbn=input('Enter Book ISBN XXXX: ')
            bookname=input('Enter Book Name: ')
            qtypurchased=int(input('Enter Quantity Purchased: '))
            sql_insert="insert into purchasedetails values('"+purchaseid+"','"+customerid+"','"+customername+"',"+str(phonenumber)+",'"+isbn+"','"+bookname+"',"+str(qtypurchased)+")"
            c.execute(sql_insert)
            conn.commit()
            print('1 Record Inserted')


        elif choice==3:
            orderid=input('Enter Order ID XXXX: ')
            isbn=input('Enter Book ISBN XXXX: ')
            bookname=input('Enter Book Name: ')
            qtyordered=int(input('Enter Quantity Ordered: '))
            supplierid=input('Enter Supplier ID XXXX: ')
            suppliername=input('Enter Supplier Name: ')
            sql_insert="insert into orderdetails values('"+orderid+"', '"+isbn+"', '"+bookname+"'", "+str(qtyordered)+", '"+supplierid+"', '"+suppliername+"'")"
            c.execute(sql_insert)
            conn.commit()
            print('1 Record Inserted')


        elif choice==4:
            t=conn.cursor()
            t.execute('select * from bookdetails')
            record=t.fetchall()
            for i in record:
                print(i)
                
        elif choice==5:
            t=conn.cursor()
            t.execute('select * from purchasedetails')
            record=t.fetchall()
            for i in record:
                print(i)

        elif choice==6:
            t=conn.cursor()
            t.execute('select * from orderdetails')
            record=t.fetchall()
            for i in record:
                print(i)
                
                
        elif choice==7:
            a=input('Enter Book Name: ')
            t='select * from bookdetails where BookName=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
      
                 
        elif choice==8:
            a=input('Enter Customer Name: ')
            t='select * from purchasedetails where CustomerName=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
               
        elif choice==9:
            a=input('Enter Book Name: ')
            t='select * from orderdetails where BookName=("{}")'.format(a)
            c.execute(t)
            v=c.fetchall()
            for i in v:
                print(v)
      

        #elif choice==10:
            #import matplotlib.pyplot as plt
            #categories=('Science','Fiction','Adventure','History','Personal Development')
            #votes=[156,200,103,206,196]
            #colors=['red','yellow','green','blue','pink','white']
            #plt.pie(votes,labels=categories,colors=colors)
            #plt.title('Popularity of Book Categories Sold')
            #plt.show()

        elif choice==12:
            exit()
            
                            

    else:
        print('Wrong Password. Please Try Again')
        
            
if choice==2:
    exit()
   


