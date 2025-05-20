# payload2rdf/cli.py

import click
from rdflib import Graph
from payload2rdf.warc_reader import extract_html_records
from payload2rdf.extract import extract_metadata
from payload2rdf.mapping import load_mapping, map_metadata_to_graph, NAMESPACES

@click.command()
@click.argument('warc_file', type=click.Path(exists=True))
@click.option('--mapping-file', type=click.Path(exists=True), default='mappings.yaml', help='YAML-Datei mit den Mapping-Regeln')
@click.option('--format', default='turtle', help='RDF-Serialisierungsformat (z. B. turtle, xml, n3)')
def cli(warc_file, mapping_file, format):
    mapping = load_mapping(mapping_file)
    for url, html in extract_html_records(warc_file):
        metadata = extract_metadata(url, html)
        graph = Graph()
        map_metadata_to_graph(graph, url, metadata, mapping, NAMESPACES)
        print(f"\n# RDF für {url}")
        print(graph.serialize(format=format))

if __name__ == '__main__':
    cli()
