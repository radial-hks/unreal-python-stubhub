## LidarPointCloudImportSettings_ASCII_Columns Objects

```python
class LidarPointCloudImportSettings_ASCII_Columns(StructBase)
```

Used to help expose the import settings to Blueprints

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudRuntime
- **File**: LidarPointCloudFileIO_ASCII.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blue`` (int32):  [Read-Write] Index of a column containing Blue channel. Set to -1 if not available
- ``green`` (int32):  [Read-Write] Index of a column containing Green channel. Set to -1 if not available
- ``intensity`` (int32):  [Read-Write] Index of a column containing Intensity channel. Set to -1 if not available
- ``location_x`` (int32):  [Read-Write] Index of a column containing Location X data
- ``location_y`` (int32):  [Read-Write] Index of a column containing Location Y data
- ``location_z`` (int32):  [Read-Write] Index of a column containing Location Z data
- ``normal_x`` (int32):  [Read-Write] Index of a column containing Normal X data. Set to -1 if not available
- ``normal_y`` (int32):  [Read-Write] Index of a column containing Normal Y data. Set to -1 if not available
- ``normal_z`` (int32):  [Read-Write] Index of a column containing Normal Z data. Set to -1 if not available
- ``red`` (int32):  [Read-Write] Index of a column containing Red channel. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.__init__"></a>

#### __init__

```python
def __init__(location_x: int = 0,
             location_y: int = 0,
             location_z: int = 0,
             red: int = 0,
             green: int = 0,
             blue: int = 0,
             intensity: int = 0,
             normal_x: int = 0,
             normal_y: int = 0,
             normal_z: int = 0) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_x"></a>

#### location_x

```python
@property
def location_x() -> int
```

(int32):  [Read-Write] Index of a column containing Location X data

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_x"></a>

#### location_x

```python
@location_x.setter
def location_x(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_y"></a>

#### location_y

```python
@property
def location_y() -> int
```

(int32):  [Read-Write] Index of a column containing Location Y data

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_y"></a>

#### location_y

```python
@location_y.setter
def location_y(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_z"></a>

#### location_z

```python
@property
def location_z() -> int
```

(int32):  [Read-Write] Index of a column containing Location Z data

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.location_z"></a>

#### location_z

```python
@location_z.setter
def location_z(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.red"></a>

#### red

```python
@property
def red() -> int
```

(int32):  [Read-Write] Index of a column containing Red channel. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.red"></a>

#### red

```python
@red.setter
def red(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.green"></a>

#### green

```python
@property
def green() -> int
```

(int32):  [Read-Write] Index of a column containing Green channel. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.green"></a>

#### green

```python
@green.setter
def green(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.blue"></a>

#### blue

```python
@property
def blue() -> int
```

(int32):  [Read-Write] Index of a column containing Blue channel. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.blue"></a>

#### blue

```python
@blue.setter
def blue(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.intensity"></a>

#### intensity

```python
@property
def intensity() -> int
```

(int32):  [Read-Write] Index of a column containing Intensity channel. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_x"></a>

#### normal_x

```python
@property
def normal_x() -> int
```

(int32):  [Read-Write] Index of a column containing Normal X data. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_x"></a>

#### normal_x

```python
@normal_x.setter
def normal_x(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_y"></a>

#### normal_y

```python
@property
def normal_y() -> int
```

(int32):  [Read-Write] Index of a column containing Normal Y data. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_y"></a>

#### normal_y

```python
@normal_y.setter
def normal_y(value: int) -> None
```

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_z"></a>

#### normal_z

```python
@property
def normal_z() -> int
```

(int32):  [Read-Write] Index of a column containing Normal Z data. Set to -1 if not available

<a id="unreal.LidarPointCloudImportSettings_ASCII_Columns.normal_z"></a>

#### normal_z

```python
@normal_z.setter
def normal_z(value: int) -> None
```

<a id="unreal.GroomCacheImportSettings"></a>