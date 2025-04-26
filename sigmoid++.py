#sigmoid ++
# import numpy as np
# import matplotlib.pyplot as plt

# # Define the activation function
# def activation_function(x, alpha=1):
#     return 1 / (1 + np.exp(-alpha * x))

# # Values for x from -10 to 10
# x = np.linspace(-10, 10, 400)

# # Plot for different values of alpha
# plt.figure(figsize=(8, 6))

# for alpha in [0.5, 1, 2]:
#     y = activation_function(x, alpha)
#     plt.plot(x, y, label=f'alpha = {alpha}')

# # Add labels and title
# plt.title('Non-linearity of the Activation Function for Different Alpha Values')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()

# # Show the plot
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define a novel, ultra-complex softmax-inspired activation function
def complex_softmax_activation(x):
    """
    An ultra-complex activation function inspired by softmax.
    Combines elements from softmax, trigonometric functions, exponential growth, and polynomial terms.
    """
    x = np.array(x)
    exp_component = np.exp(x**2 - np.tanh(x) + np.sin(x))
    sum_exp = np.sum(exp_component)
    output = (exp_component / sum_exp) * np.cos(x**3 - np.exp(-x)) + np.sin(np.log1p(np.abs(x)))**2
    return output

# Generate input values
x_vals = np.linspace(-100, 100, 500)
# Evaluate the complex activation function
y_vals = complex_softmax_activation(x_vals)

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Complex Softmax Activation')
plt.title("Ultra-Complex Softmax-Inspired Activation Function")
plt.xlabel("Input")
plt.ylabel("Activation Output")
plt.grid(True)
plt.legend()
plt.show()
