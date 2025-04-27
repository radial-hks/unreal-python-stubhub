## AbcMaterialSettings Objects

```python
class AbcMaterialSettings(StructBase)
```

Abc Material Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``create_materials`` (bool):  [Read-Write] Whether or not to create materials according to found Face Set names (will not work without face sets)
- ``find_materials`` (bool):  [Read-Write] Whether or not to try and find materials according to found Face Set names (will not work without face sets)

<a id="unreal.AbcMaterialSettings.__init__"></a>

#### __init__

```python
def __init__(create_materials: bool = False,
             find_materials: bool = False) -> None
```

<a id="unreal.AbcMaterialSettings.create_materials"></a>

#### create_materials

```python
@property
def create_materials() -> bool
```

(bool):  [Read-Write] Whether or not to create materials according to found Face Set names (will not work without face sets)

<a id="unreal.AbcMaterialSettings.create_materials"></a>

#### create_materials

```python
@create_materials.setter
def create_materials(value: bool) -> None
```

<a id="unreal.AbcMaterialSettings.find_materials"></a>

#### find_materials

```python
@property
def find_materials() -> bool
```

(bool):  [Read-Write] Whether or not to try and find materials according to found Face Set names (will not work without face sets)

<a id="unreal.AbcMaterialSettings.find_materials"></a>

#### find_materials

```python
@find_materials.setter
def find_materials(value: bool) -> None
```

<a id="unreal.AbcStaticMeshSettings"></a>