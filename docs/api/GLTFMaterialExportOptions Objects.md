## GLTFMaterialExportOptions Objects

```python
class GLTFMaterialExportOptions(AssetUserData)
```

glTF-specific user data that can be added to material assets to override export options

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFMaterialUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default`` (GLTFOverrideMaterialBakeSettings):  [Read-Write] Default bake settings for this material in general.
- ``inputs`` (Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific bake settings that override the defaults above.
- ``proxy`` (MaterialInterface):  [Read-Write] If assigned, export will use the proxy instead of the original material.

<a id="unreal.GLTFMaterialExportOptions.proxy"></a>

#### proxy

```python
@property
def proxy() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] If assigned, export will use the proxy instead of the original material.

<a id="unreal.GLTFMaterialExportOptions.proxy"></a>

#### proxy

```python
@proxy.setter
def proxy(value: MaterialInterface) -> None
```

<a id="unreal.GLTFMaterialExportOptions.default"></a>

#### default

```python
@property
def default() -> GLTFOverrideMaterialBakeSettings
```

(GLTFOverrideMaterialBakeSettings):  [Read-Write] Default bake settings for this material in general.

<a id="unreal.GLTFMaterialExportOptions.default"></a>

#### default

```python
@default.setter
def default(value: GLTFOverrideMaterialBakeSettings) -> None
```

<a id="unreal.GLTFMaterialExportOptions.inputs"></a>

#### inputs

```python
@property
def inputs(
) -> Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
```

(Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]):  [Read-Write] Input-specific bake settings that override the defaults above.

<a id="unreal.GLTFMaterialExportOptions.inputs"></a>

#### inputs

```python
@inputs.setter
def inputs(
    value: Map[GLTFMaterialPropertyGroup, GLTFOverrideMaterialBakeSettings]
) -> None
```

<a id="unreal.LidarPointCloud"></a>