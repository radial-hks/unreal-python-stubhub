## LensFilePicker Objects

```python
class LensFilePicker(StructBase)
```

Wrapper to facilitate default LensFile vs picker

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensFile.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lens_file`` (LensFile):  [Read-Write] LensFile asset to use if DefaultLensFile is not desired
- ``use_default_lens_file`` (bool):  [Read-Write] If true, default LensFile will be used, if one is set

<a id="unreal.LensFilePicker.__init__"></a>

#### __init__

```python
def __init__(use_default_lens_file: bool = False,
             lens_file: LensFile = None) -> None
```

<a id="unreal.LensFilePicker.use_default_lens_file"></a>

#### use_default_lens_file

```python
@property
def use_default_lens_file() -> bool
```

(bool):  [Read-Write] If true, default LensFile will be used, if one is set

<a id="unreal.LensFilePicker.use_default_lens_file"></a>

#### use_default_lens_file

```python
@use_default_lens_file.setter
def use_default_lens_file(value: bool) -> None
```

<a id="unreal.LensFilePicker.lens_file"></a>

#### lens_file

```python
@property
def lens_file() -> LensFile
```

(LensFile):  [Read-Write] LensFile asset to use if DefaultLensFile is not desired

<a id="unreal.LensFilePicker.lens_file"></a>

#### lens_file

```python
@lens_file.setter
def lens_file(value: LensFile) -> None
```

<a id="unreal.LensFileEvaluationInputs"></a>