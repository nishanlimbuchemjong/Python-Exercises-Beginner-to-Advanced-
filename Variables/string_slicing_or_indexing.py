"""
Q. Assign a multi-line string to a variable and extract specific lines from it using slicing or indexing.
"""
sentence = "My name is Nishan Limbu."
index = 8
final_index = 15
print(f"Indexing the String index[{index}] from the '{sentence}': {sentence[index]}")
print(f"Slicing the String [{index, final_index}] from the '{sentence}': {sentence[index:final_index]}")
