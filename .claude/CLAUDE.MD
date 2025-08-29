## Code Style Guidelines

For python code：

- Use reStructuredText style docstring like this:
```
"""Explain the method.

:param <param_name>: explain the parameter.
:return: explain the return value.
:raises: what may raise.
"""
```
Do NOT add param, return and raises doc for unittest test functions and methods.

- Do not go too verbose in docstring.
- Add detailed type hint where ever possible.
- Use type hinting generics in standard collections. Avoid type hinting like `typing.List[int]`, use `list[int]` instead.
- Do not violate PEP8 style guide.
- Prefer aiohttp over requests and httpx.
- Prefer Python 3.11 over other python version.
- Prefer msgspec.Struct over TypedDict, dataclass and pydantic.BaseModel.
- Prefer uv to create and manage Python projects.
- Do not import module inside function unless absolutely necessary.
- If a variable name conflicts with a python keyword, add a "_" suffix to the variable name.
- Before design or write unit tests, you **MUST** first read the guidelines in .codemaker/rule/unittest.md.
- To find test related code, read the .codemaker/rule/unittest.md file.

For C++ code:
- Use C++17 standard.
- Avoid std containers(except std::vector) if possible.
- Make memory allocation explict. Allow custom allocator if possible.

For html code:
- Use tailwind and htmx. Do not use other frameworks unless told to.
