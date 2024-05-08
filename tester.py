import math
class Chatbot:
    """Retrieval-based chatbot using TF-IDF vectors"""
    
    def __init__(self, dialogue_file):
        """Given a corpus of dialoge utterances (one per line), computes the
        document frequencies and TF-IDF vectors for each utterance"""
        
        # We store all utterances (as lists of lowercased tokens)
        self.utterances = []
        fd = open(dialogue_file)
        for line in fd:
            utterance = self._tokenise(line.rstrip("\n"))
            self.utterances.append(utterance)
        fd.close()
        
        self.doc_freqs = self._compute_doc_frequencies()
        self.tf_idfs = [self.get_tf_idf(utterance) for utterance in self.utterances]

        
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

    
    def get_tf_idf(self, utterance):
        """Compute the TF-IDF vector of an utterance. The vector can be represented 
        as a dictionary mapping words to TF-IDF scores."""
         
        tf_idf_vals = {}
        word_counts = {word:utterance.count(word) for word in utterance}
        for word, count in word_counts.items():
            idf = math.log(len(self.utterances)/(self.doc_freqs.get(word,0) + 1))
            tf_idf_vals[word] = count * idf
        return tf_idf_vals
    
    def get_response(self, query):
        """
        Finds out the utterance in the corpus that is closest to the query
        (based on cosine similarity with TF-IDF vectors) and returns the 
        utterance following it. 
        """

        # If the query is a string, we first tokenize it
        if type(query) == str:
            query = self._tokenise(query)

        # Initialize variables to store the best similarity and its corresponding index
        best_similarity = -1
        best_index = -1

        # Compute the TF-IDF vector for the query
        query_tf_idf = self.get_tf_idf(query)

        # Iterate over all utterances in the corpus
        for i, utterance_tf_idf in enumerate(self.tf_idfs):
            # Compute the cosine similarity between the query and the current utterance
            similarity = self.compute_cosine(utterance_tf_idf, query_tf_idf)
            # Update the best similarity and its corresponding index if necessary
            if similarity > best_similarity:
                best_similarity = similarity
                best_index = i

        # Return the utterance following the most similar utterance
        return ' '.join(self.utterances[best_index + 1])
    
    def compute_cosine(self, tf_idf1, tf_idf2):
        """Computes the cosine similarity between two vectors"""
        
        dotproduct = 0
        for word, tf_idf_val in tf_idf1.items():
            if word in tf_idf2:
                dotproduct += tf_idf_val*tf_idf2[word]
                
        return dotproduct / (self._get_norm(tf_idf1) * self._get_norm(tf_idf2))
    
    def _get_norm(self, tf_idf):
        """Compute the vector norm"""
        
        return math.sqrt(sum([v**2 for v in tf_idf.values()]))

