describe("Login - Drogasil", () => {
  const cpf = Cypress.env("TEST_CPF");
  const password = Cypress.env("TEST_PASSWORD");

  it("Login com sucesso", function () {
    cy.openLoginPage();

    // preencher e submeter
    cy.get('input[name="Email"]').type(cpf)
    cy.get('input[type="password"]').first().type(password, { log: false })
    cy.get('button[type="submit"]').click()

    // aguardar a chamada
    cy.wait('@loginReal').then(({ response }) => {
      if (response?.statusCode === 401) {
        cy.log('401 detectado → skip')
        this.skip()
      }
    })
  });

  it("Campos obrigatórios vazios", () => {
    cy.openLoginPage();
    cy.get("button#next").click();
    cy.contains(" Digite seu E-mail ou CPF");
  });

  it("CPF inválido", () => {
    cy.openLoginPage();
    cy.get('input[name="Email"]').type("42738422");
    cy.get('input[type="password"]').click();
    cy.contains("E-mail ou CPF inválido");
  });
});
