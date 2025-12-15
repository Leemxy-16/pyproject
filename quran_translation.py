import quran
import pdfkit

# Quran translation settings
LANGUAGE = "EN"
TRANSLATION = "MUHSIN KHAN"

# PDF settings
PDF_TITLE = "QURAN TRANSLATION (WORD BY WORD)"
PDF_FONT = "POLLINS"
PDF_FILE = "QURAN_TRANSLATION.PDF"

def get_quran_text():
    quran = quran()
    chapters = quran.get_chapters()
    return chapters

def generate_html(chapters):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
       <title>{}</title>
       <style>
          body {{
              font-family: {};
          }}
       </style>
    </head>
    <body>
    """.format(PDF_TITLE, PDF_FONT)

    for chapter in chapters:
        html += "<h1>Surah {} ({})</h1>".format(chapter['id'], chapter['name'])
        verses = quran.get_verses(chapter['id'])
        for verse in verses:
            arabic_text = verse['text']
            translation_text = verse['translations'][LANGUAGE][TRANSLATION]  # Adjust based on actual data structure
            html += """
            <p>
                <span style="float:right;">{}</span>
                <span style="float:left;">{}</span>
            </p>
            """.format(arabic_text, translation_text)

    html += "</body></html>"
    return html

def generate_pdf(html):
    options = {
        "page-size": "A4",
        "margin-right": "0.75in",
        "margin-top": "0.75in",
        "margin-bottom": "0.75in",
        "encoding": "UTF-8",
        "outline": None,
        "custom-header": [("Accept-Encoding", "gzip")]
    }
    pdfkit.from_string(html, PDF_FILE, options=options)
    print("PDF generated successfully!")

def main():
    chapters = get_quran_text()
    html =
    
    
    
      generate_html(chapters)
    generate_pdf(html)

if __name__ == "__main__":
    main()
