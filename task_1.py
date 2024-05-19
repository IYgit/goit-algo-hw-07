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

# Функція для знаходження найбільшого значення в дереві
def find_max(node):
    current = node
    
    # Йдемо вправо, доки не досягнемо кінцевого вузла
    while current.right is not None:
        current = current.right
    
    return current.value

# TEST
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

print("Найбільше значення у дереві:", find_max(root))
