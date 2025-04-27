## DisplayClusterConfigurationICVFX_PerLightcardRenderMode Objects

```python
class DisplayClusterConfigurationICVFX_PerLightcardRenderMode(EnumBase)
```

How to render a Light Card Actor in relation to the inner frustum.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Enums.h

<a id="unreal.DisplayClusterConfigurationICVFX_PerLightcardRenderMode.DEFAULT"></a>

#### DEFAULT

0: It is determined by nDisplay settings.

<a id="unreal.DisplayClusterConfigurationICVFX_PerLightcardRenderMode.OVER"></a>

#### OVER

1: Render Light Card Actor over the inner frustum.  Light Card Actor can be directly visible in camera.

<a id="unreal.DisplayClusterConfigurationICVFX_PerLightcardRenderMode.UNDER"></a>

#### UNDER

2: Render Light Card Actor under the inner frustum. Light Card Actor will not be directly visible in camera.

<a id="unreal.DisplayClusterPreviewShareMode"></a>