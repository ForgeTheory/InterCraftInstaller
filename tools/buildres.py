from pathlib import Path
import base64
import sys

def readFileBase64(path):
	f = open(path, 'rb')
	data = base64.b64encode(f.read())
	f.close()
	return data


def readFiles(directory, extensions):
	fileList = {}
	for extension in extensions:
		pathList = Path(directory).glob('**/*.' + extension)
		for path in pathList:
			pathName = str(path)[len(directory):].replace('\\', '/')
			if pathName.startswith('/'):
				pathName = pathName[1:]
			print("Building file:", pathName)
			fileList[pathName] = readFileBase64(str(path))

	return fileList


def buildPyFile(resDir, outputFile, extensions):
	
	fileList = readFiles(resDir, extensions)

	f = open(outputFile, 'w')
	f.write('import base64\n')
	f.write('\n')
	f.write('fileList = ' + str(fileList) + '\n')
	f.write('\n')
	f.write('def read(name):\n')
	f.write('\treturn base64.b64decode(fileList[name])\n')
	f.close()


def main(argv):

	extensions = ['ico', 'png']

	inputDir = argv[1]
	outputFile = argv[2]
	
	buildPyFile(inputDir, outputFile, extensions)


if __name__ == '__main__':
	main(sys.argv)