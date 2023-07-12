create database bookstore;
show databases;
use bookstore;
create table bookdetails(ISBN varchar(4), BookName varchar(20), Author varchar(20), Price float, Category varchar(20), QtyAvailable int);
insert into bookdetails values('AB01', 'The Alchemist', 'Paulo Coelho', 250, 'Fiction', 100);
insert into bookdetails values('AB02', 'Enchanted Woods', 'enid Blyton', 350, 'Fiction', 50);
insert into bookdetails values('AB03', 'Harry Potter', 'JK Rowling', 200, 'Fiction', 100);
insert into bookdetails values('AB04', 'Solo in Singapore', 'Tanushree Dutta', 450, 'Adventure', 70);
insert into bookdetails values('AB05', 'Discovery of India', 'JL Nehru', 450, 'History', 150);
insert into bookdetails values('AB07', 'Earth and Universe', 'Jyotsna M', 550, 'Science', 30);
insert into bookdetails values('AB08', 'The Human Body', 'Dr SK Singh', 940, 'Science', 0);
insert into bookdetails values('CD01', 'Indus Valley', 'Antonis McCarthy', 1000, 'History', 9);
insert into bookdetails values('CD02', 'Trip to Finland', 'S Saunders', 2050, 'Adventure', 8);
alter table bookdetails
add constraint bookdetails_pk
primary key(ISBN);

create table purchasedetails(CustomerID varchar(4), CustomerName varchar(20), PhoneNumber int, ISBN varchar(4), BookName varchar(2), QtyPurchased int);
alter table purchasedetails
modify column BookName varchar(20);
alter table purchasedetails
add column purchaseID varchar(4);
alter table purchasedetails
add constraint purchasedetails_pk
primary key(purchaseID);
alter table purchasedetails
MODIFY CustomerID varchar(4) AFTER purchaseID;
alter table purchasedetails
MODIFY CustomerID varchar(4) AFTER CustomerName;
alter table purchasedetails
MODIFY purchaseID varchar(4) AFTER CustomerName;
alter table purchasedetails
MODIFY CustomerName varchar(20) AFTER CustomerID;
ALTER TABLE purchasedetails CHANGE purchaseID PurchaseID varchar(4) ;
insert into purchasedetails values('PR01','CU01','Yamini Masand',22378947,'AB02','Enchanted Woods',2);
insert into purchasedetails values('PR02','CU02','Frank Anthony',32778947,'AB01','The Alchemist',1);
insert into purchasedetails values('PR03','CU01','Yamini Masand',22378947,'AB04','Solo in Singapore',3);
insert into purchasedetails values('PR04','CU03','Jyoti Sharma',22378732,'AB04','Solo in Singapore',1);
insert into purchasedetails values('PR05','CU04','Amit Kumar',22388948,'AB05','Discovery of India',2);
insert into purchasedetails values('PR06','CU02','Frank Anthony',32778947,'CD02','Trip to Finland',1);
insert into purchasedetails values('PR07','CU04','Amit Kumar',22388948,'CD01','Indus Valley',2);

create table booksordered(OrderID varchar(4) Primary key, ISBN varchar(4), BookName varchar(20), QtyOrdered int(4), SupplierID varchar(4), SupplierName varchar(20));
insert into booksordered values('OR01','AB08','The Human Body',30,'SU01','Behrisons Traders');
insert into booksordered values('OR02','AB01','The Alchemist',5,'SU02','Mehta Prints');
insert into booksordered values('OR03','AB02','Enchanted Woods',15,'SU02','Mehta Prints');
insert into booksordered values('OR04','AB07','Earth and Universe',75,'SU03','Teksons Traders');
insert into booksordered values('OR05','AB05','Discovery of India',21,'SU01','Behrisons Traders');







