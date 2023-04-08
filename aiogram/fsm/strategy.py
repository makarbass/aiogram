from enum import Enum, auto
from typing import Optional, Tuple


class FSMStrategy(Enum):
    USER_IN_CHAT = auto()
    CHAT = auto()
    GLOBAL_USER = auto()
    USER_IN_THREAD = auto()


def apply_strategy(
    strategy: FSMStrategy,
    chat_id: int,
    user_id: int,
    thread_id: int | None = None,
) -> Tuple[int, int, Optional[int]]:
    if strategy == FSMStrategy.CHAT:
        return chat_id, chat_id, None
    if strategy == FSMStrategy.GLOBAL_USER:
        return user_id, user_id, None
    if strategy == FSMStrategy.USER_IN_THREAD:
        return user_id, chat_id, thread_id
    return chat_id, user_id, None
