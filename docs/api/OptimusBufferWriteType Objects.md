## OptimusBufferWriteType Objects

```python
class OptimusBufferWriteType(EnumBase)
```

Write to buffer operation types.

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusDataInterfaceRawBuffer.h

<a id="unreal.OptimusBufferWriteType.WRITE"></a>

#### WRITE

0: Write the value to resource buffer.

<a id="unreal.OptimusBufferWriteType.WRITE_ATOMIC_ADD"></a>

#### WRITE\_ATOMIC\_ADD

1: AtomicAdd the value to the value in the resource buffer.

<a id="unreal.OptimusBufferWriteType.WRITE_ATOMIC_MIN"></a>

#### WRITE\_ATOMIC\_MIN

2: AtomicMin the value with the value in the resource buffer.

<a id="unreal.OptimusBufferWriteType.WRITE_ATOMIC_MAX"></a>

#### WRITE\_ATOMIC\_MAX

3: AtomicMax the value with the value in the resource buffer.

<a id="unreal.OptimusTerminalType"></a>