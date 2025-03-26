<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Clínica Veterinária</title>
    <link rel="stylesheet" href="pessoa2.css">
</head>
<body>
    <div class="container">
        <h1>Sistema de Clínica Veterinária</h1>
        
        <form action="/processar_consulta" method="post">
            <div class="section">
                <h2>Cadastro de Animal</h2>
                <div class="form-group">
                    <label for="animal_nome">Nome do animal:</label>
                    <input type="text" id="animal_nome" name="animal_nome" required>
                </div>
                <div class="form-group">
                    <label for="animal_sexo">Sexo do animal:</label>
                    <select id="animal_sexo" name="animal_sexo" required>
                        <option value="M">Macho</option>
                        <option value="F">Fêmea</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="animal_peso">Peso do animal (kg):</label>
                    <input type="number" id="animal_peso" name="animal_peso" step="0.1" required>
                </div>
                <!-- Continue com os outros campos do animal... -->
            </div>

            <!-- Seções de Cliente, Médico e Funcionário (todos dentro do mesmo formulário) -->

            <div class="section">
                <h2>Agendamento da Consulta</h2>
                <div class="form-group">
                    <label for="data_agendamento">Data do agendamento:</label>
                    <input type="date" id="data_agendamento" name="data_agendamento" required>
                </div>
                <div class="form-group">
                    <label for="valor_agendamento">Valor da consulta:</label>
                    <input type="number" id="valor_agendamento" name="valor_agendamento" step="0.01" required>
                </div>
            </div>

            <div class="flex-buttons">
                <button type="submit" name="action" value="agendar">Agendar Consulta</button>
                <button type="submit" name="action" value="finalizar">Finalizar Consulta</button>
            </div>
        </form>
    </div>
</body>
</html>