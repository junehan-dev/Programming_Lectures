#include <stdbool.h>
#include <stddef.h>

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};

bool isEqualVal(struct TreeNode *p, struct TreeNode *q);
bool isEqualLeaf(struct TreeNode *p, struct TreeNode *q);
struct TreeNode *popNode(struct TreeNode **nodes, int cur);
int pushLeafNodes(struct TreeNode *p, struct TreeNode *q, struct TreeNode **leafNodes, int cur);
void copyNodes(struct TreeNode **rootNodes, struct TreeNode **leafNodes);

bool isSameTree(struct TreeNode *p, struct TreeNode *q)
{
	struct TreeNode *rootNodes[65] = {NULL};
	struct TreeNode *leafNodes[64] = {NULL};
	int root_cur;
	int leaf_cur;

	if (!p && q || p && !q)
		return (false);

	root_cur = 0;
	leaf_cur = 0;

	rootNodes[0] = p;
	rootNodes[1] = q;
	while (rootNodes[root_cur]) {
		p = popNode(rootNodes, root_cur++);
		q = popNode(rootNodes, root_cur++);
		if (!isEqualVal(p, q) || !isEqualLeaf(p, q))
			return (false);

		leaf_cur += pushLeafNodes(p, q, leafNodes, leaf_cur);
		if (!rootNodes[root_cur] && leafNodes[0]) {
			root_cur = 0;
			leaf_cur = 0;
			copyNodes(rootNodes, leafNodes);
		}
	}

	return (true);
}

bool isEqualLeaf(struct TreeNode *p, struct TreeNode *q)
{
	return (((p->left && q->left) || !(p->left) && !(q->left)) &&
			(p->right && q->right || !(p->right) && !(q->right)));
}

bool isEqualVal(struct TreeNode *p, struct TreeNode *q)
{
	return (p->val == q->val);
}

struct TreeNode *popNode(struct TreeNode **nodes, int cur)
{
	struct TreeNode *ret;

   	ret = nodes[cur];
	nodes[cur] = NULL;

	return (ret);
}

int pushLeafNodes(struct TreeNode *p, struct TreeNode *q, struct TreeNode **leafNodes, int cur) 
{
	int ret;

	ret = 0;

	if (p->left)
	{
		leafNodes[cur++] = p->left;
		leafNodes[cur++] = q->left;
		ret += 2;
	}

	if (p->right)
	{
		leafNodes[cur++] = p->right;
		leafNodes[cur++] = q->right;
		ret += 2;
	}

	return (ret);
}

void copyNodes(struct TreeNode **rootNodes, struct TreeNode **leafNodes)
{
	while ((*rootNodes++ = *leafNodes))
		*leafNodes++ = NULL;
}

