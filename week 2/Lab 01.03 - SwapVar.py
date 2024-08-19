"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
    """-"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

def main(data):
    """-"""
    var_1, var_2 = data[0], data[1]
    var_1, var_2 = var_2, var_1
    print("(", var_1 if isinstance(var_1, float) else "%.1f" % var_1, ",", end=" ", sep="")
    print(var_2 if isinstance(var_2, float) else "%.1f" % var_2, ")", sep="")

main(convert_string_to_tuples(input()))
