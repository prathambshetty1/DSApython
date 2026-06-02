def longest_common_prefix(words):
    if not words:
        return ""
    prefix=words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix=prefix[:-1]
            if prefix =="":
                return ""
    return prefix
print("=== Longest Common Prefix Finder ===")
print("Example Input: flower flow fight")
print("Example input: sun sunrise sunset sunday")
print()
words=input("Enter words separated by spaces: ").split()
result=longest_common_prefix(words)
print("\nWords Entered: ",words)
print("\nLongest Common Prefix: ",result)