class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Вставка нового елемента в дерево (для побудови дерева)
def insert(node, key):
    # Якщо дерево порожнє, повертаємо новий вузол
    if node is None:
        return TreeNode(key)
    
    # Інакше йдемо вниз по дереву
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    
    return node

# Функція для знаходження суми всіх значень у дереві
def sum_of_values(node):
    if node is None:
        return 0
    # Сума значень в поточному вузлі, лівому піддереві і правому піддереві
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)

# TEST
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

print("Сума всіх значень у дереві:", sum_of_values(root))
