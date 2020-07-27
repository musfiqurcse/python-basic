def map(document_name, document_content):
        for line in document_content:
            words = line.split(" ")
            for word in words:
                word_length = len(word) #count the length of the wordd
                EmitIntermediate(word_length, 1)
    
def reduce(word_length, counts):
    word_length_count = 0
    for count in counts: 
        word_length_count += count
        Emit(word_length, word_length_count)
        
