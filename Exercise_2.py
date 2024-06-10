import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    if x <= 0:
        return 0
    return x

def elu(x, alpha=0.1):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    return x
def excercise2():
    x = input("Input x = ")
    if is_number(x) == False:
        print("x must be a number")
        return
    x = float(x)

    activation_function = input("Input Activation Function (sigmoid|relu|elu): ")
    if activation_function != "sigmoid" and activation_function != "relu" and activation_function != "elu":
        print(f"{activation_function} is not supported")
        return

    if activation_function == "sigmoid":
        print(f"sigmoid: f({x}) = {sigmoid(x)}")

    if activation_function == "relu":
        print(f"relu: f({x}) = {relu(x)}")

    if activation_function == "elu":
        print(f"elu: f({x}) = {elu(x)}")

if __name__ == "__main__":
    excercise2()
    excercise2()
    excercise2()