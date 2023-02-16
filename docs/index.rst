Documentation example
=====================

This document demonstrates the out-of-code documentation, which is perfect for the example-first documentation style.

Some important topic
====================

When needed, different parts of the API can be pulled in as references:

.. doxygenfunction:: function

We can also pull in parts of the code as examples:

.. literalinclude:: ../src/main.cc
   :language: cpp
   :start-line: 4
   :end-line: 7

Working with multi-file
=======================

A slightly confusing aspect of Sphinx is that for multi-file documentation to link to each section correctly, each file needs to be listed in the root table of contents.

This can be customized, which is a necessity for dynamic blog-style content, but it requires adjusting the sidebar code.

A typical place to put this root table of content is at the end of the index file, and it can also be hidden.

.. toctree::
   :maxdepth: 2

   self
   api/library_root
   other