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

### Environment Setup
Create a virtual environment and install dependencies:

```bash
# Create project directory
mkdir spaiware_poc
cd spaiware_poc

# Create virtual environment
python3 -m venv venv

# Activate environment (Linux/Mac)
source venv/bin/activate

# Activate environment (Windows)
# venv\Scripts\activate

# Install required libraries
pip install flask psycopg2-binary
