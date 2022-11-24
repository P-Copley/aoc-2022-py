from pathlib import Path
from sys import argv

command, dayNum, partNum = argv;

rootDir = Path(f'{Path(__file__).parent.parent.resolve()}');

Path(f'{rootDir}/solutions/day{dayNum}/part{partNum}').mkdir(parents=True)
Path(f'{rootDir}/solutions/day{dayNum}/part{partNum}/main.py').write_text(Path(f'{rootDir}/main.py').read_text())
