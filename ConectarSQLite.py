#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exemplo de CRUD com Python 3 e SQLite3"""

import sqlite3


class ConectarDB:

    def __init__(self):
       
        self.con = sqlite3.connect('db.sqlite3')

        self.cur = self.con.cursor()

        self.criar_tabela()

    def criar_tabela(self):
    
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS funcionario (
             
                nome TEXT NOT NULL,
                Data TEXT NOT NULL,
                salary REAL(10,2) NOT NULL)''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def inserir_registro(self, usuario):
       
        try:
            self.cur.execute(
                '''INSERT INTO funcionario VALUES (?, ?, ?)''', usuario)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
           
            self.con.rollback()
        else:
        
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_varios_registros(self, usuarios):
        try:
            self.cur.executemany(
                '''INSERT INTO funcionario VALUES (?, ?, ?)''', usuarios)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registro_pela_id(self, rowid):
       
        return self.cur.execute('''SELECT * FROM funcionario WHERE rowid=?''', (rowid,)).fetchone()

    def consultar_registros(self, limit=10):
       
        return self.cur.execute('''SELECT * FROM funcionario LIMIT ?''', (limit,)).fetchall()

    def alterar_registro(self, rowid, nome, sexo):
        
        try:
            self.cur.execute(
                '''UPDATE funcionario SET nome=?, sexo=? WHERE rowid=?''', (nome, sexo, rowid))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_registro(self, rowid):
      
        try:
            self.cur.execute(
                f'''DELETE FROM funcionario WHERE rowid=?''', (rowid,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')


if __name__ == '__main__':
    # Dados
    usuario = ('Aguinaldo Mulonde','2002-18-2002',123.45)
    usuarios = [('Gelson', '2002-03-2003', 1000.34), ('Pedro', '1995-02-25', 20.34)]

    # Criando a conexão com o banco.
    banco = ConectarDB()

    # Inserindo um registro tabela.
    banco.inserir_registro(usuario=usuario)

    # Inserindo vários registros na tabela.
    #banco.inserir_varios_registros(usuarios=usuarios)

    # Consultando com filtro.
    # print(banco.consultar_registro_pela_id(rowid=1))

    # Consultando todos (limit=10).
    # print(banco.consultar_registros())

    # Alterando registro da tabela.
    # Antes da alteração.
    # print(banco.consultar_registro_pela_id(rowid=1))
    # Realizando a alteração.
    # banco.alterar_registro(rowid=1, nome='Rafaela', sexo='Feminino')
    # Depois da alteração.
    # print(banco.consultar_registro_pela_id(rowid=1))

    # Removendo registro da tabela.
    # Antes da remoção.
    # print(banco.consultar_registros())
    # Realizando a remoção.
    # banco.remover_registro(rowid=1)
    # Depois da remoção.
    # print(banco.consultar_registros())
