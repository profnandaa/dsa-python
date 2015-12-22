from .tree_adt import Tree


class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure'''

    def left(self, p):
        '''Return a Position representing p's left child

        Return None if p does not have a left child.
        '''
        raise NonImplementedError('must be implemented by subclass')

    def right(self, p):
        '''Return a Position representing p's right child

        Return None if p does not have a right child.
        '''
        raise NonImplementedError('must be implemented by subclass')

    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling)'''
        parent = self.parent(p)
        if parent is None:
            return None 		# p must be the root
        if p == self.left(parent):
            return self.right(parent)
        return self.left(parent)

    def children(self, p):
        '''Generate an iteration of Positions representing p's children'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
