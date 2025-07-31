# GRU (Gated Recurrent Unit) is designed to solve the limitations of standard RNNs by using gates to control 
# what information is remembered or forgotten across a sequence.
# It’s faster and has fewer parameters than LSTM, but still handles long-term dependencies better than vanilla RNNs.

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GRU, Dense

# Simulated data
vocab_size = 100     # Size of vocabulary (number of unique words/tokens)
sequence_length = 20  # Number of tokens per input sequence
embedding_dim = 16
gru_units = 32
num_classes = 2       # Binary classification

# Generate random data: 1000 sequences with integer tokens
X = np.random.randint(1, vocab_size, size=(1000, sequence_length))
y = np.random.randint(0, 2, size=(1000,))  # Random binary labels

# Define model
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=sequence_length),
    GRU(gru_units, return_sequences=False),
    Dense(num_classes, activation='softmax')  # Use 'sigmoid' for binary (see note below)
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=5, batch_size=32)

# Predict a new sequence
sample = np.random.randint(1, vocab_size, size=(1, sequence_length))
prediction = model.predict(sample)
print("Predicted class probabilities:", prediction)
