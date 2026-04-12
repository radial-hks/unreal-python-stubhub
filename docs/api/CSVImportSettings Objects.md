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

#### \_\_init\_\_

```python
def __init__(
    import_row_struct: ScriptStruct = None,
    import_type: CSVImportType = CSVImportType.ECSV_DATA_TABLE,
    import_curve_interp_mode: RichCurveInterpMode = RichCurveInterpMode.
    RCIM_LINEAR
) -> None
```

<a id="unreal.CSVImportSettings.import_row_struct"></a>

#### import\_row\_struct

```python
@property
def import_row_struct() -> ScriptStruct
```

(ScriptStruct):  [Read-Write]

<a id="unreal.CSVImportSettings.import_row_struct"></a>

#### import\_row\_struct

```python
@import_row_struct.setter
def import_row_struct(value: ScriptStruct) -> None
```

<a id="unreal.CSVImportSettings.import_type"></a>

#### import\_type

```python
@property
def import_type() -> CSVImportType
```

(CSVImportType):  [Read-Write]

<a id="unreal.CSVImportSettings.import_type"></a>

#### import\_type

```python
@import_type.setter
def import_type(value: CSVImportType) -> None
```

<a id="unreal.CSVImportSettings.import_curve_interp_mode"></a>

#### import\_curve\_interp\_mode

```python
@property
def import_curve_interp_mode() -> RichCurveInterpMode
```

(RichCurveInterpMode):  [Read-Write]

<a id="unreal.CSVImportSettings.import_curve_interp_mode"></a>

#### import\_curve\_interp\_mode

```python
@import_curve_interp_mode.setter
def import_curve_interp_mode(value: RichCurveInterpMode) -> None
```

<a id="unreal.FbxMaterialBakeSize"></a>