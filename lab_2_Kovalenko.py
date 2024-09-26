print("Programming" + "***" + "Essentials" + "***" + "in" + "***Python")

print("    *    ")
print("   * *   ")
print("  *   *  ")
print(" *     * ")
print("***   ***")
print("  *   *  ")
print("  *   *  ")
print("  *   *  ")
print("  *****  ")

print("I'm student")

print('"I\'m"\n\"\"learning\"\"\n\"\"\"Python\"\"\"')

def octal_to_decimal(octal_num):
    decimal_num = int(octal_num, 8)
    return decimal_num
octal_num = "500"
decimal_num = octal_to_decimal(octal_num)
print(f"The decimal equivalent of {octal_num} is {decimal_num}")

def hex_to_decimal(hex_num):
    decimal_num = int(hex_num, 16)
    return decimal_num
hex_num = "777"
decimal_num = hex_to_decimal(hex_num)
print(f"The decimal equivalent of {hex_num} is {decimal_num}")