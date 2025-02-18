drop table if exists kategorie cascade;
drop table if exists produkt cascade ;
drop table if exists bestellung cascade;
drop table if exists kunde cascade; 
drop table if exists produkt_bestellung cascade;
drop table if exists warenkorb cascade;
drop table if exists groesse_preis cascade;
drop table if exists versand cascade;
drop table if exists benutzer cascade;






create table if not exists kategorie (
		kategorie_id serial primary key,
		kategorie_name varchar(20),
		beschreibung varchar(100)
		
);

insert into kategorie (kategorie_name, beschreibung)
		values ('männlich', 'Männerduft'),
			   ('weiblich', 'Frauenduft'),
			   ('unisex', 'Ausgleichender Duft'), 
			   ('alle drei', 'alle drei Düfte');

create table if not exists groesse_preis(
	groesse_preis_id serial primary key,
	size varchar(50),
	price integer

);

insert into groesse_preis ("size", price)
	values  ('25ml', 20),
			('50', 45),
			('100', 85),
			('200', 112),
			('3x 25', 55),
			('3x 50', 95),
			('3x 100', 165),
			('3x 200', 299);



create table if not exists produkt (
	produkt_id serial primary key,
	product_name varchar(50),
	groesse_preis_id integer,
	
	foreign key (groesse_preis_id) references groesse_preis(groesse_preis_id)
	
);

insert into produkt (product_name, groesse_preis_id)
			values ('Velorée Homme', 1),
					('Velorée Homme', 2),
					('Velorée Homme', 3),
					('Velorée Homme', 4),
					('Velorée Femme', 1),
					('Velorée Femme', 2),
					('Velorée Femme', 3),
					('Velorée Femme', 4),
					('Velorée Unisex', 1),
					('Velorée Unisex', 2),
					('Velorée Unisex', 3),
					('Velorée Unisex', 4),
					('Velorée Bundle', 5),
					('Velorée Bundle', 6),
					('Velorée Bundle', 7),
					('Velorée Bundle', 8);



create table if not exists kunde (
		kunde_id serial primary key,
		vorname_nachname varchar(50),
		email varchar(100),
		strasse varchar(100),
		ort varchar(100),
		plz integer,
		kreditkarte varchar(100)
		
		);


create table if not exists versand (
		versand_id serial primary key,
		versandart varchar(20)
);


insert into versand (versandart)
		values ('Lieferung'),
				('Click & Collect');


create table if not exists warenkorb (
		warenkorb_id serial primary key,
		produkt_id integer,	
		--benutzer_id integer,
		foreign key (produkt_id) references produkt(produkt_id)
		--foreign key (benutzer_id) references benutzer(benutzer_id)
);

		
create table if not exists bestellung (
				bestellung_id serial primary key,
				kunde_id int,
				versand_id int,
				warenkorb_id int,
				
				foreign key (kunde_id) references kunde(kunde_id),
				foreign key (versand_id) references versand(versand_id),
				foreign key (warenkorb_id) references warenkorb(warenkorb_id)
);



create table if not exists produkt_bestellung (
		produkt_bestellung_id serial primary key,
		produkt_id integer,
		bestellung_id integer,
		foreign key (produkt_id) references produkt(produkt_id),
		foreign key (bestellung_id) references bestellung(bestellung_id)
);







create table if not exists warenkorb_produkt (
		warenkorb_produkt_id serial primary key,
		produkt_id integer,
		warenkorb_id integer,
		foreign key (produkt_id) references produkt(produkt_id),
		foreign key (warenkorb_id) references warenkorb(warenkorb_id)
);

create table if not exists benutzer (
		titel varchar(20),
		vorname varchar(20),
		nachname varchar (50),
		geburtsdatum date,
		email varchar (50),
		passwort varchar(20)
);




  


select * from produkt;
select * from kategorie;
select * from bestellung;
select * from kunde;
select * from produkt_bestellung;
select * from warenkorb_produkt;
select * from warenkorb;
select * from versand;
select * from zahlung;

select * from groesse_preis;







	