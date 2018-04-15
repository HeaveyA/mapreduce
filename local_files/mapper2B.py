import sys
for line in sys.stdin:
     keyval=line.strip().split("\t")
     keyval= keyval[0]
     if keyval!="\N":
        sys.stdout.write('%s\n' % (keyval))