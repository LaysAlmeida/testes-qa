import '@shelex/cypress-allure-plugin'
Cypress.on('uncaught:exception', () => false)

import './commands'