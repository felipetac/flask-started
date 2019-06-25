import re

def role_name(text):
        text = re.sub("-", "_", text.strip())
        return re.sub("\W", "_", text).lower()
