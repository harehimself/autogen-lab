# Import the AutoGen framework
from autogen import AutoGen

# Create an instance of the AutoGen class
auto_gen = AutoGen()


# Define a function to be tested
def add(a, b):
    return a + b


# Register the function with AutoGen
auto_gen.register_function(add)

# Define test cases
test_cases = [
    {"input": (1, 2), "expected_output": 3},
    {"input": (-1, -1), "expected_output": -2},
    {"input": (0, 0), "expected_output": 0},
]

# Add test cases to the AutoGen instance
for test in test_cases:
    auto_gen.add_test_case(add, test["input"], test["expected_output"])

# Run the tests
auto_gen.run_tests()
