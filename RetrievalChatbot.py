import math

class RetrievalChatbot:
    """Retrieval-based chatbot using BM25 algorithm"""
    
    def __init__(self, dialogue_file):
        """Given a corpus of dialoge utterances (one per line), computes the
        document frequencies and average document length"""
        
        # We store all utterances (as lists of lowercased tokens)
        self.utterances = []
        fd = open(dialogue_file)
        for line in fd:
            utterance = self._tokenise(line.rstrip("\n"))
            self.utterances.append(utterance)
        fd.close()
        
        self.doc_freqs = self._compute_doc_frequencies()
        self.avg_len = self._compute_average_document_length()
        self.k1 = 1.5
        self.b = 0.75

        
    def _tokenise(self, utterance):
        """Convert an utterance to lowercase and tokenise it by splitting on space"""
        return utterance.strip().lower().split()
    
    def _compute_doc_frequencies(self):
        """Compute the document frequencies (necessary for IDF)"""
        
        doc_freqs = {}
        for utterance in self.utterances:
            for word in set(utterance):
                doc_freqs[word] = doc_freqs.get(word, 0) + 1
        return doc_freqs
    
    def _compute_average_document_length(self):
        """Compute the average document length"""
        
        total_len = sum(len(utterance) for utterance in self.utterances)
        return total_len / len(self.utterances)
    
    def get_bm25_score(self, query, utterance):
        """Compute the BM25 score between the query and an utterance"""
        
        tf_weight = {}
        for word in query:
            tf_weight[word] = (self.k1 + 1) * utterance.count(word) / (self.k1 * ((1 - self.b) + self.b * len(utterance) / self.avg_len) + utterance.count(word))
        
        bm25_score = 0
        for word in query:
            if word in self.doc_freqs:
                idf = math.log((len(self.utterances) - self.doc_freqs[word] + 0.5) / (self.doc_freqs[word] + 0.5))
                bm25_score += idf * tf_weight[word]
                
        return bm25_score
    
    def get_response(self, query):
        """ 
        Finds out the utterance in the corpus that has the highest BM25 score
        with respect to the query and returns that utterance. 
        """
        
        # If the query is a string, we first tokenise it
        if isinstance(query, str):
            query = self._tokenise(query)
        
        best_score = -1
        best_utterance = None
        
        # Iterate over all utterances in the corpus
        for utterance in self.utterances:
            score = self.get_bm25_score(query, utterance)
            if score > best_score:
                best_score = score
                best_utterance = utterance
        
        return ' '.join(best_utterance)
