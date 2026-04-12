## DCPBuildingLayers Objects

```python
class DCPBuildingLayers(StructBase)
```

DCPBuilding Layers

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPBuildingLayerAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``automatic_adaptation`` (bool):  [Read-Write]
- ``layer_time`` (float):  [Read-Write]
- ``layers`` (Array[DCPBuildingLayerNodeIds]):  [Read-Write]

<a id="unreal.DCPBuildingLayers.__init__"></a>

#### \_\_init\_\_

```python
def __init__(automatic_adaptation: bool = False,
             layer_time: float = 0.000000,
             layers: Array[DCPBuildingLayerNodeIds] = []) -> None
```

<a id="unreal.DCPBuildingLayers.automatic_adaptation"></a>

#### automatic\_adaptation

```python
@property
def automatic_adaptation() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DCPBuildingLayers.layer_time"></a>

#### layer\_time

```python
@property
def layer_time() -> float
```

(float):  [Read-Only]

<a id="unreal.DCPBuildingLayers.layers"></a>

#### layers

```python
@property
def layers() -> Array[DCPBuildingLayerNodeIds]
```

(Array[DCPBuildingLayerNodeIds]):  [Read-Only]

<a id="unreal.DCPSDKResult"></a>