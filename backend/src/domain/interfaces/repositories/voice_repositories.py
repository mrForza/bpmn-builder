from abc import ABC


class VoiceStorageRepository(ABC):
    @classmethod
    async def save_file(self, audio_file):
        raise NotImplemented()

    @classmethod
    async def get_all_files(self):
        raise NotImplemented()

    @classmethod
    async def get_file(self):
        raise NotImplemented()


class VoiceDatabaseRepository(ABC):
    @classmethod
    async def save_metadata(self, metadata):
        raise NotImplemented()
    
    @classmethod
    async def get_metadata(self):
        raise NotImplemented()
