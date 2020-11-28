import transformers

DEVICE = "cuda"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
# BERT_PATH = "input/bert-base-uncased/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "input/imdb.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
