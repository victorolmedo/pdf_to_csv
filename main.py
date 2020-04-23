import tabula
import requests

# read all pdf file into list of DataFram
#df = tabula.read_pdf("petroparFuncionarios.pdf", pages='all')

# read remote pdf into list of DataFrame
#df = tabula.read_pdf("petroparFuncionarios.pdf", pages='all')

# convert PDF into CSV file
tabula.convert_into("petroparFuncionarios.pdf","petroparFuncionarios.csv",output_format="csv",pages="all")

#convert all PDFs in a directory
tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')

