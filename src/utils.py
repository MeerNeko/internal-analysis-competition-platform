
def read_mdfile(mdfile_path:str) -> str:
    lines = []
    with open(mdfile_path, encoding='utf-8') as f:
        lines = f.readlines()
    markdown = ''.join(lines)

    return markdown