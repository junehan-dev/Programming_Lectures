struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};

int	maxDepth(struct TreeNode *root)
{
	int	left;
	int right;
	
	if (!root)
		return (0);

	left = 1;
	right = 1;
	
	if (root->left)
		left += maxDepth(root->left);
	if (root->right)
		right += maxDepth(root->left);

	return (left > right ? left : right);
}
