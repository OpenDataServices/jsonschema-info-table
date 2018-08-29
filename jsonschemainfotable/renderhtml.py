from jsonschemainfotable.jsonschema import JSONSchemaDirective


def render_html_from_filename(filename, options = {}):

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

    # TODO turn this objects into actual HTML!

    return result

