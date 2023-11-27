#include "lists.h"

/**
 * check_cycle - func checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 * Return: 1 if there is a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
    listint_t *tortoise = list;
    listint_t *hare = list;

    while (hare != NULL && hare->next != NULL)
    {
        tortoise = tortoise->next;
        hare = hare->next->next;

        if (tortoise == hare)
            return (1);
    }

    return (0);
}

