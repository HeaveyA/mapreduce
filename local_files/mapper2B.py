import sys
for line in sys.stdin:
     keyval=line.strip().split("\t")
     keyval= keyval[0]
     if key!="\N" and val!="\N":
        sys.stdout.write('%s\t%s\n' % (keyval))