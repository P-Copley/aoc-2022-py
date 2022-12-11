from pathlib import Path


def readInput():
    filePath = Path(__file__).parent.parent.resolve()
    fileContents = Path(f'{filePath}/input.txt').read_text()
    lines = fileContents.split('\n\n')
    return lines
