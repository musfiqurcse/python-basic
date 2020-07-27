def map(document_name, document_content):
        for line in document_content:
            words = line.split(" ")
            for word in words:
                EmitIntermediate(word, 1)
    
def reduce(words, counts):
    word_count = 0
    for count in counts: 
        word_count += count
    Emit(word, word_count)

def EmitIntermediate(key, value):
    intermediate[key]+=[value]

def Emit(key, value):
    final_result += [value]
