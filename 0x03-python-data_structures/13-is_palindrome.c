#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
*ongeza_nodeint - func to pre-add a new node on listint_t list
*@head: head of listint_t
*@n: integer to be added in listint_t list
*Return: add of the new element, or NULL(failure)
*/

listint_t *ongeza_nodeint(listint_t **head, const int n)
{
	listint_t *q;

	q = malloc(sizeof(listint_t));
	if (q == NULL)
		return (NULL);
	q->n = n;
	q->next = *head;
	*head = q;
	return (q);
}

/**
*is_palindrome - func identifying if a syngle linked list is palindrome
*@head: head of the listint_t
*Return: 1(palindrome) or 0(not palindrome)
*/
int is_palindrome(listint_t **head)
{
	listint_t *headb = *head;
	listint_t *ox = NULL, *ox2 = NULL;

	if (*head == NULL || headb->next == NULL)
		return (1);
	while (headb != NULL)
	{
		ongeza_nodeint(&ox, headb->n);
		headb = headb->next;
	}
	ox2 = ox;
	while (*head != NULL)
	{
		if ((*head)->n != ox2->n)
		{
			free_listint(ox);
			return (0);
		}
		*head = (*head)->next;
		ox2 = ox2->next;
	}
	free_listint(ox);
	return (1);
}
