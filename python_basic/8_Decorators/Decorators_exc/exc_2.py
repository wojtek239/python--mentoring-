def decorate_with_stars(func):
    def wrapper(text):
        decorated_text = f"{'*' * 12}\n{text}\n{'*' * 12}"
        return func(decorated_text)
    return wrapper


@decorate_with_stars
def display_text(text):
    print(text)


display_text("hello world")