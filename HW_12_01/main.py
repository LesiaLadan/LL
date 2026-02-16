import os


def delete_html_tags(html):

    draft_text = ""
    in_tags = False

    for char in html:
        if char == "<":
            in_tags = True
        elif char == ">":
            in_tags = False
        elif not in_tags:
            draft_text += char

    lines = draft_text.splitlines()
    text_lines = [line for line in lines if line.strip() != '']

    return '\n'.join(text_lines)

def process_file(input_filename, output_filename = "cleaned.txt"):
    # це спитала у gpt, бо не знала як зробити, щоб у вас і в мене знаходився файл драфта, і щоб очищений записувався саме в папку з поточною домашкою, а не в кореневий каталог
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, input_filename)
    output_path = os.path.join(base_path, output_filename)

    with open(input_path, "r", encoding="utf-8") as file:
        html = file.read()

    cleaned_text = delete_html_tags(html)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(cleaned_text)

    return output_path


result_file = process_file("draft.html")


with open(result_file, "r", encoding="utf-8") as file:
    cleaned = file.read()

assert "<" not in cleaned, "< present in text"
assert ">" not in cleaned, "> present in text"
