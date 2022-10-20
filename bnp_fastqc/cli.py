"""Console script for bnp_fastqc."""
import sys
import click
import modules


MODULES = {
   "kmer_content": modules.kmer_content
}


@click.command()
@click.option("--reads")
@click.option("--module")
def main(reads, module):
    if module not in MODULES:
        print("Invalid module", module, ". Valid modules are: %s" % ', '.join(MODULES.keys()))
        return

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
