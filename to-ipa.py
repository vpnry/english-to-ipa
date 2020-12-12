# Convert English text to IPA using: eng_to_ipa
# @pnry - version 0.0.2
# Last modified: 12 Dec 2020

# Usage: 
# toIPA(f, 1) # insert IPA paragraphs follows English paragraphs
# toIPA(f, 0) # insert IPA transcription next to each word
# In Terminal:
# python3 to-ipa.py test.txt 0 
# python3 to-ipa.py test.txt 1



import sys
args = sys.argv


#----------------------------------------------
import eng_to_ipa as ipa # pip3 install eng_to_ipa
import time

def toIPA(f, y=1):
    t1 = time.time()
    writ = ""

    print("Transcripting "+ f +" to IPA ")
    print("It may take a while, please wait...")
    print("")
    with open(f, 'r') as t:
        tex = t.read()
        tex = tex.strip()
        
        tex = tex.replace("\n"," p15081553y ")
        ip = ipa.convert(tex)
        
        tex = tex.split(" p15081553y ")
        ip = ip.split("p15081553y*")
        para = len(tex)

        print("Total: " +  str(para)+ " paragraphs" )
        
        if y == 1:
            print("Inserting IPA paragraphs follows English paragraphs")
            for i in range(para):
                print("Processing par no.: " +  str(i+1))
                writ += "[" + str(i+1) +"] " + tex[i].strip() + "\n\n" + "[" + str(i+1) +"] " + ip[i].strip()
                writ += "\n\n"
        ###
        else:
            print("Inserting IPA next to each word")
            for i in range(para):
                print("Processing par no.: " +  str(i+1))
                enp = tex[i].strip().split(" ")
                ipp = ip[i].strip().split(" ")
                for k in range(len(enp)):
                    writ += enp[k] + "[" + ipp[k] + "]  "
                writ += "\n\n"
        ###
        with open('_ipa_' + f, 'w') as p:
            p.write(writ)
        print("")
        print("#-----------------------")
        print("Done!")
        print("Took: " + str((time.time() - t1)) + " seconds")
        print("#-----------------------")
        
#------------------- TEST ---------------------

#-------------------- CLI ---------------------
# CLI tips, more here: https://stackoverflow.com/a/65108366

if __name__ == "__main__":
  # args: array. 0 = filename
  # From 1 forward, what ever follows after the filename
  # (*expand)
  if len(args[1:]) > 0:
    print("Usong CLI mode")
    globals()["toIPA"](*args[1:])
  else:
    print("Using function call")
    toIPA("input.txt", 1)
    

  