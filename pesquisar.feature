
@pesquisa_correios

Feature: pesquisa_nome
Scenario Outline: Validar pesquisa no site dos Correios
  Given que eu estou no site "<nome_site>"
  When eu inserir o nome "<pesquisador>"
  Then clico no botão de pesquisar
  Then é apresentado o resultado da pesquisa "<pesquisador>"

Examples:
  | nome_site                           | pesquisador        |
  | http://www.buscacep.correios.com.br | 69082-640          |
  | http://www.buscacep.correios.com.br | Instituto Creathus |
