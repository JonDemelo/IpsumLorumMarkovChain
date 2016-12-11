# Making a basic Markov Chain Text Generator for Lorum Ipsum.
import random, re

def getTextInput(textFile):
    textSource = open(textFile, 'r'); # Associate file at location.
    return textSource.read() # Read file.

def buildGenerator(textFile, order):
    textInput = getTextInput(textFile) # IO File
    markovDict = {} # New Markov Dictionary.

    for index in range(0, len(textInput) - order): # Build out Markov Sets.
        end = index + order
        key = textInput[index:end].lower()
        if(key in markovDict):
            pass
        else: # New List at dictionary key-value pair.
            markovDict[key] = []
        markovDict[key].append(textInput[end:end+1].lower()) # Add to list.

    return markovDict

def generateText(generator, exportedLength, order, start=None):
    # Build Start of text.
    if start is None:
        current = random.choice(generator.keys()) # Random key start.
    else:
        current = start # Starts with optional argument.

    # Use start text on generator to continue until end of desired length.
    for index in range(0, exportedLength-order):
        lastOrderSet = current[-order:]
        if lastOrderSet in generator: # Next set of probablistic Markov options.
            currentMarkovList = generator[lastOrderSet]
        else: # Markov Order Set does not exist in training text, therefore end.
            break
        current = current + random.choice(currentMarkovList) # Random pick.

    return current

def cleanUpText(generatedText):
    if generatedText[-1:] is ' ': # Remove Trailing Whitespace.
        generatedText = generatedText[:-1]

    if generatedText[-1:] is not '.': # Add sentence ending period.
        generatedText = generatedText + '.'

    # Capitalize starts of new sentences.
    p = re.compile(r'((?<=[\.\?!]\s)(\w+)|(^\w+))')

    def cap(match):
         return(match.group().capitalize())

    generatedText = p.sub(cap, generatedText)

    return generatedText

if __name__ == "__main__":
    # User adjustable arguments.
    textFile = "ipsum.txt" # Training text.
    order = 4 # Markov order key size.
    exportLength = 200  # Max length of generated text.

    generator = buildGenerator(textFile, order)
    generatedText = generateText(generator, exportLength, order, "Lorum Ipsum")
    cleanedText = cleanUpText(generatedText)

    print("Generated text: \n\n" + cleanedText + '\n') # To console.
