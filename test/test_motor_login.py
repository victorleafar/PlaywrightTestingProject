from playwright.sync_api import sync_playwright
import pytest
import time
import json
# executa os tezstes e cria reksatirio
# python3 -m pytest --html=retorno.html
#Para gerar test: python3 -m playwright codegen demo.playwright.dev/todomvc

@pytest.fixture(scope="module")
def configuracao():
    # Carregar configurações do arquivo JSON
    with open('config.json') as config_file:
        return json.load(config_file)

def test_abrir_pagina_login(configuracao):
    with sync_playwright() as p:
        login_url = configuracao['site']
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        time.sleep(5)  # Aguarda 5 segundos
        browser.close()

def test_fazer_login_dados_invalidos(configuracao):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(configuracao['site'])
        time.sleep(5) # Aguarda 5 segundos
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victorfake")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("senhafake@123")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_text("Nome de usuário ou senha inválida.").click()
        time.sleep(5) # Aguarda um tempo para o login ser concluído
        browser.close()

def test_fazer_login_dados_validos(configuracao):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(configuracao['site'])
        time.sleep(5) # Aguarda 5 segundos
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(configuracao['usuario'])
        page.get_by_label("Senha").click()
        page.get_by_label("Senha").fill(configuracao['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        time.sleep(5) # Aguarda um tempo para o login ser concluído
        browser.close()

def test_logout(configuracao):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(configuracao['site'])
        time.sleep(5) # Aguarda 5 segundos
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(configuracao['usuario'])
        page.get_by_label("Senha").click()
        page.get_by_label("Senha").fill(configuracao['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("banner").get_by_role("img").nth(1).click()
        page.get_by_role("heading", name="Sair").click()
        time.sleep(5) # Aguarda um tempo para o logout ser concluído
        browser.close()

# Para executar os testes, use pytest com a opção -v para verbosidade
# pytest -v
