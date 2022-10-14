import bionumpy as bnp


def test_read_file():
    f = bnp.open("example_data/big.fq.gz")
    print(f.read_chunk())
