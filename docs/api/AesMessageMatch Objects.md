## AesMessageMatch Objects

```python
class AesMessageMatch(EnumBase)
```

Match rule for message listeners

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMessageSystem
- **File**: AesMessageTypes.h

<a id="unreal.AesMessageMatch.EXACT_MATCH"></a>

#### EXACT\_MATCH

0: An exact match will only receive messages with exactly the same channel
(e.g., registering for "A.B" will match a broadcast of A.B but not A.B.C)

<a id="unreal.AesMessageMatch.PARTIAL_MATCH"></a>

#### PARTIAL\_MATCH

1: A partial match will receive any messages rooted in the same channel
(e.g., registering for "A.B" will match a broadcast of A.B as well as A.B.C)

<a id="unreal.RasterTool"></a>