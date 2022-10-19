from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

t = LpVariable("t", 0, None)
s = LpVariable("s", 0, None)
a = LpVariable("a", 0, None)

prob = LpProblem("problem", LpMaximize)

prob += t + s + a <= 100000
prob += s <= .15*t + .03*a

prob += .15*t + .5*s + .16*a

status = prob.solve()
LpStatus[status]

print("Solution")
t = round(value(t),2)
s = round(value(s),2)
a = round(value(a),2)
print("t={}, s={}, a={}".format(t,s,a))
print("Sign Ups = ", round(0.15*t + 0.5*s + 0.16*a,0))