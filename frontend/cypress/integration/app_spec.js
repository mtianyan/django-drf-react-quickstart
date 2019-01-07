describe("Django REST framework / React quickstart app", () => {
  const lead = {
    name: "mtianyan",
    email: "1147727180@qq.com",
    message: "I am a happy pythoner"
  };
  before(() => {
    cy.exec("npm run dev");
    cy.exec("npm run flush");
  });
  it("should be able to fill a web form", () => {
    cy.visit("/");
    cy
      .get('input[name="name"]')
      .type(lead.name)
      .should("have.value", lead.name);
    cy
      .get('input[name="email"]')
      .type(lead.email)
      .should("have.value", lead.email);
    cy
      .get('textarea[name="message"]')
      .type(lead.message)
      .should("have.value", lead.message);
    cy.get("form").submit();
  });
  // more tests here
  // insert after the first "it" block in ./cypress/integration/app_spec.js
  it("should be able to see the table", () => {
    cy.visit("/");
    cy.get("tr").contains(`${lead.name}${lead.email}${lead.message}`);
  });
});