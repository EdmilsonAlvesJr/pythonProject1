import str

from playwright.sync_api import sync_playwright


def pesquisa_correios(nome_site: str, pesquisador: str):
    with sync_playwright() as p:
        navegador = p.firefox.launch()
        page = navegador.new_page()
        page.goto(nome_site)
        page.fill('//*[@id="endereco"]', pesquisador)
        page.locator('//*[@id="btn_pesquisar"]').click()
        page.get_by_role("contentinfo", nome=pesquisador)

    # def pesquisa_por_nome(site: str, nome: str):
    #     with sync_playwright() as c:
    #         navegador = c.firefox.launch()
    #         page = navegador.new_page()
    #         page.goto(site)
    #         page.fill('//*[@id="endereco"]', nome)
    #         page.locator('//*[@id="btn_pesquisar"]').click()
    #         page.get_by_role("contentinfo", name= nome)

    # if nome_site = num():
    #     return pesquisa_por_cep

    # if nome_site = string():
    #    return pesquisa_por_nome

    return pesquisa_correios()
