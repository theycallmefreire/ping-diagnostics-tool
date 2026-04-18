@echo off
setlocal

set DATA=%date:~6,4%-%date:~3,2%-%date:~0,2%
set HORA=%time:~0,2%-%time:~3,2%-%time:~6,2%
set HORA=%HORA: =0%

set PASTA=logs_%DATA%_%HORA%
mkdir %PASTA%

echo Iniciando testes de ping...
echo Salvando em: %PASTA%
echo.

start cmd /k "ping google.com -n 10000 > %PASTA%\google.txt 2>&1"
start cmd /k "ping youtube.com -n 10000 > %PASTA%\youtube.txt 2>&1"
start cmd /k "ping cloudflare.com -n 10000 > %PASTA%\cloudflare.txt 2>&1"
start cmd /k "ping uol.com.br -n 10000 > %PASTA%\uol.txt 2>&1"

echo.
echo Testes iniciados! Cada janela está rodando separadamente.
echo Quando terminar, verifique os arquivos dentro da pasta.
pause