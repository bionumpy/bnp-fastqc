"""Console script for bnp_fastqc."""
import sys
import click
import bionumpy as bnp
import bnp_fastqc
from bnp_fastqc.modules import kmer_content

MODULES = {
   "kmer_content": kmer_content
}



@click.command()
@click.option("--module", required=True)
@click.option("--reads", required=True)
def main(module, reads):
    if module not in MODULES:
        print("Invalid module", module, ". Valid modules are: %s" % ', '.join(MODULES.keys()))
        return
    else:
        file = bnp.open(reads)
        MODULES[module].run(file.read_chunks())

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
