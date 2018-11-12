import nbformat as nbf

nb = nbformat.read("File_Path_Goes_Here", nbformat.NO_CONVERT)
insertCell = nbf.v4.new_markdown_cell(source = ["Insert differences in code here"])

for index, cell in nb['cells']:
    if cell.cell_type is "code":
        meta = cell.metadata
        if meta["kernel"] is "Python3":
            nb['cells'].insert(index + 1, insertCell)