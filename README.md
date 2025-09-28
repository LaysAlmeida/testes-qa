# Test Automation Pack — SWAPI (API) + Drogasil (Web)

Este repositório contém **duas automações de testes** com relatórios **Allure**.  
Os **casos de teste estão na raiz**:

- `TEST_CASES_API.md` — Casos de teste da API (SWAPI)  
- `TEST_CASES_WEB.md` — Casos de teste Web (login Drogasil)  

Projetos incluídos:  
- `swapi-behave/` — Testes de API (Python + Behave + Allure)  
- `drogasil-cypress/` — Testes Web (Cypress + Allure)  

---

## 🚀 Pré-requisitos gerais
- **Java 8+** (necessário para o Allure CLI)  
- **Allure CLI** instalado e disponível no PATH  
  👉 Instalação: [Instruções oficiais](https://allurereport.org/docs/gettingstarted-installation)  
- Internet habilitada (para acessar SWAPI e site Drogasil)  

---

## 1) API — SWAPI (Python + Behave + Allure)
**Pasta:** `swapi-behave`

### Requisitos
- **Python 3.10 ou 3.11** (não usar 3.13, incompatível com dependências atuais)  
- Java 8+ (para o Allure)  

### Instalação
```bash
cd swapi-behave
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
