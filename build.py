import markdown2
import os
from weasyprint import HTML

def build_newsletter():
    """
    Reads content from content.md, converts it to HTML,
    injects it into the newsletter template, and generates a PDF.
    """
    try:
        # Read the Markdown content
        with open('content.md', 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Read the HTML template
        with open('templates/newsletter.html', 'r', encoding='utf-8') as f:
            template_html = f.read()

        # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables', 'cuddled-lists', 'break-on-newline', 'header-ids', 'pyshell', 'smarty-pants', 'spoiler', 'wiki-tables', 'xml'])

        # Inject the content into the template
        final_html = template_html.replace('{{content}}', html_content)

        # Write the final HTML to a new file
        output_filename = 'docs/index.html'
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Successfully built the newsletter: {output_filename}")

        # Generate PDF from HTML
        pdf_output_filename = 'docs/newsletter.pdf'
        HTML(string=final_html, base_url=os.getcwd()).write_pdf(pdf_output_filename)
        print(f"Successfully generated PDF: {pdf_output_filename}")

        print("You can open the HTML file in your browser to see the result.")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure 'content.md' and 'templates/newsletter.html' exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    build_newsletter()
