## DCPBuildingLayerData Objects

```python
class DCPBuildingLayerData(AssetUserData)
```

DCPBuilding Layer Data

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPBuildingLayerAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_name`` (str):  [Read-Only]
- ``layer_info`` (DCPBuildingLayerNodeIds):  [Read-Only]
- ``moved`` (bool):  [Read-Only]
- ``relative_location`` (Vector):  [Read-Only]
- ``relative_z`` (float):  [Read-Only]

<a id="unreal.DCPBuildingLayerData.group_name"></a>

#### group\_name

```python
@property
def group_name() -> str
```

(str):  [Read-Only]

<a id="unreal.DCPBuildingLayerData.relative_z"></a>

#### relative\_z

```python
@property
def relative_z() -> float
```

(float):  [Read-Only]

<a id="unreal.DCPBuildingLayerData.relative_location"></a>

#### relative\_location

```python
@property
def relative_location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.DCPBuildingLayerData.moved"></a>

#### moved

```python
@property
def moved() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DCPBuildingLayerData.layer_info"></a>

#### layer\_info

```python
@property
def layer_info() -> DCPBuildingLayerNodeIds
```

(DCPBuildingLayerNodeIds):  [Read-Only]

<a id="unreal.DCPBuildingLayerSDKLibrary"></a>