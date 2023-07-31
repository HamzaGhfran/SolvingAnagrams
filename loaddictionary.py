"""Code to read dictionary file and then load it into a list"""
import sys
def load(file):
    """load the dictionary file and after read return list of words"""
    try:
        with open(file) as in_file:
            load_text = in_file.read().strip().split()
            load_text = [x.lower() for x in load_text]
            return load_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),file=sys.stderr)
        sys.exit()