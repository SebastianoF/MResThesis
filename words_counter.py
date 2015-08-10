import os
import subprocess


'''
    Counts the words in the manually selected latex files in the list list_file
    
    Commands to obtain the number of words in a .tex file:
    'detex my_file.tex | wc -w'
    where my_file.tex is one of the string in the list list_files
'''

root_project = os.getcwd()

list_files = ["chapters/Ch_introduction.tex",
              "chapters/Ch_tools",
              "chapters/Ch_spatial_transformations",
              "chapters/Ch_log_computations",
              "chapters/Ch_results.tex",
              "chapters/Ch_conclusions.tex"]

pagg = [0]*len(list_files)

for i in range(len(pagg)):
    proc = subprocess.Popen(["detex " + list_files[i] + " | wc -w"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    pagg[i] = int(out)
    print "Number of words in file: " + list_files[i] + " is: " + str(pagg[i])

print "\n Summary:"
print pagg
print "\n Total: " + str(sum(pagg)) + " \n"
print "Thanks for using words count, by Opossum Software Society. \n"