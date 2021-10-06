# 1.
add:int = 50+50
print(add)
add = 100-10
print(add)

# 2.
print(6**6)
print(6^6)
print(6+6+6+6+6+6)

# 3.
hello:str = "Hello World"
print(hello)
hello += " : 10"
print(hello)

# 4.

def mortgageMonth(P, R, M):
    if(P <= M):
        return 1
    return 1+mortgageMonth(P + P*R/12-M, R, M)

def mortgagePayment(P, R, c):
    monthly_payment:float = round(R/12*P/(1-(1+R/12)**(-c)), 2)
    for i in range(c):
        new_p:float = round(P+ P*(R)/12-monthly_payment, 2)
        print("P: %.2f" %P, " Interest Gain: %.2f" %float(P*R/12), " M: %.2f" %monthly_payment, " new P: %.0f" %new_p)
        P = new_p
    return monthly_payment

print("Monthly payment for 103 months $%.2f" %mortgagePayment( 800000, .06, 103))
print("Number of months to pay off $800,000 with monthly payments of $10000: ", mortgageMonth(800000, .06, 10000))