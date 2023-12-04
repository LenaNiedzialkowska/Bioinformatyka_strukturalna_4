from modeller import *
from modeller.automodel import *
env = Environ()
env.io.atom_files_directory = ['.', './atom_files']
a = AutoModel(env, alnfile='aln-clustal.txt',
knowns=(('4WIH'), ('4AE6'), ('1CTP')), sequence='model')
a.starting_model = 1
a.ending_model = 5
a.make()
a.write("model.pdb")
