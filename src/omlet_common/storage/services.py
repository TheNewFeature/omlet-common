import os
import uuid
from typing import Iterable, Optional

import minio
from minio import Minio

from omlet_common.storage.models import Artifact, Checkpoint, Dataset
from omlet_common.storage.utils import Progress


class BaseStorage:
    def get(self, object_name: str, file_path: str, bucket_name: str):
        raise NotImplementedError()

    def put(self, file_path: str, object_name: str, bucket_name: str):
        raise NotImplementedError()

    def exists(self, object_name: str, bucket_name: str, version_id: Optional[str] = None):
        raise NotImplementedError()

    def delete(self, object_names: Iterable[str], bucket_name: str):
        raise NotImplementedError()


class MinioStorage(BaseStorage):
    def __init__(self, endpoint: str, access_key: str, secret_key: str, port: int = 9000, secure: bool = False):
        super(MinioStorage, self).__init__()
        self._client = Minio(f'{endpoint}:{port}', access_key=access_key, secret_key=secret_key, secure=secure)

    def get(self, object_name: str, file_path: str, bucket_name: str = 'omlet') -> Optional[minio.datatypes.Object]:
        try:
            return self._client.fget_object(bucket_name, object_name, file_path=file_path, version_id=None)
        except minio.error.S3Error:
            return None

    def put(self, file_path: str, object_name: str, bucket_name: str = 'omlet'):
        if not self._client.bucket_exists(bucket_name):
            self._client.make_bucket(bucket_name)
        return self._client.fput_object(bucket_name, object_name, file_path=file_path, progress=Progress())

    def exists(self, object_name: str, bucket_name: str = 'omlet', version_id: Optional[str] = None):
        try:
            self._client.stat_object(bucket_name=bucket_name, object_name=object_name, version_id=version_id)
        except minio.error.S3Error:
            return False
        return True

    def delete(self, object_names: Iterable[str], bucket_name: str = 'omlet'):
        try:
            for object_name in object_names:
                self._client.remove_object(bucket_name, object_name, version_id=None)
        except minio.error.S3Error:
            pass


class BaseStorageService:
    def __init__(self, storage: BaseStorage):
        self._storage = storage

    def get(self, object_name: str, file_path: str, bucket_name: str = 'omlet'):
        raise NotImplementedError()

    def put(self, file_path: str, object_name: str, bucket_name: str = 'omlet'):
        raise NotImplementedError()

    def exists(self, object_name: str, bucket_name: str = 'omlet', version_id: Optional[str] = None):
        return self._storage.exists(object_name=object_name, bucket_name=bucket_name, version_id=version_id)

    def delete(self, object_names: Iterable[str], bucket_name: str = 'omlet'):
        self._storage.delete(object_names=object_names, bucket_name=bucket_name)


class ArtifactStorageService(BaseStorageService):
    def __init__(self, storage: BaseStorage):
        super(ArtifactStorageService, self).__init__(storage)

    def get(self, object_name: str, file_path: str, bucket_name: str = 'artifacts') -> Optional[minio.datatypes.Object]:
        return self._storage.get(object_name=object_name, file_path=file_path, bucket_name=bucket_name)

    def put(self, file_path: str, object_name: Optional[str] = None, bucket_name: str = 'artifacts') -> Artifact:
        object_name = str(uuid.uuid4())     # + os.path.splitext(file_path)[-1]
        result = self._storage.put(file_path=file_path, object_name=object_name, bucket_name=bucket_name)
        return Artifact(etag=result.etag, object_name=result.object_name, version_id=result.version_id)

    def exists(self, object_name: str, bucket_name: str = 'artifacts', version_id: Optional[str] = None):
        return super(ArtifactStorageService, self).exists(object_name=object_name, bucket_name=bucket_name, version_id=version_id)

    def delete(self, object_name: str):
        super(ArtifactStorageService, self).delete(object_name, bucket_name='artifacts')


class CheckpointStorageService(BaseStorageService):
    def __init__(self, storage: BaseStorage):
        super(CheckpointStorageService, self).__init__(storage)

    def get(self, object_name: str, file_path: str, bucket_name: str = 'checkpoints') -> Optional[minio.datatypes.Object]:
        return self._storage.get(object_name=object_name, file_path=file_path, bucket_name=bucket_name)

    def put(self, file_path: str, episode: int, session_id: int, object_name: Optional[str] = None, bucket_name: str = 'checkpoints') -> Checkpoint:
        object_name = str(uuid.uuid4())     # + os.path.splitext(file_path)[-1]
        result = self._storage.put(file_path=file_path, object_name=object_name, bucket_name=bucket_name)
        return Checkpoint(object_name=result.object_name, etag=result.etag, episode=episode, session_id=session_id)

    def exists(self, object_name: str, bucket_name: str = 'checkpoints', version_id: Optional[str] = None):
        return super(CheckpointStorageService, self).exists(object_name=object_name, bucket_name=bucket_name, version_id=version_id)

    def delete(self, object_names: Iterable[str]):
        super(CheckpointStorageService, self).delete(object_names, bucket_name='checkpoints')


class DatasetStorageService(BaseStorageService):
    def __init__(self, storage: BaseStorage):
        super(DatasetStorageService, self).__init__(storage)

    def get(self, object_name: str, file_path: str, bucket_name: str = 'datasets') -> Optional[minio.datatypes.Object]:
        return self._storage.get(object_name=object_name, file_path=file_path, bucket_name=bucket_name)

    def put(self, file_path: str, object_name: str, bucket_name: str = 'datasets') -> Dataset:
        display_name = object_name
        object_name = str(uuid.uuid4())     # + os.path.splitext(file_path)[-1]
        result = self._storage.put(file_path=file_path, object_name=object_name, bucket_name=bucket_name)
        return Dataset(display_name=display_name, object_name=result.object_name, etag=result.etag)

    def exists(self, object_name: str, bucket_name: str = 'datasets', version_id: Optional[str] = None):
        return super(DatasetStorageService, self).exists(object_name=object_name, bucket_name=bucket_name, version_id=version_id)

    def delete(self, object_names: Iterable[str]):
        super(DatasetStorageService, self).delete(object_names, bucket_name='datasets')


def main():
    pass


if __name__ == "__main__":
    try:
        main()
    except minio.error.S3Error as e:
        print('Error:', e)
