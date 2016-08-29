# Compile and run Scala and Java in one line


import os
import sys

# Usage run <jvm file> <input>

jvm_file = sys.argv[1]
input_file = sys.argv[2]

if "scala" in jvm_file:
    program = "scala"
elif "java" in jvm_file:
    program = "java"

compile_command = "%sc %s" % (program, jvm_file)
run_command = "%s %s" % (program, jvm_file.split(".%s" % program)[0])

if input_file:
    run_command += "< %s" % input_file

print compile_command
print run_command

os.system(compile_command)
os.system(run_command)
