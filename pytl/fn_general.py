#**************************************************************************************************
__copyright__ = "in revision"
__credits__ = ["PyTL"]
__license__ = "in revision"
__version__ = "1.0.3"
__status__ = "Testing"
#**************************************************************************************************


import hashlib


def encode(filename):


	print "Please type the csv file name to encrypt without header (Example: mails.csv)"
	filename = raw_input()

	print "Select the SHA hash algorithm. Formato csv y sin encabezado"
	print "1 = sha1"
	print "2 = sha224"							
	print "3 = sha256"
	print "4 = sha384"
	print "5 = sha512"
	election = raw_input()

	if election > "5":
			print "Invalid option"
	else:


		file = open(filename, "r")
		filenameout="encrypted_"+filename
		out = open(filenameout, "w")
		lin = file.read()
		file_lines = lin.split()


		for line in file_lines:
		


			if election == "1":
				m = hashlib.sha1()
				m.update(line)
				m.digest()
				lines = line + " " + m.hexdigest()
				out.writelines(lines+"\n")
				m = 0


			elif election == "2":
				m = hashlib.sha224()
				m.update(line)
				m.digest()
				lines = line + " " + m.hexdigest()
				out.writelines(lines+"\n")
				m = 0


			elif election == "3":
				m = hashlib.sha256()
				m.update(line)
				m.digest()
				lines = line + " " + m.hexdigest()
				out.writelines(lines+"\n")
				m = 0


			elif election == "4":
				m = hashlib.sha384()
				m.update(line)
				m.digest()
				lines = line + " " + m.hexdigest()
				out.writelines(lines+"\n")
				m = 0


			elif election == "5":
				m = hashlib.sha512()
				m.update(line)
				m.digest()
				lines = line + " " + m.hexdigest()
				out.writelines(lines+"\n")
				m = 0


	print "Encrypted File: "+filenameout
	out.close()
	file.close()
				
