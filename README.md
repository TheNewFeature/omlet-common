# omlet-common
![CI Lint](https://github.com/TheNewFeature/omlet-common/workflows/Lint/badge.svg)
![CI Build](https://github.com/TheNewFeature/omlet-common/workflows/Build/badge.svg)

`omlet` 프로젝트에서 공통적으로 사용되는 `python` 모듈을 관리하는 패키지입니다.
- [src/omlet_common/errors](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/errors) (`omlet_common.errors`)
  - `Custom Exception`이 정의된 모듈입니다.
- [src/omlet_common/grpc](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/grpc) (`omlet_common.grpc`)
  - 원격 [`omlet-agent`](https://github.com/TheNewFeature/omlet-agent)에 위치한 `Docker` 컨테이너와 통신하기 위한 `grpc` 구현체 클래스입니다.
- [src/omlet_common/message_queue](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/message_queue) (`omlet_common.message_queue`)
  - 메시지 큐 `Publisher` 및 `Subscriber`의 기능을 수행할 수 있는 클래스입니다.
  - 현재 [`RabbitMQ`](https://www.rabbitmq.com/)를 이용하여 구현되어 있습니다.
- [src/omlet_common/protos](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/protos)
  - `grpc` 서비스 및 메시지가 정의된 모듈입니다.
- [src/omlet_common/schemas](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/schemas) (`omlet_common.schemas`)
  - `Auth`, `Device`, `Session` 등 도메인별 `DTO` 클래스가 정의된 모듈입니다.
- [src/omlet_common/storage](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/storage) (`omlet_common.storage`)
  - 파일 저장소를 이용하기 위한 인터페이스와 구현체 클래스, 그리고 `DTO` 클래스가 정의된 모듈입니다.
  - 현재 [`Minio`](https://min.io)를 이용하여 구현되어 있습니다.
- [src/omlet_common/requests](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/requests.py) (`omlet_common.requests`)
  - [omlet-core](https://github.com/TheNewFeature/omlet)과 [omlet-cli](https://github.com/TheNewFeature/omlet-cli)에서 공통적으로 사용하는 `DTO` 클래스입니다.
- [src/omlet_common/responses](https://github.com/TheNewFeature/omlet-common/tree/master/src/omlet_common/responses.py) (`omlet_common.responses`)
  - [omlet-core](https://github.com/TheNewFeature/omlet)과 [omlet-cli](https://github.com/TheNewFeature/omlet-cli)에서 공통적으로 사용하는 `DTO` 클래스입니다.
