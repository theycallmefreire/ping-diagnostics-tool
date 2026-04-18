# Teste de Qualidade de Conexão (Ping)

Este é um projeto simples para testar a **qualidade da sua internet**, focando em identificar:

- Instabilidade (variação de latência)
- Perda de pacotes
- Picos de resposta (lag)

---

## Como funciona?

O script `teste_ping.bat` envia **10.000 pings** simultaneamente para 4 serviços conhecidos:

- google.com
- youtube.com
- cloudflare.com
- uol.com.br

Cada teste é salvo em um arquivo `.txt` separado, permitindo comparar os resultados depois.

---

## Exemplo:

Na pasta `exemplo` tem um teste que eu fiz do meu computador aonde você pode ver como vai ficar o seu. Também tem o arquivo `ping.py` que basicamente cria um grafico com os dados pra você ver a latência melhor.

Gráfico do exemplo:
<img width="1814" height="887" alt="image" src="https://github.com/user-attachments/assets/25e2cac4-f761-476b-931f-5f5c87de5657" />

---

## Dica

Para um teste mais preciso:
- use cabo de rede ao invés de Wi-Fi
- evite downloads durante o teste
- rode em horários diferentes para comparar
