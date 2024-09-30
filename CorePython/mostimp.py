import tensorflow as tf
import keras_nlp
from keras_nlp.models import GPT2CausalLM

# Load the pre-trained GPT-2 model
preprocessor = keras_nlp.models.GPT2CausalLMPreprocessor.from_preset("gpt2_base_en")
gpt2_lm = GPT2CausalLM.from_preset("gpt2_base_en", preprocessor=preprocessor)

# Configure the preprocessor
MAX_SEQUENCE_LENGTH = 128  # Define your desired sequence length
preprocessor = keras_nlp.models.GPT2CausalLMPreprocessor.from_preset(
    "gpt2_base_en",
    sequence_length=MAX_SEQUENCE_LENGTH,
    pad_token_id=preprocessor.tokenizer.pad_token_id,
    attention_mask_function=lambda x: keras_nlp.attention_mask_from_sequence_length(x, gpt2_lm.model.decoder.embedding_dim),
)

# Fine-tune the model
# Replace `train_ds` with your actual training dataset
train_ds = (
    # Your training dataset preprocessing steps here
    .map(lambda x, y: preprocessor(x))
    .batch(BATCH_SIZE)
    .cache()
    .prefetch(tf.data.AUTOTUNE)
)

EPOCHS = 10  # Define the number of epochs for fine-tuning

gpt2_lm.fit(
    train_ds,
    epochs=EPOCHS,
    callbacks=[
        # Add any desired callbacks here
        # e.g., GPUMemoryCallback if needed
    ],
)

# Save the fine-tuned model
gpt2_lm.save_pretrained("fine-tuned_gpt2")
