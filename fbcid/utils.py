"""Set of some utilities"""

from pathlib import Path
from enum import Enum
import os
import wget

class AttachmentType(Enum):
    """Attachment types"""
    IMAGE = 0
    VIDEO = 1

def print_logo():
    """Print FBCID logo"""
    print('█▀▀ █▄▄ █▀▀ █ █▀▄')
    print('█▀  █▄█ █▄▄ █ █▄▀')

def download_attachment(url, filename, user, attachment_type):
    """Downloads the attachment to its directory, creates it if necessary"""
    data_path = Path(os.path.dirname(__file__)).parent/"Downloads"/str(user)
    data_path.mkdir(parents=True, exist_ok=True)

    images_path = data_path/"Images"
    videos_path = data_path/"Videos"

    Path(images_path).mkdir(exist_ok=True)
    Path(videos_path).mkdir(exist_ok=True)

    if attachment_type == AttachmentType.IMAGE:
        wget.download(url, str(images_path/filename))
    if attachment_type == AttachmentType.VIDEO:
        wget.download(url, str(videos_path/filename))
