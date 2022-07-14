import socket
import os
from dotenv import load_dotenv
from emoji import demojize
import pandas as pd
import csv
import logging
logging.basicConfig(filename="chat.log", filemode="w", format="%(message)s")
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 

load_dotenv()
sock = socket.socket()
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'learndatasci'
token = os.environ.get("OAUTH_TOKEN")
channel = '#adinross'

sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')
messagesFile = open("messages.txt", "w")

while True:
    resp = sock.recv(2048).decode('utf-8')

    if resp.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))
    
    elif len(resp) > 0:

        message = resp.split(f"{channel} :")[-1].strip()
        # for word in message:
        #     logger.info(demojize(message))
        logger.info(demojize(message))
        # logger.info(demojize(resp))
        
     
  


