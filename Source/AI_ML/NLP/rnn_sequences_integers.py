# RNN - Recurrent Neural Network to handle sequential data, where order and context matter.
# RNNs have loops inside their architecture, that allows to remember information from previous steps in the sequence.
# RNN - vanishing gradients limitations, use LSTM and GRU to fix this.

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

# Parameters
vocab_size = 50      # Number of distinct tokens (like words)
max_len = 10         # Length of each input sequence
embedding_dim = 8    # Size of embedding vectors
rnn_units = 16       # Number of units in RNN layer
num_classes = 2      # Number of output classes

# Generate dummy data: 1000 sequences of length max_len with integers 1..vocab_size
X = np.random.randint(1, vocab_size, size=(1000, max_len))
# Dummy binary labels (0 or 1)
y = np.random.randint(0, 2, size=(1000,))

# Build model
model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_len),
    SimpleRNN(rnn_units, activation='tanh'),
    Dense(num_classes, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
model.fit(X, y, epochs=5, batch_size=32)

# Predict example
sample_input = np.random.randint(1, vocab_size, size=(1, max_len))
prediction = model.predict(sample_input)
print("Predicted class probabilities:", prediction)
