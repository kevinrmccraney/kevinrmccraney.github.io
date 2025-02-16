import markdown
import re
import os
import logging
import sys

# Configure logging to output to stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger()

# Get the current working directory dynamically (for GitHub Actions)
cwd = os.getcwd()

### ONE LINE FUNCTIONS

# process text; args Text, Regex, Substitution string
def choose_template(m): return f"{cwd}/templating/templates/{m.get('template', 'default')}.html"

def process_text(t, r, s=""): return re.sub(r, s, t, count=1, flags=re.DOTALL).strip()

def parse_markdown_to_html(markdown_txt): return markdown.markdown(markdown_txt)

def replace_details(content, html_sub=False):
    """
    Replaces <details> with $DETAILS and </details> with $CLOSEDETAILS in the content.
    """
    logging.debug("substituting details and summary tags")
    mapping = {
        "<details>": "!!DETAILS",
        "</details>": "!!CLOSE_DETAILS",
        "<summary>": "!!SUMMARY",
        "</summary>": "!!CLOSE_SUMMARY",
    }

    for key, value in mapping.items():
        sub_one = key if not html_sub else value
        sub_two = value if not html_sub else key
        content = re.sub(rf'{sub_one}', f'{sub_two}', content)
    return content

def parse_markdown_metadata(markdown_content, input):
    logging.info(f"parsing markdown metadata for {input}")
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

        markdown_content = process_text(markdown_content, re_str)

    return metadata, markdown_content

def embed_into_template(data_dict, template_path):
    logging.info("embedding data elements into template")
    # Read the selected HTML template from a file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template = template_file.read()

    # Iterate through the keys in data_dict and substitute in the template
    for key, value in data_dict.items():
        placeholder = "{"+key+"}"  # Create a placeholder like {{key}}
        template = template.replace(placeholder, str(value))  # Substitute value into the template

    # Handle special case for 'index'
    if data_dict.get("keywords") == "index":
        html_string = r'<x-placeholder>(.*?)</x-placeholder>'
        template = process_text(template, html_string)

    return template


def process_files(input, directory):
        # Read Markdown content from a file (replace 'input.md' with your file name)
        markdown_path = os.path.join(directory, "templating/markdown", input)
        with open(markdown_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # Parse metadata to determine the template
        metadata, updated_markdown = parse_markdown_metadata(markdown_content, input)

        # Choose a template based on metadata
        template_path = choose_template(metadata)

        # Parse Markdown to HTML
        updated_markdown = replace_details(updated_markdown)
        html_content = parse_markdown_to_html(updated_markdown)
        html_content = replace_details(html_content, html_sub=True)
        metadata["content"] = html_content

        # Embed HTML content into the template
        final_html = embed_into_template(metadata, template_path)

        # get the output filename stem
        output_filename = input.split(".md")[0]

        # Write the final HTML to a file (replace 'output.html' with your desired output file name)
        logging.info(f"writing output {output_filename}.html")
        with open(f"{cwd}/{output_filename}.html", 'w', encoding='utf-8') as file:
            file.write(final_html)

def main():
    # iterate through everything in the markdown directory
    for file in os.listdir("templating/markdown"):
        if file.endswith(".md"):
            process_files(file, cwd)

if __name__ == "__main__":
    main()
