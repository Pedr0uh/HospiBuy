
CREATE TABLE Hospitais (
    ID_hospital INT PRIMARY KEY AUTO_INCREMENT,
    cnes VARCHAR(20),
    cnpj VARCHAR(18),
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    cpfADM VARCHAR(11),
    nomeADM VARCHAR(100),
    senha VARCHAR(255),
    plano VARCHAR(50)
);
INSERT INTO Hospitais (cnes, cnpj, nome, telefone, email, cpfADM, nomeADM, senha, plano) VALUES
('100001', '11.111.111/0001-11', 'Hospital Vida Nova', '1130001000', 'contato@vidanova.com', '12345678901', 'Carlos Almeida', 'senha1', 'Premium'),
('100002', '22.222.222/0001-22', 'Hospital São Lucas', '1130002000', 'lucas@sla.com', '98765432100', 'João Pedro', 'senha2', 'Standard'),
('100003', '33.333.333/0001-33', 'Hospital Esperança', '1130003000', 'esperanca@hosp.com', '11122233344', 'Marcos Silva', 'senha3', 'Plus'),
('100004', '44.444.444/0001-44', 'Hospital Central Norte', '1130004000', 'central@hosp.com', '22233344455', 'Ana Borges', 'senha4', 'Premium'),
('100005', '55.555.555/0001-55', 'Clínica Saúde Total', '1130005000', 'st@clin.com', '33344455566', 'Paulo Lima', 'senha5', 'Standard'),
('100006', '66.666.666/0001-66', 'Hospital Santa Rita', '1130006000', 'sr@hosp.com', '44455566677', 'Beatriz Rezende', 'senha6', 'Premium'),
('100007', '77.777.777/0001-77', 'Hospital Vida Plena', '1130007000', 'vp@hosp.com', '55566677788', 'Ricardo Souza', 'senha7', 'Plus'),
('100008', '88.888.888/0001-88', 'Clínica Bem Cuidar', '1130008000', 'bc@clin.com', '66677788899', 'Laura Mendes', 'senha8', 'Standard'),
('100009', '99.999.999/0001-99', 'Hospital Horizonte', '1130009000', 'hh@hosp.com', '77788899900', 'Thiago Costa', 'senha9', 'Premium'),
('100010', '12.345.678/0001-10', 'Hospital Clemente', '11998770001', 'hc@hosp.com', '10101010101', 'Julia Lopes', 'senha10', 'Standard'),
('100011', '98.765.432/0001-98', 'Hospital Sol Nascente', '11988776655', 'sol@hosp.com', '12121212121', 'Gabriel Reis', 'senha11', 'Plus'),
('100012', '23.456.789/0001-23', 'Hospital Bela Vista', '11933554422', 'bv@hosp.com', '13131313131', 'Fernanda Rocha', 'senha12', 'Premium'),
('100013', '32.165.497/0001-32', 'Hospital São Miguel', '11900221144', 'sm@hosp.com', '14141414141', 'Davi Azevedo', 'senha13', 'Standard'),
('100014', '65.498.321/0001-65', 'Clínica Nova Saúde', '11954871233', 'ns@clin.com', '15151515151', 'Camila Prado', 'senha14', 'Plus'),
('100015', '54.621.987/0001-54', 'Hospital Aliança', '1133002299', 'alianca@hosp.com', '16161616161', 'Pedro Martins', 'senha15', 'Premium');

-- Criar tabela usuario
CREATE TABLE usuario (
    ID_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    cnpj VARCHAR(18) NULL,
    cpf VARCHAR(11),
    cargo VARCHAR(100),
    endereco VARCHAR(100),
    login VARCHAR(100),
    senha VARCHAR(100),
    ID_hospital INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, ## data conforme vai entrando no sistema 
    FOREIGN KEY (ID_hospital) REFERENCES Hospitais(ID_hospital)
);

INSERT INTO usuario (nome, email, cnpj, cpf, cargo, endereco, login, senha, ID_hospital) VALUES
('Marina Torres', 'marina@saude.com', NULL, '11122233344', 'Enfermeira', 'Rua Azul 100', 'marinaT', '123', 1),
('João Silva', 'joao@hosp.com', NULL, '22233344455', 'Médico', 'Av Verde 200', 'joaos', 'abc', 2),
('Lucas Santos', 'lucas@hosp.com', '11.222.333/0001-99', NULL, 'Fornecedor', 'Rua Ypê 21', 'lucasFornecedor', 'senha', 3),
('Ana Paula', 'ana@hosp.com', NULL, '33344455566', 'Recepção', 'Av Laranja 231', 'anaPaula', 'senha', 4),
('Fernanda Lima', 'fernanda@hosp.com', NULL, '44455566677', 'Farmacêutica', 'Rua Rosa 77', 'fLima', 'senha', 5),
('Rafael Souza', 'rafael@hosp.com', NULL, '55566677788', 'TI', 'Rua A 90', 'rafaTI', 'senha', 1),
('Juliana Alves', 'juliana@hosp.com', NULL, '66677788899', 'Médica', 'Av B 102', 'juA', 'senha', 2),
('Carlos Pinto', 'carlos@hosp.com', NULL, '77788899900', 'Segurança', 'Praça 45', 'carlin', 'senha', 3),
('Patrícia Moraes', 'patricia@hosp.com', NULL, '88899900011', 'Nutricionista', 'Rua C 66', 'paty', 'senha', 4),
('Marcelo Oliveira', 'marcelo@hosp.com', NULL, '99900011122', 'Enfermeiro', 'Rua D 12', 'marceloO', 'senha', 5),
('Bruna Vasconcelos', 'bruna@hosp.com', NULL, '10111213141', 'Farmácia', 'Av XPTO 91', 'bruV', 'senha', 6),
('Diego Fernandes', 'diego@hosp.com', '77.888.999/0001-66', NULL, 'Fornecedor', 'Rua M 87', 'diegoForn', 'senha', 7),
('Marcos André', 'marcos@hosp.com', NULL, '12131415161', 'RH', 'Rua Alfa 101', 'marcosRH', 'senha', 8),
('Fernanda Souza', 'fersouza@hosp.com', NULL, '13141516171', 'TI', 'Rua Beta 209', 'fernandaTI', 'senha', 9),
('Vitor Hugo', 'vitor@hosp.com', NULL, '14151617181', 'Admin', 'Rua Gama 56', 'vitorAdmin', 'senha', 10);


CREATE TABLE fornecedor (
    ID_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    cnpj VARCHAR(18),
    cpf VARCHAR(11),
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO fornecedor (nome, cnpj, cpf, email, telefone, endereco) VALUES
('BioMed Distribuidora', '10.111.222/0001-10', NULL, 'bio@med.com', '1130010010', 'Rua X 12'),
('Hospital Supply', '11.111.111/0001-11', NULL, 'hs@supp.com', '1130020020', 'Rua Y 33'),
('MedPrime', '22.222.222/0001-22', NULL, 'medprime@forn.com', '1130030030', 'Rua Z 44'),
('Casa da Saúde', NULL, '12345678901', 'saude@casa.com', '11988990011', 'Av A 55'),
('FarmaBrás', '33.333.333/0001-33', NULL, 'farmabras@forn.com', '1130040040', 'Av B 66'),
('PharmaPlus', '44.444.444/0001-44', NULL, 'pl@pharma.com', '1130050050', 'Rua C 77'),
('Vida Farma', NULL, '98765432100', 'vidafarma@forn.com', '11988776655', 'Rua D 88'),
('AlphaMedic', '55.555.555/0001-55', NULL, 'alpha@med.com', '1130060060', 'Rua E 99'),
('CleanHosp', '66.666.666/0001-66', NULL, 'clean@hosp.com', '1130070070', 'Rua F 11'),
('ProMedic', '77.777.777/0001-77', NULL, 'pro@medic.com', '1130080080', 'Rua G 22'),
('SafeDistribuidora', '88.888.888/0001-88', NULL, 'safe@dist.com', '1130090090', 'Rua H 33'),
('MasterMed', '99.999.999/0001-99', NULL, 'master@med.com', '11933112200', 'Rua I 44'),
('BioPlus', '12.345.678/0001-10', NULL, 'bio@plus.com', '11944556677', 'Rua J 55'),
('Hospital Clean', NULL, '10293847566', 'clean@hc.com', '11955667788', 'Rua K 66'),
('FarmaGold', '98.765.432/0001-90', NULL, 'gold@farma.com', '11966778899', 'Rua L 77');

CREATE TABLE produto (
    ID_produto INT PRIMARY KEY AUTO_INCREMENT,
    sku VARCHAR(100) UNIQUE,
    descricao VARCHAR(200) NOT NULL,
    quantidade INT DEFAULT 0,
    tipo VARCHAR(100),
    data_compra DATE,
    lote VARCHAR(50),
    validade DATE,
    localizacao varchar (100),
    ID_fornecedor INT,
    ID_hospital INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_fornecedor) REFERENCES fornecedor(ID_fornecedor)
        ON DELETE SET NULL ON UPDATE CASCADE, 
    FOREIGN KEY (ID_hospital) REFERENCES Hospitais(ID_hospital)
        ON DELETE SET NULL ON UPDATE CASCADE
);

INSERT INTO produto (sku, descricao, quantidade, tipo, data_compra, lote, validade, localizacao, ID_fornecedor, ID_hospital) VALUES
('SKU001', 'Dipirona 500mg', 100, 'Medicamento', '2025-01-10', 'L001', '2026-01-10', 'Estoque A1', 1, 1),
('SKU002', 'Soro Fisiológico 0,9%', 200, 'Medicamento', '2025-01-12', 'L002', '2027-02-11', 'Estoque A2', 2, 2),
('SKU003', 'Luvas M', 500, 'Descartável', '2025-01-15', 'L003', '2027-03-01', 'Sala 01', 3, 3),
('SKU004', 'Máscara Cirúrgica', 1000, 'Descartável', '2025-01-17', 'L004', '2027-05-31', 'Sala 02', 4, 1),
('SKU005', 'Gaze 7cm', 350, 'Descartável', '2025-01-20', 'L005', '2027-04-15', 'Estoque B1', 5, 2),
('SKU006', 'Álcool 70%', 300, 'Higiene', '2025-01-22', 'L006', '2027-05-21', 'Estoque B2', 6, 3),
('SKU007', 'Amoxicilina 500mg', 120, 'Medicamento', '2025-01-25', 'L007', '2026-07-11', 'Farmácia 01', 1, 4),
('SKU008', 'Omeprazol 20mg', 90, 'Medicamento', '2025-01-27', 'L008', '2026-08-11', 'Farmácia 02', 2, 5),
('SKU009', 'Agulhas 25x7', 400, 'Descartável', '2025-01-29', 'L009', '2027-01-19', 'Sala 03', 3, 6),
('SKU010', 'Seringas 5ml', 800, 'Descartável', '2025-02-01', 'L010', '2027-03-10', 'Sala 04', 4, 7),
('SKU011', 'Esparadrapo 10cm', 150, 'Material', '2025-02-05', 'L011', '2028-02-05', 'Ala C', 5, 8),
('SKU012', 'Paracetamol 750mg', 130, 'Medicamento', '2025-02-07', 'L012', '2026-03-07', 'Farmácia 03', 6, 9),
('SKU013', 'Termômetro Digital', 40, 'Equipamento', '2025-02-09', 'L013', '2030-01-01', 'Sala Equip', 7, 10),
('SKU014', 'Curativo Transparente', 270, 'Material', '2025-02-12', 'L014', '2027-11-30', 'Ala A', 8, 1),
('SKU015', 'Álcool Gel', 600, 'Higiene', '2025-02-15', 'L015', '2027-06-12', 'Corredor 3', 9, 2);


CREATE TABLE operacoes (
    id_operacao INT PRIMARY KEY AUTO_INCREMENT,
    nome_operacao VARCHAR(100),
    descartar VARCHAR(200),
    quantidade INT,
    unidade VARCHAR(10),
    ID_produto int,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ID_produto) REFERENCES produto (ID_produto)
);

INSERT INTO operacoes (nome_operacao, descartar, quantidade, unidade,ID_produto) VALUES
('Entrada', NULL, 50, 'UN',1),
('Saída', 'Luvas M', 20, 'UN',3),
('Entrada', NULL, 100, 'CX',9),
('Saída','Soro', 15, 'UN',2),
('Saída',  'Máscaras', 30, 'UN',4),
('Entrada', NULL, 200, 'UN',2),
('Entrada', NULL, 90, 'CX',4),
('Saída','Dipirona', 10, 'UN',1),
('Saída','Gaze', 25, 'UN',5),
('Entrada',NULL, 120, 'UN',11),
('Saída', 'Omeprazol', 12, 'UN',8),
('Entrada', NULL, 300, 'UN',4),
('Entrada', NULL, 70, 'CX',14),
('Saída', 'Agulhas', 40, 'UN',9),
('Entrada', NULL, 45, 'UN',10);


CREATE TABLE movimentacao (
    id_mov INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    quantidade INT,
    id_operacao INT,
    data_mov DATE,
    status VARCHAR(50),
    FOREIGN KEY (id_produto) REFERENCES produto(ID_produto),
    FOREIGN KEY (ID_operacao) REFERENCES operacoes(ID_operacao)
);

INSERT INTO movimentacao (id_produto, quantidade, id_operacao, data_mov, status) VALUES
(1, 20, 1, '2025-03-01', 'APROVADA'),
(2, 15, 2, '2025-03-02', 'PENDENTE'),
(3, 50, 3, '2025-03-03', 'APROVADA'),
(4, 30, 4, '2025-03-04', 'APROVADA'),
(5, 25, 5, '2025-03-05', 'PENDENTE'),
(6, 90, 6, '2025-03-06', 'APROVADA'),
(7, 60, 7, '2025-03-07', 'APROVADA'),
(8, 10, 8, '2025-03-08', 'APROVADA'),
(9, 40, 9, '2025-03-09', 'PENDENTE'),
(10, 80, 10, '2025-03-10', 'APROVADA'),
(11, 12, 11, '2025-03-11', 'APROVADA'),
(12, 100, 12, '2025-03-12', 'APROVADA'),
(13, 30, 13, '2025-03-13', 'APROVADA'),
(14, 45, 14, '2025-03-14', 'PENDENTE'),
(15, 50, 15, '2025-03-15', 'APROVADA');




