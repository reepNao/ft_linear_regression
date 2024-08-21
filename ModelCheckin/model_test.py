import numpy as np

def model(X, Theta):
    return X.dot(Theta)

def load_parameters():
    try:
        with open("thetas.json", "r") as json_file:
            data = json.load(json_file)
        return data["theta0"], data["theta1"]
    except Exception as e:
        print(f"Failed to load thetas.json: {e}")
        sys.exit(-1)

def estimate_price(mileage):
    theta0, theta1 = load_parameters()
    # Normalize mileage for consistent results
    normalized_mileage = (mileage - 22899) / (240000 - 22899)
    return theta0 + theta1 * normalized_mileage

# Test the model
mileage_samples = [240000, 139800, 150500, 185530, 176000, 114800, 166800]
for mileage in mileage_samples:
    print(f"Estimated price for mileage {mileage}: {estimate_price(mileage)}")
