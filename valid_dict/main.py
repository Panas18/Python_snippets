def validate(doc, schema):
    error_message = []
    for key in schema:
        rule = schema[key]

        if type(rule) == list:
            _type, minm, maxm = rule
        else:
            _type, minm, maxm = rule, None, None

        try:
            if key not in doc:
                raise KeyNotFoundError()

            if type(doc[key]) is _type:
                if minm or maxm:
                    if _type == str:
                        str_len = len(doc[key])
                        if str_len < minm or str_len > maxm:
                            error_message.append(
                                f"** Length of [{key}] expected {minm} - {maxm}, found {str_len}")

                    if _type == int:
                        value = doc[key]
                        if value < minm or value > maxm:
                            error_message.append(
                                f"** Value of [{key}] expected {minm} - {maxm}, found {value}")
            else:
                error_message.append(
                    f">> [{key}] has wrong type. Expected {_type}, found {type(doc[key])}")

        except KeyNotFoundError:
            error_message.append(f" >> Missing Field: [{key}]")

    if error_message:
        for error in error_message:
            print(error)
    else:
        return True


if __name__ == "__main__":

    schema = {"full name": [str, 5, 50], "country": str, "age": [int, 1, 110],
              "active": bool}

    doc = {"full name": "Panas Tiwari",  "age": 200,
           "active": False}

    validate(doc, schema)
