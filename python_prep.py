# Copyright 2021 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def exercise_1(S):


    sum_ = 0
    for i in range(6):
        sum_ += i
        if sum_ is not None:
            print(sum_)
    else:
# no need for else: really if it doesn't contain anything useful
        pass
    return sum_


# TODO: Add up the numbers in S using a for-loop and return the sum.


def exercise_2(S):

# TODO: Add up the numbers in S in 2 lines or less and return the sum.

    return sum (S)

#def exercise_3():
# TODO: Build a dictionary with:
# - keys: tuple of points (x, y)
# - values: value of function f = 8x + 3y
def create_function_dictionary(points):

    function_dict = {}
    for point in points:
        x, y = point
        function_value = 8*x + 3*y
        function_dict[point] = function_value

    return function_dict

# List of points
points_list = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

# Create the function dictionary
function_dictionary = create_function_dictionary(points_list)

# Print the resulting dictionary
for point, value in function_dictionary.items():
    print(f"Point: {point}, Value: {value}")





# ------- Main program -------
if __name__ == "__main__":

    S = [1, 2, 3, 4, 5]

print("\nExercise 1:")
ex_sum = exercise_1(S)
print("\tSum:", ex_sum)

print("\nExercise 2:")
ex_sum = exercise_2(S)
print("\tSum:", ex_sum)

#print("\nExercise 3:")
#exercise_3()
# for key, val in f.items():
# print("\tInput:", key, "Output:", val)
