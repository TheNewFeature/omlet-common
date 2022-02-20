from concurrent import futures

import docker
import grpc

from omlet_common.protos import container_pb2
from omlet_common.protos import container_pb2_grpc

DOCKER_DESKTOP_DEFAULT_PORT = 2375


class ContainerServiceServicer(container_pb2_grpc.ContainerServiceServicer):
    def __init__(self):
        pass

    def AttachStandardOutput(self, request, context):
        print(f'[ContainerServiceServicer] request: {request}')
        client = docker.DockerClient(f'tcp://{request.ip_address}:{DOCKER_DESKTOP_DEFAULT_PORT}')
        try:
            container = client.containers.get(request.container_id)
        except (docker.errors.NullResource, docker.errors.NotFound) as e:
            print(f'[ContainerServiceServicer] {type(e)}\n{e}')
            yield container_pb2.AttachStandardOutputResponse(stdout=str(e))
            return
        for log in container.logs(stream=True):
            print(f'[ContainerServiceServicer] log={log}')
            yield container_pb2.AttachStandardOutputResponse(stdout=log.decode('utf-8'))


class ContainerServiceClient:
    def __init__(self, server_address: str = '127.0.0.1'):
        self._server_address = server_address

    def attach_standard_output(self, ip_address: str, container_id: str):
        with grpc.insecure_channel(f'{self._server_address}:50051') as channel:
            stub = container_pb2_grpc.ContainerServiceStub(channel)
            request = container_pb2.AttachStandardOutputRequest(ip_address=ip_address, container_id=container_id)
            for response in stub.AttachStandardOutput(request=request):
                print(response.stdout)


def serve(wait_for_termination: bool = True):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    container_pb2_grpc.add_ContainerServiceServicer_to_server(ContainerServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    if wait_for_termination:
        server.wait_for_termination()


if __name__ == "__main__":
    pass
