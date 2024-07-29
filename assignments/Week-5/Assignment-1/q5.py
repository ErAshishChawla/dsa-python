from typing import Dict


def generateSampleDict(n: int) -> Dict[int, int]:
    sampleDict = dict()

    for i in range(1, n + 1):
        sampleDict[i] = i**2

    return sampleDict


print(generateSampleDict(5))
