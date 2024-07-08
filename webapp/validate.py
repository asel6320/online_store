from django.core.exceptions import ValidationError

def product_validate(product):
    errors = {}

    if not product.title:
        errors["title"] = "Title is mandatory"

    if product.description and len(product.description) > 50:
        errors["description"] = "The length of this field should be less than 50"

    if not product.category:
        errors["category"] = "Category is mandatory"

    if 0 >= product.price > 100000:
        errors["price"] = "The price should be between 0 and 100000, inclusive"

    if product.remainder <= 0:
        errors["remainder"] = "The remainder should be greater than 0, inclusive"

    if not product.image:
        errors["image"] = "The product image url is mandatory"

    return errors
