#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_string - prints Python strings
 * @p: pointer to PyObject
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;
	wchar_t *str;

	printf("[.] string object info\n");
	/* Check if p is a valid string object */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	/* Get the length and value of the string */
	len = PyUnicode_GET_LENGTH(p);
	str = PyUnicode_AsWideCharString(p, &len);
	/* Print the type, length and value of the string */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);
}
