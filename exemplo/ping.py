import re
import matplotlib.pyplot as plt

arquivos = {
    "google": "google.txt",
    "youtube": "youtube.txt",
    "uol": "uol.txt",
    "cloudflare": "cloudflare.txt"
}

dados = {}

for nome, arquivo in arquivos.items():
    tempos = []
    with open(arquivo, 'r', encoding='utf-8', errors='ignore') as f:
        for linha in f:
            if "tempo=" in linha:
                match = re.search(r"tempo=(\d+)ms", linha)
                if match:
                    tempos.append(int(match.group(1)))
            elif "Esgotado" in linha:
                tempos.append(None)
    dados[nome] = tempos[:200]  # limita pra visualização

plt.figure()

for nome, tempos in dados.items():
    y = [t if t is not None else float('nan') for t in tempos]
    plt.plot(y, label=nome)

plt.title("Latência da Internet (ms ao longo do tempo)")
plt.xlabel("Número do ping")
plt.ylabel("Tempo (ms)")
plt.legend()

plt.show()