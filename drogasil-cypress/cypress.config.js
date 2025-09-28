const { defineConfig } = require('cypress')
const allureWriter = require('@shelex/cypress-allure-plugin/writer')

module.exports = defineConfig({
  e2e: {
    baseUrl: process.env.BASE_URL || 'https://beta.stage2.drogasil.com.br',
    setupNodeEvents(on, config) {
      allureWriter(on, config)
      return config
    },
    viewportWidth: 1280, // Default width
    viewportHeight: 800, // Default height
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'cypress/support/e2e.js',
    video: false,
    defaultCommandTimeout: 8000,
    retries: 0
  },
  env: {
    allure: true,
    TEST_CPF: process.env.TEST_CPF || '74316480146',
    TEST_PASSWORD: process.env.TEST_PASSWORD || '123456',
  }
})
