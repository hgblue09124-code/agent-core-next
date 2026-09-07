# Plan Tree 10/10  
Đẩy. Lần này em chốt theo chuẩn **10/10 về kiến trúc**, nhưng vẫn giữ nguyên luật: **Plan Tree chỉ là xương sống**, chưa biến thành functional mapping, chưa nhét implementation giả.  
```
agent-core-next/
│
├── Core/
│   ├── Agent/
│   │   ├── Identity/
│   │   ├── Lifecycle/
│   │   ├── Context/
│   │   ├── State/
│   │   ├── Session/
│   │   └── Agent/
│   │
│   ├── Runtime/
│   │   ├── Runtime/
│   │   ├── Run/
│   │   ├── Session/
│   │   ├── Lifecycle/
│   │   ├── State/
│   │   ├── Events/
│   │   ├── Policies/
│   │   └── Errors/
│   │
│   ├── Contracts/
│   │   ├── Actions/
│   │   ├── Capabilities/
│   │   ├── Requests/
│   │   ├── Responses/
│   │   ├── Results/
│   │   ├── Events/
│   │   ├── Metadata/
│   │   └── Errors/
│   │
│   ├── Policies/
│   │   ├── Runtime/
│   │   ├── Safety/
│   │   ├── Authorization/
│   │   ├── Resource/
│   │   └── Limits/
│   │
│   ├── Events/
│   │   ├── Domain/
│   │   ├── Runtime/
│   │   └── System/
│   │
│   └── Errors/
│       ├── Domain/
│       ├── Runtime/
│       └── Contract/
│
├── Intelligence/
│   ├── Model/
│   │   ├── Identity/
│   │   ├── Metadata/
│   │   ├── Capabilities/
│   │   ├── Requirements/
│   │   ├── Configuration/
│   │   └── Lifecycle/
│   │
│   ├── Provider/
│   │   ├── Contracts/
│   │   ├── Registry/
│   │   ├── Discovery/
│   │   ├── Capabilities/
│   │   ├── Configuration/
│   │   └── Errors/
│   │
│   ├── Inference/
│   │   ├── Contracts/
│   │   ├── Engine/
│   │   ├── Request/
│   │   ├── Response/
│   │   ├── Streaming/
│   │   ├── Sampling/
│   │   ├── Tokenization/
│   │   ├── Native/
│   │   │   ├── GGUF/
│   │   │   ├── Runtime/
│   │   │   ├── Memory/
│   │   │   └── Hardware/
│   │   └── Remote/
│   │       ├── HTTP/
│   │       ├── Streaming/
│   │       └── Providers/
│   │
│   ├── Prompt/
│   │   ├── Messages/
│   │   ├── Templates/
│   │   ├── Rendering/
│   │   ├── Formatting/
│   │   ├── Context/
│   │   └── Policies/
│   │
│   ├── Context/
│   │   ├── Builder/
│   │   ├── Window/
│   │   ├── Budget/
│   │   ├── Compression/
│   │   └── Policies/
│   │
│   ├── Reasoning/
│   │   ├── Decision/
│   │   ├── Planning/
│   │   ├── ToolSelection/
│   │   ├── Response/
│   │   └── Policies/
│   │
│   └── Tools/
│       ├── Definitions/
│       ├── Schemas/
│       ├── Registry/
│       ├── Selection/
│       └── Invocation/
│
├── Model/
│   ├── Catalog/
│   │   ├── Registry/
│   │   ├── Records/
│   │   ├── Index/
│   │   ├── Discovery/
│   │   ├── Metadata/
│   │   └── Compatibility/
│   │
│   ├── Download/
│   │   ├── Requests/
│   │   ├── Transfers/
│   │   ├── Progress/
│   │   ├── Resume/
│   │   ├── Retry/
│   │   └── Errors/
│   │
│   ├── Validation/
│   │   ├── Integrity/
│   │   ├── Checksums/
│   │   ├── Metadata/
│   │   ├── Format/
│   │   ├── Compatibility/
│   │   └── Errors/
│   │
│   ├── Storage/
│   │   ├── Artifacts/
│   │   ├── Paths/
│   │   ├── Cache/
│   │   ├── Index/
│   │   ├── Quota/
│   │   └── Policies/
│   │
│   ├── Lifecycle/
│   │   ├── Install/
│   │   ├── Update/
│   │   ├── Remove/
│   │   ├── Activate/
│   │   └── State/
│   │
│   └── Manifest/
│       ├── Schema/
│       ├── Parser/
│       ├── Validation/
│       └── Versioning/
│
├── Execution/
│   ├── Planner/
│   │   ├── Planning/
│   │   ├── Plans/
│   │   ├── Context/
│   │   ├── Resolution/
│   │   ├── Dependencies/
│   │   └── Policies/
│   │
│   ├── Executor/
│   │   ├── Execution/
│   │   ├── Actions/
│   │   ├── Context/
│   │   ├── Dispatch/
│   │   ├── Retry/
│   │   ├── Timeout/
│   │   ├── Cancellation/
│   │   └── Errors/
│   │
│   ├── Verification/
│   │   ├── Verification/
│   │   ├── Outcomes/
│   │   ├── Assertions/
│   │   ├── Policies/
│   │   └── Errors/
│   │
│   ├── Capabilities/
│   │   ├── Registry/
│   │   ├── Resolution/
│   │   ├── Definitions/
│   │   └── Handlers/
│   │
│   ├── Scheduling/
│   │   ├── Scheduler/
│   │   ├── Queue/
│   │   ├── Priority/
│   │   ├── Workers/
│   │   └── Cancellation/
│   │
│   └── Lifecycle/
│       ├── Start/
│       ├── Pause/
│       ├── Resume/
│       ├── Abort/
│       └── Complete/
│
├── Memory/
│   ├── Store/
│   │   ├── Contracts/
│   │   ├── Records/
│   │   ├── Queries/
│   │   ├── Transactions/
│   │   └── Lifecycle/
│   │
│   ├── Retrieval/
│   │   ├── Query/
│   │   ├── Search/
│   │   ├── Ranking/
│   │   ├── Filtering/
│   │   └── Results/
│   │
│   ├── Indexing/
│   │   ├── Index/
│   │   ├── Embedding/
│   │   ├── Chunking/
│   │   └── Updates/
│   │
│   ├── Context/
│   │   ├── Assembly/
│   │   ├── Selection/
│   │   ├── Compression/
│   │   └── Policies/
│   │
│   └── Lifecycle/
│       ├── Retention/
│       ├── Expiration/
│       ├── Cleanup/
│       └── Migration/
│
├── Infrastructure/
│   ├── Networking/
│   │   ├── HTTP/
│   │   ├── WebSocket/
│   │   ├── Connections/
│   │   ├── Retry/
│   │   ├── Timeout/
│   │   └── Transport/
│   │
│   ├── Persistence/
│   │   ├── FileSystem/
│   │   ├── Database/
│   │   ├── Serialization/
│   │   ├── Transactions/
│   │   └── Migration/
│   │
│   ├── Logging/
│   │   ├── Logger/
│   │   ├── Formatters/
│   │   ├── Handlers/
│   │   └── Sinks/
│   │
│   ├── Platform/
│   │   ├── OS/
│   │   ├── Environment/
│   │   ├── Paths/
│   │   ├── Process/
│   │   ├── Hardware/
│   │   └── Devices/
│   │
│   ├── Concurrency/
│   │   ├── Tasks/
│   │   ├── Workers/
│   │   ├── Locks/
│   │   └── Synchronization/
│   │
│   ├── Configuration/
│   │   ├── Sources/
│   │   ├── Loading/
│   │   ├── Parsing/
│   │   ├── Validation/
│   │   └── Profiles/
│   │
│   └── Security/
│       ├── Secrets/
│       ├── Credentials/
│       ├── Isolation/
│       └── SecureStorage/
│
├── Integration/
│   ├── Composition/
│   │   ├── Root/
│   │   ├── Factories/
│   │   ├── Providers/
│   │   └── Configuration/
│   │
│   ├── DependencyContainer/
│   │   ├── Container/
│   │   ├── Bindings/
│   │   ├── Factories/
│   │   └── Scopes/
│   │
│   ├── Bootstrap/
│   │   ├── Startup/
│   │   ├── Shutdown/
│   │   ├── Health/
│   │   └── Recovery/
│   │
│   └── Adapters/
│       ├── Intelligence/
│       ├── Model/
│       ├── Execution/
│       ├── Memory/
│       └── Infrastructure/
│
├── Interfaces/
│   ├── CLI/
│   │   ├── Commands/
│   │   ├── Arguments/
│   │   ├── Output/
│   │   └── Errors/
│   │
│   ├── API/
│   │   ├── Routes/
│   │   ├── Requests/
│   │   ├── Responses/
│   │   ├── Middleware/
│   │   └── Errors/
│   │
│   ├── SDK/
│   │   ├── Client/
│   │   ├── Models/
│   │   ├── Requests/
│   │   └── Responses/
│   │
│   └── Events/
│       ├── Publishers/
│       ├── Subscribers/
│       └── Schemas/
│
├── Observability/
│   ├── Metrics/
│   │   ├── Runtime/
│   │   ├── Inference/
│   │   ├── Execution/
│   │   └── Memory/
│   │
│   ├── Tracing/
│   │   ├── Runtime/
│   │   ├── Inference/
│   │   └── Execution/
│   │
│   ├── Diagnostics/
│   │   ├── Runtime/
│   │   ├── Model/
│   │   └── System/
│   │
│   ├── Audit/
│   │   ├── Events/
│   │   ├── Records/
│   │   └── Policies/
│   │
│   └── Health/
│       ├── Checks/
│       ├── Status/
│       └── Reports/
│
├── Security/
│   ├── Authentication/
│   ├── Authorization/
│   ├── Credentials/
│   ├── Secrets/
│   ├── Isolation/
│   ├── Sandboxing/
│   └── Policies/
│
├── Testing/
│   ├── Unit/
│   │   ├── Core/
│   │   ├── Intelligence/
│   │   ├── Model/
│   │   ├── Execution/
│   │   ├── Memory/
│   │   └── Infrastructure/
│   │
│   ├── Integration/
│   ├── Contract/
│   ├── Architecture/
│   │   ├── DependencyRules/
│   │   ├── ImportRules/
│   │   ├── BoundaryRules/
│   │   └── LayerRules/
│   │
│   ├── Runtime/
│   ├── EndToEnd/
│   ├── Fixtures/
│   ├── Doubles/
│   └── Utilities/
│
├── Benchmarks/
│   ├── Inference/
│   ├── Model/
│   ├── Execution/
│   ├── Memory/
│   └── Runtime/
│
├── Documentation/
│   ├── Architecture/
│   │   ├── Overview/
│   │   ├── Boundaries/
│   │   ├── DependencyDirection/
│   │   └── Decisions/
│   │
│   ├── Core/
│   ├── Intelligence/
│   ├── Model/
│   ├── Execution/
│   ├── Memory/
│   ├── Infrastructure/
│   ├── Integration/
│   ├── Interfaces/
│   ├── Testing/
│   └── Development/
│
├── Tools/
│   ├── Development/
│   ├── Validation/
│   ├── Diagnostics/
│   ├── Migration/
│   └── Maintenance/
│
├── Scripts/
│   ├── Setup/
│   ├── Development/
│   ├── Testing/
│   ├── Validation/
│   └── CI/
│
├── Examples/
│   ├── Basic/
│   ├── Runtime/
│   ├── Inference/
│   ├── Execution/
│   └── Integration/
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE/
│
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore

```
**Chuẩn 10/10 em chốt cho cây này**  
**1. Core là trung tâm, nhưng không biết Infrastructure.**  
**2. Intelligence không sở hữu Runtime.**  
**3. Model lifecycle tách hoàn toàn khỏi Inference.**  
**4. Native GGUF là một nhánh riêng:**  
```
Intelligence/
└── Inference/
    ├── Native/
    │   └── GGUF/
    └── Remote/

```
Không có kiểu:  
```
Native GGUF
    ↓
HTTP
    ↓
Ollama

```
**5. Execution có đủ vòng đời:**  
```
Plan
  ↓
Resolve
  ↓
Execute
  ↓
Verify
  ↓
Complete / Retry / Cancel / Abort

```
**6. Memory không chui vào Runtime bằng dependency ngược.**  
**7. Integration là Composition Root**, không biến thành “God Container”.  
**8. Architecture Tests trở thành hàng rào bảo vệ cây.**  
```
Architecture Tests
       ↓
Dependency Rules
Import Rules
Boundary Rules
Layer Rules

```
**9. Interfaces nằm ngoài Core.** CLI/API/SDK chỉ là cửa vào, không được biến Core thành web framework.  
**10. Benchmark không được trở thành cái đuôi kéo kiến trúc đi lệch.** Chỉ benchmark khi có mục đích đo lường thực tế.  
Và quan trọng nhất:  
**Cây này là trần kiến trúc, không phải checklist bắt buộc phải tạo hàng trăm file ngay.**  
Đây mới là bản em coi là **10/10 Plan Tree**: đủ rộng để Agent Core Next phát triển rất lớn mà vẫn có chỗ đặt đúng trách nhiệm, nhưng không ép code hiện tại phải gánh toàn bộ tương lai.  
