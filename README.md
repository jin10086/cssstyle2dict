cssstyle2dict
===========

方便查找css style里面的属性,css反爬虫用的比较多

Sample Code
-----------

```python
>>> from cssstyle2dict import styleParsel
>>> css = '.a { float:left } .b { margin-right:-1em } .c { float:left } .a { position:relative }'
>>> style_dict = styleParsel(css)
>>> print(style_dict)
{'a': {'float': 'left', 'position': 'relative'},
'b': {'margin-right': '-1em'},
'c': {'float': 'left'}}
```
Installation
------------
* `pip install cssstyle2dict`


