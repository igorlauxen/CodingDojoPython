WORDS = ["a", "b", "c"]

class Diamond:
    def __init__(self, letter):
        self.letter = letter

    def getLetter(self):
        return self.letter

    def draw(self):
        if self.letter not in WORDS:
            raise Exception("No word found")

        wordIndex = WORDS.index(self.letter)
        result = self.drawTop(wordIndex)
        result += self.drawBottom(wordIndex)

        return result

    def drawTop(self, wordIndex):
        counter = 0
        result = ""
        while (counter < wordIndex):
            if counter == 0:
                result = WORDS[0] + "\n"
            else:
                result = result + self.getLine(counter)
            counter  += 1
        return result

    def drawBottom(self, wordIndex):
        result = ""
        while (wordIndex >= 0):
            if (wordIndex == 0):
                result = result + WORDS[wordIndex]
            else:
                result = result + self.getLine(wordIndex)
            wordIndex -= 1
        return result

    def getLine(self, index):
        word = WORDS[index]

        if index == 0:
            return word
        else:
            return word + self.drawSpaces(index) + word + "\n"

        return result

    def drawSpaces(self, size):
        result = ""
        x = 0
        lessThan =  size  if size%2 == 0 else size-1
        while (x <= lessThan):
            result += " "
            x += 1
        return result