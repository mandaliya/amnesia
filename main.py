from flask import Flask, request, jsonify
import pandas as pd
import anonypy
import pyarrow as pa

app = Flask(__name__)

# Helper function for k-anonymity
def k_anonymize(df, columns, k):
    anonymized = anonypy.Anonymizer(df, columns, k).anonymize()
    return anonymized

# Helper function for differential privacy
def differential_privacy(df, column, epsilon):
    # Simple Laplace mechanism for differential privacy
    scale = 1.0 / epsilon
    noise = pd.Series(np.random.laplace(0, scale, len(df)))
    df[column] = df[column] + noise
    return df

@app.route('/anonymize', methods=['POST'])
def anonymize():
    data = request.json
    df = pd.DataFrame(data['data'])
    method = data.get('method', 'k_anonymity')
    
    if method == 'k_anonymity':
        columns = data.get('columns', [])
        k = data.get('k', 2)
        result = k_anonymize(df, columns, k)
    elif method == 'differential_privacy':
        column = data.get('column', '')
        epsilon = data.get('epsilon', 1.0)
        result = differential_privacy(df, column, epsilon)
    else:
        return jsonify({"error": "Invalid method"}), 400
    
    return jsonify(result.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))