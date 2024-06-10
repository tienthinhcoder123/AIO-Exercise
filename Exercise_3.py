import random
import math

def MAE(loss_name, samples_number):
    mae = 0
    for i in range(samples_number):
        loss = 0
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        loss += abs(target - pred)
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        mae += loss

    print(f"final MAE: {mae / samples_number}")

def MSE(loss_name, samples_number):
    mse = 0
    for i in range(samples_number):
        loss = 0
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        loss += (target - pred) ** 2
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        mse += loss

    print(f"final MSE: {mse / samples_number}")


def RMSE(loss_name, samples_number):
    rmse = 0
    for i in range(samples_number):
        loss = 0
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        loss += (target - pred) ** 2
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
        rmse += loss
        
    print(f"final RMSE: {math.sqrt(rmse / samples_number)}")

def exercise3():
    samples_number = input("Input number of samples (integer number) which are generated: ")
    if not samples_number.isnumeric():
        print("number of samples must be an integer number")
        return
    samples_number = int(samples_number)
    if samples_number <= 0:
        print("number of samples must be positive")
        return

    loss_name = input("Input loss name: ")

    if loss_name == "MSE":
        MSE(loss_name, samples_number)
    if loss_name == "RMSE":
        RMSE(loss_name, samples_number)
    if loss_name == "MAE":
        MAE(loss_name, samples_number)

if __name__ == "__main__":
    exercise3()
    exercise3()
