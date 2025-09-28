# Test Automation Pack — SWAPI (API) + Drogasil (Web)

Este repositório contém **duas automações de testes** com relatórios **Allure**.  
Os **casos de teste estão na raiz do projeto**:

- `TEST_CASES_API.md` — Casos de teste da API (SWAPI)  
- `TEST_CASES_WEB.md` — Casos de teste Web (login Drogasil)  

Projetos incluídos:
- `swapi-behave/` — Testes de API (Python + Behave + Allure)  
- `drogasil-cypress/` — Testes Web (Cypress + Allure)  

---

## Pré-requisitos gerais:
- **Java 8+** (necessário para o Allure CLI)  
- **Allure CLI** instalado e disponível no PATH  
  - Docs: https://allurereport.org/docs/gettingstarted-installation  
- Internet habilitada (para acessar SWAPI e o site)  

> Obs.: validar a instalação do Allure com `allure --version`.

---

## 1) API — SWAPI (Python + Behave + Allure)
**Pasta:** `swapi-behave`

### Requisitos
- **Python 3.10 ou 3.11** (evite 3.13)  
- Java 8+ (para o Allure)

### Instalação
```bash
cd swapi-behave
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
````
## 1) Executar os testes e salvar os resultados do Allure
behave -f allure_behave.formatter:AllureFormatter -o allure-results

## 2) Abrir o relatório (modo servidor - abre no navegador)
allure serve allure-results

# (opção alternativa)
# 2a) Gerar estático e abrir
allure generate allure-results -o allure-report --clean
allure open allure-report

## 1) WEB — Drogasil
**Pasta:** `drogasil-cypress`

### Requisitos
- Node.js 18+
- Java 8+ (para o Allure)

### Instalação
```bash
cd drogasil-cypress
npm install
````
#Como executar (headless) + gerar relatório Allure:
# 1) Limpar resultados anteriores
npm run allure:clear

# 2) Rodar testes (headless)
npm run cy:run

# 3) Gerar e abrir o Allure
npm run allure:generate
npm run allure:open

#Como executar (interativo/GUI)
npm run cy:open
