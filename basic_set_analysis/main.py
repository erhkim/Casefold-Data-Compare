# read file A
with open('_sourceA.txt', "r") as fileA:
    linesAset = {lineA.rstrip('\n').lower() for lineA in fileA if lineA.isspace() == False and lineA}
    print(f"Number of unique elements in A: {len(linesAset)}")
    # read file B
    with open('_sourceB.txt', "r") as fileB:
        linesBset = {lineB.rstrip('\n').lower() for lineB in fileB if lineB.isspace() == False and lineB}
        print(f"Number of unique elements in B: {len(linesBset)}")
        # find intersects
        with open('ABintersect.txt', "w") as ABintersect:
            intersect = linesAset & linesBset
            print(f"Number of intersecting elements in A and B: {len(intersect)}")
            for l in intersect:
                ABintersect.write(f"{l}\n")
        # find A - B
        with open('AminusB.txt', "w") as AminusB:
            difference = linesAset - linesBset
            print(f"Number of elements in A but not in B: {len(difference)}")
            for l in difference:
                AminusB.write(f"{l}\n")

        # find B - A
        with open('BminusA.txt', "w") as BminusA:
            difference = linesBset - linesAset
            print(f"Number of elements in B but not in A: {len(difference)}")
            for l in difference:
                BminusA.write(f"{l}\n")
        # find symmetric difference
        with open('symmetricDiff.txt', "w") as symmetricDiff:
            difference = linesAset ^ linesBset
            print(f"Number of non-intersecting elements : {len(difference)}")
            for l in difference:
                symmetricDiff.write(f"{l}\n")
        # subset qualities
        print(f"Is A a subset of B: {linesAset <= linesBset}")
        print(f"Is B a subset of A: {linesBset <= linesAset}")
