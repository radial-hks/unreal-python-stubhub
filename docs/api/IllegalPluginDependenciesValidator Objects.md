## IllegalPluginDependenciesValidator Objects

```python
class IllegalPluginDependenciesValidator(EditorValidatorBase)
```

Ensures that non-GameFeaturePlugins do not depend on GameFeaturePlugins.
GameFeaturePlugins will load content later than non-GameFeaturePlugins which could cause linker load issues if they do not exist.

**C++ Source:**

- **Plugin**: GameFeatures
- **Module**: GameFeaturesEditor
- **File**: IllegalPluginDependenciesValidator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_enabled`` (bool):  [Read-Write]
- ``only_print_custom_message`` (bool):  [Read-Write] Whether we should also print out the source validator when printing validation errors.

<a id="unreal.MovieSceneGeometryCacheSection"></a>