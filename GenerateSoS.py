import nbformat as nbf

nb = nbf.v4.new_notebook(metadata = {
  "kernelspec": {
   "display_name": "SoS",
   "language": "sos",
   "name": "sos"
  },
  "language_info": {
   "codemirror_mode": "sos",
   "file_extension": ".sos",
   "mimetype": "text/x-sos",
   "name": "sos",
   "nbconvert_exporter": "sos_notebook.converter.SoS_Exporter",
   "pygments_lexer": "sos"
  },
  "sos": {
   "kernels": [],
   "panel": {
    "displayed": True,
    "height": 0,
    "style": "side"
   },
   "version": "0.16.10"
  }})



nb['cells'] = [nbf.v4.new_code_cell(cell_type = 'code',
                                    execution_count = None,
                                    metadata = { 'kernel': "Python3" }
                                    )]

nbf.write(nb, 'Auto.ipynb')