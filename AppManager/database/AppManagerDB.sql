--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Apps; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Apps" (
    "ID" integer NOT NULL,
    app_name character varying(100) NOT NULL,
    version character varying(20) NOT NULL,
    "description " text NOT NULL
);


ALTER TABLE public."Apps" OWNER TO postgres;

--
-- Data for Name: Apps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Apps" ("ID", app_name, version, "description ") FROM stdin;
1	App_1	1.1	Desc 1
2	App_2	1.2	Desc 2
3	App_3	1.3	Desc 3
4	App_4	1.4	Desc 4
\.


--
-- Name: Apps Apps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Apps"
    ADD CONSTRAINT "Apps_pkey" PRIMARY KEY ("ID");


--
-- PostgreSQL database dump complete
--

