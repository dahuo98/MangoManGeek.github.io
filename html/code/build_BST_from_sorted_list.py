def build(arr, l, r) -> TreeNode:
    if l > r:
        return None
    mid = l + (r - l) // 2
    root = TreeNode(arr[mid])
    root.left = build(arr, l, mid - 1)
    root.right = build(arr, mid+1, r)
    return root