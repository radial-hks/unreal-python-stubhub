## AesTilesOutlineLayerParam Objects

```python
class AesTilesOutlineLayerParam(AesTilesOutlineParam)
```

Aes Tiles Outline Layer Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``layers`` (Array[str]):  [Read-Write]
- ``outline`` (bool):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesOutlineLayerParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             outline: bool = False,
             style_name: Name = "None",
             layers: Array[str] = []) -> None
```

<a id="unreal.AesTilesOutlineLayerParam.layers"></a>

#### layers

```python
@property
def layers() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.AesTilesOutlineLayerParam.layers"></a>

#### layers

```python
@layers.setter
def layers(value: Array[str]) -> None
```

<a id="unreal.AesTilesHighlightParam"></a>