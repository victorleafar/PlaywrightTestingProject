from playwright.sync_api import Playwright, sync_playwright, expect
import re
import pytest
import json


def test_dashboard_acess() -> None:
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
        page.locator("div").filter(has_text=re.compile(r"^Lançamentos$")).get_by_role("img").click()
        page.locator("div").filter(has_text=re.compile(r"^Sem Retorno$")).get_by_role("img").click()
        page.locator("div").filter(has_text=re.compile(r"^Rejeitado$")).get_by_role("img").click()
        page.locator("div").filter(has_text=re.compile(r"^Rejeitado$")).get_by_role("img").click()
        page.locator("div").filter(has_text=re.compile(r"^Processamento$")).get_by_role("img").click()
        page.locator("div").filter(has_text=re.compile(r"^Processamento$")).locator("line").nth(1).click()

def test_dashboard_filtro_novembro2023() -> None:
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
        page.get_by_role("button", name="Filtrar").click()
        page.locator("div").filter(has_text=re.compile(r"^PeríodoEscolha o período$")).locator("svg").click()
        page.get_by_text("Novembro 2023", exact=True).click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()

def test_dashboard_filtro_outubro2023() -> None:
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
        page.get_by_role("button", name="Filtrar").click()
        page.locator("div").filter(has_text=re.compile(r"^PeríodoEscolha o período$")).locator("svg").click()
        page.get_by_text("Outubro 2023", exact=True).click()
        page.get_by_label("Filtrar").get_by_role("button", name="Filtrar").click()

def test_dashboard_filtro_outubro2023() -> None:
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
        page.get_by_role("button", name="Filtrar").click()
        page.locator("div").filter(has_text=re.compile(r"^PeríodoEscolha o período$")).locator("svg").click()
        page.get_by_text("Abril 2023", exact=True).click()
        page.get_by_role("button", name="Limpar Filtro").click()