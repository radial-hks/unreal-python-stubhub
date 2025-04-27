## CompositeCurveTable Objects

```python
class CompositeCurveTable(CurveTable)
```

Curve table composed of a stack of other curve tables.

**C++ Source:**

- **Module**: Engine
- **File**: CompositeCurveTable.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_import_data`` (AssetImportData):  [Read-Only]
- ``parent_tables`` (Array[CurveTable]):  [Read-Write] Parent tables
  Tables with higher indices override data in tables with lower indices

<a id="unreal.CompositeCurveTable.parent_tables"></a>

#### parent_tables

```python
@property
def parent_tables() -> Array[CurveTable]
```

(Array[CurveTable]):  [Read-Only] Parent tables
Tables with higher indices override data in tables with lower indices

<a id="unreal.CompositeDataTable"></a>