from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5227462308:AAGxHrd_77vtCo9vuZ9AacI8p3gU5ijE4io"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001102718567]# List of chat id's to forward messages from.
    TO_CHATS = [-1001439901698]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
