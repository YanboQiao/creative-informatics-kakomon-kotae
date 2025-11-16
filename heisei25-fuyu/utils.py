import sympy as sym
from sympy.logic.boolalg import Boolean
sym.init_printing()

def split_formula(formula: str) -> list[str]:
    kotae: list[str] = formula.split('+')
    
    return kotae

def get_variables(formula: str) -> list[str]:
    var_set = {ch for ch in formula if 'a' <= ch <= 'z'}
    return sorted(var_set)

def parse_expr(formula: str, var_names: list[str]) -> tuple[Boolean, dict[str, sym.Symbol]]:
    symbols: dict[str, sym.Symbol] = {name: sym.Symbol(name) for name in var_names}
    expr_str = formula.replace('&', ' & ').replace('+', ' | ').replace('!', ' ~ ').replace('(', ' ( ').replace(')', ' ) ')
    expr = sym.simplify(expr_str, locals = symbols)
    return expr, symbols

def get_kai(formula: str) -> list[str]:
    var_names = get_variables(formula)
    if not var_names:
        return []

    expr, symbols = parse_expr(formula, var_names)
    kotae: list[str] = []

    models = sym.satisfiable(expr, all_models=True)

    for model in models:
        parts: list[str] = []
        for name in var_names:
            sym_var = symbols[name]
            val: bool = bool(model.get(sym_var, False))
            parts.append(f"{name}={'true' if val else 'false'}")
        kotae.append(", ".join(parts))

    return kotae

def get_DNF(formula: str) -> str:
    var_names = get_variables(formula)
    if not var_names:
        return []

    expr, symbols = parse_expr(formula, var_names)
    kotae: list[str] = []

    models = sym.satisfiable(expr, all_models=True)

    for model in models:
        parts: list[str] = []
        for name in var_names:
            sym_var = symbols[name]
            val: bool = bool(model.get(sym_var, False))
            parts.append(f"{'' if val else '!'}{name}")
        kotae.append(''.join(parts))

    return ' + '.join(kotae)

def get_CNF(formula: str) -> str:
    var_names = get_variables(formula)
    if not var_names:
        return []

    expr, symbols = parse_expr(formula, var_names)
    kotae: list[str] = []

    models = sym.satisfiable(sym.Not(expr), all_models=True)

    for model in models:
        parts: list[str] = []
        for name in var_names:
            sym_var = symbols[name]
            val: bool = bool(model.get(sym_var, False))
            parts.append(f"!{name}" if val else name)
        kotae.append(f"({'+'.join(parts)})")

    return ' & '.join(kotae)
