## ClothingAssetCommon Objects

```python
class ClothingAssetCommon(ClothingAssetBase)
```

Implementation of non-solver specific, but common Engine related functionality.

Solver specific implementations may wish to override this class to construct
their own default instances of child classes, such as \c ClothSimConfig and
\c CustomData, as well as override the \c AddNewLod() factory to build their
own implementation of \c UClothLODDataBase.

**C++ Source:**

- **Module**: ClothingSystemRuntimeCommon
- **File**: ClothingAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cloth_configs`` (Map[Name, ClothConfigBase]):  [Read-Only] Simulation specific cloth parameters.
  Use GetClothConfig() to retrieve the correct parameters/config type for the desired cloth simulation system.
- ``custom_data`` (ClothingAssetCustomData):  [Read-Write]
  deprecated: This property is obsolete.
- ``imported_file_path`` (str):  [Read-Only] If this asset was imported from a file, this will be the original path
- ``physics_asset`` (PhysicsAsset):  [Read-Write] The physics asset to extract collisions from when building a simulation.

<a id="unreal.ClothingAssetCommon.cloth_configs"></a>

#### cloth_configs

```python
@property
def cloth_configs() -> Map[Name, ClothConfigBase]
```

(Map[Name, ClothConfigBase]):  [Read-Only] Simulation specific cloth parameters.
Use GetClothConfig() to retrieve the correct parameters/config type for the desired cloth simulation system.

<a id="unreal.ClothingAssetCommon.custom_data"></a>

#### custom_data

```python
@property
def custom_data() -> ClothingAssetCustomData
```

(ClothingAssetCustomData):  [Read-Write]
deprecated: This property is obsolete.

<a id="unreal.ClothingAssetCommon.custom_data"></a>

#### custom_data

```python
@custom_data.setter
def custom_data(value: ClothingAssetCustomData) -> None
```

<a id="unreal.ClothingAsset"></a>