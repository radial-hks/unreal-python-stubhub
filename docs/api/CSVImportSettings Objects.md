## CSVImportSettings Objects

```python
class CSVImportSettings(StructBase)
```

CSVImport Settings

**C++ Source:**

- **Module**: UnrealEd
- **File**: CSVImportFactory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``import_curve_interp_mode`` (RichCurveInterpMode):  [Read-Write]
- ``import_row_struct`` (ScriptStruct):  [Read-Write]
- ``import_type`` (CSVImportType):  [Read-Write]

<a id="unreal.CSVImportSettings.__init__"></a>

#### __init__

```python
def __init__(
    import_row_struct: ScriptStruct = None,
    import_type: CSVImportType = CSVImportType.ECSV_DATA_TABLE,
    import_curve_interp_mode: RichCurveInterpMode = RichCurveInterpMode.
    RCIM_LINEAR
) -> None
```

<a id="unreal.CSVImportSettings.import_row_struct"></a>

#### import_row_struct

```python
@property
def import_row_struct() -> ScriptStruct
```

(ScriptStruct):  [Read-Write]

<a id="unreal.CSVImportSettings.import_row_struct"></a>

#### import_row_struct

```python
@import_row_struct.setter
def import_row_struct(value: ScriptStruct) -> None
```

<a id="unreal.CSVImportSettings.import_type"></a>

#### import_type

```python
@property
def import_type() -> CSVImportType
```

(CSVImportType):  [Read-Write]

<a id="unreal.CSVImportSettings.import_type"></a>

#### import_type

```python
@import_type.setter
def import_type(value: CSVImportType) -> None
```

<a id="unreal.CSVImportSettings.import_curve_interp_mode"></a>

#### import_curve_interp_mode

```python
@property
def import_curve_interp_mode() -> RichCurveInterpMode
```

(RichCurveInterpMode):  [Read-Write]

<a id="unreal.CSVImportSettings.import_curve_interp_mode"></a>

#### import_curve_interp_mode

```python
@import_curve_interp_mode.setter
def import_curve_interp_mode(value: RichCurveInterpMode) -> None
```

<a id="unreal.FbxMaterialBakeSize"></a>