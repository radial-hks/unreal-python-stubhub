## OpenColorIODisplayExtensionWrapper Objects

```python
class OpenColorIODisplayExtensionWrapper(Object)
```

This Blueprintable object can hold an OCIO Scene View Extension.
You can change its OCIO config, and specify the context in which you want it to be active on.

**C++ Source:**

- **Plugin**: OpenColorIO
- **Module**: OpenColorIO
- **File**: OpenColorIODisplayExtensionWrapper.h

<a id="unreal.OpenColorIODisplayExtensionWrapper.set_scene_extension_is_active_functions"></a>

#### set_scene_extension_is_active_functions

```python
def set_scene_extension_is_active_functions(
        is_active_functions: Array[SceneViewExtensionIsActiveFunctor]) -> None
```

x.set_scene_extension_is_active_functions(is_active_functions) -> None
Sets an array of activation functions. Will remove any others.

Args:
    is_active_functions (Array[SceneViewExtensionIsActiveFunctor]):

<a id="unreal.OpenColorIODisplayExtensionWrapper.set_scene_extension_is_active_function"></a>

#### set_scene_extension_is_active_function

```python
def set_scene_extension_is_active_function(
        is_active_function: SceneViewExtensionIsActiveFunctor) -> None
```

x.set_scene_extension_is_active_function(is_active_function) -> None
Sets a single activation function. Will remove any others.

Args:
    is_active_function (SceneViewExtensionIsActiveFunctor):

<a id="unreal.OpenColorIODisplayExtensionWrapper.set_open_color_io_configuration"></a>

#### set_open_color_io_configuration

```python
def set_open_color_io_configuration(
        display_configuration: OpenColorIODisplayConfiguration) -> None
```

x.set_open_color_io_configuration(display_configuration) -> None
Sets the display extension OCIO configuration.

Args:
    display_configuration (OpenColorIODisplayConfiguration):

<a id="unreal.OpenColorIODisplayExtensionWrapper.remove_scene_extension"></a>

#### remove_scene_extension

```python
def remove_scene_extension() -> None
```

x.remove_scene_extension() -> None
Removes the extension.

<a id="unreal.OpenColorIODisplayExtensionWrapper.get_open_color_io_configuration"></a>

#### get_open_color_io_configuration

```python
def get_open_color_io_configuration() -> OpenColorIODisplayConfiguration
```

x.get_open_color_io_configuration() -> OpenColorIODisplayConfiguration
Gets the display extension OCIO configuration.

Returns:
    OpenColorIODisplayConfiguration:

<a id="unreal.OpenColorIODisplayExtensionWrapper.create_open_color_io_display_extension"></a>

#### create_open_color_io_display_extension

```python
@classmethod
def create_open_color_io_display_extension(
    cls, display_configuration: OpenColorIODisplayConfiguration,
    is_active_function: SceneViewExtensionIsActiveFunctor
) -> OpenColorIODisplayExtensionWrapper
```

X.create_open_color_io_display_extension(display_configuration, is_active_function) -> OpenColorIODisplayExtensionWrapper
Creates an instance of this object, configured with the given arguments (OCIO and activation function).

Args:
    display_configuration (OpenColorIODisplayConfiguration): 
    is_active_function (SceneViewExtensionIsActiveFunctor): 

Returns:
    OpenColorIODisplayExtensionWrapper:

<a id="unreal.OpenColorIODisplayExtensionWrapper.create_in_game_open_color_io_display_extension"></a>

#### create_in_game_open_color_io_display_extension

```python
@classmethod
def create_in_game_open_color_io_display_extension(
    cls, display_configuration: OpenColorIODisplayConfiguration
) -> OpenColorIODisplayExtensionWrapper
```

X.create_in_game_open_color_io_display_extension(display_configuration) -> OpenColorIODisplayExtensionWrapper
Creates an instance of this object, configured for use in game with the given OCIO configuration.

Args:
    display_configuration (OpenColorIODisplayConfiguration): 

Returns:
    OpenColorIODisplayExtensionWrapper:

<a id="unreal.CaptureCardMediaSource"></a>