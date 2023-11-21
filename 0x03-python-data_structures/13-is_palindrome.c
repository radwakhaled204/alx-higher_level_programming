#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *next = NULL;
	int result = 1;

	if (!head || !*head || !(*head)->next)
		return (1);
	/* Find the middle of the list using slow and fast pointers */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	fast = *head; /* Reset fast pointer to the head */
	slow = prev; /* Set slow pointer to the last node */
	while (slow)
	{
		if (fast->n != slow->n) /* Mismatch found */
		{
			result = 0;
			break;
		}
		fast = fast->next;
		slow = slow->next;
	}
	slow = prev; /* Set slow pointer to the last node */
	prev = NULL; /* Reset prev pointer to NULL */
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	return (result);
}
