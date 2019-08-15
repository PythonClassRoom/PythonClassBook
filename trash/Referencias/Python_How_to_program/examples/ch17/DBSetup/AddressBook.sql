create table addresses (
	ID bigint AUTO_INCREMENT NOT NULL,
	FIRST_NAME text,
	LAST_NAME text NOT NULL,
	ADDRESS text,
	CITY text,
	STATE_PROVINCE text,
	POSTAL_CODE text,
	COUNTRY text,
	EMAIL_ADDRESS text,
	HOME_PHONE text,
	FAX_NUMBER text,
	constraint pk_addresses primary key (ID)
) 
;
