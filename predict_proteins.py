import click
import pickle
import torch
import os
import csv
import time
import torch.nn.functional as F
from transformers import EsmTokenizer

# Загрузка модели и токенизатора
model_save_path = "my_trained_model.pkl"
with open(model_save_path, 'rb') as file:
    loaded_model = pickle.load(file)
tokenizer = EsmTokenizer.from_pretrained("facebook/esm2_t12_35M_UR50D")

def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def predict_protein_sequences(sequences, model, tokenizer):
    tokenized_data = tokenizer(sequences, max_length=1024, truncation=True, padding='max_length', return_tensors='pt')
    with torch.no_grad():
        outputs = model(**tokenized_data)
        probabilities = F.softmax(outputs.logits, dim=1).numpy()
    return probabilities

@click.command()
@click.option('--input_file', type=click.Path(exists=True), help="Path to the input FASTA file containing protein sequences.")
def predict(input_file):
    """Predicts the class probabilities of protein sequences."""
    start_time = time.time()
    sequences = read_fasta(input_file)
    probabilities = predict_protein_sequences(sequences, loaded_model, tokenizer)
    script_path = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(script_path, 'output.csv')

    with open(output_file, 'w', newline='') as file:
        fieldnames = ['ID', 'Sequence', 'non-T6SE', 'T6SE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i, seq_prob in enumerate(probabilities):
            writer.writerow({
                'ID': i + 1,
                'Sequence': sequences[i],
                'non-T6SE': seq_prob[0],
                'T6SE': seq_prob[1]
            })
    end_time = time.time()
    elapsed_time = end_time - start_time #(end_time - start_time) / 60
    print(f"Время выполнения: {elapsed_time:.2f} секунд")


if __name__ == '__main__':
    predict()
