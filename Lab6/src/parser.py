def parse_product_basic(response):
    return {
        "id": response["id"],
        "name": response["name"]
    }


def parse_availability(response):
    return response.get("in_stock", False)