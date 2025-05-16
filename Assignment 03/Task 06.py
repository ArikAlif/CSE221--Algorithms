N = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

def postorder_converter(inorder, preorder):
    if not inorder:
        return []
    root = preorder[0]
    r_ind= inorder.index(root)

    post_left = postorder_converter(inorder[:r_ind], preorder[1:r_ind+1])
    post_right = postorder_converter(inorder[r_ind+1:], preorder[r_ind+1:])
    
    return post_left + post_right + [root]

new = postorder_converter(inorder, preorder)
print(' '.join(map(str, new)))

