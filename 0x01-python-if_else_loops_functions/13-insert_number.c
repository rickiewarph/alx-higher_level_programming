#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "lists.h"

/**
 * insert_node - func inserting a no. into a sorted list
 * @head: the linked list
 * @number: no. to insert
 * Return: pointer to the head
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *qurent = *head;
	listint_t *qew = NULL;
	listint_t *tmp = NULL;

	if (!head)
		return (NULL);
	qew = malloc(sizeof(listint_t));
	if (!qew)
		return (NULL);
	qew->n = number;
	qew->next = NULL;

	if (!*head || (*head)->n > number)
	{
		qew->next = *head;
		return (*head = qew);
	}
	else
	{
		while (qurent && qurent->n < number)
		{
			tmp = qurent;
			qurent = qurent->next;
		}
		tmp->next = qew;
		qew->next = qurent;
	}
	return (qew);
}
