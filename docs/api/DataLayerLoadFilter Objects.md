## DataLayerLoadFilter Objects

```python
class DataLayerLoadFilter(EnumBase)
```

EData Layer Load Filter

**C++ Source:**

- **Module**: Engine
- **File**: DataLayerAsset.h

<a id="unreal.DataLayerLoadFilter.NONE"></a>

#### NONE

0: Data Layer is considered by the client and the server. Client runtime state is replicated.

<a id="unreal.DataLayerLoadFilter.CLIENT_ONLY"></a>

#### CLIENT_ONLY

1: Data Layer is only considered by the client.

<a id="unreal.DataLayerLoadFilter.SERVER_ONLY"></a>

#### SERVER_ONLY

2: Data layer is only considered by the server.

<a id="unreal.OverrideBlockOnSlowStreaming"></a>