import os
import markdown
from bs4 import BeautifulSoup

# Convert markdown content to HTML
def convert_md_to_html(md_content, breadcrumb_items):
    # Convert Markdown content to HTML
    html_content = markdown.markdown(md_content)

    # Parse the HTML content with BeautifulSoup for modifications
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the title directly from the first header in the Markdown
    title = soup.find('h1').text.strip()

    # Generate breadcrumb HTML
    breadcrumb_html = ''.join([f'<li class="writ"><a href="{item[1]}">{item[0]}</a></li>' for item in breadcrumb_items])

    # Dynamically create the HTML structure using the extracted title
    final_html = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="DC.rights.owner" content="(C) Copyright 2024">
        <meta name="copyright" content="(C) Copyright 2024">
        <meta name="generator" content="DITA-OT">
        <meta name="DC.type" content="concept">
        <meta name="DC.format" content="HTML5">
        <meta name="DC.identifier" content="{title.lower().replace(' ', '_')}_Topic">
        <title>minoggin | {title}</title>
        <link rel="stylesheet" type="text/css" href="../../../css/commonltr.css">
    </head>
    <body id="{title.lower().replace(' ', '_')}_Topic">
        <main role="main">
            <article role="article" aria-labelledby="ariaid-title1">
                <h1 class="title topictitle1" id="ariaid-title1">{title}</h1>
                <hr>

                <!-- Breadcrumbs Section -->
                <ul class="breadcrumb">
                    {breadcrumb_html}
                    <li><span class="box-word grammar">{title}</span></li>
                </ul>

                <div class="body conbody">
                    <!-- Summary Section -->
                    <div class="summary">
                        <section class="section">
                            <h2 class="title sectiontitle">Summary</h2>
                            <p>{soup.p.text if soup.p else ''}</p>
                        </section>
                    </div>

                    <!-- Explanation Section -->
                    <div class="detailsec">
                        <section class="section">
                            <h2 class="title sectiontitle">Explanation</h2>
                            <p>{soup.find_all('p')[1].text if len(soup.find_all('p')) > 1 else ''}</p>
                        </section>

                        <!-- Examples Section -->
                        <section class="section examples">
                            <h2 class="title sectiontitle">Examples</h2>
                            <ol class="ol">
                                {''.join(str(li) for li in soup.find_all('li'))}
                            </ol>
                        </section>
                    </div>
                </div>
            </article>
        </main>
    </body>
    </html>
    """
    return final_html

# Function to process a single markdown file and convert it to HTML
def process_single_file(md_file_path, html_output_path, breadcrumb_items):
    # Read the markdown content
    with open(md_file_path, "r") as md_file:
        md_content = md_file.read()

    # Convert to HTML
    html_content = convert_md_to_html(md_content, breadcrumb_items)

    # Write the HTML content to a file
    with open(html_output_path, "w") as html_file:
        html_file.write(html_content)

    print(f"Converted {md_file_path} to {html_output_path}")

# Function to process all markdown files in a directory
def process_files_in_directory(md_directory, html_directory, breadcrumb_items):
    for filename in os.listdir(md_directory):
        if filename.endswith(".md"):
            md_path = os.path.join(md_directory, filename)
            html_filename = filename.replace(".md", ".html")
            html_path = os.path.join(html_directory, html_filename)

            # Process single file
            process_single_file(md_path, html_path, breadcrumb_items)

# Example usage with predefined breadcrumbs
if __name__ == "__main__":
    # Directory containing markdown files
    md_directory = "markdown_files"
    html_directory = "html_files"

    # Define common breadcrumbs (you can adjust or make this dynamic based on the file)
    common_breadcrumbs = [
        ("Parts of Speech", "site_files/html/grammar/parts_of_speech/parts-of-speech.html"),
        ("Descriptive Adverbs", "site_files/html/grammar/parts_of_speech/descriptive_adverbs.html"),
        ("Possessive Adverbs", "site_files/html/grammar/parts_of_speech/possessive_adverbs.html")
    ]

    # Create the output directory if it doesn't exist
    if not os.path.exists(html_directory):
        os.makedirs(html_directory)

    # Process all markdown files in the directory
    process_files_in_directory(md_directory, html_directory, common_breadcrumbs)