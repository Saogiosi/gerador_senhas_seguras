# Projeto - Gerador de Senhas Seguras
## Descrição do Projeto
O Gerador de Senhas Seguras é uma aplicação web desenvolvida em Python utilizando o framework Flask, com o objetivo de gerar senhas fortes e personalizadas de forma rápida, simples e segura.
O sistema permite que o usuário selecione os critérios desejados para a senha, como:
- Inclusão de caracteres especiais
- Inclusão de números
- Letras minúsculas
- Letras maiúsculas
- Definição da quantidade de dígitos (mínimo de 4 e máximo de 20)
Além disso, a aplicação possui a funcionalidade de copiar a senha gerada com apenas um clique, proporcionando melhor usabilidade e praticidade.
O projeto foi desenvolvido como atividade acadêmica de pós-graduação, com foco em desenvolvimento web, automação de testes e boas práticas de QA (Quality Assurance).
---
## Objetivo do Projeto
Desenvolver uma aplicação funcional para geração de senhas seguras e aplicar conceitos de:
- Desenvolvimento Back-end com Python
- Desenvolvimento Front-end com HTML, CSS e JavaScript
- Integração entre Front-end e Back-end
- Automação de testes com Selenium e Pytest
- Validação de regras de negócio
- Estruturação de projeto profissional
- Versionamento com Git e GitHub
---
## Funcionalidades
### Geração de senha personalizada
O usuário pode selecionar os tipos de caracteres que deseja incluir:
- Caracteres especiais
- Números
- Letras minúsculas
- Letras maiúsculas
### Controle de quantidade de caracteres
Permite definir o tamanho da senha com validação entre:
- Mínimo: 4 caracteres
- Máximo: 20 caracteres
### Botão Gerar
Responsável por processar as seleções do usuário e gerar uma senha segura com base nas regras definidas.
### Botão Copiar Senha
Permite copiar automaticamente a senha gerada para a área de transferência.
### Validações implementadas
- Não permite gerar senha sem selecionar ao menos uma opção
- Não permite quantidade inferior a 4
- Não permite quantidade superior a 20
---
## Tecnologias Utilizadas
### Back-end
- Python 3
- Flask
### Front-end
- HTML5
- CSS3
- JavaScript
### Automação de Testes
- Selenium WebDriver
- Pytest
### Controle de versão
- Git
- GitHub
### Ambiente de Desenvolvimento
- Visual Studio Code (VS Code)
---
## Estrutura do Projeto
## Estrutura do Projeto
```text
GERADOR_SENHAS_SEGURAS/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── Test/
│   └── test_gerador_senhas.py
│
├── app.py
├── requirements.txt
└── README.md
```
---
## Casos de Teste Automatizados
Foram implementados testes automatizados para validação das principais funcionalidades do sistema:
### Testes realizados
- Validar geração de senha com números
- Validar geração com caracteres especiais
- Validar mínimo de 4 dígitos
- Validar máximo de 20 dígitos
- Validar ausência de checkbox selecionado
- Validar funcionalidade do botão copiar senha
Esses testes garantem maior confiabilidade, qualidade e estabilidade da aplicação.
---
## Como Executar o Projeto
### 1. Clonar o repositório
bash git clone URL_DO_REPOSITORIO 
---
### 2. Acessar a pasta do projeto
bash cd GERADOR_SENHAS_SEGURAS 
---
### 3. Instalar as dependências
bash pip install -r requirements.txt 
---
### 4. Executar a aplicação
bash python app.py 
---
### 5. Abrir no navegador
text http://127.0.0.1:5000 
---
## Como Executar os Testes Automatizados
### 1. Manter a aplicação Flask em execução
bash python app.py 
---
### 2. Abrir um novo terminal
### 3. Executar os testes com Pytest
bash pytest Test/test_gerador_senhas.py -v 
---
## Resultado Esperado
Todos os testes devem retornar como:
text PASSED 
Isso indica que a aplicação está funcionando corretamente e validada.
---
## Melhorias Futuras
Como evolução do projeto, podem ser implementadas:
- Histórico de senhas geradas
- Login e autenticação de usuário
- Integração com banco de dados
- Deploy em nuvem
- Responsividade mobile
- Exportação de senhas
- Dashboard administrativo
- Relatórios automatizados de testes
---
## Autor
Giovani Jeronimo da Silva
Testador de Software Jr
---
## Licença
Este projeto está sob a licença MIT.

*NOTA:* Este projeto foi desenvolvido com foco em aprendizado na aplicação de Inteligência Artificial Generativa, especialmente no contexto de criação de testes e melhoria da qualidade de software.
