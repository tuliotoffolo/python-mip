import mip

model = mip.Model(solver_name=mip.HIGHS)
solver = model.solver

x = model.add_var(name="x")
y = model.add_var(name="y", lb=5, ub=23, var_type=mip.INTEGER)
z = model.add_var(name="z", var_type=mip.BINARY)

model += x + y == 99
model += x <= 99 * z
model += x + y + z >= 1

# methods
print(f"objective bound: {model.objective_bound}, {solver.get_objective_bound()}")

# internals
print(f"Solver: {solver}")
print(f"Var names: {solver._var_name}")
print(f"Var cols: {solver._var_col}")
print(f"Cons names: {solver._cons_name}")
print(f"Cons cols: {solver._cons_col}")
