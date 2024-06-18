create database campeonato; --cria o banco de dados

--comecar com tabelas que nao possuem chaves estrangeiras

create table modalidade (
    codigo    int(5)      not null,  --tipo inteiro (maximo de caracteres), not null significa que é obrigatorio
    nome      varchar(50) not null,  --tipo string  (maximo de caracteres)
    treinador varchar(50) not null,  --tipo string  (maximo de caracteres)
    primary key(codigo));            --primarykey  (chave primaria)

create table atleta (
    codigo        int(5)      not null,
    nome          varchar(50) not null,
    peso          float(5,2)  not null,
    altura        float(3,2)  not null,
    codmodalidade int(5)      not null,
    primary key(codigo),
    foreign key(codmodalidade) references modalidade (codigo)); --puxa uma coluna de uma outra tabela (precisa ser primary key)

create table campeonato (
    codigo int(5) not null,
    data   data   not null,
    local  varchar(50) not null,
    cidade varchar(50) not null,
    estado varchar(50) not null,
    pais   varchar(50) not null,
    codatleta int(5)   not null,
    primary key(codigo),
    foreign key (atleta) references codatleta (codigo));

-----alterar tabela-----

ALTER TABLE nome
ADD campo data_type tamanho;
DROP campo
ALTER campo_antigo SET campo_novo data_type tamanho;

--exemplo--

--inserir
alter table modalidade
add preparador varchar(50) not null;

--excluir
alter table modalidade
drop trainador;

--alterar
alter table modalidade
alter treinador varchar(100) not null; --muda o varchar
--ou
alter table modalidade
alter treinador set preparador;        --muda o nome de treinador para preparador

--excluir
drop table nome_tabela;

