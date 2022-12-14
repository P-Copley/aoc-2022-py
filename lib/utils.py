from pathlib import Path


def readInput(example):
    filePath = Path(__file__).parent.parent.resolve()
    fileContents = Path(f'{filePath}/input.txt').read_text(
    ) if example == False else Path(f'{filePath}/exampleInput.txt').read_text()
    lines = fileContents.split('\n\n')
    return lines
