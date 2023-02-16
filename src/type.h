#pragma once

/** \brief A custom type

This is a longer description for a custom type.

\verbatim embed:rst
Some extended information:

.. warning::

    This is a warning.

An inline example for MyType.

.. code-block:: cpp
    :linenos:

    MyType x;
    x.foo();

\endverbatim
*/
struct MyType {
    /** \brief Do a lot of foo */
    void foo();
};


/** \brief Some more advanced Doxygen 

This description is using purely Doxygen formatting unlike MyType.

\see MyType

1. A Markdown list
2. Followed by a code sample

\code{cpp}
OtherType x;
\endcode
*/
struct OtherType {
};