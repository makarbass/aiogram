from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from ..types import InputFile
from .base import Request, TelegramMethod

if TYPE_CHECKING:
    from ..client.bot import Bot


class SetStickerSetThumbnail(TelegramMethod[bool]):
    """
    Use this method to set the thumbnail of a regular or mask sticker set. The format of the thumbnail file must match the format of the stickers in the set. Returns :code:`True` on success.

    Source: https://core.telegram.org/bots/api#setstickersetthumbnail
    """

    __returning__ = bool

    name: str
    """Sticker set name"""
    user_id: int
    """User identifier of the sticker set owner"""
    thumbnail: Optional[Union[InputFile, str]] = None
    """A **.WEBP** or **.PNG** image with the thumbnail, must be up to 128 kilobytes in size and have a width and height of exactly 100px, or a **.TGS** animation with a thumbnail up to 32 kilobytes in size (see `https://core.telegram.org/stickers#animated-sticker-requirements <https://core.telegram.org/stickers#animated-sticker-requirements>`_`https://core.telegram.org/stickers#animated-sticker-requirements <https://core.telegram.org/stickers#animated-sticker-requirements>`_ for animated sticker technical requirements), or a **WEBM** video with the thumbnail up to 32 kilobytes in size; see `https://core.telegram.org/stickers#video-sticker-requirements <https://core.telegram.org/stickers#video-sticker-requirements>`_`https://core.telegram.org/stickers#video-sticker-requirements <https://core.telegram.org/stickers#video-sticker-requirements>`_ for video sticker technical requirements. Pass a *file_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. :ref:`More information on Sending Files » <sending-files>`. Animated and video sticker set thumbnails can't be uploaded via HTTP URL. If omitted, then the thumbnail is dropped and the first sticker is used as the thumbnail."""

    def build_request(self, bot: Bot) -> Request:
        data: Dict[str, Any] = self.dict()

        return Request(method="setStickerSetThumbnail", data=data)
