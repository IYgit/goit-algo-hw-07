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

# Функція для знаходження найменшого значення в дереві
def find_min(node):
    current = node
    
    # Йдемо вліво, доки не досягнемо кінцевого вузла
    while current.left is not None:
        current = current.left
    
    return current.value

# Приклад використання
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

print("Найменше значення у дереві:", find_min(root))
