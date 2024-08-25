from playwright.sync_api import sync_playwright
import re
import pytest
import time
import json

@pytest.fixture(scope="module")
def configuracao():
    # Carregar configurações do arquivo JSON
    with open('config.json') as config_file:
        return json.load(config_file)
    
def test_acessar_clientes() -> None:
    with sync_playwright() as p:
        # Carregar configurações do arquivo JSON
        with open('config.json') as config_file:
            config = json.load(config_file)

        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.locator("div").filter(has_text=re.compile(r"^Nome de usuário ou e-mail$")).click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()


def test_acessar_clientes_filtrar_adimplente() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.locator("div").filter(has_text=re.compile(r"^Nome de usuário ou e-mail$")).click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("heading", name="Filtrar").get_by_role("button").click()
        page.get_by_role("button", name="ADIMPLENTE", exact=True).click()
        page.get_by_role("button", name="ADIMPLENTE", exact=True).click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()

def test_acessar_clientes_filtrar_inadimplente() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.locator("div").filter(has_text=re.compile(r"^Nome de usuário ou e-mail$")).click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("button", name="Filtrar").click()
        page.get_by_role("button", name="INADIMPLENTE").click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()


def test_acessar_clientes_filtrar_pendente() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("button", name="Filtrar").click()
        page.get_by_role("button", name="PENDENTE").click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()


def test_acessar_clientes_limpar_filtro() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("button", name="Filtrar").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("LESTE PAULISTA", exact=True).click()
        page.get_by_label("Filtrar").locator("svg").nth(1).click()
        page.get_by_role("button", name="ADIMPLENTE", exact=True).click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()
        page.get_by_role("button", name="Limpar Filtro").click()


def test_acessar_clientes_paginacao() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_text("2", exact=True).click()
        page.get_by_text("3", exact=True).click()
        page.get_by_text("4").click()
        page.get_by_text("5").click()
        page.get_by_text("6").click()
        page.get_by_text("Primeira").click()
        page.get_by_text("Última").click()

def test_acessar_clientes_dados() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("cell", name="John Doe").click()

def test_acessar_clientes_dados_historico_cobranca() -> None:
    with sync_playwright() as p:
        with open('config.json') as config_file:
            config = json.load(config_file)
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(config['site'])
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill(config['usuario'])
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill(config['senha'])
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Clientes").click()
        page.get_by_role("cell", name="John Doe").click()
        page.get_by_role("button", name="HISTÓRICO DE COBRANÇA").click()
