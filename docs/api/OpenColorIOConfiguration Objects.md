## OpenColorIOConfiguration Objects

```python
class OpenColorIOConfiguration(Object)
```

Asset to manage allowed OpenColorIO color spaces. This will create required transform objects.

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIOConfiguration.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``configuration_file`` (FilePath):  [Read-Write]
- ``context`` (Map[str, str]):  [Read-Write] OCIO context of key-value string pairs, typically used to apply shot-specific looks (such as a CDL color correction, or a 1D grade LUT).
- ``desired_color_spaces`` (Array[OpenColorIOColorSpace]):  [Read-Write]
- ``desired_display_views`` (Array[OpenColorIODisplayView]):  [Read-Write]

<a id="unreal.OpenColorIOConfiguration.configuration_file"></a>

#### configuration_file

```python
@property
def configuration_file() -> FilePath
```

(FilePath):  [Read-Write]

<a id="unreal.OpenColorIOConfiguration.configuration_file"></a>

#### configuration_file

```python
@configuration_file.setter
def configuration_file(value: FilePath) -> None
```

<a id="unreal.OpenColorIOConfiguration.desired_color_spaces"></a>

#### desired_color_spaces

```python
@property
def desired_color_spaces() -> Array[OpenColorIOColorSpace]
```

(Array[OpenColorIOColorSpace]):  [Read-Write]

<a id="unreal.OpenColorIOConfiguration.desired_color_spaces"></a>

#### desired_color_spaces

```python
@desired_color_spaces.setter
def desired_color_spaces(value: Array[OpenColorIOColorSpace]) -> None
```

<a id="unreal.OpenColorIOConfiguration.desired_display_views"></a>

#### desired_display_views

```python
@property
def desired_display_views() -> Array[OpenColorIODisplayView]
```

(Array[OpenColorIODisplayView]):  [Read-Write]

<a id="unreal.OpenColorIOConfiguration.desired_display_views"></a>

#### desired_display_views

```python
@desired_display_views.setter
def desired_display_views(value: Array[OpenColorIODisplayView]) -> None
```

<a id="unreal.OpenColorIOConfiguration.context"></a>

#### context

```python
@property
def context() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] OCIO context of key-value string pairs, typically used to apply shot-specific looks (such as a CDL color correction, or a 1D grade LUT).

<a id="unreal.OpenColorIOConfiguration.context"></a>

#### context

```python
@context.setter
def context(value: Map[str, str]) -> None
```

<a id="unreal.OpenColorIOConfiguration.reload_existing_colorspaces"></a>

#### reload_existing_colorspaces

```python
def reload_existing_colorspaces(force: bool = False) -> None
```

x.reload_existing_colorspaces(force=False) -> None
This forces to reload colorspaces and corresponding shaders if those are not loaded already.

Args:
    force (bool):

<a id="unreal.OpenColorIODisplayExtensionWrapper"></a>