## MoviePipelineConfigBase Objects

```python
class MoviePipelineConfigBase(Object)
```

Movie Pipeline Config Base

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineConfigBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``settings`` (Array[MoviePipelineSetting]):  [Read-Only] Array of settings classes that affect various parts of the output pipeline.

<a id="unreal.MoviePipelineConfigBase.set_config_origin"></a>

#### set_config_origin

```python
def set_config_origin(config: MoviePipelineConfigBase) -> None
```

x.set_config_origin(config) -> None
Sets the config that this config originated from (if any). The origin should only be set for transient configs.

Args:
    config (MoviePipelineConfigBase):

<a id="unreal.MoviePipelineConfigBase.remove_setting"></a>

#### remove_setting

```python
def remove_setting(setting: MoviePipelineSetting) -> None
```

x.remove_setting(setting) -> None
Removes the specific instance from our Setting list.

Args:
    setting (MoviePipelineSetting):

<a id="unreal.MoviePipelineConfigBase.get_user_settings"></a>

#### get_user_settings

```python
def get_user_settings() -> Array[MoviePipelineSetting]
```

x.get_user_settings() -> Array[MoviePipelineSetting]
Returns an array of all settings in this config that the user has added via the UI or via Scripting.

Returns:
    Array[MoviePipelineSetting]:

<a id="unreal.MoviePipelineConfigBase.get_config_origin"></a>

#### get_config_origin

```python
def get_config_origin() -> MoviePipelineConfigBase
```

x.get_config_origin() -> MoviePipelineConfigBase
Gets the config that this config was originally based on (if any). The origin will only be set on transient
configs; the origin will be nullptr for non-transient configs because the origin will be this object.

Returns:
    MoviePipelineConfigBase:

<a id="unreal.MoviePipelineConfigBase.find_settings_by_class"></a>

#### find_settings_by_class

```python
def find_settings_by_class(
        class_: Class,
        include_disabled_settings: bool = False,
        exact_match: bool = False) -> Array[MoviePipelineSetting]
```

x.find_settings_by_class(class_, include_disabled_settings=False, exact_match=False) -> Array[MoviePipelineSetting]
Find all settings of a particular type for this config.

Args:
    class_ (type(Class)): Class that you wish to find the setting object for.
    include_disabled_settings (bool): if true, disabled settings will be included in the search
    exact_match (bool): if true, only exact matches of the specified class will be found, otherwise subclasses of the specified class will also be found

Returns:
    Array[MoviePipelineSetting]: An array of instances of this class if it already exists as a setting on this config

<a id="unreal.MoviePipelineConfigBase.find_setting_by_class"></a>

#### find_setting_by_class

```python
def find_setting_by_class(class_: Class,
                          include_disabled_settings: bool = False,
                          exact_match: bool = False) -> MoviePipelineSetting
```

x.find_setting_by_class(class_, include_disabled_settings=False, exact_match=False) -> MoviePipelineSetting
Find a setting of a particular type for this config.

Args:
    class_ (type(Class)): Class that you wish to find the setting object for.
    include_disabled_settings (bool): if true, disabled settings will be included in the search
    exact_match (bool): if true, only exact matches of the specified class will be found, otherwise subclasses of the specified class will also be found

Returns:
    MoviePipelineSetting: An instance of this class if it already exists as a setting on this config, otherwise null.

<a id="unreal.MoviePipelineConfigBase.find_or_add_setting_by_class"></a>

#### find_or_add_setting_by_class

```python
def find_or_add_setting_by_class(
        class_: Class,
        include_disabled_settings: bool = False,
        exact_match: bool = False) -> MoviePipelineSetting
```

x.find_or_add_setting_by_class(class_, include_disabled_settings=False, exact_match=False) -> MoviePipelineSetting
Finds a setting of a particular type for this pipeline config, adding it if it doesn't already exist.

Args:
    class_ (type(Class)): Class you wish to find or create the setting object for.
    include_disabled_settings (bool): if true, disabled settings will be included in the search
    exact_match (bool): if true, only exact matches of the specified class will be found, otherwise subclasses of the specified class will also be found

Returns:
    MoviePipelineSetting: An instance of this class as a setting on this config.

<a id="unreal.MoviePipelineConfigBase.copy_from"></a>

#### copy_from

```python
def copy_from(config: MoviePipelineConfigBase) -> None
```

x.copy_from(config) -> None
Copy this configuration from another existing configuration.

Args:
    config (MoviePipelineConfigBase):

<a id="unreal.MoviePipelineDebugSettings"></a>