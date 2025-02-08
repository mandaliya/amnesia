# Amnesia - Anonymization Tool

Amnesia is a Python-based tool for k-anonymity and differential privacy. It can be deployed on Google Cloud Run.

## Usage

1. Deploy the app on Google Cloud Run.
2. Send a POST request to `/anonymize` with the following JSON payload:

```json
{
  "data": [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 35, "city": "Los Angeles"}
  ],
  "method": "k_anonymity",
  "columns": ["age", "city"],
  "k": 2
}