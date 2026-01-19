kafka-helm-project/
│
├── apps/
│   ├── producer/
│   │   ├── producer.py
│   │   └── Dockerfile
│   │
│   └── consumer/
│       ├── consumer.py
│       └── Dockerfile
│
└── helm/
    └── kafka-app/
        ├── Chart.yaml
        ├── values.yaml
        └── templates/
            ├── producer-deployment.yaml
            └── consumer-deployment.yaml

-----------------------------------------------

Kubernetes
│
├── Strimzi Operator
│     │
│     ├── KafkaNodePool
│     │       └── creates Kafka Pods
│     │             ├── broker role
│     │             └── controller role
│     │
│     └── Entity Operator
│             ├── manages KafkaTopic
│             └── manages KafkaUser
│
└── Your Apps
      ├── Producer
      └── Consumer

