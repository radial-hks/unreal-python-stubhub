## AesTilesHighlightLayerParam Objects

```python
class AesTilesHighlightLayerParam(AesTilesHighlightParam)
```

Aes Tiles Highlight Layer Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``layers`` (Array[str]):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesHighlightLayerParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             highlight: bool = False,
             style_name: Name = "None",
             layers: Array[str] = []) -> None
```

<a id="unreal.AesTilesHighlightLayerParam.layers"></a>

#### layers

```python
@property
def layers() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.AesTilesHighlightLayerParam.layers"></a>

#### layers

```python
@layers.setter
def layers(value: Array[str]) -> None
```

<a id="unreal.AesTilesVisibilityLayerParam"></a>