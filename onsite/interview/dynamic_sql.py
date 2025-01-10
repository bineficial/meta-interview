filter_json = {"column": "age", "operator": ">", "value": 30}

query_json = {
    "select": ["name", "email", "age"],
    "from": "users",
    "where": None,  # We'll construct the WHERE clause dynamically
}


def build_where_clause(filter_json):
    column = filter_json.get("column")
    operator = filter_json.get("operator")
    value = filter_json.get("value")

    res_str = ""
    if column and operator and value:
        res_str = f"WHERE {column} {operator} {value}"

    return res_str


def build_select_clause(columns):
    return f"SELECT {', '.join(columns)}"


def build_from_clause(table):
    return f"FROM {table}"


q = f"""
{build_select_clause(query_json['select'])}
{build_from_clause(query_json['from'])}
{build_where_clause(filter_json)}
"""
print(q)
