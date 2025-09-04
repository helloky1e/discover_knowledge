# Discover Knowledge Homepage

Generate a simple static `index.html` homepage from a JSON configuration file.

## Configuration

Edit `homepage_config.json` to customize the page. The file supports:

- `title`: text for the `<title>` element.
- `header`: heading displayed at the top of the page.
- `footer`: footer text.
- `sections`: list of sections with `title` and `content` fields.

## Generate the Homepage

Run the generator:

```bash
python generate_homepage.py
```

The script creates `index.html` based on the configuration.
