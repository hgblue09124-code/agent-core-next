# Benchmarks

Benchmark code lives here, outside production runtime.

It must never be imported by `Core`, `AgentRuntime`, or Integration's default
wiring. Keep measurements replaceable and isolated.
