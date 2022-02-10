from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5252527313:AAESwCnQis-4hjKulln4JLbNyYH_k_WGfaA"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001792138222,-1001352576623]# List of chat id's to forward messages from.
    TO_CHATS = [-1001766840002]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
