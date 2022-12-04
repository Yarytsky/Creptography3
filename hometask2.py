from ECurve import ECurve, ECPoint
# За потребності можна зробити запит на ввід з клавіатури, але це тест, щоб ви могли зразу запустити

curve = ECurve(3, 4)

J = curve.BasePointGGet()
J.PrintECPoint()

Y = 2
T = 5

V_Y = G.ScalarMult(Y)
V_T = G.ScalarMult(T)

TOY = V_Y.ScalarMult(T)
YOT = V_T.ScalarMult(Y)

TOY.PrintECPoint()
YOT.PrintECPoint()

print(TOY.ECPointToString() == TOY.ECPointToString())