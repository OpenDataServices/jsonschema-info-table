# jsonschema-info-table

This Python library takes [JSON Schema](http://json-schema.org/) and presents human readable information about it as a table.

It includes a Sphinx directive.

## Usage in Sphinx

Include this extension in conf.py::

    extensions = ['jsonschemainfotable.jsonschema']

Write ``jsonschemainfotable`` directive into reST file where you want to import schema::

    .. jsonschemainfotable:: path/to/your.json

## History

This was created by [Takeshi KOMIYA](https://github.com/tk0miya/sphinxcontrib-jsonschema)
and then developed by [Open Data Services](http://opendataservices.coop/).

It was renamed to reflect the fact they wanted to use this in non-Sphinx situations.
