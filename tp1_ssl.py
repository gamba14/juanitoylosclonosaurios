#!/usr/bin/python

import os.path
import fileinput
import sys, getopt


# {0,1,2}
# {a,b}
# {0}
# {1,2}
# 0a1b2&0#
# 1a1b0#
# 2a2b2#
# de la linea 1 a 4 se dan los elementos fijos que son 
# linea 1 : el conjunto de estado
# linea 2: el conjunto de entradas
# linea 3 : el estado inicial
# linea 4 : los estados aceptados

def parseStates(asf, line):
    """ Parse the line with the states"""
    pass


def parseInputs(asf, line):
    """ Parse the line with the inputs"""
    pass


def parseInitState(asf, line):
    """ Parse the line with the Init state"""
    pass


def parseFinalStates(asf, line):
    """ Parse the line with the final/accepted states"""
    pass


def parseTransition(asf, line):
    """ Parse one line with a part of the transition function """
    pass


def parseFile(path):
    """Parse the file, path must be the path to a existing text file"""

    # automata
    asf = { 
        "states": set([]),
        "inputs": set([]),
        "init": 0,
        "final": set([]),
        "transtion": []
    }

    # define a dictionary becase are cool and don't have a swith case 
    parsers = {
        0: parseStates,
        1: parseInputs,
        2: parseInitState,
        3: parseFinalStates
    }

    # read each line in the file and parse it
    for lineNumber, line in enumerate(fileinput.input(path)):
        parser = parsers.get(lineNumber, parseTransition)
        parser(asf, line)

    # return the automata
    return asf


def cllambda (estados):
	""" Funcion clausura lambda """
    l=estados
    while length(l) > 0: #aca quiero asumir que la lista l se ira consumiendo a medida que itere
    	estados.pop([])


def mover (estado,sigma): #sea sigma un elemento de sigma :P
	""" funcion mover """
	pass
    

def isValid(asd, input):
    """Check if the input string is acepted by the Automata"""
    #TODO: implementar, devolver True o False
    pass


def main(argv):
    """Main process"""

    path = ""
    inputString = ""
    withString  = False

    # Parse arguments
    try:
        opts, args = getopt.getopt(argv,"ha:s:",["automata=","string="])

    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>' #TODO: cambiar
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>' #TODO: cambiar
            sys.exit()

        elif opt in ("-a", "--automata"):
            path = arg

        elif opt in ("-s", "--string"):
            inputString = arg
            withString  = True

    # Parse the file if exist
    if (os.path.exists(path) && os.path.isfile(path))
        asf = parseFile(path)
    else
        print "El archivo no es valido" # TODO: mejorar mensaje de error

    if (withString)
        if (isValid(asf, inputString))
            print "La cadena es aceptada por el automata" #TODO: mejorar el mensaje
        else
            print "La cadena NO es aceptada por el automata" #TODO: mejorar el mensaje
    else
        # TODO: leer la cadena que ingresa el usuario y chekear si la acepta el automata
        print "implementame (?)"


if __name__ == "__main__":
    # the code being run directly, other wise is imported
    if __name__ == "__main__":
        main(sys.argv[1:])
    