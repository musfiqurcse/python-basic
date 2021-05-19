def map(document_name, document_content):
        for link in document_content:
            EmitIntermediate(link, 1)
            
def reduce(link, values):
    result = 0
    for v in values: 
        result += v
        Emit(link, result)
