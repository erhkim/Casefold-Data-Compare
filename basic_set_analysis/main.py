from typing import Set, TextIO

def write_to_file(set: Set, file: TextIO) -> None:
    for l in set:
        file.write(f"{l}\n")

# read file A
with open('_sourceA.txt', "r") as fileA:
    linesAset = {lineA.rstrip('\n').casefold() for lineA in fileA if lineA.isspace() == False and lineA}
    print(f"Number of unique elements in A: {len(linesAset)}")
    # read file B
    with open('_sourceB.txt', "r") as fileB:
        linesBset = {lineB.rstrip('\n').casefold() for lineB in fileB if lineB.isspace() == False and lineB}
        print(f"Number of unique elements in B: {len(linesBset)}")
        # find intersects
        with open('ABintersect.txt', "w") as ABintersect:
            intersect = linesAset & linesBset
            print(f"Number of intersecting elements in A and B: {len(intersect)}")
            write_to_file(intersect, ABintersect)
        # find A - B
        with open('AminusB.txt', "w") as AminusB:
            difference = linesAset - linesBset
            print(f"Number of elements in A but not in B: {len(difference)}")
            write_to_file(difference, AminusB)
        # find B - A
        with open('BminusA.txt', "w") as BminusA:
            difference = linesBset - linesAset
            print(f"Number of elements in B but not in A: {len(difference)}")
            write_to_file(difference, BminusA)
        # find symmetric difference
        with open('symmetricDiff.txt', "w") as symmetricDiff:
            difference = linesAset ^ linesBset
            print(f"Number of non-intersecting elements : {len(difference)}")
            write_to_file(difference, symmetricDiff)
        # subset qualities
        print(f"Is A a subset of B: {linesAset <= linesBset}")
        print(f"Is B a subset of A: {linesBset <= linesAset}")
