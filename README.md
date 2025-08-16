# TP1 – Transformadas de Laplace (SymPy)

Este trabajo práctico contiene dos ejercicios de transformadas de Laplace y un generador de informe en LaTeX.

- Cálculo simbólico y salida por consola: `TP1-Python.py`
- Generación de informe LaTeX: `export_latex.py` → produce `laplace_report.tex`

## Requisitos
- Windows con PowerShell
- Python 3.10+ (probado con 3.13)
- Pip (incluido en Python)
- LaTeX para compilar el PDF (opcional): MiKTeX o TeX Live, y latexmk recomendado

Paquetes Python:
- sympy

Puedes instalar desde `requirements.txt`.

## Instalación (PowerShell)
En la carpeta del proyecto:

```powershell
# 1) Crear entorno virtual (opcional pero recomendado)
py -3 -m venv .venv  # o: python -m venv .venv

# 2) Activar el entorno
.\.venv\Scripts\Activate.ps1

# 3) Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Cómo ejecutar
- Cálculos y salida en consola (Ej.1 y Ej.2):

```powershell
python TP1-Python.py
```

- Generar archivo LaTeX del informe (`laplace_report.tex`):

```powershell
python export_latex.py
```

El archivo `laplace_report.tex` queda en la misma carpeta.

### Ejecutar todo con doble clic (opcional)
- Usa `run_todo.bat` para:
  - Activar el entorno (si existe), instalar dependencias si falta SymPy,
  - Ejecutar `TP1-Python.py`,
  - Ejecutar `export_latex.py`,
  - Compilar a PDF con `latexmk` si está disponible.
  - Solo haz doble clic en `run_todo.bat`.

## Compilar el informe a PDF (opcional)
- Con VS Code + LaTeX Workshop: abre `laplace_report.tex` y usa “Build LaTeX project”.
- Con latexmk (si está instalado en el sistema):

```powershell
latexmk -pdf laplace_report.tex
```

El PDF resultante puede ser `laplace_report.pdf`.

## Resultados esperados (consola)
- Ejercicio 1:
  - L{F}(s) = 9/s + 24/s**2 + 32/s**3
- Ejercicio 2 (derivado de la función por tramos, sin Heaviside):
  - L{f}(s) = (1 - exp(1 - s))/(s - 1) + exp(-3*s/2)/s

En el informe LaTeX se muestra:
- F(t) = (3 + 4t)^2 y su transformada en forma separada
- f(t) definida por tramos en español y su transformada compacta

## Estructura del proyecto
```
TP1-Python.py        # Cálculo simbólico y salida por consola
export_latex.py      # Genera laplace_report.tex con el informe
laplace_report.tex   # (Generado) Informe LaTeX del TP
requirements.txt     # Dependencias Python
README.md            # Este documento
```

## Entrega sugerida
Incluye al menos:
- `TP1-Python.py`
- `export_latex.py`
- `laplace_report.tex` y el PDF compilado (si corresponde)
- `README.md`
- `requirements.txt`
 - `run_todo.bat` (opcional)

Opcional: agrega “Datos del alumno” en el encabezado del .tex (autor, curso, fecha) si tu cátedra lo requiere.

## Solución de problemas
- “python” no se reconoce: usa `py -3` en lugar de `python`, o verifica que Python esté en el PATH.
- Error al activar `.venv`: habilita scripts de PowerShell (abriendo PowerShell como administrador):
  - `Set-ExecutionPolicy RemoteSigned` (confirma y vuelve a intentar activar el entorno)
- No puedes compilar a PDF: instala MiKTeX/TeX Live y/o usa VS Code con LaTeX Workshop. Alternativamente, sube `laplace_report.tex` a un compilador en línea (Overleaf).

## Notas técnicas
- El cálculo de L{f}(s) se realiza integrando cada tramo de la función `f(t)` (Piecewise), asumiendo s > 1 para evaluar las integrales impropias; luego se muestra una forma canónica equivalente, deducida a partir de los cortes y el valor en la cola (sin fórmulas fijas ni Heaviside en la entrada).
- SymPy simplifica automáticamente la transformada de F(t) en forma separada con `apart`.
