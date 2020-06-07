# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##### O(log n) Solution #######
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        predStack = collections.deque() # less than or equal to target
        succStack = collections.deque() # greater than target
        
        def popSuccStack():
            nonlocal succStack
            if not succStack:
                return None
            curr = succStack.pop()
            temp = curr
            if not temp.right:
                return curr
            else:
                temp = temp.right
                succStack.append(temp)
                while temp.left:
                    temp = temp.left
                    succStack.append(temp)
            return curr
        def popPredStack():
            nonlocal predStack
            if not predStack:
                return None
            curr = predStack.pop()
            temp = curr
            if not temp.left:
                return curr
            else:
                temp = temp.left
                predStack.append(temp)
                while temp.right:
                    temp = temp.right
                    predStack.append(temp)
            return curr
        
        temp = root
        while temp:
            if temp.val == target:
                predStack.append(temp)
                succStack.append(temp)      # when temp is the target, we need to keep only one copy of temp, while 
                popSuccStack()              # we also want to consider temp's succcessor, so we keep the predStack, and append temp's successor
                break                       # to succStack if there is any
            elif target < temp.val:
                succStack.append(temp)
                temp = temp.left
            else:
                predStack.append(temp)
                temp = temp.right
                    
        rv = []
        while len(rv) < k:
            pred = predStack[-1] if predStack else None
            succ = succStack[-1] if succStack else None
            curr = None
            
            if not pred:
                curr = popSuccStack()
            elif not succ:
                curr = popPredStack()
            elif abs(succ.val - target) < abs(pred.val - target):
                curr = popSuccStack()
            else:
                curr = popPredStack()
            rv.append(curr.val)
        return rv
                
                

###### O(n) Solution ########
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        heap = []
        def inorder(root):
            nonlocal heap
            # nonlocal target
            # nonlocal k
            if not root:
                return
            inorder(root.left)
            heapq.heappush(heap, (-abs(root.val - target), root.val))
            if len(heap) > k:
                heapq.heappop(heap)
            inorder(root.right)
        inorder(root)
        return [i[1] for i in heap]
                
            