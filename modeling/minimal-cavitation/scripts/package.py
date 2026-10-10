"""Create a single-folder delivery ZIP, excluding generated intermediates."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / 'Minimal_Cavitation_Models_20261010.zip'
SUPERSEDED_VERIFICATION = {
    f'{case}_{suffix}.csv'
    for case in ('A_baseline', 'B_open_baseline')
    for suffix in ('original_1ns', 'original_2ns', 'fresh_process_1ns', 'fresh_process_2ns')
}


def main():
    files = []
    for path in sorted(ROOT.rglob('*')):
        relative = path.relative_to(ROOT)
        if not path.is_file() or any(part in ('build', 'tmp', '__pycache__', 'practice', '.git') for part in relative.parts):
            continue
        if path.suffix.lower() in ('.zip', '.class', '.pyc') or path.name.endswith(('.mph.log', '.mph.recovery', '.mph.lock')):
            continue
        if relative.parts[0] == 'verification' and path.name in SUPERSEDED_VERIFICATION:
            continue
        files.append((path, relative))
    if sum(path.suffix == '.mph' for path, _ in files) != 2:
        raise AssertionError('Exactly two native final models required')
    with zipfile.ZipFile(TARGET, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path, relative in files:
            archive.write(path, (Path('Minimal_Cavitation_Models') / relative).as_posix())
    with zipfile.ZipFile(TARGET) as archive:
        failed = archive.testzip()
        if failed:
            raise AssertionError('ZIP integrity failed: ' + failed)
    print(f'Created {TARGET.name}: {len(files)} files, {TARGET.stat().st_size:,} bytes; ZIP integrity PASS')


if __name__ == '__main__':
    main()
