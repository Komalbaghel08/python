#you're given: `items = ["pen", "pencil", "eraser", "scale", "sharpener"]`
# - Find the index of `"scale"`.
# - Count how many times `"pencil"` appears.
# - Remove `"eraser"`.
# - Show the list.

item = ["pen","pencil","eraser","scale","sharpener"]
print(item.index("scale"))#index of scale
print(item.count("pencil"))
item.remove("eraser")
print(item)