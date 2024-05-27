-- Table: public.category
DROP TABLE IF EXISTS public.category;
CREATE TABLE IF NOT EXISTS PUBLIC.CATEGORY (
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (
		INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
	),
	NAME CHARACTER VARYING COLLATE PG_CATALOG."default",
	PAYMENT NUMERIC,
	CONSTRAINT CATEGORY_PKEY PRIMARY KEY (ID)
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.CATEGORY OWNER TO POSTGRES;

-- Table: public.department
DROP TABLE IF EXISTS public.department;
CREATE TABLE IF NOT EXISTS PUBLIC.DEPARTMENT (
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (
		INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
	),
	NAME CHARACTER VARYING COLLATE PG_CATALOG."default",
	ADDRESS CHARACTER VARYING COLLATE PG_CATALOG."default",
	CONSTRAINT DEPARTMENT_PKEY PRIMARY KEY (ID)
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.DEPARTMENT OWNER TO POSTGRES;

-- Table: public.patient
DROP TABLE IF EXISTS public.patient;
CREATE TABLE IF NOT EXISTS PUBLIC.PATIENT (
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (
		INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
	),
	NAME CHARACTER VARYING COLLATE PG_CATALOG."default",
	BIRTHDAY DATE,
	CONSTRAINT PATIENT_PKEY PRIMARY KEY (ID)
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.PATIENT OWNER TO POSTGRES;

-- Table: public.doctor
DROP TABLE IF EXISTS public.doctor;
CREATE TABLE IF NOT EXISTS PUBLIC.DOCTOR (
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (
		INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
	),
	NAME CHARACTER VARYING COLLATE PG_CATALOG."default",
	ID_CATEGORY INTEGER,
	ID_DEPARTMENT INTEGER,
	CONSTRAINT DOCTOR_PKEY PRIMARY KEY (ID),
	CONSTRAINT DOC_CAT FOREIGN KEY (ID_CATEGORY) REFERENCES PUBLIC.CATEGORY (ID) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT DOC_DEP FOREIGN KEY (ID_DEPARTMENT) REFERENCES PUBLIC.DEPARTMENT (ID) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.DOCTOR OWNER TO POSTGRES;

-- Table: public.attendance
DROP TABLE IF EXISTS public.attendance;
CREATE TABLE IF NOT EXISTS PUBLIC.ATTENDANCE (
	ID_DOCTOR INTEGER NOT NULL,
	ID_PATIENT INTEGER NOT NULL,
	CONSTRAINT ATTENDANCE_PKEY PRIMARY KEY (ID_DOCTOR, ID_PATIENT),
	CONSTRAINT ATTENDANCE_ID_DOCTOR_FKEY FOREIGN KEY (ID_DOCTOR) REFERENCES PUBLIC.DOCTOR (ID) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT ATTENDANCE_ID_PATIENT_FKEY FOREIGN KEY (ID_PATIENT) REFERENCES PUBLIC.PATIENT (ID) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.ATTENDANCE OWNER TO POSTGRES;

-- Table: public.insurance
DROP TABLE IF EXISTS public.insurance;
CREATE TABLE IF NOT EXISTS PUBLIC.INSURANCE (
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (
		INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
	),
	NAME CHARACTER VARYING COLLATE PG_CATALOG."default",
	BIRTHDAY DATE,
	POLICY CHARACTER VARYING COLLATE PG_CATALOG."default",
	CONSTRAINT INSURANCE_PKEY PRIMARY KEY (ID)
) TABLESPACE PG_DEFAULT;

ALTER TABLE IF EXISTS PUBLIC.INSURANCE OWNER TO POSTGRES;

INSERT INTO
	CATEGORY (NAME, PAYMENT)
VALUES
	('Высшая', 430),
	('Вторая', 380),
	('Первая', 400);

INSERT INTO
	DEPARTMENT (NAME, ADDRESS)
VALUES
	('Терапевтическое отделение', 'ул. Ленина, д. 1'),
	('Педиатрическое отделение', 'ул. Мира, д. 2'),
	(
		'Стоматологическое отделение',
		'ул. Садовая, д. 3'
	),
	(
		'Отделение акушерства и гинекологии',
		'ул. Лесная, д. 4'
	),
	('Хирургическое отделение', 'ул. Морская, д. 5'),
	(
		'Отделение медицинской профилактики',
		'ул. Речная, д. 6'
	);

INSERT INTO
	PATIENT (NAME, BIRTHDAY)
VALUES
	('Светлана Евгеньевна Смирнова', '22.07.2009'),
	('Юлия Николаевна Семенова', '01.06.2012'),
	('Станислав Владимирович Федоров', '18.02.1977'),
	('Константин Петрович Николаев', '25.08.1981'),
	('Татьяна Николаевна Петрова', '30.10.2011'),
	('Маргарита Сергеевна Семенова', '13.05.1979'),
	('Павел Петрович Орлов', '11.11.1978'),
	('Федор Иванович Николаев', '16.04.2007'),
	('Ольга Владимировна Новикова', '17.09.2001'),
	('Николай Александрович Иванов', '29.01.2005');

INSERT INTO
	DOCTOR (NAME, ID_CATEGORY, ID_DEPARTMENT)
VALUES
	('Александр Сергеевич Иванов', 1, 1),
	('Алексей Владимирович Смирнов', 2, 2),
	('Анна Ивановна Петрова', 3, 3),
	('Борис Юрьевич Семенов', 3, 4),
	('Василий Петрович Николаев', 2, 5),
	('Вера Сергеевна Андреева', 2, 6),
	('Геннадий Алексеевич Орлов', 2, 2),
	('Дарья Николаевна Новикова', 1, 4),
	('Евгений Борисович Федоров', 2, 5),
	('Екатерина Алексеевна Козлова', 3, 1),
	('Иван Петрович Сидоров', 2, 6),
	('Ирина Александровна Сергеева', 2, 6),
	('Кирилл Владимирович Павлов', 1, 6),
	('Лариса Ивановна Смирнова', 2, 1),
	('Максим Сергеевич Васильев', 3, 1),
	('Мария Евгеньевна Новикова', 2, 4),
	('Николай Петрович Смирнов', 1, 1),
	('Оксана Владимировна Иванова', 2, 3),
	('Сергей Геннадьевич Орлов', 3, 1);

INSERT INTO
	ATTENDANCE (ID_DOCTOR, ID_PATIENT)
VALUES
	(1, 1),
	(2, 2),
	(3, 1),
	(4, 1),
	(5, 3),
	(6, 4),
	(7, 5),
	(8, 6),
	(9, 7),
	(10, 8),
	(11, 6),
	(12, 4),
	(13, 9),
	(14, 6),
	(15, 9),
	(16, 6),
	(17, 9),
	(18, 8),
	(19, 1),
	(1, 10),
	(14, 4),
	(3, 10),
	(18, 9),
	(3, 4),
	(18, 6),
	(12, 6),
	(13, 6),
	(15, 1),
	(17, 10),
	(8, 9);

INSERT INTO
	PUBLIC.INSURANCE (NAME, BIRTHDAY, POLICY)
VALUES
	(
		'Светлана Евгеньевна Смирнова',
		'22.07.2009',
		'ОМС'
	),
	('Юлия Николаевна Семенова', '01.06.2012', 'ОМС'),
	(
		'Станислав Владимирович Федоров',
		'18.02.1977',
		'ОМС'
	),
	(
		'Константин Петрович Николаев',
		'25.08.1981',
		'ОМС'
	),
	('Татьяна Николаевна Петрова', '30.10.2011', 'ДМС'),
	(
		'Маргарита Сергеевна Семенова',
		'13.05.1979',
		'ОМС'
	),
	('Павел Петрович Орлов', '11.11.1978', 'ДМС'),
	('Федор Иванович Николаев', '16.04.2007', 'ОМС'),
	(
		'Ольга Владимировна Новикова',
		'17.09.2001',
		'ОМС'
	),
	(
		'Николай Александрович Иванов',
		'29.01.2005',
		'ДМС'
	),
	('Евгений Борисович Федоров', '21.06.1982', 'ОМС'),
	('Ольга Викторовна Смирнова', '03.07.1991', 'ОМС'),
	('Кирилл Александрович Попов', '18.02.1979', 'ДМС'),
	(
		'Екатерина Алексеевна Кузнецова',
		'04.11.1980',
		'ОМС'
	),
	('Михаил Сергеевич Васильев', '29.09.1985', 'ОМС'),
	('Анна Ивановна Афанасьева', '08.05.1978', 'ОМС'),
	('Глеб Николаевич Борисов', '15.01.1987', 'ОМС'),
	('Татьяна Олеговна Розова', '24.03.1983', 'ДМС'),
	('Илья Владимирович Соколов', '12.10.1977', 'ДМС'),
	(
		'Оксана Владимировна Иванова',
		'09.08.1986',
		'ОМС'
	),
	('Сергей Васильевич Новиков', '17.06.1984', 'ДМС'),
	('Елена Сергеевна Петрова', '30.04.2008', 'ДМС'),
	('Дмитрий Алексеевич Андреев', '01.03.2010', 'ОМС'),
	('Мария Ивановна Миронова', '14.12.2009', 'ДМС'),
	('Борис Сергеевич Тарасов', '25.11.2007', 'ОМС'),
	('Анна Анатольевна Егорова', '16.07.2005', 'ОМС'),
	('Евгений Николаевич Волков', '05.02.2006', 'ДМС'),
	('Мария Евгеньевна Новикова', '11.08.2001', 'ДМС'),
	(
		'Максим Владимирович Степанов',
		'27.01.2002',
		'ОМС'
	),
	('Екатерина Юрьевна Симонова', '31.12.2011', 'ОМС');