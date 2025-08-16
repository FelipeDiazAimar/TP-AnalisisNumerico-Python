@echo off
setlocal

REM Activa el entorno virtual si existe
if exist .venv\Scripts\activate.bat (
  call .venv\Scripts\activate.bat
) else (
  echo [INFO] No se encontro .venv. Usando Python del sistema.
)

REM Instalar dependencias si falta sympy
python -c "import sympy" 2>NUL
if errorlevel 1 (
  echo [INFO] Instalando dependencias...
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
)

REM Ejecutar calculos
python TP1-Python.py || goto :err

REM Generar LaTeX
python export_latex.py || goto :err

REM Compilar a PDF si latexmk esta disponible
where latexmk >NUL 2>&1
if not errorlevel 1 (
  echo [INFO] Compilando PDF con latexmk...
  latexmk -pdf -quiet laplace_report.tex
  if not errorlevel 1 echo [OK] PDF generado.
) else (
  echo [INFO] latexmk no encontrado.
  echo [INFO] Compilacion alternativa ^(Overleaf^):
  echo   1^)^  Ir a https://www.overleaf.com
  echo   2^)^  Crear un proyecto en blanco - Blank Project
  echo   3^)^  Abrir laplace_report.tex y copiar/pegar su contenido en Overleaf, luego compilar
  echo   Nota - el archivo laplace_report.tex ya fue generado en esta carpeta.
)

echo.
echo [OK] Proceso finalizado.
exit /b 0

:err
echo [ERROR] Ocurrio un problema. Revisa la salida anterior.
exit /b 1
