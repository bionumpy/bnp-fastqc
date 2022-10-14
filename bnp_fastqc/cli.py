"""Console script for bnp_fastqc."""
import sys
import click


@click.command()
@click.option("--reads")
def main(reads):
    print(reads)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
