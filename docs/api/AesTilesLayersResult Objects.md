## AesTilesLayersResult Objects

```python
class AesTilesLayersResult(ResultBase)
```

Aes Tiles Layers Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``layers`` (Array[AesTilesVisibilityLayerStatus]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AesTilesLayersResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             layers: Array[AesTilesVisibilityLayerStatus] = []) -> None
```

<a id="unreal.AesTilesLayersResult.layers"></a>

#### layers

```python
@property
def layers() -> Array[AesTilesVisibilityLayerStatus]
```

(Array[AesTilesVisibilityLayerStatus]):  [Read-Write]

<a id="unreal.AesTilesLayersResult.layers"></a>

#### layers

```python
@layers.setter
def layers(value: Array[AesTilesVisibilityLayerStatus]) -> None
```

<a id="unreal.EnterEarthEditorParams"></a>