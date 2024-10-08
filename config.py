import configparser
import os


class CleanFileConfig:
    def __int__(self):
        self.age = 10
        self.base_path = ""
        self.config_path = ""
        self.telegram_token =""
        self.telegram_conversation_id = -1
        self.cpu_threshold = 50.0
        self.memory_threshold = 50.0
        self.disk_threshold = 50.0
        self.db_master =""
        self.db_master_db=""
        self.db_master_port= 5432
        self.db_master_user= ""
        self.db_master_password = ""
        self.db_slaves = ""



# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the properties file
CONFIG = CleanFileConfig()
script_dir = os.path.dirname(os.path.abspath(__file__))
CONFIG.config_path = f'{script_dir}/config.properties'
config.read(CONFIG.config_path)
CONFIG.age = int(config['settings']['age'])
CONFIG.base_path = config['settings']['clean_path']
CONFIG.telegram_token = config["telegram"]["token"]
CONFIG.telegram_conversation_id = config["telegram"]["conversation_id"]
CONFIG.cpu_threshold = float(config["monitor"]["cpu_threshold"])
CONFIG.memory_threshold = float(config["monitor"]["memory_threshold"])
CONFIG.disk_threshold = float(config["monitor"]["disk_threshold"])
CONFIG.db_master = config["postgres"]["db_master"]
CONFIG.db_master_user = config["postgres"]["db_master_user"]
CONFIG.db_master_password = config["postgres"]["db_master_password"]
CONFIG.db_master_port = int(config["postgres"]["db_master_port"])
CONFIG.db_master_db= config["postgres"]["db_master_db"]
CONFIG.db_slaves = config["postgres"]["db_slaves"]
