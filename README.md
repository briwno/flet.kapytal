# 💰 Kapytal

> **Gestão financeira pessoal e para pequenos empreendedores, com foco em simplicidade e organização.**  
> Desenvolvido com [Flet](https://flet.dev/) + Python, com um design moderno e acessível.

## 📱 Sobre o Projeto

O **Kapytal** é um aplicativo de gestão financeira que busca ajudar pessoas e pequenos negócios a organizarem suas finanças de forma prática e intuitiva. A proposta surgiu como parte de um projeto acadêmico da faculdade, com o objetivo de desenvolver um app funcional com tecnologias acessíveis e sem o uso de inteligência artificial.

### ✨ Funcionalidades (Planejadas)

- Cadastro e login de usuários
- Registro de receitas e despesas
- Comparação de preços
- Sugestões financeiras básicas
- Acompanhamento de saldo e histórico
- Interface moderna em Flet (Python)
- Design inspirado em tons **branco**, **preto** e **dourado**

> **Obs:** O projeto ainda está em desenvolvimento. As funcionalidades serão implementadas por etapas.

## 🧱 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flet](https://flet.dev/) (UI)
- [MySQL](https://www.mysql.com/) *(planejado para o backend)*
- Figma *(para o protótipo de interface)*
## 🌐 API Utilizada

O projeto utiliza a API da [Financial Modeling Prep](https://financialmodelingprep.com/) para obter dados financeiros em tempo real.  

### Endpoint Integrado

- **Endpoint:** `https://financialmodelingprep.com/stable/quote?symbol=BTCUSD&apikey=api_key`  
- **Descrição:** Retorna informações atualizadas sobre o preço do Bitcoin (BTC) em relação ao dólar americano (USD).  

## 🛠 Como Rodar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/briwno/flet.kapytal.git
cd flet.kapytal
```

2. Instale as dependências:

```bash
pip install flet
```

3. Rode o projeto:

```bash
flet main.py
```

> **Requisitos:** Python 3.10+

## 🧑‍🎓 Sobre o Desenvolvedor

Desenvolvido por **[briwno](https://github.com/briwno)** como parte de um projeto acadêmico na [Unifacear](https://www.unifacear.edu.br/).

## 📌 Status do Projeto

🚧 **Em desenvolvimento**  
Atualmente, estou focando na construção da interface e estrutura das telas antes da integração com banco de dados e autenticação de usuários.
