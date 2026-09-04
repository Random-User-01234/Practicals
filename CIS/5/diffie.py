P = 29
G = 3

print("The Value of N is: %d" % P)
print("The Value of G is: %d" % G)

a = 4
print("Secret number for Ram is: %d" % a)
X = pow(G,a,P)

b = 8
print("Secret number for Sham is: %d" % b)
y = pow(G,b,P)

Ka = pow(y,a,P)
Kb = pow(X,b,P)

print("Secret key for Ram is: %d" % Ka)
print("Secret key for Sham is: %d" % Kb)

