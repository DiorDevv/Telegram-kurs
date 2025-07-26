from .group import register_group_handlers
from .user import register_user_handlers

def register_handlers(dp):
    register_group_handlers(dp)
    register_user_handlers(dp)
