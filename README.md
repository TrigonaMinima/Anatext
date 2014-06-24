Anatext
=======

External Modules used - 

xlrd - For reading the xlsx files
xlsxwritrer - To write in the xlsx files

extras/trialName : determines the name of companies in a list of companies having individual companies in one list item. [Will try to create a separate module responsible for recognising company names and org names ie NER for companies]

extras/trialEditDist : determines the closest matches of a word from a list of words and their ratio.

extras/files.py : python file containing all the functions in one.

filesNew.py : file containing the necessary functions and other funstions defined in other files.

getData.py : module responsible for reading the data from xlsx file and input them in various lists.

printing.py : module responsible for printing the lists.

accounts.py : module responsible for mapping the comments having the sub-strings 'cd' or 'cc' with the corresponding account numbers. If more then 1 accounts are given then it just writes interconnected, for now. Will change it later.

comp.py : module responsible for mapping direct matches, incomplete direct matches, matches with spelling mistakes in them, matches having sub-strings - 'salary', 'cash', 'atm', 'nfs', 'self', 'various'. Have to implement the method for entities in this module which will extract the unknown entities.

[TODO] identities.py : module responsible for the mapping of unknown entities (direct matches, incomplete direct matches and matches with spelling mistakes) extracted in the comp.py.

commons.py : module having some common functions used in other modules.

[TODO] freq.py : module responsible for calculating the frequencies distribution.