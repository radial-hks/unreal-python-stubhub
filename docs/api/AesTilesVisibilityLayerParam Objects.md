## AesTilesVisibilityLayerParam Objects

```python
class AesTilesVisibilityLayerParam(AesTilesVisualApiParamBase)
```

Visibility

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``layers`` (Array[str]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityLayerParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             layers: Array[str] = [],
             visible: bool = False) -> None
```

<a id="unreal.AesTilesVisibilityLayerParam.layers"></a>

#### layers

```python
@property
def layers() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.AesTilesVisibilityLayerParam.layers"></a>

#### layers

```python
@layers.setter
def layers(value: Array[str]) -> None
```

<a id="unreal.AesTilesVisibilityLayerParam.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityLayerParam.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.AesTilesVisibilityNodesParam"></a>