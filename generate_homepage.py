import json
from pathlib import Path

def generate_homepage(config_path: str = "homepage_config.json", output_path: str = "index.html") -> None:
    """Generate a simple HTML homepage from a JSON configuration file.

    The configuration file may define the following keys:
    - title:     text for the <title> element
    - header:    heading displayed at the top of the page
    - footer:    footer text displayed at the bottom of the page
    - sections:  list of {"title": str, "content": str} dictionaries representing
                  page sections
    """
    config_file = Path(config_path)
    config = json.loads(config_file.read_text()) if config_file.exists() else {}

    def section_html(section: dict) -> str:
        title = section.get("title", "")
        content = section.get("content", "")
        return f"<section>\n  <h2>{title}</h2>\n  <p>{content}</p>\n</section>"

    sections = config.get("sections", [])
    sections_html = "\n".join(section_html(s) for s in sections)

    html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <title>{config.get('title', '')}</title>
</head>
<body>
  <header>
    <h1>{config.get('header', '')}</h1>
  </header>
  <main>
{sections_html}
  </main>
  <footer>
    {config.get('footer', '')}
  </footer>
</body>
</html>
"""

    Path(output_path).write_text(html)
    print(f"Generated {output_path} from {config_path}")

if __name__ == "__main__":
    generate_homepage()
