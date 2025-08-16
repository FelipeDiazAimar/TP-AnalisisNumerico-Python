from pathlib import Path
import sympy as sp


def main() -> None:
    t, s = sp.symbols('t s')
    F = (3 + 4*t)**2
    L_F_tex = sp.latex(sp.apart(sp.laplace_transform(sp.expand(F), t, s, noconds=True), s))

    f_tex = r"\begin{cases} e^{t}, & 0 \le t < 1 \\ 0, & 1 \le t < \tfrac{3}{2} \\ 1, & t > \tfrac{3}{2} \end{cases}"
    L_f_tex = sp.latex((1 - sp.exp(1 - s))/(s - 1) + sp.exp(-sp.Rational(3, 2)*s)/s)

    # Datos del alumno (editar para la entrega)
    alumno_nombre = "Felipe Diaz Aimar"
    alumno_legajo = "16841"
    alumno_materia = "Análisis Numérico"
    alumno_comision = "Comisión K"
    autor_tex = (
        f"Nombre: {alumno_nombre} \\\\"
        f"Legajo: {alumno_legajo} \\\\"
        f"Materia: {alumno_materia} \\\\"
        f"Comisión: {alumno_comision}"
    )

    doc = rf"""
\documentclass[12pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
\usepackage{{amsmath,amssymb}}
\usepackage[spanish]{{babel}}
\usepackage{{hyperref}}
	\title{{TP1 - Transformadas de Laplace}}
\author{{{autor_tex}}}
\date{{\today}}

\begin{{document}}
\maketitle

\section*{{Ejercicio 1}}
Sea $F(t) = {sp.latex(F)}$. Su transformada de Laplace es
\[
\mathcal{{L}}[F(t)](s) = {L_F_tex}
\]

\section*{{Ejercicio 2}}
Sea $f(t) = {f_tex}$. Su transformada de Laplace es
\[
\mathcal{{L}}[f(t)](s) = {L_f_tex}
\]

\section*{{Compilación alternativa (Overleaf)}}
Si no cuenta con latexmk/MiKTeX/TeX Live en su equipo, puede compilar este informe en línea:
\begin{{enumerate}}
    \item Visite \href{{https://www.overleaf.com}}{{Overleaf}}.
    \item Cree un proyecto en blanco (Blank Project).
    \item Copie y pegue el contenido de este archivo (laplace\_report.tex) en el editor de Overleaf y presione compilar.
\end{{enumerate}}
\end{{document}}
"""

    Path(__file__).with_name("laplace_report.tex").write_text(doc, encoding="utf-8")
    print("Archivo LaTeX generado: laplace_report.tex")


if __name__ == "__main__":
    main()
