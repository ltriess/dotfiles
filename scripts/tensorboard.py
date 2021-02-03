import os
import sys

args = sys.argv
idx = args.index("--")

cmd = "tensorboard "
cmd += " ".join(args[1:idx])
cmd += " --logdir "
cmd += ",".join([(d + ":" + d) for d in args[idx+1:]])

os.system(cmd)

