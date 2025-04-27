## DisplayClusterConfigurationCameraMotionBlurMode Objects

```python
class DisplayClusterConfigurationCameraMotionBlurMode(EnumBase)
```

EDisplay Cluster Configuration Camera Motion Blur Mode

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Enums.h

<a id="unreal.DisplayClusterConfigurationCameraMotionBlurMode.OFF"></a>

#### OFF

0: Subtract blur due to all global motion of the ICVFX camera, but preserve blur from object motion.

<a id="unreal.DisplayClusterConfigurationCameraMotionBlurMode.ON"></a>

#### ON

1: Allow blur from camera motion. This option should not normally be used for shooting, but may be useful for diagnostic purposes.

<a id="unreal.DisplayClusterConfigurationCameraMotionBlurMode.OVERRIDE"></a>

#### OVERRIDE

2: Subtract blur due to motion of the ICVFX camera relative to the nDisplay root, but preserve blur from both object motion and movement of the nDisplay root, which can be animated to represent vehicular motion through an environment.

<a id="unreal.DisplayClusterConfigurationViewportCustomFrustumMode"></a>