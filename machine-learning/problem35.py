''''
kaggle llm challenge
Large language models (LLMs) are rapidly entering our lives, but ensuring their responses resonate with users is critical for successful interaction.

In this competition, you'll receive a large multilingual dataset from the Chatbot Arena (formerly LMSYS),
 where users chat with two anonymous LLMs and select their preferred answer. Your challenge is to develop a machine learning model that accurately predicts user preferences.

'''

import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from transformers import XLMRobertaTokenizer, XLMRobertaModel
from torch.utils.data import Dataset, DataLoader
from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, f1_score
import torch.nn as nn

# 1. Data Loading and Preprocessing
df = pd.read_csv('chatbot_arena_dataset.csv')  # Replace with your actual file path
df['label'] = df['preferred'].apply(lambda x: 0 if x == 'a' else 1)

# 2. Dataset Preparation
class PreferenceDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_length=512):
        self.df = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        user_query = row['user_query']
        response_a = row['response_a']
        response_b = row['response_b']
        label = row['label']

        text_a = user_query + " " + response_a
        text_b = user_query + " " + response_b

        encoding_a = self.tokenizer(
            text_a,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        encoding_b = self.tokenizer(
            text_b,
            add_special_tokens=True,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        input_ids_a = encoding_a['input_ids'].squeeze()
        attention_mask_a = encoding_a['attention_mask'].squeeze()

        input_ids_b = encoding_b['input_ids'].squeeze()
        attention_mask_b = encoding_b['attention_mask'].squeeze()

        return {
            'input_ids_a': input_ids_a,
            'attention_mask_a': attention_mask_a,
            'input_ids_b': input_ids_b,
            'attention_mask_b': attention_mask_b,
            'labels': torch.tensor(label, dtype=torch.long)
        }

# 3. Model Definition
class PreferenceModel(nn.Module):
    def __init__(self, model_name='xlm-roberta-base'):
        super(PreferenceModel, self).__init__()
        self.model_a = XLMRobertaModel.from_pretrained(model_name)
        self.model_b = XLMRobertaModel.from_pretrained(model_name)
        self.classifier = nn.Sequential(
            nn.Linear(self.model_a.config.hidden_size * 2, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 2)
        )

    def forward(self, input_ids_a, attention_mask_a, input_ids_b, attention_mask_b):
        outputs_a = self.model_a(input_ids=input_ids_a, attention_mask=attention_mask_a)
        outputs_b = self.model_b(input_ids=input_ids_b, attention_mask=attention_mask_b)
        
        cls_a = outputs_a.last_hidden_state[:, 0, :]
        cls_b = outputs_b.last_hidden_state[:, 0, :]
        
        combined = torch.cat((cls_a, cls_b), dim=1)
        logits = self.classifier(combined)
        return logits

# 4. Training Setup
tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')
train_df, eval_df = train_test_split(df, test_size=0.1, random_state=42, stratify=df['label'])
train_dataset = PreferenceDataset(train_df, tokenizer)
eval_dataset = PreferenceDataset(eval_df, tokenizer)
model = PreferenceModel('xlm-roberta-base')

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    evaluation_strategy='epoch',
    logging_dir='./logs',
    logging_steps=100,
    save_total_limit=2,
    load_best_model_at_end=True,
    metric_for_best_model='accuracy'
)

def compute_metrics(pred):
    labels = pred.label_ids
    preds = np.argmax(pred.predictions, axis=1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds)
    return {'accuracy': acc, 'f1': f1}

def collate_fn(batch):
    input_ids_a = torch.stack([item['input_ids_a'] for item in batch])
    attention_mask_a = torch.stack([item['attention_mask_a'] for item in batch])
    input_ids_b = torch.stack([item['input_ids_b'] for item in batch])
    attention_mask_b = torch.stack([item['attention_mask_b'] for item in batch])
    labels = torch.stack([item['labels'] for item in batch])

    return {
        'input_ids_a': input_ids_a,
        'attention_mask_a': attention_mask_a,
        'input_ids_b': input_ids_b,
        'attention_mask_b': attention_mask_b,
        'labels': labels
    }

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    compute_metrics=compute_metrics,
    tokenizer=tokenizer,
    data_collator=collate_fn
)

# 5. Training
trainer.train()

# 6. Evaluation
eval_results = trainer.evaluate()
print(f"Validation Accuracy: {eval_results['eval_accuracy']:.4f}")
print(f"Validation F1 Score: {eval_results['eval_f1']:.4f}")

# 7. Save the Best Model
trainer.save_model('./best_preference_model')
tokenizer.save_pretrained('./best_preference_model')
