from jsonschemainfotable.jsonschema import JSONSchemaDirective


def render_html_from_filename(filename, options={}):

    jsonschemadirective = JSONSchemaDirective(
        name='',
        arguments=[],
        options=options,
        content=[filename],
        lineno=1,
        content_offset=None,
        block_text=None,
        state=None,
        state_machine=None
    )

    result = jsonschemadirective.run()

    # From https://stackoverflow.com/questions/32167384/how-do-i-convert-a-docutils-document-tree-into-an-html-string
    # but I couldn't get it to work  .....
    # from docutils.core import  publish_from_doctree
    # html = publish_from_doctree(result[0], writer_name='html').decode()

    # so I just did this instead - which I don't like as it assumes html rather than specifies it but it seems to work!
    html = str(result[0])

    return html
