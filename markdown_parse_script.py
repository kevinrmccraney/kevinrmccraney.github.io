# usr/bin/python
import markdown
import re
import os

cwd = os.getcwd()
MD_DIR = "markdown/"

def line_containing_pattern(markdown_content, pattern):
    return re.sub(pattern, '', markdown_content, count=1, flags=re.DOTALL).strip()


def parse_markdown_metadata(markdown_content):
    # Extract metadata from the Markdown content
    re_str = r'^---(.*?)---'
    metadata = {}
    metadata_match = re.match(re_str, markdown_content, re.DOTALL)
    if metadata_match:
        metadata_str = metadata_match.group(1).strip()
        metadata_lines = metadata_str.split('\n')
        for line in metadata_lines:
            key, value = map(str.strip, line.split(':', 1))
            metadata[key] = value

        markdown_content = re.sub(re_str, '', markdown_content, count=1, flags=re.DOTALL).strip()

    return metadata, markdown_content


def choose_template(m): return f"{MD_DIR}/templates/{m.get('template', 'default')}.html"

def parse_markdown_to_html(markdown_txt): return markdown.markdown(markdown_txt)

def embed_into_template(data_dict, template_path):
    # Read the selected HTML template from a file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    data = template.format(**data_dict)

    # handle special case for index
    if data_dict["keywords"] == "index":
        html_string = r'<span style="float:left;"><a href="./index\.html">Back to Home</a></span>'
        data = line_containing_pattern(data, html_string)

    # Embed HTML content into the template
    return data


def process_files(input, directory):
        # Read Markdown content from a file (replace 'input.md' with your file name)
        with open(f"{directory}/{MD_DIR}/{input}", 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # Parse metadata to determine the template
        metadata, updated_markdown = parse_markdown_metadata(markdown_content)

        # Choose a template based on metadata
        template_path = choose_template(metadata)

        # Parse Markdown to HTML
        html_content = parse_markdown_to_html(updated_markdown)
        metadata["content"] = html_content

        # Embed HTML content into the template
        final_html = embed_into_template(metadata, template_path)

        # get the output filename stem
        output_filename = input.split(".md")[0]

        # Write the final HTML to a file (replace 'output.html' with your desired output file name)
        with open(f'{directory}/{output_filename}.html', 'w', encoding='utf-8') as file:
            file.write(final_html)

def main():
    # iterate through everything in the markdown directory
    for file in os.listdir(f"{cwd}/{MD_DIR}"):
        if file.endswith(".md"):
            process_files(file, cwd)

if __name__ == "__main__":
    main()
