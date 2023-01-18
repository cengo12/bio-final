import os
from flask import Flask, request, jsonify, render_template
from app import from_ncbi, get_primer_sequences, parse_fasta, endprimers


gui_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'gui')  # development path

if not os.path.exists(gui_dir):  # frozen executable path
    gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui')
    print(gui_dir)

server = Flask(__name__, static_url_path='', static_folder=gui_dir, template_folder=gui_dir)
server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching


@server.route("/")
def hello():
    return render_template('index.html')


@server.route('/id', methods=['POST'])
def from_id():
    ncbiId = request.json.get('ncbi_id')
    geneseq = from_ncbi(ncbiId)
    primers = get_primer_sequences(geneseq)
    print(ncbiId)
    return jsonify(primers)


@server.route('/raw', methods=['POST'])
def from_raw():
    geneseq = parse_fasta(request.json.get('gene_raw'))
    primers = get_primer_sequences(geneseq)
    return jsonify(primers)


@server.route('/endprimers', methods=['POST'])
def end_primers():
    location = int(request.json.get('location'))
    primer = request.json.get('primer')
    endPrimers = endprimers(location, primer)
    return jsonify(endPrimers)


@server.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404