create table Publishers (
	PublisherID int AUTO_INCREMENT NOT NULL,
	PublisherName varchar (30) NOT NULL,
	constraint pk_Publishers primary key (PublisherID)
) 
;
create table Authors (
	AuthorID int AUTO_INCREMENT NOT NULL,
	FirstName varchar (20) NOT NULL,
	LastName varchar (30) NOT NULL,
	constraint pk_Authors primary key (AuthorID)
) 
;
create table Titles (
	ISBN varchar (20) NOT NULL,
	Title varchar (100) NOT NULL,
	EditionNumber varchar (4) NOT NULL,
	PublisherID int NOT NULL,
	Copyright varchar (4) NOT NULL,
	ImageFile varchar (20) NOT NULL,
	Price real NOT NULL,
	constraint fk_Titles foreign key (PublisherID)
		references Publishers (PublisherID), 
	constraint pk_Titles primary key (ISBN)
) 
;
create table AuthorISBN (
	AuthorID int NOT NULL,
	ISBN varchar (20) NOT NULL,
	constraint fk_AuthorISBN_1 foreign key (AuthorID)
		references authors (AuthorID), 
	constraint fk_AuthorISBN_2 foreign key (ISBN)
		references Titles (ISBN)
) 
;
