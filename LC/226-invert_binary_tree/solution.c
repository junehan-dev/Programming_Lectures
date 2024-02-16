#include <stddef.h>

struct TreeNode *swapNodes(struct TreeNode *parent);
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};

struct TreeNode *invertTree(struct TreeNode *root)
{
	if (!root)
		return (NULL);

	swapNodes(root);
	(root->left) ? invertTree(root->left) : 0;
	(root->right) ? invertTree(root->right) : 0;
	return (root);
}

struct TreeNode *swapNodes(struct TreeNode *parent)
{
	struct TreeNode *temp;

	temp = parent->left;
	parent->left = parent->right;
	parent->right = temp;

	return (parent);
}

