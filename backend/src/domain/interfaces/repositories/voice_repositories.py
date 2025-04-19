from abc import ABC, abstractmethod


class VoiceStorageRepository(ABC):
    @abstractmethod
    async def save_file(self, audio_file):
        raise NotImplementedError

    @abstractmethod
    async def get_all_files(self):
        raise NotImplementedError

    @abstractmethod
    async def get_file(self):
        raise NotImplementedError


class VoiceDatabaseRepository(ABC):
    @abstractmethod
    async def save_metadata(self, metadata):
        raise NotImplementedError

    @abstractmethod
    async def get_metadata(self):
        raise NotImplementedError
