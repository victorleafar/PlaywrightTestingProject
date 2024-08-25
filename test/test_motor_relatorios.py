from playwright.sync_api import sync_playwright
import pytest
import time
import re

#python3 -m playwright codegen demo.playwright.dev/todomvc

def test_motor_acessar_relatorios():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.get_by_role("heading", name="Novo Relatório").click()
        


def test_motor_acessar_relatorios_venda():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.get_by_role("heading", name="Novo Relatório").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Venda", exact=True).click()

def test_motor_acessar_relatorios_cobranca():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Cobrança", exact=True).click()

def test_motor_acessar_relatorios_cobranca_filtros():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Cobrança", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^StatusEscolha o status$")).locator("svg").nth(1).click()
        page.get_by_text("Pago", exact=True).click()
        page.get_by_text("CARTÃO DE TODOS QA", exact=True).click()
        

def test_motor_acessar_relatorios_vendas_filtros():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Venda", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^StatusEscolha o status$")).locator("svg").nth(1).click()
        page.get_by_text("Aprovado", exact=True).click()

def test_motor_acessar_relatorios_vendas_favoritar_venda():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19fgvfq").click()
        page.get_by_text("Venda", exact=True).click()
        page.get_by_role("button", name="Favoritar").click()
        page.get_by_placeholder("Nome do relatório").fill("Favorito")
        page.get_by_role("button", name="Favoritar").click()

def test_motor_acessar_relatorios_vendas_favoritar_cobranca():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19fgvfq").click()
        page.get_by_text("Cobrança", exact=True).click()
        page.get_by_role("button", name="Favoritar").click()
        page.get_by_placeholder("Nome do relatório").fill("Favorito cobran")
        page.get_by_role("button", name="Favoritar").click()

def test_motor_acessar_relatorios_vendas_gerar_cobranca():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Cobrança", exact=True).click()
        page.get_by_role("button", name="Gerar Relatório").click()
        page.get_by_placeholder("Nome do relatório").click()
        page.get_by_placeholder("Nome do relatório").fill("Relatorio 1")
        page.get_by_role("button", name="OK").click()

def test_motor_acessar_relatorios_vendas_gerar_venda():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Venda", exact=True).click()
        page.get_by_role("button", name="Gerar Relatório").click()
        page.get_by_placeholder("Nome do relatório").click()
        page.get_by_placeholder("Nome do relatório").fill("Relatorio 1")
        page.get_by_role("button", name="OK").click()

def test_motor_acessar_relatorios_vendas_baixar():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.get_by_role("link", name="Favoritos").click()
        page.get_by_role("row", name="Favorito cobran 103").get_by_label("", exact=True).check()
        page.get_by_role("button", name="Gerar Relatório").click()
        page.locator(".css-19bb58m").click()
        page.get_by_text("Janeiro 2023", exact=True).click()
        page.get_by_role("button", name="Confirmar").click()
        page.get_by_role("button", name="OK").click()




def test_motor_acessar_relatorios_vendas_excluir_favorito():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()
        page.get_by_role("link", name="Favoritos").click()
        page.get_by_role("row", name="Favorito cobran 102").get_by_role("button").nth(1).click()
        page.get_by_role("button", name="NÃO").click()

def test_motor_acessar_relatorios_vendas_excluir_historico():
    with sync_playwright() as p:
        login_url = "http://auth.dev.mrce.sistematodos.com.br:8080/realms/motor-rce/protocol/openid-connect/auth?client_id=motor-rce-front&scope=openid%20email%20profile&response_type=code&redirect_uri=https%3A%2F%2Fdev.mrce.sistematodos.com.br%2Fapi%2Fauth%2Fcallback%2Fkeycloak&state=3j_5AVqEGUWuPcU8Sh02NqH1TWK78TIHiJC8A-7BXaM&code_challenge=lx4fUtQHkUoeRgjDgVWSv3aadrP-hk7j1iHzrkRZuC4&code_challenge_method=S256"
        browser = p.chromium.launch(headless=False)        
        context = browser.new_context()
        page = context.new_page()
        page.goto(login_url)
        page.get_by_label("Nome de usuário ou e-mail").click()
        page.get_by_label("Nome de usuário ou e-mail").fill("victor.qa")
        page.get_by_label("Nome de usuário ou e-mail").press("Tab")
        page.get_by_label("Senha").fill("Victor001")
        page.get_by_role("button", name="Entrar").click()
        page.get_by_role("button", name="Sign in with Keycloak").click()
        page.get_by_role("link", name="Relatórios").click()       
        page.get_by_role("link", name="Histórico").click()
        page.locator("tr:nth-child(3) > td:nth-child(4) > .sc-8be4d2ec-1").click()
        page.get_by_role("button", name="NÃO").click()
