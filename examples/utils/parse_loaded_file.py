import opfython.utils.loader as l
import opfython.utils.parser as p

# Loading a .txt file to a dataframe
txt = l.load_txt('data/sample.txt')

# Parsing a pre-loaded dataframe
data = p.parse_df(txt)
