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

nb['cells'] = [nbf.v4.new_markdown_cell(source = ["""<html>

<head>

</head>

<body>

    <div class="row">
        <div class="column" style="border: 1px solid black;">
            <b>Incorrect 1</b>

            <p>data[is.na(data$Embarked)]</p>

            <p>
                <font size="3" color="red">Operation returns an error:</font>
            </p>

            <br>

            <code>Error in '[.data.frame'(train, is.na(train$Embarked) == TRUE): undefined columns selected</code>

            <p>

                <font size="4">WHY:
                    <br>
                    <br> Column subsetting is attempted when there is no comma after
                    <code>is.na(data$Embarked)</code>.
                    <br>
                    <br> This results in column subsetting for columns that might be undefined.</font>

            </p>
        </div>
        <div class="column" style="border: 1px solid black;">
            <b>Incorrect 2</b>

            <p>data[data$Embarked == NA]</p>

            <p>
                <font size="3" color="red">The value of NA is filled for all row values:</font>
            </p>

            <table class="tg">
                <tr>
                    <th class="tg-ohoh"></th>
                    <th class="tg-3ij2">Name</th>
                    <th class="tg-3ij2">Survived</th>
                </tr>
                <tr>
                    <td class="tg-kn9s">NA</td>
                    <td class="tg-7cxr">NA</td>
                    <td class="tg-7cxr">NA</td>
                </tr>
                <tr>
                    <td class="tg-kn9s">NA.1</td>
                    <td class="tg-7cxr">NA</td>
                    <td class="tg-7cxr">NA</td>
                </tr>
                <tr>
                    <td class="tg-kn9s">...</td>
                    <td class="tg-7cxr">...</td>
                    <td class="tg-7cxr">...</td>
                </tr>
                <tr>
                    <td class="tg-kn9s">NA.n</td>
                    <td class="tg-7cxr">NA</td>
                    <td class="tg-7cxr">NA</td>
                </tr>
            </table>

            <p>

                <font size="4">WHY:
                    <br>
                    <br> Missing values (NA) are regarded as non-comparable. Comparisons involving them will always result in
                    NA.
                    <br>
                    <br>
                </font>

            </p>
        </div>
        <div class="column" style="border: 1px solid black;">
            <b>Incorrect 3</b>

            <p>data[na.omit(data$Embarked == NA), ]</p>

            <p>
                <font size="3" color="red">Operation returns 0 rows:</font>
            </p>

            <table class="tg">
                <tr>
                    <th class="tg-ohoh"></th>
                    <th class="tg-3ij2">Name</th>
                    <th class="tg-3ij2">Survived</th>
                </tr>
            </table>

            <p>

                <font size="4">WHY:
                    <br>
                    <br> Result of
                    <code>data$Embarked == NA</code> all have value NA. The
                    <code>na.omit</code> removes all occurrences of rows with NA.
                    <br>
                    <br>
                </font>

            </p>
        </div>
    </div>

</body>

</html>"""])]
# Python cell
nb['cells'].append(nbf.v4.new_code_cell(
  source = "print(\"hello\")", 
  metadata = { 'kernel': "Python3" }))
# R cell
nb['cells'].append(nbf.v4.new_code_cell(
  source = "x <- 2\nx", 
  metadata = { 'kernel': "R" }))
  


nbf.write(nb, 'TestFullyFunctionalHTMLExample.ipynb')