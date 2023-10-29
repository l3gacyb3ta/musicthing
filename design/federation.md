
Things that federate:

- Artist follows (AP Compatible ?)
- Artist Updates (new releases / newsletter stuff) (AP?)
- The music buying process !!!

```mermaid
sequenceDiagram
    Buyer Server->>Artist Server: Request buy information
    Artist Server->>Buyer Server: Return buy struct
    Buyer Server->>Payment Processor: Complete purchase
    Payment Processor->>Artist Server: Confirm purchase
    Artist Server->>Buyer Server: Deliver content
```

