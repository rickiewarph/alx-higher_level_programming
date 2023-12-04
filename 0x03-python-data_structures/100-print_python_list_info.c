#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  func printing basic info about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)
{
	int elmnt;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elmnt = 0; elmnt < Py_SIZE(p); elmnt++)
		printf("Element %d: %s\n", elmnt, Py_TYPE(PyList_GetItem(p, elmnt))->tp_name);
}
