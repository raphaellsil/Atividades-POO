class Pessoa:
    def __init__(self, nome, telefone, email, endereco, cpf):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__endereco = endereco
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome=nome

    def get_telefone(self):
        return self.__telefone
    def set_telefone(self, telefone):
        self.__telefone=telefone

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email=email

    def get_endereco(self):
        return self.__endereco
    def set_endereco(self, endereco):
        self.__endereco=endereco

    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf=cpf

class Animal:
    def __init__(self, nome, sexo, peso, especie, raca, data_nascimento):
        self.__nome = nome
        self.__sexo = sexo
        self.__peso = peso
        self.__especie = especie
        self.__raca = raca
        self.__data_nascimento = data_nascimento

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome= nome

    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, sexo):
        self.__sexo= sexo

    def get_especie(self):
        return self.__especie
    def set_especie(self, especie):
        self.__especie= especie

    def get_raca(self):
        return self.__raca
    def set_raca(self, raca):
        self.__raca= raca

    def get_data_nascimento(self):
        return self.__data_nascimento
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento= data_nascimento

class Medico(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf, registro_profissional, especialidade, carga_horaria_semanal):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__registro_profissional = registro_profissional
        self.__especialidade = especialidade
        self.__carga_horaria_semanal = carga_horaria_semanal

    def get_registro_profissional(self):
        return self.__registro_profissional
    def set_registro_profissional(self, registro_profissional):
        self.__registro_profissional= registro_profissional

    def get_especialidade(self):
        return self.__especialidade
    def set_especialidade(self, especialidade):
        self.__especialidade= especialidade

    def get_carga_horaria_semanal(self):
        return self.__carga_horaria_semanal
    def set_carga_horaria_semanal(self, carga_horaria_semanal):
        self.__carga_horaria_semanal= carga_horaria_semanal


class Funcionario(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf, carga_horaria_semanal, sindicalizado, funcao):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__carga_horaria_semanal = carga_horaria_semanal
        self.__sindicalizado = sindicalizado
        self.__funcao = funcao

    def get_carga_horaria_semanal(self):
        return self.__carga_horaria_semanal
    def set_carga_horaria_semanal(self, carga_horaria_semanal):
        self.__carga_horaria_semanal= carga_horaria_semanal


    def get_sindicalizado(self):
        return self.__sindicalizado
    def set_sindicalizado(self, sindicalizado):
        self.__sindicalizado= sindicalizado

    def get_funcao(self):
        return self.__funcao
    def set_funcao(self, funcao):
        self.__funcao= funcao



class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf, animal, status_inadimplencia):
        super().__init__(nome, telefone, email, endereco, cpf)
        self.__animal = animal
        self.__status_inadimplencia = status_inadimplencia

    def get_animal(self):
        return self.__animal
    def set_animal(self, animal):
        self.__animal= animal

    def get_status_inadimplencia(self):
        return self.__status_inadimplencia
    def set_status_inadimplencia(self, status_inadimplencia):
        self.__status_inadimplencia= status_inadimplencia


class Agendamento:
    def __init__(self, data, medico, cliente, funcionario, valor):
        self.__data = data
        self.__medico = medico
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__compareceu = False
        self.__concluido = False
        self.__pago = False
        self.__valor = valor

    def agendar(self):
        return "Agendamento realizado com sucesso"

    def finalizar(self):
        self.__compareceu = True
        self.__concluido = True
        self.__pago = True
        return "Consulta concluída com sucesso"

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data= data

    def get_medico(self):
        return self.__medico
    def set_medico(self, medico):
        self.__medico= medico

    def get_cliente(self):
        return self.__cliente
    def set_cliente(self, cliente):
        self.__cliente= cliente

    def get_funcionario(self):
        return self.__funcionario
    def set_funcionario(self, funcionario):
        self.__funcionario= funcionario

    def get_compareceu(self):
        return self.__compareceu
    def set_funcionario(self, compareceu):
        self.__compareceu= compareceu

    def get_concluido(self):
        return self.__concluido
    def set_concluido(self, concluido):
        self.__concluido= concluido

    def get_pago(self):
        return self.__pago
    def set_pago(self, pago):
        self.__pago= pago

    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor= valor


#Solicitando entrada do usuário
print("=== Cadastro de Animal ===")
animal_nome = input("Nome do animal: ")
animal_sexo = input("Sexo do animal (M/F): ")
animal_peso = float(input("Peso do animal (kg): "))
animal_especie = input("Espécie do animal: ")
animal_raca = input("Raça do animal: ")
animal_data_nascimento = input("Data de nascimento do animal (DD/MM/AAAA): ")
animal = Animal(animal_nome, animal_sexo, animal_peso, animal_especie, animal_raca, animal_data_nascimento)

print("\n=== Cadastro de Cliente ===")
cliente_nome = input("Nome do cliente: ")
cliente_telefone = input("Telefone: ")
cliente_email = input("Email: ")
cliente_endereco = input("Endereço: ")
cliente_cpf = input("CPF: ")
cliente_status = input("Está inadimplente? (S/N): ").strip().upper() == "S"
cliente = Cliente(cliente_nome, cliente_telefone, cliente_email, cliente_endereco, cliente_cpf, animal, cliente_status)

print("\n=== Cadastro de Médico ===")
medico_nome = input("Nome do médico: ")
medico_telefone = input("Telefone: ")
medico_email = input("Email: ")
medico_endereco = input("Endereço: ")
medico_cpf = input("CPF: ")
medico_registro = input("Registro profissional: ")
medico_especialidade = input("Especialidade: ")
medico_carga_horaria = int(input("Carga horária semanal: "))
medico = Medico(medico_nome, medico_telefone, medico_email, medico_endereco, medico_cpf, medico_registro, medico_especialidade, medico_carga_horaria)

print("\n=== Cadastro de Funcionário ===")
funcionario_nome = input("Nome do funcionário: ")
funcionario_telefone = input("Telefone: ")
funcionario_email = input("Email: ")
funcionario_endereco = input("Endereço: ")
funcionario_cpf = input("CPF: ")
funcionario_carga_horaria = int(input("Carga horária semanal: "))
funcionario_sindicalizado = input("Sindicalizado? (S/N): ").strip().upper() == "S"
funcionario_funcao = input("Função: ")
funcionario = Funcionario(funcionario_nome, funcionario_telefone, funcionario_email, funcionario_endereco, funcionario_cpf, funcionario_carga_horaria, funcionario_sindicalizado, funcionario_funcao)

print("\n=== Agendamento da Consulta ===")
data_agendamento = input("Data do agendamento (DD/MM/AAAA): ")
valor_agendamento = float(input("Valor da consulta: "))
agendamento = Agendamento(data_agendamento, medico, cliente, funcionario, valor_agendamento)

print("\n" + agendamento.agendar())

#Finalizando a consulta
input("\nPressione ENTER para finalizar a consulta...")
print(agendamento.finalizar())

#Exibir a mensagem final
print(f"\nO animal de nome {cliente.get_animal().get_nome()}, dono de nome {cliente.get_nome()}, "
      f"concluiu uma consulta com o médico de nome {medico.get_nome()}, "
      f"conforme registrado pelo funcionário de nome {funcionario.get_nome()}.")
