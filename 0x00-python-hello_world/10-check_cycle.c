#include "lists.h"
/**
 * check_cycle - to check is a linked list contains a cycle
 * @list: The linked list to be checked
 *
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
