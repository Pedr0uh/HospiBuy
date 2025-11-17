# Criar Banco de Dados
CREATE SCHEMA HospiBuy;

# Selecionando o Banco de dados
USE HospiBuy;

# Criação Tabelas
CREATE TABLE Hospitais (
    cnes VARCHAR(20),
    cnpj VARCHAR(18),
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    cpfADM VARCHAR(11),
    nomeADM VARCHAR(100),
    plano INT,
    primary key(cnes)
);

-- Criar tabela usuario
CREATE TABLE usuario (
    ID_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    cnes VARCHAR(20),
    cpf VARCHAR(11),
    cargo VARCHAR(100),
    endereco VARCHAR(100),
    senha VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, ## data conforme vai entrando no sistema 
    FOREIGN KEY (cnes) REFERENCES Hospitais(cnes)
);


CREATE TABLE fornecedor (
    ID_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    tipo VARCHAR(99) NOT NULL,
    cnpj VARCHAR(18),
    cpf VARCHAR(11),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE produto (
    sku VARCHAR(100) UNIQUE PRIMARY KEY,
    descricao VARCHAR(200) NOT NULL,
    quantidade INT DEFAULT 0,
    tipo VARCHAR(100),
    data_compra DATE,
    lote VARCHAR(50),
    validade DATE,
    localizacao varchar (100),
    ID_fornecedor INT,
    cnes VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_fornecedor) REFERENCES fornecedor(ID_fornecedor)
        ON DELETE SET NULL ON UPDATE CASCADE, 
    FOREIGN KEY (cnes) REFERENCES Hospitais(cnes)
        ON DELETE SET NULL ON UPDATE CASCADE
);


CREATE TABLE operacoes (
    id_operacao INT PRIMARY KEY AUTO_INCREMENT,
    nome_operacao VARCHAR(100),
    descartar VARCHAR(200),
    quantidade INT,
    unidade VARCHAR(10),
    sku VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sku) REFERENCES produto (sku)
);


CREATE TABLE movimentacao (
    id_mov INT PRIMARY KEY AUTO_INCREMENT,
    sku VARCHAR(100) UNIQUE,
    quantidade INT,
    id_operacao INT,
    data_mov DATE,
    status VARCHAR(50),
    FOREIGN KEY (sku) REFERENCES produto(sku),
    FOREIGN KEY (ID_operacao) REFERENCES operacoes(ID_operacao)
);


# Inserindo dados ficticios
INSERT INTO operacoes (nome_operacao, descartar, quantidade, unidade, sku) VALUES
('Entrada', NULL, 50, 'UN','SKU001'),
('Saída', 'Luvas M', 20, 'UN','SKU003'),
('Entrada', NULL, 100, 'CX','SKU009'),
('Saída','Soro', 15, 'UN','SKU002'),
('Saída',  'Máscaras', 30, 'UN','SKU004'),
('Entrada', NULL, 200, 'UN','SKU002'),
('Entrada', NULL, 90, 'CX','SKU004'),
('Saída','Dipirona', 10, 'UN','SKU001'),
('Saída','Gaze', 25, 'UN','SKU005'),
('Entrada',NULL, 120, 'UN','SKU011'),
('Saída', 'Omeprazol', 12, 'UN','SKU008'),
('Entrada', NULL, 300, 'UN','SKU004'),
('Entrada', NULL, 70, 'CX','SKU014'),
('Saída', 'Agulhas', 40, 'UN','SKU009'),
('Entrada', NULL, 45, 'UN','SKU010');


INSERT INTO produto (sku, descricao, quantidade, tipo, data_compra, lote, validade, localizacao, ID_fornecedor, cnes) VALUES
('SKU001', 'Dipirona 500mg', 100, 'Medicamento', '2025-01-10', 'L001', '2026-01-10', 'Estoque A1', 1, '100001'),
('SKU002', 'Soro Fisiológico 0,9%', 200, 'Medicamento', '2025-01-12', 'L002', '2027-02-11', 'Estoque A2', 2, '100001'),
('SKU003', 'Luvas M', 500, 'Descartável', '2025-01-15', 'L003', '2027-03-01', 'Sala 01', 3, '100001'),
('SKU004', 'Máscara Cirúrgica', 1000, 'Descartável', '2025-01-17', 'L004', '2027-05-31', 'Sala 02', 4, '100001'),
('SKU005', 'Gaze 7cm', 350, 'Descartável', '2025-01-20', 'L005', '2027-04-15', 'Estoque B1', 5, '100001'),
('SKU006', 'Álcool 70%', 300, 'Higiene', '2025-01-22', 'L006', '2027-05-21', 'Estoque B2', 6, '100001'),
('SKU007', 'Amoxicilina 500mg', 120, 'Medicamento', '2025-01-25', 'L007', '2026-07-11', 'Farmácia 01', 1, '100001'),
('SKU008', 'Omeprazol 20mg', 90, 'Medicamento', '2025-01-27', 'L008', '2026-08-11', 'Farmácia 02', 2, '100001'),
('SKU009', 'Agulhas 25x7', 400, 'Descartável', '2025-01-29', 'L009', '2027-01-19', 'Sala 03', 3, '100001'),
('SKU010', 'Seringas 5ml', 800, 'Descartável', '2025-02-01', 'L010', '2027-03-10', 'Sala 04', 4, '100001'),
('SKU011', 'Esparadrapo 10cm', 150, 'Material', '2025-02-05', 'L011', '2028-02-05', 'Ala C', 5, '100001'),
('SKU012', 'Paracetamol 750mg', 130, 'Medicamento', '2025-02-07', 'L012', '2026-03-07', 'Farmácia 03', 6, '100001'),
('SKU013', 'Termômetro Digital', 40, 'Equipamento', '2025-02-09', 'L013', '2030-01-01', 'Sala Equip', 7, '100001'),
('SKU014', 'Curativo Transparente', 270, 'Material', '2025-02-12', 'L014', '2027-11-30', 'Ala A', 8, '100001'),
('SKU015', 'Álcool Gel', 600, 'Higiene', '2025-02-15', 'L015', '2027-06-12', 'Corredor 3', 9, '100001');

INSERT INTO usuario (nome, email, cnes, cpf, cargo, endereco, senha) VALUES
('Pedro Henrique', 'pedro@saude.com', '100001', '11122233344', 'ADM', 'Rua Azul 100', '1234'),
('João Silva', 'joao@hosp.com', '100002', '22233344455', 'Médico', 'Av Verde 200', 'abc'),
('Lucas Santos', 'lucas@hosp.com', '100003', 12345678910, 'Fornecedor', 'Rua Ypê 21', 'senha'),
('Ana Paula', 'ana@hosp.com', '100003', '33344455566', 'Recepção', 'Av Laranja 231', 'senha'),
('Fernanda Lima', 'fernanda@hosp.com', '100004', '44455566677', 'Farmacêutica', 'Rua Rosa 77', 'senha'),
('Rafael Souza', 'rafael@hosp.com', '100005', '55566677788', 'TI', 'Rua A 90', 'senha'),
('Juliana Alves', 'juliana@hosp.com', '100006', '66677788899', 'Médica', 'Av B 102', 'senha'),
('Carlos Pinto', 'carlos@hosp.com', '100006', '77788899900', 'Segurança', 'Praça 45', 'senha'),
('Patrícia Moraes', 'patricia@hosp.com', '100007', '88899900011', 'Nutricionista', 'Rua C 66', 'senha'),
('Marcelo Oliveira', 'marcelo@hosp.com', '100008', '99900011122', 'Enfermeiro', 'Rua D 12', 'senha'),
('Bruna Vasconcelos', 'bruna@hosp.com', '100008', '10111213141', 'Farmácia', 'Av XPTO 91', 'senha'),
('Diego Fernandes', 'diego@hosp.com', '100009', 78945612310, 'Fornecedor', 'Rua M 87', 'senha'),
('Marcos André', 'marcos@hosp.com', '100010', '12131415161', 'RH', 'Rua Alfa 101', 'senha'),
('Fernanda Souza', 'fersouza@hosp.com', '100011', '13141516171', 'TI', 'Rua Beta 209', 'senha'),
('Vitor Hugo', 'vitor@hosp.com', '100012', '14151617181', 'ADM', 'Rua Gama 56', 'senha');


INSERT INTO Hospitais (cnes, cnpj, nome, telefone, email, cpfADM, nomeADM, plano) VALUES
('100001', '11.111.111/0001-11', 'Hospital Vida Nova', '1130001000', 'contato@vidanova.com', '11122233344', 'Marina Torres',  3),
('100002', '22.222.222/0001-22', 'Hospital São Lucas', '1130002000', 'lucas@sla.com', '98765432100', 'João Pedro',  1),
('100003', '33.333.333/0001-33', 'Hospital Esperança', '1130003000', 'esperanca@hosp.com', '11122233344', 'Marcos Silva',  2),
('100004', '44.444.444/0001-44', 'Hospital Central Norte', '1130004000', 'central@hosp.com', '22233344455', 'Ana Borges', 3),
('100005', '55.555.555/0001-55', 'Clínica Saúde Total', '1130005000', 'st@clin.com', '33344455566', 'Paulo Lima',  1),
('100006', '66.666.666/0001-66', 'Hospital Santa Rita', '1130006000', 'sr@hosp.com', '44455566677', 'Beatriz Rezende',  3),
('100007', '77.777.777/0001-77', 'Hospital Vida Plena', '1130007000', 'vp@hosp.com', '55566677788', 'Ricardo Souza',  2),
('100008', '88.888.888/0001-88', 'Clínica Bem Cuidar', '1130008000', 'bc@clin.com', '66677788899', 'Laura Mendes',  1),
('100009', '99.999.999/0001-99', 'Hospital Horizonte', '1130009000', 'hh@hosp.com', '77788899900', 'Thiago Costa', 3),
('100010', '12.345.678/0001-10', 'Hospital Clemente', '11998770001', 'hc@hosp.com', '10101010101', 'Julia Lopes', 1),
('100011', '98.765.432/0001-98', 'Hospital Sol Nascente', '11988776655', 'sol@hosp.com', '12121212121', 'Gabriel Reis', 2),
('100012', '23.456.789/0001-23', 'Hospital Bela Vista', '11933554422', 'bv@hosp.com', '13131313131', 'Fernanda Rocha', 3),
('100013', '32.165.497/0001-32', 'Hospital São Miguel', '11900221144', 'sm@hosp.com', '14141414141', 'Davi Azevedo', 1),
('100014', '65.498.321/0001-65', 'Clínica Nova Saúde', '11954871233', 'ns@clin.com', '15151515151', 'Camila Prado', 2),
('100015', '54.621.987/0001-54', 'Hospital Aliança', '1133002299', 'alianca@hosp.com', '16161616161', 'Pedro Martins', 3);

INSERT INTO fornecedor (nome, cnpj, cpf, email, telefone, endereco) VALUES
('BioMed Distribuidora', 'medicamento','10.111.222/0001-10', NULL, 'bio@med.com', '1130010010', 'Rua X 12'),
('Hospital Supply','medicamento', '11.111.111/0001-11', NULL, 'hs@supp.com', '1130020020', 'Rua Y 33'),
('MedPrime', 'medicamento','22.222.222/0001-22', NULL, 'medprime@forn.com', '1130030030', 'Rua Z 44'),
('Casa da Saúde', 'descarte', NULL, '12345678901', 'saude@casa.com', '11988990011', 'Av A 55'),
('FarmaBrás', 'medicamento', '33.333.333/0001-33', NULL, 'farmabras@forn.com', '1130040040', 'Av B 66'),
('PharmaPlus', 'medicamento','44.444.444/0001-44', NULL, 'pl@pharma.com', '1130050050', 'Rua C 77'),
('Vida Farma','itens', NULL, '98765432100', 'vidafarma@forn.com', '11988776655', 'Rua D 88'),
('AlphaMedic', 'itens', '55.555.555/0001-55', NULL, 'alpha@med.com', '1130060060', 'Rua E 99'),
('CleanHosp', 'itens', '66.666.666/0001-66', NULL, 'clean@hosp.com', '1130070070', 'Rua F 11'),
('ProMedic', 'itens', '77.777.777/0001-77', NULL, 'pro@medic.com', '1130080080', 'Rua G 22'),
('SafeDistribuidora', 'itens', '88.888.888/0001-88', NULL, 'safe@dist.com', '1130090090', 'Rua H 33'),
('MasterMed', 'itens', '99.999.999/0001-99', NULL, 'master@med.com', '11933112200', 'Rua I 44'),
('BioPlus', 'medicamentos','12.345.678/0001-10', NULL, 'bio@plus.com', '11944556677', 'Rua J 55'),
('Hospital Clean', 'descarte', NULL, '10293847566', 'clean@hc.com', '11955667788', 'Rua K 66'),
('FarmaGold', 'medicamento', '98.765.432/0001-90', NULL, 'gold@farma.com', '11966778899', 'Rua L 77');


INSERT INTO movimentacao (id_produto, quantidade, id_operacao, data_mov, status) VALUES
('SKU001', 20, 1, '2025-03-01', 'APROVADA'),
('SKU002', 15, 2, '2025-03-02', 'PENDENTE'),
('SKU003', 50, 3, '2025-03-03', 'APROVADA'),
('SKU004', 30, 4, '2025-03-04', 'APROVADA'),
('SKU005', 25, 5, '2025-03-05', 'PENDENTE'),
('SKU006', 90, 6, '2025-03-06', 'APROVADA'),
('SKU007', 60, 7, '2025-03-07', 'APROVADA'),
('SKU008', 10, 8, '2025-03-08', 'APROVADA'),
('SKU009', 40, 9, '2025-03-09', 'PENDENTE'),
('SKU010', 80, 10, '2025-03-10', 'APROVADA'),
('SKU011', 12, 11, '2025-03-11', 'APROVADA'),
('SKU012', 100, 12, '2025-03-12', 'APROVADA'),
('SKU013', 30, 13, '2025-03-13', 'APROVADA'),
('SKU014', 45, 14, '2025-03-14', 'PENDENTE'),
('SKU015', 50, 15, '2025-03-15', 'APROVADA');




