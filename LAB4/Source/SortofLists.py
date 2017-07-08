products = input("items please!!")
items = [item for item in products.split(",")]
print(",".join(sorted(list(set(items)))))
