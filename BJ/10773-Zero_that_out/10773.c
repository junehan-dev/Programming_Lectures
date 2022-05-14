#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

struct stack {
	size_t			siz;
	unsigned int	len;
	unsigned int	cur;
	void			*data;
};

struct stack	*make_stack(size_t siz, unsigned int len);
unsigned int	stack_push(struct stack *s, const void *src);
unsigned int	stack_pop(struct stack *s, void *dest );

int		main(void)
{
	struct stack	*num_stack;
	unsigned int	max;
	unsigned int	len;
	unsigned int	i;
	char			v;
	int				ret;

	i = 0;
	ret = 0;

	scanf("%u", &len);
	num_stack = make_stack(1, len);
	max = len;

	while (i++ < num_stack->len && scanf("%d", &v))
		(!v) ? stack_pop(num_stack, &v) : stack_push(num_stack, &v);

	while (stack_pop(num_stack, &v))
		ret += v;

	free(num_stack->data);
	free(num_stack);
	printf("%d", ret);
	return (0);
}


struct stack 	*make_stack(size_t siz, unsigned int len)
{
	struct stack	*ret;

	ret			= malloc(sizeof(struct stack));
	ret->siz	= siz;
	ret->len	= len;
	ret->cur	= 0;
	ret->data	= (void *)malloc(siz * len);

	return (ret);	
}

unsigned int	stack_pop(struct stack *s, void *dest)
{
	char			*dest_data;
	const char		*top;
	unsigned int	n;

	if (!s->cur)
		return (0);

	n = 0;
	(s->cur)--;
	dest_data = (char *)dest;
	top = (const char *)(s->data) + (s->cur) * (s->siz);
	while (n < (s->siz)) {
		*(dest_data + n) = *(top + n);
		n++;
	}

	return (n);
}


unsigned int	stack_push(struct stack *s, const void *src)
{
	const char	*src_data;
	char		*top;
	size_t		n;

	if ((s->cur) == (s->len))
		return 0;

	n = 0;
	src_data = (const char *)src;
	top = (char *)(s->data) + (s->cur) * (s->siz);
	while (n < (s->siz)) {
		*(top + n) = *(src_data + n);
		n++;
	}
	s->cur++;

	return (n);
}


