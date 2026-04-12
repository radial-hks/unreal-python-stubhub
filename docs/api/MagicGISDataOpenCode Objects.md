## MagicGISDataOpenCode Objects

```python
class MagicGISDataOpenCode(EnumBase)
```

EMagic GISData Open Code

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISCore
- **File**: MagicGISDataProviderInterface.h

<a id="unreal.MagicGISDataOpenCode.NO_ERROR"></a>

#### NO\_ERROR

0: 打开成功，无错误.

<a id="unreal.MagicGISDataOpenCode.CONFIGURATION_ERROR"></a>

#### CONFIGURATION\_ERROR

1: 配置错误，如文件名为空，某些必要配置选项为空.

<a id="unreal.MagicGISDataOpenCode.RESOURCE_UNAVAILABLE"></a>

#### RESOURCE\_UNAVAILABLE

2: 资源不可用，如文件路径、URL、数据库或其他文件资源无法打开.

<a id="unreal.MagicGISDataOpenCode.SERVICE_UNAVAILABLE"></a>

#### SERVICE\_UNAVAILABLE

3: 服务不可用，如插件、扩展或模块无法打开.

<a id="unreal.MagicGISDataOpenCode.ASSERTION_FAILURE"></a>

#### ASSERTION\_FAILURE

4: 断言失败，检测到软件程序逻辑错误.

<a id="unreal.MagicGISDataOpenCode.GENERAL_ERROR"></a>

#### GENERAL\_ERROR

5: 其他错误.

<a id="unreal.MagicGISDataType"></a>