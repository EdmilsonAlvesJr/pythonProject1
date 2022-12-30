
from behave import Given, When, Then
from src.features import functions

@Given("que eu estou na página {nome_site}")
def context.nome_site(context, nome_site: str):
    context.web.get("nome_site")

http://www.buscacep.correios.com.br
69082-640

@When("eu inserir o cep {cep: str}")
def


@Then("clico no botão pesquisar")
@Then("é apresentado o resultado da pesquisa com sucesso")

