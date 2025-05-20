# payload2rdf

**Extract structured metadata from WARC HTML payloads and convert it to RDF.**

`payload2rdf` is a Python-based tool that processes HTML content embedded in WARC (Web ARChive) files, extracts metadata using [extruct](https://github.com/scrapinghub/extruct), and serializes the result as RDF using common vocabularies such as [Dublin Core](http://purl.org/dc/elements/1.1/).

---

## 🚀 Features

- Extracts structured data from HTML using:
  - JSON-LD
  - Microdata
  - RDFa
  - Open Graph
  - Microformats
- Falls back to `<title>` and `<meta name="description">` if no structured data is found
- Outputs RDF in XML serialization (compatible with common triple stores)
- Designed for integration with large-scale WARC workflows

---

## 🛠 Usage

```bash
python extract.py <url> <html_file>
```

Example:

```bash
python extract.py http://example.org/ example.html
```

This will output RDF/XML metadata for the given HTML page.

---

## 📦 Dependencies

- Python 3.8+
- [`extruct`](https://pypi.org/project/extruct/)
- [`w3lib`](https://pypi.org/project/w3lib/)
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/)

Install with Poetry:

```bash
poetry install
```

---

## 📄 License

MIT License. See `LICENSE` file for details.
