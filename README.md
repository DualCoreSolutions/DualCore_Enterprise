# 🟢 DualCore Solutions | Enterprise System

Sistema oficial da **DualCore Solutions**, desenvolvido para centralizar a gestão de clientes, solicitações de orçamentos e monitorização de serviços de **Infraestrutura, Python e Automação**.

## 🚀 Sobre o Projeto
Este ecossistema web foi construído com **Django 5.1**, focado em alta performance, segurança de dados e uma interface moderna em *Dark Mode*. O sistema permite a captação de leads qualificados e oferece um painel de controlo personalizado para utilizadores e administradores.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**: Linguagem base para toda a lógica e automação.
* **Django 5.1.4**: Framework web robusto para gestão de rotas, segurança e base de dados.
* **SQLite**: Base de dados leve utilizada para o ambiente de desenvolvimento.
* **HTML5 / CSS3**: Interface customizada com variáveis globais para manutenção facilitada.
* **Python-dotenv**: Gestão segura de chaves de API e configurações sensíveis.

## 📂 Estrutura de Módulos (Apps)
* **`apps.accounts`**: Gere o modelo de utilizador customizado (`CustomUser`), suportando campos adicionais como bio e telefone.
* **`apps.website`**: Interface pública que inclui a página institucional e o motor de captação de orçamentos.
* **`apps.dashboard`**: Centro de comando restrito com níveis de acesso diferenciados para clientes e equipa técnica.

## ⚙️ Como Configurar o Ambiente Local

1. **Clonar o Repositório:**
   ```bash
   git clone [https://github.com/teu-utilizador/dualcore_enterprise.git](https://github.com/teu-utilizador/dualcore_enterprise.git)
   cd dualcore_enterprise