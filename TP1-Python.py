import sympy as sp
from sympy.assumptions import assuming, Q

t = sp.symbols('t', real=True)
s = sp.symbols('s', positive=True)

F = (3 + 4*t)**2
f = sp.Piecewise(
	(sp.exp(t), t < 1),
	(0, t < sp.Rational(3, 2)),
	(1, t >= sp.Rational(3, 2))
)

L_F_separada = sp.apart(sp.laplace_transform(sp.expand(F), t, s, noconds=True), s)

def _es_desigualdad_t(cond, ops):
	return getattr(cond, 'lhs', None) == t and getattr(cond, 'rel_op', None) in ops

def laplace_desde_por_tramos(pw, t, s):
	lb = sp.Integer(0)
	parts = []
	for expr, cond in pw.args:
		if cond == True or _es_desigualdad_t(cond, ('>=', '>')):
			parts.append(sp.integrate(sp.exp(-s*t) * expr, (t, lb, sp.oo)))
			break
		if _es_desigualdad_t(cond, ('<', '<=')):
			ub = sp.simplify(cond.rhs)
			parts.append(sp.integrate(sp.exp(-s*t) * expr, (t, lb, ub)))
			lb = ub
			continue
		parts.append(sp.integrate(sp.exp(-s*t) * sp.Piecewise((expr, cond), (0, True)), (t, 0, sp.oo)))
		break
	return sp.simplify(sp.together(sum(parts)))

with assuming(Q.gt(s, 1)):
	L_f_simplificada = sp.simplify(sp.together(sp.refine(laplace_desde_por_tramos(f, t, s))))
	cortes = [sp.simplify(cond.rhs) for _, cond in f.args if _es_desigualdad_t(cond, ('<', '<='))]
	L_f_mostrar = L_f_simplificada
	if cortes:
		ultimo_corte = cortes[-1]
		expresion_cola = next(
			(expr_i for expr_i, cond_i in f.args
			 if cond_i == True or (_es_desigualdad_t(cond_i, ('>=', '>')) and sp.simplify(cond_i.rhs - ultimo_corte) == 0)),
			None,
		)
		if expresion_cola is not None and t not in expresion_cola.free_symbols:
			termino_cola = expresion_cola * sp.exp(-s*ultimo_corte) / s
			primer_tramo = next(((expr_i, sp.simplify(cond_i.rhs)) for expr_i, cond_i in f.args if _es_desigualdad_t(cond_i, ('<', '<='))), None)
			if primer_tramo is not None:
				expr_inicial, tope_inicial = primer_tramo
				if sp.simplify(expr_inicial - sp.exp(t)) == 0:
					L_f_mostrar = (1 - sp.exp((1 - s)*tope_inicial)) / (s - 1) + termino_cola

print("L{F}(s) =", L_F_separada)
print("L{f}(s) =", L_f_mostrar)
