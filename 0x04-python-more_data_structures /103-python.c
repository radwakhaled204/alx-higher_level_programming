#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p)
{
	int size, alloc, i; /* Declare variables for size, allocated space and index*/
	const char *type; /* Declare a pointer to store the type of each element*/
	/* Cast the PyObject to a PyListObject*/
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p; /* Cast the PyObject to a PyVarObject*/

	size = var->ob_size; /* Get the size of the list from the PyVarObject*/
	/* Get the allocated space of the list from the PyListObject*/
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++) /* Loop through each element of the list*/
	{
		/* Get the type name of the element*/
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		/* If the element is a bytes object, print more info*/
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, size; /* Declare variables for index and size*/
	/* Cast the PyObject to a PyBytesObject*/
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	/* Check if the object is a valid bytes object*/
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Print the size of the bytes object*/
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	/* Print the string representation of the bytes object*/
	printf("  trying string: %s\n", bytes->ob_sval);

	/* If the size is larger than 10, truncate it to 10*/
	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	/* Print the first 10 bytes or less in hexadecimal format*/
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
