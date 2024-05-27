-- Table: public.care

-- DROP TABLE IF EXISTS public.care;

CREATE TABLE IF NOT EXISTS public.care
(
    doctor character varying COLLATE pg_catalog."default",
    category character varying COLLATE pg_catalog."default",
    patient character varying COLLATE pg_catalog."default",
    birthday date,
    department character varying COLLATE pg_catalog."default",
    address character varying COLLATE pg_catalog."default",
    payment numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.care
    OWNER to postgres;