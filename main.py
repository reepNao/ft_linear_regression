import matplotlib.pyplot as plt
import pandas as pd
import os


def save_thetas(df_path):
    if not os.path.exists(df_path):
        with open(df_path, 'w') as f:
            f.write("0.0,0.0")
            return 0.0, 0.0
    else:
        with open(df_path, 'r') as f:
            line = f.readline()
            theta0, theta1 = line.split(',')
            return float(theta0), float(theta1)

def validate_km(km):
    if km is None:
        print("Invalid input")
        return False
    if not isinstance(km, int):
        print("KM must be an integer")
        return False
    if km < 0:
        print("KM must be a positive integer")
        return False
    if km > 240000:
        print("KM must be less than 240000")
        return False
    return True

def main():
    try:
        data = input("CSV file path : ")
        df = pd.read_csv(data)
        theta0, theta1 = save_thetas('model.csv')
        km = int(input("KM's: "))
        if not validate_km(km):
            return
        print("Price: ", float(theta0) + float(theta1) * km)
        plt.title('Ft_Linear_Regression')
        plt.xlabel('Km')
        plt.ylabel('Price')
        plt.plot(df.km, df.price)
        plt.scatter(km, float(theta0) + float(theta1) * km, color='red')
        plt.show()
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    main()