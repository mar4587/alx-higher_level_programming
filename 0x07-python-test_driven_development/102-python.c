#include <Python.h>
#include <object.h>
#include <unicodeobject.h>


void print_python_string(PyObject *p)
{
    const char *type = NULL;
    Py_ssize_t lengt = 0;
    wchar_t *str = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        type = "compact ascii";
    else
        type = "compact unicode object";

    str = PyUnicode_AsWideCharString(p, &lengt);

    printf("  type: %s\n", type);
    printf("  lengtth: %ld\n", lengt);
    printf("  value: %ls\n", str);
}
