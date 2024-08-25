from playwright.sync_api import sync_playwright
import pytest
import time
import re


def test_motor_acessar_servicos():
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
        page.get_by_role("link", name="Serviços").click()
        
def test_motor_servicos_ver_observacao():
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
        page.get_by_role("link", name="Serviços").click()
        page.get_by_role("heading", name="Ver Observação").first.click()
        page.get_by_role("button").nth(1).click()

def test_motor_servicos_rejeitado_tentar_novamente():
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
        page.get_by_role("link", name="Serviços").click()
        page.get_by_role("heading", name="Ver Observação").first.click()
        page.get_by_role("paragraph").locator("svg").nth(1).click()
        page.get_by_text("LESTE PAULISTA", exact=True).click()
        page.get_by_placeholder("Nome do produto").click()
        page.get_by_placeholder("Nome do produto").click()
        page.get_by_placeholder("Nome do produto").fill("A")
        page.get_by_placeholder("Linha na conta de energia").click()
        page.get_by_role("button", name="Tentar novamente").click()
        page.get_by_role("button", name="OK").click()

def test_motor_servicos_ativar_desativar():
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
        page.get_by_role("link", name="Serviços").click()
        page.locator("div").filter(has_text=re.compile(r"^ServiçoPlano RegularValor mensalR\$29,90Código33697$")).get_by_role("switch").click()
        page.locator("div").filter(has_text=re.compile(r"^ServiçoPlano Regular 100Valor mensalR\$29,90Código56981$")).get_by_role("switch").click()
        page.locator("div").filter(has_text=re.compile(r"^ServiçoPlano RegularValor mensalR\$29,90Código33697$")).get_by_role("switch").click()
        page.locator("div").filter(has_text=re.compile(r"^ServiçoPlano Regular 100Valor mensalR\$29,90Código56981$")).get_by_role("switch").click()

def test_motor_servicos_status():
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
        page.get_by_role("link", name="Serviços").click()
        page.get_by_role("heading", name="Aprovado").click()
        page.locator("div").filter(has_text=re.compile(r"^Pendente$")).get_by_role("heading").click()
        page.get_by_role("heading", name="Rejeitado").click()

def test_motor_servicos_cadastrar():
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
        page.get_by_role("link", name="Serviços").click()
        page.locator(".sc-f179a8c2-0 > svg").click()
        page.get_by_role("paragraph").locator("svg").nth(1).click()
        page.get_by_text("LESTE PAULISTA", exact=True).click()
        page.get_by_placeholder("Nome do produto").click()
        page.get_by_placeholder("Nome do produto").click()
        page.get_by_placeholder("Nome do produto").fill("Teste produto qa")
        page.get_by_placeholder("Valor mensal do serviço").click()
        page.get_by_placeholder("Valor mensal do serviço").fill("30")
        page.get_by_role("button", name="Solicitar").click()
        page.get_by_role("button", name="OK").click()

def test_motor_servicos_cadastrar_e_desistir():
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
        page.get_by_role("link", name="Serviços").click()
        page.locator(".sc-f179a8c2-0 > svg").click()
        page.get_by_role("paragraph").locator("svg").nth(1).click()
        page.get_by_role("button").nth(1).click()
        