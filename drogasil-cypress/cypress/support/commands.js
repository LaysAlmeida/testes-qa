Cypress.Commands.add('openLoginPage', () => {
   cy.visit('/')
    cy.get('[data-qa="header_login"]')
      .click()
    cy.get('[href="/customer/account/login"]')
      .click()
})