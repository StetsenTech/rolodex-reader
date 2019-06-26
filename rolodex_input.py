import json

import click

from rolodex.components.entry import EntryComponent

@click.command()
@click.option('--input_file', '-i', default="data.in",
              type=click.Path(exists=True),
              help="Path to data file for input")
@click.option('--output_file', '-o', default="result.out",
              type=click.Path(exists=False),
              help="Path to output file")
def run_rolodex(input_file, output_file):
    """Starts processing the rolodex"""
    with open(input_file, mode='r') as data_in:
        #@ TODO: Convert print to logging output
        print "Reading input from", input_file 
        entry_input = data_in.readlines()

    entry_component = EntryComponent()
    #@ TODO: Convert print to logging output
    print "Processing input..."
    result = entry_component.create_output(entry_input, sort=True)

    with open(output_file, 'w+') as result_out:
        #@ TODO: Convert print to logging output
        print "Writing output to", output_file
        result_out.write(result)

if __name__ == '__main__':
    run_rolodex()
